open Str;;
open List;;

exception Sair;;

(* let imprime = fun vetor ->

			let tamanho = (Array.length vetor) in
			for i=0 to tamanho-1 do
				match vetor.(i) with (a,b) -> Printf.printf "(%d,%d) " a b;
			done;
;; *)

let chegaPrimeiro = fun vetorA a b ->
	
					let tamanhoA = ref (Array.length !vetorA) in
					let resposta = ref 0 in

					for i=0 to !tamanhoA-1 do
						match !vetorA.(i) with (x,y) -> if (y=a || y=b) then begin resposta := y; tamanhoA := i end;
					done;
					!resposta;;

let existeCaminho = fun colonias tamanho origem fim -> (* função que verifica se há um caminho entre as colónias "a" e "b" *)

						let resposta = ref "NO" in
						for i=0 to !tamanho-1 do
							match (!(!colonias.(origem-1))).(i) with (a,b) -> if (b=fim) then begin resposta := "YES"; tamanho := i end
						done;
						!resposta;;

let diferencaAux = fun vetorA tuplo ->

				let tamanhoA = ref (Array.length !vetorA) in
				let resposta = ref "NO" in

				for i=0 to !tamanhoA-1 do
					match !vetorA.(i),tuplo with (x,y),(z,c) -> if ((x=z && y=c) || (x=c && y=z)) then begin resposta := "YES"; tamanhoA := i end;
				done;
				!resposta;;

let diferenca = fun vetorA vetorB e -> 

				let tamanhoB = (Array.length !vetorB) in
				let novo = ref (Array.make 0 (0,0)) in

				for i=0 to tamanhoB-1 do
					match !vetorB.(i),e with (a,b),(x,y) -> if (a=x && b=y) then () else if ((diferencaAux vetorA (a,b))="NO") then novo := (Array.append !novo [|(a,b)|]);
				done;
				novo;;

let acrescentaCaminho = fun colonias n a b -> (* função que acrescenta um caminho entre as colónias "a" e "b" *)
						
						let tamanhoA = ref 0 in
						let primeiro = ref 0 in

						if((existeCaminho colonias (ref(Array.length !(!colonias.(a-1)))) a b)="NO") then begin

							!colonias.(a-1)<-(ref(Array.append [|b|] (Array.append (!(!colonias.(a-1))) !(diferenca !colonias.(a-1) !colonias.(b-1) (b,a)))));
							!colonias.(b-1)<-(ref(Array.append [|(b,a)|] (Array.append (!(!colonias.(b-1))) !(diferenca !colonias.(b-1) !colonias.(a-1) (a,b)))));

							tamanhoA := Array.length (!(!colonias.(a-1)));

							for i=0 to !tamanhoA-1 do
								match (!(!colonias.(a-1))).(i) with (x,y) -> if (y!=a && y!=b) then begin primeiro := (chegaPrimeiro !colonias.(y-1) a b);
																										  !colonias.(y-1)<-(ref(Array.append (!(!colonias.(y-1))) !(diferenca !colonias.(y-1) !colonias.(!primeiro-1) (!primeiro,y)))) 
																										  end;
							done;					
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

					let eliminar = ref (Array.make 1 (n+1)) in
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
let resposta = ref "NO" in
	for i=0 to p-1 do begin
		Printf.printf "%d\n" (i+1);
		s := read_line();
		col := (map int_of_string (Str.split (regexp "[ \t]+") (string_after !s 4)));
		a := (nth !col 0);
		b := (nth !col 1);
		if (!s.[0]='L') then begin resposta := (existeCaminho colonias (ref(Array.length !(!colonias.(!a-1)))) !a !b); if (!resposta="YES") then final := (!final ^ "YES" ^ "\n") else final := (!final ^ "NO" ^ "\n") end
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