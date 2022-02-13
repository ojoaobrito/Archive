open Printf

type tree = Node of tree * int * tree
		  | Leaf of int 

let arvore = Node(Node(Leaf(1),2,Leaf(3)),4,Leaf(5));; (* a árvore seria esta:
																				 4
																			   /   \
																			  2     5
																			 / \
																			1   3     *)

let rec imprime = fun (arvore) -> match arvore with
								  | Node(l,i,d) -> printf "%d\n" i; printf "(esquerda do %d) > " i; imprime(l); printf "(direita do %d) > " i; imprime(d)
								  | Leaf(i) -> printf "%d\n" i;;

imprime(arvore);;