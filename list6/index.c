#include <unistd.h>

char shellcode[] = "\xeb\x1e\xb8\x04\x00\x00\x00\xbb\x01\x00\x00\x00\x59\xba\x0f\x00\x00\x00\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xdd\xff\xff\xff\x32\x35\x30\x31\x30\x35\x0d\x0a";
int main(int argc, char* argv[])
{
    int* ret;
    ret = (int*)&ret + 2;
    (*ret) = (int)shellcode;
}
