open Str;;
open List;;

(* let rec imprime = fun lista -> 

			  match lista with

			  | [] -> Printf.printf "\n"
			  | hd::tl -> match hd with (a,b) -> begin (Printf.printf "(%d,%d) " a b); imprime tl end;; *)

let rec diferenca_aux = fun lista b -> (* função auxiliar à função "diferenca", verifica se "a" está na lista "listB" *)
						
						match lista with

						| [] -> 0
						| hd::tl -> match hd,b with (x,y),(z,c) -> if ((x=z && y=c) || (x=c && y=z)) then 1 else diferenca_aux tl b;;

let rec diferenca = fun listA listB e acc -> (* função que devolve todos os elementos que estão em "list2" e não em "listB" *)
					
					match listB with

					| [] -> List.rev acc
					| hd::tl -> if (hd=e || (diferenca_aux listA hd)=1) then (diferenca listA tl e acc) else (diferenca listA tl e (hd::acc));;

let rec existeCaminho = fun caminhos origem fim -> (* função que verifica se há um caminho entre as colónias "a" e "b" *)
						
						match caminhos with

						| [] -> "NO"
						| hd::tl -> match hd with (a,b) -> if (a=origem && b=fim) then "YES" else if (a=fim || b=fim) then "YES" else existeCaminho tl origem fim;;

let acrescentaCaminho = fun colonias n a b -> (* função que acrescenta um caminho entre as colónias "a" e "b" *)
						
						if((existeCaminho colonias.(a-1) a b)="NO") then begin
						colonias.(a-1)<-(colonias.(a-1)@((a,b)::(diferenca colonias.(a-1) colonias.(b-1) (b,a) []))); (* "@" une listas *)
						colonias.(b-1)<-(colonias.(b-1)@((b,a)::(diferenca colonias.(b-1) colonias.(a-1) (a,b) [])));

						for i=0 to n-1 do begin
							if(i!=(a-1) && i!=(b-1)) then begin 
								if (existeCaminho colonias.(i) (i+1) a)="YES" then colonias.(i)<-(colonias.(i)@(diferenca colonias.(i) colonias.(a-1) (a,(i+1)) []))
								else if (existeCaminho colonias.(i) (i+1) b)="YES" then colonias.(i)<-(colonias.(i)@(diferenca colonias.(i) colonias.(b-1) (b,(i+1)) []))
							end;
						end;
						done;
					end;
;;

let rec adiciona = fun lista a -> (* função auxiliar à função "removeElemento", adiciona "a" à lista "lista", mas só se este não se encontrar já na lista *)

					match lista with

					| [] -> 1
					| hd::tl -> if hd=a then 0 else adiciona tl a;;

let rec eliminarCaminho = fun tuplo lista -> (* função auxiliar à função "removeElemento", verifica se o elemento "tuplo" deve ser removido da lista a que pertence *)

						match lista with

						| [] -> 0
						| hd::tl -> match tuplo with (x,y) -> if x=hd then 1 else eliminarCaminho tuplo tl;;

let rec removeElemento = fun lista a eliminar acc-> (* função auxiliar à função "removeCaminho", devolve uma nova "lista", sem os caminhos que vamos eliminar *)
						 
						 match lista with

						 | [] -> List.rev acc
						 | hd::tl -> match hd,a with (x,y),(b,c) -> if ((x=b && y=c) || (x=c && y=b) || (eliminarCaminho (x,y) eliminar)=1) then begin if (adiciona eliminar y)=1 then removeElemento tl a (y::eliminar) acc else removeElemento tl a eliminar acc end else removeElemento tl a eliminar (hd::acc);;

let removeCaminho = fun colonias n a b -> (* função que remove o caminho entre as colónias "a" e "b", atualizando as demais colónias *)

					for i=0 to n-1 do
						colonias.(i)<-(removeElemento colonias.(i) (a,b) [] []);
					done;													
;;

let lista_int = (map int_of_string (Str.split (regexp "[ \t]+") (read_line())));;

let n = match lista_int with | [hd;tl] -> hd | _ -> 0;; (* número de colónias *)
let p = match lista_int with | [hd;tl] -> tl | _ -> 0;; (* número de informações processadas *)

let colonias = Array.make n [];;

let final = ref "";;

let s = ref "" in
let col = ref [] in
	for i=0 to p-1 do begin
		Printf.printf "%d\n" (i+1);
		s := read_line();
		col := (map int_of_string (Str.split (regexp "[  \t]+") (string_after !s 4)));
		if (!s.[0]='L') then final := (!final ^ (existeCaminho colonias.((nth !col 0)-1) (nth !col 0) (nth !col 1)) ^ "\n")
		else if (!s.[0]='A') then (acrescentaCaminho colonias n (nth !col 0) (nth !col 1))
		else if (!s.[0]='D') then (removeCaminho colonias n (nth !col 0) (nth !col 1))
   	end;
	done;
;;

let() = Printf.printf "%s" !final;;

(* Printf.printf "\n";;
for i=0 to n-1 do
	Printf.printf "%d: " (i+1);
	imprime (colonias.(i));
done; *)