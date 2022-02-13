let b = read_int();; (* base numérica *)
let x = read_int();; (* número introduzido *)
let i = 1;; (* variável auxiliar *)
let y = 0;; (* número invertido *)

let rec palindroma = function (x,b,a,y,i) -> 
						
						if (a mod (10*i))>=(b*i) then print_string "ERROR\n"
						else if x=0 && y=a then print_string "YES\n"
						else if x=0 && y!=a then print_string "NO\n"
						else palindroma(x/10,b,a,(y*10)+(x mod 10),i*10);;
palindroma(x,b,x,y,i);;						