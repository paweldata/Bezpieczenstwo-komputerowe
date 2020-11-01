#ifndef CIPHERTEXT_H
#define CIPHERTEXT_H


#include <string>
#include <vector>

class Cryptogram {
public:
    explicit Cryptogram(const std::string& text);
    char getChar(int index);
    uint32_t getSize();

private:
    static char eightBitsToChar(std::string s);

    std::vector<char> chars;
};


#endif //CIPHERTEXT_H
