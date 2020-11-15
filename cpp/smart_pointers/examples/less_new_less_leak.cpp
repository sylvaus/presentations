#include <exception>
#include <stdexcept>
#include <memory>

using namespace std;

class Config {};

class ComplexApp
{
public:
    /* lots of methods to configure */

    bool is_config_valid(const Config& config);
    void run();
};

ComplexApp* create_app_98(const Config& config)
{
    auto app = new ComplexApp();

    if (!app->is_config_valid(config))
        // forgot to delete there
        throw runtime_error("Invalid configuration");

    // other configuration that may throw and
    // would need to free memory

    return app;
}

unique_ptr<ComplexApp> create_app_11(const Config& config)
{
    auto app = unique_ptr<ComplexApp>(new ComplexApp());

    if (!app->is_config_valid(config))
        // No need to delete
        throw std::runtime_error("Invalid configuration");

    // other configuration that may throw and
    // would need to free memory

    return app;
}

int main()
{
    ComplexApp* app98;
    try
    {
        app98 = create_app_98(Config());
    }
    catch (runtime_error&)
    {
        return -1;
    }
    app98->run();
    delete app98;

    unique_ptr<ComplexApp> app11;
    try
    {
        app11 = create_app_11(Config());
    }
    catch (runtime_error&)
    {
        return -1;
    }
    app11->run();
    // No need to remember to delete
}
