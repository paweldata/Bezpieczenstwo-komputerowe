global _start

section .text

_start:
    jmp MESSAGE

MAIN:
    mov eax, 0x4     ; system call number (sys_write)
    mov ebx, 0x1     ; file descriptor (stdout)
    pop ecx          ; address of string 
    mov edx, 0xF
    int 0x80

    mov eax, 0x1     ; system call number (sys_exit)
    mov ebx, 0x0
    int 0x80

MESSAGE:
    call MAIN        ; return address on stack
    db "250105", 0dh, 0ah

section .data
