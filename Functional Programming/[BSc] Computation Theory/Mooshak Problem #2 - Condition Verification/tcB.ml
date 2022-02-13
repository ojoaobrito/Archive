open List;;
open Str;;

exception Sair;;
exception Acabar;;

let rec comprimento = fun lista acc -> (* função que calcula o comprimento de uma lista *)
						match lista with
						| [] -> acc
						| hd::tl -> comprimento tl acc+1;;

let rec converteEmVetor = fun lista vetor i -> (* função que converte uma lista num vetor de igual conteúdo *)
						  match lista with
						  | [] -> ()
						  | hd::tl -> begin vetor.(i)<-hd; converteEmVetor tl vetor (i+1); end;;

let s = (List.map int_of_string (Str.split (Str.regexp "[  \t]+") (read_line())));;

let n = match s with | [hd;tl] -> hd | _ -> -1;; (* número de negociadores *)
let m = match s with | [hd;tl] -> tl | _ -> -1;; (* número de condições *)

let k = read_int();; (* negociador chave *)

let cond = Array.make n [||];;
let aux = ref [] in
for i=0 to m-1 do
	aux := (List.map int_of_string (Str.split (Str.regexp "[  \t]+") (read_line())));
	cond.(i)<-(Array.make (comprimento !aux 0) 0);
	converteEmVetor !aux cond.(i) 0;
done;;

let v = Array.make n 0;; (* vetor com os potenciais negociadores *)

let volta = ref 1 in (* voltas dadas no ciclo "for" *)
let abertas = ref m in (* condições abertas *)
let mud = ref 0 in (* mudanças de iteração para iteração *)
try begin
	while (!abertas != 0) do begin (* enquanto houver condições abertas *)
		for i=0 to m-1 do begin
			if (cond.(i).(0)=0 && cond.(i).(1)=k) then begin v.(k)<-1; raise Acabar end (* caso ideal *)
			else if (cond.(i).(0)=0 && !volta = 1) then begin (v.(cond.(i).(1))<-1); if(cond.(i).(0)!=(-1)) then (mud := !mud + 1); cond.(i).(0)<-(-1); abertas := (!abertas - 1) end (* potencial negociador "!cond.(i).(1)" entra nas negociações sem qualquer condição *)
			else if (cond.(i).(0) != (-1)) then begin
				try begin
					for j=1 to cond.(i).(0) do begin (* percorrer as condições do potencial negociador atual *)
						if (v.(cond.(i).(j))=0) then raise Sair
						else if (j=(cond.(i).(0))) then begin (v.(cond.(i).(j+1))<-1); if(cond.(i).(0)!=(-1)) then (mud := !mud + 1); cond.(i).(0)<-(-1); abertas := (!abertas - 1); raise Sair end
					end
					done;
				end;
				with Sair -> if (v.(k)=1) then raise Acabar (* negociador-chave entra nas negociações *)
			end
		end
		done;
		volta := (!volta + 1);
		if(!mud = 0) then raise Acabar
		else mud := 0
	end
	done;
	raise Acabar;
end;
with Acabar ->
	if (v.(k)=1) then Printf.printf "YES\n" (* negociador-chave entra nas negociações *)
	else Printf.printf "NO\n";; (* negociador-chave não entra nas negociações *)
