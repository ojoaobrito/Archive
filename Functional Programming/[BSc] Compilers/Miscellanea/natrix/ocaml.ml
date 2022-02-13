open Printf

exception VarUndef of string

let teste = ref (Array.make 0 "");;
teste := (Array.append !teste [|"x"|]);;

let find_variable = fun variables var -> (* simple function that checks if the given variable has been defined or not *)
                  let final = ref false in
                  for i=0 to (Array.length variables)-1 do if(String.equal variables.(i) var) then final := true done;
                  !final;;

if(find_variable !teste "x") then printf "Sucesso\n" else raise (VarUndef "Undefined variable!");;