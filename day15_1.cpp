#include <iostream>
#include <cstdint>
#include <vector>
#include <sstream>
#include <algorithm>
#include <string_view>

int_fast32_t get_hash(const std::string_view& text) noexcept {
    int_fast32_t result = 0;
    for (const auto& v: text) { result = ((result + v) * 17) % 256; }
    return result;
}

int main() {
    std::string_view text = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7";
    std::vector<std::string> vec;
    
    std::istringstream iss{(std::string(text))};
    std::string token;
    
    while (std::getline(iss, token, ',')) {
        vec.push_back(token);
    }
    
    int_fast32_t n = 0;
    for (const auto& v: vec) { 
        n += get_hash(v);
    }

    std::cout << n;
    return 0;
}