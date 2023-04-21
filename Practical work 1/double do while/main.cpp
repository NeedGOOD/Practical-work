#include <iostream>

int main() {
    std::cout << "Removing the Christmas tree\n";

    int number;

    std::cout << "Enter the number of numbers: ";
    std::cin >> number;
    std::cout << '\n';

    int i = 0;

    do {
        int j = 0;

        do {
            std::cout << '*';
            ++j;
        } while (j <= i);
        ++i;
        std::cout << '\n';
    } while (i < number);
    std::cout << '\n';
    return 0;
}