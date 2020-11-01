#include "Cryptogram.h"

Cryptogram::Cryptogram(const std::string& text) {
    int size = text.size();
    this->chars = std::vector<char>(text.size() / 9 + 1);
    for (int i = 0, j = 0; j < size; i ++, j += 9)
        this->chars[i] = eightBitsToChar(text.substr(j, 8));
}

char Cryptogram::getChar(int index) {
    return this->chars[index];
}

uint32_t Cryptogram::getSize() {
    return this->chars.size();
}

char Cryptogram::eightBitsToChar(std::string s) {
    int value = 0;

    for (int i = 0; i < 8; i++) {
        value *= 2;
        value += s[i] - '0';
    }

    return (char)value;
}
