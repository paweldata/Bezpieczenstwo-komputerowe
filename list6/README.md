# Bezpieczenstwo-komputerowe
## Lista 6

Bezpieczeństwo niskopoziomowe

### Login

Program ma na celu pokazanie, jak działa pamięć na stosie oraz jak doprowadzić do nadpisania danych. 

Przykład wywołania
```Shell
$ gcc login.c -o login -fno-stack-protector
$ ./login 12345
$ ./login 1234567890
$ ./login 123456789012
$ ./login 123456789012345678
```

### Index oraz shell
Programy mają na celu pokazanie, jak nadpisać pamięć tak, by program po zakończeniu funkcji main() skoczył do innego miejsca w pamięci i wykonał inny kod.

Przykład wywołania
```Shell
$ gcc index.c -o index -m32 -fno-stack-protector -z execstack
$ ./index
```

Zdobycie shellcode'a

```Shell
$ nasm -f elf32 -o index.o index.nasm && ld -m elf_i386 -o indexASM index.o
$ # pierwszy sposób
$ objdump -d indexASM
$ # drugi sposób
$ objdump -d indexASM | grep -Po '\s\K[a-f0-9]{2}(?=\s)' | sed 's/^/\\x/g' | perl -pe 's/\r?\n//' | sed 's/$/\n/'
```
