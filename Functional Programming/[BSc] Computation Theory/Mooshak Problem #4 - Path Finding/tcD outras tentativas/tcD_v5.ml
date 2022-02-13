open Str;;
open List;;

exception Sair;;

(* let imprime = fun vetor ->

			let tamanho = (Array.length vetor) in
			for i=0 to tamanho-1 do
				match vetor.(i) with (a,b) -> Printf.printf "(%d,%d) " a b;
			done;
;; *)

let existeCaminho = fun colonias tamanho origem fim1 fim2 -> (* função que verifica se há um caminho entre as colónias "a" e "b" *)

						let resposta = ref (-1) in
						for i=0 to !tamanho-1 do
							match (!(!colonias.(origem-1))).(i) with (a,b) -> if (b=fim1 && origem!=fim1) then begin resposta := fim1; tamanho := i end 
																			  else if (b=fim2 && origem!=fim2) then begin resposta := fim2; tamanho := i end
						done;
						!resposta;;

let acrescentaCaminho = fun colonias n a b -> (* função que acrescenta um caminho entre as colónias "a" e "b" *)
						
						let caminho = ref (-1) in
						let temp = ref [||] in

						caminho := (existeCaminho colonias (ref(Array.length !(!colonias.(a-1)))) a a b);

						if(!caminho=(-1)) then begin

							for i=0 to n-1 do
								if(i!=(a-1) && i!=(b-1)) then begin
									caminho := (existeCaminho colonias (ref(Array.length !(!colonias.(i)))) (i+1) a b);
									if !caminho=a then !colonias.(i)<-(ref(Array.append (Array.append (!(!colonias.(i))) [|(a,b)|]) !(!colonias.(b-1))))
									else if !caminho=b then !colonias.(i)<-(ref(Array.append (Array.append (!(!colonias.(i))) [|(b,a)|]) !(!colonias.(a-1))))
								end;
							done;

							temp := !(!colonias.(a-1));
							!colonias.(a-1)<-(ref(Array.append (Array.append (!(!colonias.(a-1))) [|(a,b)|]) !(!colonias.(b-1))));
							!colonias.(b-1)<-(ref(Array.append (Array.append (!(!colonias.(b-1))) [|(b,a)|]) !temp));
						end;
;;

let adiciona = fun eliminar a -> (* função auxiliar à função "removeElemento", adiciona "a" ao vetor "eliminar", mas só se este não se encontrar já no vetor *)

			let resposta = ref "NO" in
			let tamanhoV = ref (Array.length !eliminar) in
				for i=0 to !tamanhoV-1 do
					if !eliminar.(i)=a then tamanhoV := i 
					else if i=(!tamanhoV-1) then resposta := "YES"
				done;
			!resposta;;

let eliminarCaminho = fun eliminar tuplo -> (* função auxiliar à função "removeElemento", verifica se o elemento "tuplo" deve ser removido do vetor de caminhos a que pertence *)
	
					let resposta = ref "NO" in
					let tamanhoV = ref (Array.length !eliminar) in
						for i=0 to !tamanhoV-1 do
							match tuplo with (a,b) -> if a=(!eliminar.(i)) then begin resposta := "YES"; tamanhoV := i end;
						done;
					!resposta;;

let removeElemento = fun vetor r eliminar tamanho -> (* função auxiliar à função "removeCaminho", remove o caminho "r" da colónia a que pertence *)
						 
						 let novo = ref [||] in
						 for i=0 to tamanho-1 do
							match !vetor.(i),r with (x,y),(b,c) -> if ((x=b && y=c) || (x=c && y=b) || (eliminarCaminho eliminar (x,y))="YES") then begin if (adiciona eliminar y)="YES" then eliminar := (Array.append !eliminar [|y|]) end else novo := (Array.append !novo [|!vetor.(i)|])
						 done;
						 !novo;;

let removeCaminho = fun colonias n a b -> (* função que remove o caminho entre as colónias "a" e "b", atualizando as demais colónias *)

					let eliminar = ref [||] in
					for i=0 to n-1 do
						!colonias.(i)<-(ref(removeElemento !colonias.(i) (a,b) eliminar (Array.length !(!colonias.(i)))));
					done;
;;		
		
				

let lista_int = (map int_of_string (Str.split (regexp "[ \t]+") (read_line())));;

let n = match lista_int with | [hd;tl] -> hd | _ -> 0;; (* número de colónias *)
let p = match lista_int with | [hd;tl] -> tl | _ -> 0;; (* número de informações processadas *)

let colonias = ref (Array.make n (ref [||]));;

let final = ref "";;

let a = ref 0 in
let b = ref 0 in
let s = ref "" in
let col = ref [] in
let resposta = ref (-1) in
	for i=0 to p-1 do begin
		Printf.printf "%d\n" (i+1);
		s := read_line();
		col := (map int_of_string (Str.split (regexp "[  \t]+") (string_after !s 4)));
		a := (nth !col 0);
		b := (nth !col 1);
		if (!s.[0]='L') then begin resposta := (existeCaminho colonias (ref(Array.length !(!colonias.(!a-1)))) !a !a !b); if (!resposta != -1) then final := (!final ^ "YES" ^ "\n") else final := (!final ^ "NO" ^ "\n") end
		else if (!s.[0]='A') then (acrescentaCaminho colonias n !a !b)
		else if (!s.[0]='D') then (removeCaminho colonias n !a !b)
	end;
	done;
;;

let() = Printf.printf "%s" !final;;

(* let() = Printf.printf "\n";;
let() = for i=0 to n-1 do begin
	Printf.printf "%d: " (i+1);
	imprime (!(!colonias.(i)));
	Printf.printf "\n";
end;
done; *)