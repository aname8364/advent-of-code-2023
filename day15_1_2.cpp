#include <iostream>
#include <cstdint>
#include <vector>
#include <algorithm>
#include <string_view>
#include <ranges>

template <std::size_t N>
constexpr std::array<std::string_view, N> split_string(std::string_view input, char delimiter) {
    std::array<std::string_view, N> result = {};

    std::size_t start = 0;
    std::size_t end = input.find(delimiter);

    std::size_t i = 0;
    while (i < N - 1 && end != std::string_view::npos) {
        result[i++] = input.substr(start, end - start);
        start = end + 1;
        end = input.find(delimiter, start);
    }

    result[i] = input.substr(start);

    return result;
}

constexpr int_fast32_t get_hash(const std::string_view& text) noexcept {
    int_fast32_t result = 0;
    for (const auto& v: text) { result = ((result + v) * 17) % 256; }
    return result;
}

constexpr std::size_t get_count(const std::string_view& text, const char& sub) noexcept {
    int_fast32_t result = 0;
    for (const auto& v: text) {
        if (v == sub) { ++result; }
    }
    return result;
}

constexpr int_fast32_t sum_hash(const auto arr) noexcept {
    int_fast32_t result = 0;
    for (const auto& v: arr) { result += get_hash(v); }
    return result;
}

int main() {
    constexpr std::string_view text = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7";
    const char delim = ',';
    constexpr auto count = get_count(text, delim);

    constexpr auto arr = split_string<count+1>(text, delim);

    constexpr auto hash = sum_hash(arr);

    std::cout << hash;

    return 0;
}