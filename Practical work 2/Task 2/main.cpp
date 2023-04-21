#include <iostream>
#include <iomanip>
#include <string>

struct Client {
    std::string surname;
    std::string name;
    std::string middleName;
    std::string address;
    std::string email;
};

void result(int size, Client* client) {
    system("cls");
    std::cout << std::setiosflags(std::ios::left);
    std::cout << std::setw(5) << '#'
              << std::setw(15) << "Surname"
              << std::setw(20) << "Name"
              << std::setw(17) << "Middle name"
              << std::setw(20) << "Address"
              << std::setw(15) << "Email" << '\n';
    
    for (int i = 0; i < size; ++i) {
        std::cout << std::setw(5) << i + 1
                  << std::setw(15) << client[i].surname
                  << std::setw(20) << client[i].name
                  << std::setw(17) << client[i].middleName
                  << std::setw(20) << client[i].address
                  << std::setw(15) << client[i].email;
        std::cout << '\n';
    }
    std::cout << '\n';
}

int main() {
    const int size = 5;

    Client client[size];

    std::cout << "Enter your data:\n";
    for (int i = 0; i < size; ++i) {
        std::cout << "Surname: ";
        std::cin >> client[i].surname;

        std::cout << "Name: ";
        std::cin >> client[i].name;

        std::cout << "Middle name: ";
        std::cin >> client[i].middleName;
        
        std::cout << "Address(street number): ";
        std::cin.get();
        std::getline(std::cin, client[i].address);

        std::cout << "Email: ";
        std::cin >> client[i].email;
        std::cout << '\n';
    }
    result(size, client);
    return 0;
}