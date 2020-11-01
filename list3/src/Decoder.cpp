#include <iostream>
#include <fstream>
#include <utility>

#include "Decoder.h"

std::map<char, uint32_t> Decoder::KeyGenerator::charsFrequency = {
        {'a', 89},
        {'b', 15},
        {'c', 40},
        {'d', 33},
        {'e', 77},
        {'f', 3},
        {'g', 14},
        {'h', 11},
        {'i', 82},
        {'j', 23},
        {'k', 35},
        {'l', 21},
        {'m', 28},
        {'n', 55},
        {'o', 78},
        {'p', 31},
        {'r', 47},
        {'s', 43},
        {'t', 40},
        {'u', 25},
        {'v', 1},
        {'w', 47},
        {'x', 1},
        {'y', 38},
        {'z', 56},
        {' ', 100},
        {'.', 2},
        {',', 1},
};

Decoder::Decoder() {
    this->cryptograms = std::vector<Cryptogram>();
}

void Decoder::getCryptograms(int argc, char **argv) {
    std::ifstream file = getFile(argc, argv);
    std::string text;
    while (std::getline( file, text))
        this->cryptograms.emplace_back(Cryptogram(text));
}

std::ifstream Decoder::getFile(int argc, char *const *argv) const {
    if (argc < 2)
        showErrorAndEndProgram();
    std::ifstream file(argv[1]);
    if (!file.is_open())
        showErrorAndEndProgram();
    return file;
}

void Decoder::showErrorAndEndProgram() {
    printf("Give filename as argument\n");
    exit(-1);
}

void Decoder::generateKey() {
    KeyGenerator keyGenerator(*this);
    keyGenerator.generate();
}

void Decoder::printPlaintext() const {
    for (Cryptogram cryptogram : this->cryptograms) {
        for (int i = 0; i < cryptogram.getSize(); i++)
            printf("%c", cryptogram.getChar(i) ^ this->key[i]);
        printf("\n");
    }
}

void Decoder::KeyGenerator::generate() {
    this->setKeyLength();
    int size = this->decoder.key.size();
    for (int i = 0; i < size; i++)
        generateOnIndex(i);
}

void Decoder::KeyGenerator::setKeyLength() {
    uint32_t maxSize = 0;
    for (Cryptogram c : this->decoder.cryptograms)
        maxSize = std::max(maxSize, c.getSize());
    this->decoder.key = std::string(maxSize, ' ');
}

void Decoder::KeyGenerator::generateOnIndex(int i) {
    std::map<char, uint32_t> possibleKeys = getPossibleKeys(i);

    char bestKey = ' ';
    uint32_t bestKeyValidEncoding = 0;
    uint32_t bestKeyFrequency = 0;

    for (auto &[key, frequency] : possibleKeys) {
        uint32_t validEncoding = countValidEncodingOnIndex(i, key);
        if (validEncoding > bestKeyValidEncoding
        || (validEncoding == bestKeyValidEncoding && frequency > bestKeyFrequency)) {
            bestKey = key;
            bestKeyValidEncoding = validEncoding;
            bestKeyFrequency = frequency;
        }
    }

    this->decoder.key[i] = bestKey;
}

std::map<char, uint32_t > Decoder::KeyGenerator::getPossibleKeys(int i) const {
    std::map<char, uint32_t > possibleKeys;

    for (Cryptogram cryptogram : this->decoder.cryptograms)
        for (auto &[letter, frequency] : Decoder::KeyGenerator::charsFrequency)
            if (i < cryptogram.getSize()) {
                char possibleKey = cryptogram.getChar(i) ^ letter;
                possibleKeys[possibleKey] += frequency;
            }

    return possibleKeys;
}

uint32_t Decoder::KeyGenerator::countValidEncodingOnIndex(int i, char charKey) const {
    uint32_t counter = 0;

    for (Cryptogram cryptogram : this->decoder.cryptograms)
        if (i < cryptogram.getSize()) {
            char c = cryptogram.getChar(i) ^ charKey;
            if (Decoder::KeyGenerator::charsFrequency.find(c) != Decoder::KeyGenerator::charsFrequency.end()) {
                counter++;
            }
        }

    return counter;
}
