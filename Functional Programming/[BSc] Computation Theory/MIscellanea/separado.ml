let removeEspacos = fun s n -> (* função para remover espaços de uma string *)
let v = Array.make n 0 in
let k = ref 0 in
let aux = ref 0 in
let j = ref 10 in
let len = (String.length s) in
for i=0 to len-1 do
	if (s.[i]!=' ') then begin
		aux := (!aux * !j) + ((int_of_char)s.[i] - 48);
	end
	else if (s.[i]=' ') then begin
		v.(!k)<-(!aux);
		k := !k + 1;
		aux := 0;
	end
done;
if(v.(!k)=0) then v.(!k)<-(!aux);
v;;

let contaEspacos = fun s -> (* função auxiliar, conta os espaços de uma string de forma ajustada ao problema *)
let aux = ref 0 in
let c = ref 0 in 
let len = (String.length s) in
for i=0 to len-1 do
	if (s.[i] = ' ') then aux := !aux +1
	else if (s.[i] != ' ') then c := !c + 1
done;
if(!c > !aux + 1) then aux := (!aux + (!c - !aux - 1));
!aux;;

let aux = read_line();; (* primeira linha de input, ou seja "n" e "m" *)
let s = removeEspacos aux ((String.length aux) - (contaEspacos aux));;