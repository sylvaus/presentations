#include <vector>
#include <mutex>
#include <optional>
#include <thread>
#include <memory>
#include <iostream>

class DataBaseConnector
{
public:
    int64_t get_value(const int64_t index) {return (index * 14457) % 12374894548;}
};

void list_service(const std::shared_ptr<DataBaseConnector>& database)
{
    for (int i = 0; i < 25; ++i)
    {
        std::cout << "Listing: " << database->get_value(i) << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}

void welcome_employee(const std::shared_ptr<DataBaseConnector>& database)
{
    for (int i = 0; i < 10; ++i)
    {
        std::cout << "Welcome to: Employee " << database->get_value(i) << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}


int main()
{
    auto database = std::make_shared<DataBaseConnector>();
    std::thread listing(list_service, std::ref(database));
    std::thread welcome(welcome_employee, std::ref(database));

    // More code for the app
    welcome.join();

    // More code
    listing.join();

    return 0;
}

