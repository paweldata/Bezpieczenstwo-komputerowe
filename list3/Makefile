all: decoder clean

decoder:  main.o Decoder.o Cryptogram.o
	g++ -o decoder main.o Decoder.o Cryptogram.o

main.o: main.cpp
	g++ -c main.cpp -o main.o

Decoder.o: src/Decoder.cpp src/Decoder.h
	g++ -c src/Decoder.cpp -o Decoder.o -std=c++17
	
Cryptogram.o: src/Cryptogram.cpp src/Cryptogram.h
	g++ -c src/Cryptogram.cpp -o Cryptogram.o

clean:
	rm -f *.o
