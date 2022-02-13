(* função para remover espaços de uma string *)
exception Exit;;
exception Acabar;;

let removeEspacos = fun s n -> 
let v = Array.make n 0 in
let k = ref 0 in
for i=0 to (String.length s)-1 do
if s.[i] != ' ' then begin 
v.(!k)<-((int_of_char s.[i])-48);
k := !k + 1
end
done;
v

(* função auxiliar, conta os espaços de uma string *)
let contaEspacos = fun s -> 
let aux = ref 0 in
for i=0 to (String.length s)-1 do
if s.[i] = ' ' then (aux := !aux +1)
done;
!aux;;

let aux = read_line();;

let s = removeEspacos aux ((String.length aux) - (contaEspacos aux));;

let n = s.(0);; (* número de potenciais negociadores *)
let m = s.(1);; (* número de condições *)
let k = read_int();; (* negociador chave *)

let v = Array.make n 0;; (* vetor com os potenciais negociadores *)

let() = Printf.printf "\nNº negociadores:%d, Nº condições: %d, Negociador chave: %d\n\n" s.(0) s.(1) k;;

let aux2 = ref "" in
let cond = ref (Array.make 1 0) in (* condições *)
try
for i=0 to m-1 do begin
aux2 := read_line();
cond := removeEspacos !aux2 ((String.length !aux2) - (contaEspacos !aux2));
if v.(k)=1 then begin Printf.printf "YES\n"; raise Acabar end
else if (!cond.(0)=0 && !cond.(1)=k) then Printf.printf "YES\n"
else if !cond.(0)=0 then v.(!cond.(1))<-1
else if (i=(m-1) && v.(k)=0) then Printf.printf "NO\n"
else 
try
	begin
	for j=1 to !cond.(0) do
	if v.(!cond.(j))=0 then raise Exit
	else if (j=(!cond.(0))) then v.(!cond.(j+1))<-1
	done;
	end

with Exit -> ()
end
done;
with Acabar -> ()