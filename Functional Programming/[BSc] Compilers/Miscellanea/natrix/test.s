.text
.globl main
main:
	mov $1, %rax
	pushq %rax
	# 	adição
	mov $2, %rax
	pushq %rax
	mov $2, %rax
	pushq %rax
	popq %rax
	popq %rbx
	add %rbx, %rax
	pushq %rax
	popq %rbp
	popq i
for1:
	cmp i, %rbp
	jl exit1
	# 	multiplicação
	pushq fatorial
	pushq i
	popq %rax
	popq %rbx
	imul %rbx, %rax
	pushq %rax
	# 	atribuição
	popq fatorial
	add $1, i
	jmp for1
exit1:
	# 	impressão
	pushq fatorial
	popq %rsi
	call print_int
	# 	saída
	mov $0, %rax
	ret
print_int: 	# função que imprime o conteúdo de %rsi
	mov $message, %rdi
	call printf
	mov $0, %rax
	ret
.data
num: 	.quad 5
fatorial: 	.quad 1
i: 	.quad 0
message: 	.string "%d\n"
