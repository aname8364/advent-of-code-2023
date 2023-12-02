#include <iostream>
#include <algorithm>

int main() {
    std::string s;
    int n = 0;
    while (std::getline(std::cin, s)) {
        auto first_it = std::find_if(s.begin(), s.end(), ::isdigit);
        auto last_it = std::find_if(s.rbegin(), s.rend(), ::isdigit);
        auto x = *first_it - '0';
        auto y = *last_it - '0';
        n += (x*10) + y;
    }
    std::cout << n;
}