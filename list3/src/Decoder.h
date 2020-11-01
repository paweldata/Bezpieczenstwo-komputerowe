#ifndef DECODER_H
#define DECODER_H


#include <vector>
#include <map>

#include "Cryptogram.h"

class Decoder {
public:
    Decoder();
    void getCryptograms(int argc, char** argv);
    void generateKey();
    void printPlaintext() const;

private:
    std::ifstream getFile(int argc, char *const *argv) const;
    static void showErrorAndEndProgram();

    std::vector<Cryptogram> cryptograms;
    std::string key;

    class KeyGenerator {
    public:
        explicit KeyGenerator(Decoder& d) : decoder(d) {}
        void generate();

    private:
        void setKeyLength();
        void generateOnIndex(int i);
        std::map<char, uint32_t> getPossibleKeys(int i) const;
        uint32_t countValidEncodingOnIndex(int i, char c) const;

        static std::map<char, uint32_t> charsFrequency;
        Decoder& decoder;
    };
};


#endif //DECODER_H
