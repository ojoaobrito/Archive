# **LINGUAGEM NATRIX**

## SINTAXE BASE
* Tipos: "int"
* Possui "arrays"
* Possui versões do "if" e do "for"
* Possui funções (passagem por valor)
* Possui comentários ("//")

## PALAVRAS RESERVADAS
> "var", "int", "type", "array", "maxint", "minint", "print", "let", "if", "then", "else", "foreach" (ciclo for), "in", "do", "filled by", entre outras

## DEFINIÇÃO DE TIPOS
> um intervalo pode ser considerado um novo tipo

**(formalmente)** type nome = inicio .. fim ; **OU** type nome = [inicio .. fim];\
**(exemplo)** type i = 0 .. 100;\
**(exemplo)** type i_max = [10 .. maxint];

> tipo para os arrays

**(formalmente)** type nome = array indices of tipo; // os índices podem ser um intervalo específico ou um número "n", sendo os índices de 0 a "n"-1\
**(exemplo)** type arr = array 10 of int;

## DECLARAÇÃO DE VARIÁVEIS
> as variáveis são mutáveis, tipadas (explicitamente) e sempre inicializadas

**(formalmente)** var nome : tipo = valor;\
**(exemplo)** var x : int = 5;\
**(exemplo)** var y : i_max = 12; // i_max é o tipo definido acima, ou seja, é o tipo dos inteiros entre 10 e "maxint"

> declaração de variáveis locais

**(formalmente)** let nome = valor in (...);\
**(exemplo)** let x = 2 in y + x; 

> declaração de arrays (podem ser indexados como normalmente, e.g. nome[0])

**(formalmente)** var nome : tipo filled by valor;\
**(exemplo)** var lista : arr filled by 0; // array do tipo "arr" (tem 10 elementos) e preenchido por 0

## ATRIBUIÇÃO
> existe a função "size()" que devolve o tamanho dos intervalos e dos vectores

**(formalmente)** nome := novo_valor;\
**(exemplo)** x := 10;

## INSTRUÇÃO PRINT
**(formalmente)** print (variável/expressão);\
**(exemplo)** print (x);

## INSTRUÇÃO IF
> seguem o padrão clássico =, != , <, <=, >, >=, & e |

**(formalmente)** if (condição) then {expressão1;} else {expressão2;}\
**(exemplo)** if (2<3) then {print (1);} else {print(2);}

## CICLO FOR
**(formalmente)** foreach contador in intervalo do {expressão;}\
**(exemplo)** foreach i in 1..19 do {x := x + 1;}