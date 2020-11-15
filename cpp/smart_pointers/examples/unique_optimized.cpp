#include <string>
#include <iostream>
#include <memory>
#include <utility>

class Stream
{
public:
    virtual void write(const std::string& value) = 0;
    virtual void flush() = 0;
    virtual ~Stream() = default;
};

class StdoutStream: public Stream
{
public:
    void write(const std::string &value) override {std::cout << value;}
    void flush() override {std::cout.flush();}
};

class Printer
{
public:
    explicit Printer(std::unique_ptr<Stream> stream): stream_(std::move(stream)) {}
    void print(const std::string &value) {stream_->write(value); stream_->flush();}
private:
    std::unique_ptr<Stream> stream_;
};

class NameProvider
        {
public:
    const std::string &get_name() const {return name_;}
    void set_name(const std::string &name) {name_ = name;}
    bool is_valid_name(const std::string& name) const {return !name.empty();}
private:
    std::string name_;
};

class Application
        {
public:
    Application(std::unique_ptr<Printer> printer) : printer_(std::move(printer)), name_provider_(nullptr) {}
    void run() {printer_->print("Hello, " + (name_provider_ ? name_provider_->get_name() : "World"));}
    void set_name_provider(std::unique_ptr<NameProvider> name_provider) {name_provider_ = std::move(name_provider);}
private:
    std::unique_ptr<Printer> printer_;
    std::unique_ptr<NameProvider> name_provider_;
};

int main(int argc, char** argv)
{
    auto stream = std::unique_ptr<StdoutStream>(new StdoutStream());
    auto printer = std::unique_ptr<Printer>(new Printer(std::move(stream)));
    auto application = Application(std::move(printer));

    auto name_provider = std::unique_ptr<NameProvider>(new NameProvider());
    if ((argc > 1) && name_provider->is_valid_name(argv[1]))
    {
        name_provider->set_name(argv[1]);
        application.set_name_provider(std::move(name_provider));
    }
    application.run();
}
