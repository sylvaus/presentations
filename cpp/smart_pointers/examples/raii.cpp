#include <memory>

using namespace std;

class Engine {};
class EngineModel {};

class Car98Older
{
public:
    Car98Older(EngineModel* engine_model) :
            engine_(new Engine()),
            engine_model_(engine_model)
    {}

    ~Car98Older()
    {
        // Ok, probably the only one using this engine
        delete engine_;
        // Isn't the engine model shared ?
        // Who is supposed to clean it ?
        delete engine_model_;
    }
private:
    Engine* engine_;
    EngineModel* engine_model_;
};

class Car11Plus
{
public:
    Car11Plus(shared_ptr<EngineModel> engine_model):
            engine_{new Engine()},
            engine_model_(std::move(engine_model))
    {}
private:
    // Unique owner of the engine
    unique_ptr<Engine> engine_;
    // Engine Model can be shared among cars
    shared_ptr<EngineModel> engine_model_;
};

int main_98()
{
    EngineModel* engine_model = new EngineModel();

    Car98Older car = Car98Older(engine_model);

    // Should it be deleted ?
    // Can a thread be still using it ?
    delete engine_model;
    return 0;
};

int main_11()
{
    auto engine_model = make_shared<EngineModel>();

    auto car = Car11Plus(engine_model);
    return 0;
};

int main()
{
//    main_98();
//    main_11();
}
