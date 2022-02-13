open Str;;
open List;;

let rec comprimento = fun lista acc->
						match lista with
						| [] -> acc
						| hd::tl -> comprimento tl acc+1;;

let rec converteEmVetor = fun lista vetor i->
						  match lista with
						  | [] -> ()
						  | hd::tl -> begin vetor.(i)<-hd; converteEmVetor tl vetor (i+1); end;;

let s = (List.map int_of_string (Str.split (regexp "[  \t]+") (read_line())));;

let n = match s with | [hd;tl] -> hd | _ -> -1;;
let m = match s with | [hd;tl] -> tl | _ -> -1;;

let condicoes = Array.make n [||];;
let aux = ref [] in
for i=0 to m-1 do 
	aux := (List.map int_of_string (Str.split (regexp "[  \t]+") (read_line())));
	condicoes.(i)<-(Array.make (comprimento !aux 0) 0);
	converteEmVetor !aux condicoes.(i) 0;
done;

(* for j=0 to m-1 do begin
	
	for i=0 to (condicoes.(j).(0)+1) do
		Printf.printf "%d" condicoes.(j).(i);
	done;
	Printf.printf "\n";
end;
done; *) (* só para imprimir e testar *)