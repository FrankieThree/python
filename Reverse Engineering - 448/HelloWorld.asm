;-------------------------------
; Assignment 1 / Hellow World
; Runs a loop that prints “Hello World!” string five (5) times.
; Frankie Cook / Dec 11, 2023
;-------------------------------

format ELF64 executable 			; specify program, x64
entry start					; declare entry point

xor rbx, rbx					; clear register RBX

segment readable executable
start:
    mov     rax, 1				; system call for write
    mov     rdi, 1				; file handle 1 is stdout
    mov     rsi, message			; address of string to output
    mov     rdx, message_end - message	; number of bytes
    syscall					; invokes OS to do the write
    				
    inc rbx					; RBX += 1
    add rsp, 8					; Add 8 to stack pointer (clean up arguments)
    
    cmp rbx, 5					; compare RBX to 5 (5 - RBX)
    jl start					; if comparison is less than 5, then jump to start
    
    mov     rax, 60				; system call for exit
    xor     rdi, rdi				; exit code 0
    syscall					; invoke OS to exit

segment readable writable
message db 'Hello World!', 0x0A		; db (Define Byte) allocates 1 byte
						; 0x0A terminates the string (newline)
message_end:					; end of message
