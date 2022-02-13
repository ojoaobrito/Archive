open Str;;
open List;;
open Stack;;

let hopcroft_karp (estados_M1, estados_M2) =

	let pilha = Stack.create in (* pilha a ser usada no algoritmo *)
	let sigma = (Array.make 26 'a') in

	for i=0 to 25 do (* definir o alfabeto *)
		sigma.(i)<-(char_of_int (97+i));
	done;

	try begin
		
	end

	with Stack.Empty -> ();;

let rec lista_para_vetor (lista, vetor, i) = (* função para colocar o conteúdo de uma lista num vetor *)
	match lista with
	| [] -> ()
	| hd::tl -> vetor.(i)<-hd; lista_para_vetor(tl,vetor,i+1);;

let n1 = read_int();; (* número de estados de M1 *)
let estados_M1 = (Array.make n1 (Array.make 0 (0,'a',0)));; (* estados de M1 e respetivas transições *)
let s1 = read_int();; (* estado inicial de M1 *)
let f1 = read_int();; (* número de estados finais de M1 *)
let finais_M1 = (Array.make f1 0);; (* estados finais de M1 *)

let str = (map int_of_string (Str.split (Str.regexp "[ \t]+") (read_line())));;
lista_para_vetor(str,finais_M1,0);;

let t1 = read_int();; (* número de transições de M1 *)

for i=0 to t1-1 do
let x,y,z = Scanf.sscanf (read_line()) " %d %c %d" (fun a b c -> a,b,c) in
	estados_M1.(x-1)<-(Array.append estados_M1.(x-1) [|(x,y,z)|]);
done;
;;

let n2 = read_int();; (* número de estados de M2 *)
let estados_M2 = (Array.make n2 (Array.make 0 (0,'a',0)));; (* estados de M2 e respetivas transições *)
let s2 = read_int();; (* estado inicial de M2 *)
let f2 = read_int();; (* número de estados finais de M2 *)
let finais_M2 = (Array.make f2 0);; (* estados finais de M2 *)

let str = (map int_of_string (Str.split (Str.regexp "[ \t]+") (read_line())));;
lista_para_vetor(str,finais_M2,0);;

let t2 = read_int();; (* número de transições de M2 *)

for i=0 to t2-1 do
let x,y,z = Scanf.sscanf (read_line()) " %d %c %d" (fun a b c -> a,b,c) in
	estados_M2.(x-n1-1)<-(Array.append estados_M2.(x-n1-1) [|(x,y,z)|]);
done;
;;