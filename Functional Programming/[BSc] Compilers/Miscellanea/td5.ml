open Printf;;

type symbol = Terminal of string
			| Non_terminal of string;;

type production = symbol list;;
type rule = symbol * production;;
type grammar = { start: symbol; rules: rule list; };;

let rec fixpoint = fun funcao x -> if (funcao x) then fixpoint funcao 

let gramatica = { start = Non_terminal("S"); rules = [(Non_terminal("S"), [Non_terminal("T"); Non_terminal("E'")]); (* E -> TE' *)
													  (Non_terminal("E'"), [Terminal("+"); Non_terminal("T"); Non_terminal("E'")]); (* E' -> "+"TE' *)
													  (Non_terminal("E'"), []); (* E -> epsilon *)
													  (Non_terminal("T"), [Non_terminal("F"); Non_terminal("T'")]); (* T -> FT' *)
													  (Non_terminal("T'"), [Terminal("+"); Non_terminal("F"); Non_terminal("T'")]); (* T' -> "+"FT' *)
													  (Non_terminal("T'"), []); (* T -> epsilon *)
													  (Non_terminal("F"), [Terminal("("); Non_terminal("E"); Terminal(")")]); (* F -> "("E")" *)
													  (Non_terminal("F"), [Terminal("int")])] };; (* F -> "int" *)