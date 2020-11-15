#include <string>
#include <iostream>

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
    explicit Printer(Stream* stream): stream_(stream) {}
    void print(const std::string &value) {stream_->write(value); stream_->flush();}
private:
    Stream* stream_;
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
    Application(Printer *printer) : printer_(printer), name_provider_(nullptr) {}
    void run() {printer_->print("Hello, " + (name_provider_ ? name_provider_->get_name() : "World"));}
    void set_name_provider(NameProvider *name_provider) {name_provider_ = name_provider;}
    ~Application() {delete printer_; delete name_provider_;}
private:
    Printer* printer_;
    NameProvider* name_provider_;
};

int main(int argc, char** argv)
{
    auto stream = new StdoutStream();
    auto printer = new Printer(stream);
    auto application = Application(printer);

    auto name_provider = new NameProvider();
    if ((argc > 1) && name_provider->is_valid_name(argv[1]))
    {
        name_provider->set_name(argv[1]);
        application.set_name_provider(name_provider);
    }
    application.run();
}



