open Str;;
open List;;

let rec estado1 (lista) =
	match lista with
	| [] -> false
	| hd::tl -> if(hd='a') then estado2(tl)
				else if(hd='b' || hd='c') then estado1(tl)
				else false

	and estado2 (lista) = 
	match lista with
	| [] -> true
	| hd::tl -> if(hd='a') then estado2(tl)
				else if(hd='b') then estado3(tl)
				else if(hd='c') then estado1(tl)
				else false

	and estado3 (lista) =
	match lista with
	| [] -> false
	| hd::tl -> if(hd='b') then estado2(tl)
				else if(hd='a') then estado3(tl)
				else if(hd='c') then estado1(tl)
				else false;;

let s = read_line();;
let buffer = ref [];;

for i=0 to (String.length s)-1 do
	buffer:=(s.[i]::(!buffer));
done;
;;

let resposta = estado1((List.rev !buffer));;

if(resposta=true) then Printf.printf "Palavra reconhecida pelo autómato\n" else Printf.printf "Palavra não reconhecida pelo autómato\n";;