#include "src/Decoder.h"

int main(int argc, char** argv) {
    Decoder decoder;
    decoder.getCryptograms(argc, argv);
    decoder.generateKey();
    decoder.printPlaintext();
    return 0;
}
