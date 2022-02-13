open Printf

type ichar = char * int (* carateres com índice *)

module Cset = Set.Make(struct type t = ichar let compare = compare end);; (* conjunto *)

type regexp =
| Epsilon
| Character of ichar
| Union of regexp * regexp
| Concat of regexp * regexp
| Star of regexp;; (* operador de Kleene *)

let rec null = fun expressao -> (* função que determina se a linguagem aceita a palavra vazia ("Epsilon") *)
	
	match expressao with
	| Epsilon -> true
	| Character(a) -> false
	| Union(a,b) -> (null a) || (null b)
	| Concat(a,b) -> (null a) && (null b)
	| Star(a) -> true;;

let rec first = fun expressao conjunto -> (* função que devolve as primeiras letras de qualquer palavra reconhecida pela linguagem dada *)

	match expressao with
	| Epsilon -> ()
	| Character(a,b) -> conjunto := (Cset.add (a,b) !conjunto) (* acrescentar o carater ao conjunto, sendo único neste caso *)
	| Union(a,b) -> (first a conjunto); (first b conjunto)
	| Concat(a,b) -> if (null a) then begin (first a conjunto); (first b conjunto) end else (first a conjunto)
	| Star(a) -> (first a conjunto);;

let rec last = fun expressao conjunto -> (* função que devolve as últimas letras de qualquer palavra reconhecida pela linguagem dada *)

	match expressao with
	| Epsilon -> ()
	| Character(a,b) -> conjunto := (Cset.add (a,b) !conjunto) (* acrescentar o carater ao conjunto, sendo único neste caso *)
	| Union(a,b) -> (last a conjunto); (last b conjunto)
	| Concat(a,b) -> if (null b) then begin (last a conjunto); (last b conjunto) end else (last b conjunto)
	| Star(a) -> (last a conjunto);;

let rec follow = fun carater expressao conjunto -> (* função que devolve as letras seguintes ao carater "carater" nas expressão regular "expressao" *)

	let aux = ref Cset.empty in

	match expressao with
	| Epsilon -> ()
	| Character(a,b) -> ()
	| Union(a,b) -> begin (follow carater a conjunto); (follow carater b conjunto) end
	| Concat(a,b) -> begin (last expressao aux); if (Cset.mem carater !aux) then begin (follow carater a conjunto); (follow carater b conjunto); (first b conjunto) end else begin (follow carater a conjunto); (follow carater b conjunto) end end
	| Star(a) -> begin (last expressao aux); if (Cset.mem carater !aux) then begin (follow carater a conjunto); (first a conjunto) end else (follow carater a conjunto) end;;

(* expressão ((a1 + b1)* a2 (a3 + b2)) *)
(* let expressao = Concat(Concat(Star(Union(Character('a',1),Character('b',1))),Character('a',2)),Union(Character('a',3),Character('b',2)));;*)

let expressao = Concat(Concat(Character('a',1),Character('b',1)),Character('a',2));;

if (null expressao) then printf "\nA expressão aceita o Epsilon\n" else printf "\nA expressão não aceita o Epsilon\n";;

let conjunto = ref Cset.empty;;
(first expressao conjunto);;
let primeiras = (Cset.elements !conjunto);; (* obter os elementos do conjunto *)

let rec imprime = fun lista ->
				match lista with
				| (a,b)::tl -> (printf "%c%d " a b); (imprime tl)
				| _ -> ();;

printf "As primeiras letras são: ";;
imprime primeiras;;
printf "\n";;

let conjunto = ref Cset.empty;;
(last expressao conjunto);;
let ultimas = (Cset.elements !conjunto);; (* obter os elementos do conjunto *)

printf "As últimas letras são: ";;
imprime ultimas;;
printf "\n";;

let conjunto = ref Cset.empty;;
(follow ('a',1) expressao conjunto);;
let seguintes = (Cset.elements !conjunto);; (* obter os elementos do conjunto *)
printf "As letras seguintes ao a1 são: ";;
imprime seguintes;;
printf "\n\n"