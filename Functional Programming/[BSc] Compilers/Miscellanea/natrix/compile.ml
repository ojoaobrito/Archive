open Format
open X86
open Ast

exception VarUndef of string (* variável não declarada *)

(* contadores que garantem que o labels "main", "else", "while" e "exit" nunca se repetem *)
let contador_main = ref 1
let contador_if = ref 1
let contador_loop = ref 1

let variables = ref (Array.make 0 ("","")) (* as variáveis globais são arquivadas num array *)
module StrMap = Map.Make(String)

let data_variables = fun variables -> (* função auxiliar que carrega para o ficheiro as variáveis, o tipo de dados e o valor inicial *)
                                    let code = ref nop in
                                    for i=0 to ((Array.length !variables)-1) do 
                                    begin
                                        let variable = (match !variables.(i) with (a,b) -> a) in
                                        let numero = (match !variables.(i) with (a,b) -> b) in
                                        code := !code ++ ((label variable) ++ quad (int_of_string(numero)) ++ newline_data)
                                    end
									done;
									code := !code ++ label "message" ++ string_type "%d\n" ++ newline_data;
                                    !code

let find_variable = fun variables var -> (* função auxiliar que verifica se a variável "var" já foi declarada ou não *)
                                    let final = ref false in
                                    for i=0 to (Array.length variables)-1 do 
                                    begin 
                                        if((compare (match variables.(i) with (a,b) -> a) var)==0) then final := true 
                                    end 
                                    done;
                                    !final

let compile_expr = (* função que compila expressões *) 

  let rec comprec env next = function

	| I i -> (* inteiros *)
			mov_val_reg i rax ++ newline ++
			pushq rax ++ newline

	| Var x -> (* variáveis *)
			begin
			if(find_variable !variables x) then begin
				pushq_var x ++ newline
			end
			else raise (VarUndef (x))
			end
        

	| Op (Add, e1, e2)-> (* operação de soma *)
						comment "\tadição" ++ newline ++
						comprec env next e1 ++
						comprec env next e2 ++
						popq rax ++ newline ++
						popq rbx ++ newline ++
						add_reg_reg rbx rax ++ newline ++
						pushq rax ++ newline

    | Op (Sub, e1, e2)-> (* operação de subtração *)
						comment "\tsubtração" ++ newline ++
						comprec env next e1 ++
						comprec env next e2 ++
						popq rax ++ newline ++
						popq rbx ++ newline ++
						sub_reg_reg rbx rax ++ newline ++
						pushq rax ++ newline
		
    | Op (Mul, e1, e2)-> (* operação de multiplicação *)
						comment "\tmultiplicação" ++ newline ++
						comprec env next e1 ++
						comprec env next e2 ++
						popq rax ++ newline ++
						popq rbx ++ newline ++
						mul_reg_reg rbx rax ++ newline ++
						pushq rax ++ newline
						
    | Op (Div, e1, e2)-> (* operação de divisão *)
						comment "\tdivisão" ++ newline ++
						comprec env next e1 ++
						comprec env next e2 ++
						popq rbx ++ newline ++
						mov_val_reg 0 rdx ++ newline ++
						popq rax ++ newline ++
						div_reg_reg rbx ++ newline ++
						pushq rax ++ newline
  in
  comprec StrMap.empty 0

(* função que compila instruções *) 
let rec compile_instr = function 

    | Dec (x, e) -> (* declaração de variáveis *)
                (match e with | I i -> variables := (Array.append !variables [|(x,string_of_int(i))|])); 
                nop

    | Set (x, e) -> (* atribuição de expressões a variáveis *)
                let code = ref nop in
                if(find_variable !variables x) then begin
                code := !code ++ (compile_expr e ++ comment "\tatribuição" ++ newline ++ popq_var x ++ newline); !code
                end
                else raise (VarUndef (x))
                !code

	| Print e -> (* imprimir uma expressão/variável *)
				comment "\timpressão" ++ newline ++
				compile_expr e ++
				popq rsi ++ newline ++
				call "print_int" ++ 
				newline

    | Cond (t, i1, i2) -> (* if-else *)
                        begin

                        match t with
                        | Neg t_in -> begin (* o compilador faz pré-processamento *)
                        
                                        match t_in with
                                        | B true -> compile_instr (Cond (B false,i1,i2))

                                        | B false -> compile_instr (Cond (B true,i1,i2))

                                        | Comp (e1,e2) -> begin
															let code = ref nop in
															let code2 = ref nop in
															let code3 = ref nop in
															let code4 = ref nop in
															let code5 = ref nop in
													
															begin
																	code := compile_expr e1 ++
																	compile_expr e2 ++
																	popq rax ++ newline ++
																	popq rbx ++ newline ++
																	cmp_reg_reg rax rbx ++ newline ++ 
																	je ("else" ^ string_of_int(!contador_if)) ++ newline;
																	
																	for i=0 to ((List.length i1)-1) do code2 := !code2 ++ compile_instr (List.nth i1 i) done; 
																	
																	code3 := jmp ("main" ^ string_of_int(!contador_main)) ++ newline ++
																	label_jump ("else" ^ string_of_int(!contador_if)) ++ newline;
																	
																	for i=0 to ((List.length i2)-1) do code4 := !code4 ++ compile_instr (List.nth i2 i) done; 
																	
																	code5 := label_jump ("main" ^ string_of_int(!contador_main)) ++ newline;
																	contador_if := !contador_if + 1;
																	contador_main := !contador_main + 1;
																	(!code ++ !code2 ++ !code3 ++ !code4 ++ !code5)
															end
														end

										| Big (e1,e2) -> compile_instr (Cond (SmallEqual(e1,e2),i1,i2))

										| BigEqual (e1,e2) -> compile_instr (Cond (Small(e1,e2),i1,i2))

										| Small (e1,e2) -> compile_instr (Cond (BigEqual(e1,e2),i1,i2))

										| SmallEqual (e1,e2) -> compile_instr (Cond (Big(e1,e2),i1,i2))
									end

                        | B true -> begin 
										let code = ref nop in 
										for i=0 to ((List.length i1)-1) do code := !code ++ compile_instr (List.nth i1 i) done; 
										!code 
									end

                        | B false -> begin 
										let code = ref nop in 
										for i=0 to ((List.length i2)-1) do code := !code ++ compile_instr (List.nth i2 i) done; 
										!code 
									end

                        | Comp (e1, e2) -> (* a==b *)
										begin
											let code = ref nop in
											let code2 = ref nop in
											let code3 = ref nop in
											let code4 = ref nop in
											let code5 = ref nop in
									
											begin
													code := compile_expr e1 ++
													compile_expr e2 ++
													popq rax ++ newline ++
													popq rbx ++ newline ++
													cmp_reg_reg rax rbx ++ newline ++ 
													jne ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i1)-1) do code2 := !code2 ++ compile_instr (List.nth i1 i) done; 
													
													code3 := jmp ("main" ^ string_of_int(!contador_main)) ++ newline ++
													label_jump ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i2)-1) do code4 := !code4 ++ compile_instr (List.nth i2 i) done; 
													
													code5 := label_jump ("main" ^ string_of_int(!contador_main)) ++ newline;
													contador_if := !contador_if + 1;
													contador_main := !contador_main + 1;
													(!code ++ !code2 ++ !code3 ++ !code4 ++ !code5)
											end
										end

                        | Big (e1, e2) -> (* a>b *)
										begin
											let code = ref nop in
											let code2 = ref nop in
											let code3 = ref nop in
											let code4 = ref nop in
											let code5 = ref nop in
									
											begin
													code := compile_expr e1 ++
													compile_expr e2 ++
													popq rax ++ newline ++
													popq rbx ++ newline ++
													cmp_reg_reg rax rbx ++ newline ++ 
													jle ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i1)-1) do code2 := !code2 ++ compile_instr (List.nth i1 i) done; 
													
													code3 := jmp ("main" ^ string_of_int(!contador_main)) ++ newline ++
													label_jump ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i2)-1) do code4 := !code4 ++ compile_instr (List.nth i2 i) done; 
													
													code5 := label_jump ("main" ^ string_of_int(!contador_main)) ++ newline;
													contador_if := !contador_if + 1;
													contador_main := !contador_main + 1;
													(!code ++ !code2 ++ !code3 ++ !code4 ++ !code5)
											end
										end

                        | BigEqual (e1, e2) -> (* a>=b *)
										begin
											let code = ref nop in
											let code2 = ref nop in
											let code3 = ref nop in
											let code4 = ref nop in
											let code5 = ref nop in
									
											begin
													code := compile_expr e1 ++
													compile_expr e2 ++
													popq rax ++ newline ++
													popq rbx ++ newline ++
													cmp_reg_reg rax rbx ++ newline ++ 
													jl ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i1)-1) do code2 := !code2 ++ compile_instr (List.nth i1 i) done; 
													
													code3 := jmp ("main" ^ string_of_int(!contador_main)) ++ newline ++
													label_jump ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i2)-1) do code4 := !code4 ++ compile_instr (List.nth i2 i) done; 
													
													code5 := label_jump ("main" ^ string_of_int(!contador_main)) ++ newline;
													contador_if := !contador_if + 1;
													contador_main := !contador_main + 1;
													(!code ++ !code2 ++ !code3 ++ !code4 ++ !code5)
											end
										end

                        | Small (e1, e2) -> (* a<b *)
										begin
											let code = ref nop in
											let code2 = ref nop in
											let code3 = ref nop in
											let code4 = ref nop in
											let code5 = ref nop in
									
											begin
													code := compile_expr e1 ++
													compile_expr e2 ++
													popq rax ++ newline ++
													popq rbx ++ newline ++
													cmp_reg_reg rax rbx ++ newline ++ 
													jge ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i1)-1) do code2 := !code2 ++ compile_instr (List.nth i1 i) done; 
													
													code3 := jmp ("main" ^ string_of_int(!contador_main)) ++ newline ++
													label_jump ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i2)-1) do code4 := !code4 ++ compile_instr (List.nth i2 i) done; 
													
													code5 := label_jump ("main" ^ string_of_int(!contador_main)) ++ newline;
													contador_if := !contador_if + 1;
													contador_main := !contador_main + 1;
													(!code ++ !code2 ++ !code3 ++ !code4 ++ !code5)
											end
										end

                        | SmallEqual (e1, e2) -> (* a<=b *)
										begin
											let code = ref nop in
											let code2 = ref nop in
											let code3 = ref nop in
											let code4 = ref nop in
											let code5 = ref nop in
									
											begin
													code := compile_expr e1 ++
													compile_expr e2 ++
													popq rax ++ newline ++
													popq rbx ++ newline ++
													cmp_reg_reg rax rbx ++ newline ++ 
													jg ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i1)-1) do code2 := !code2 ++ compile_instr (List.nth i1 i) done; 
													
													code3 := jmp ("main" ^ string_of_int(!contador_main)) ++ newline ++
													label_jump ("else" ^ string_of_int(!contador_if)) ++ newline;
													
													for i=0 to ((List.length i2)-1) do code4 := !code4 ++ compile_instr (List.nth i2 i) done; 
													
													code5 := label_jump ("main" ^ string_of_int(!contador_main)) ++ newline;
													contador_if := !contador_if + 1;
													contador_main := !contador_main + 1;
													(!code ++ !code2 ++ !code3 ++ !code4 ++ !code5)
											end
										end
                        end

    | While (t, i) -> (* while while *)
                    begin
                        match t with
                        | Neg t_in -> begin (* o compilador faz pré-processamento *)
                        
                                        match t_in with
                                        | B true -> compile_instr (While (B false,i))

                                        | B false -> compile_instr (While (B true,i))

                                        | Comp (e1,e2) -> begin
															let code = ref nop in
															let code2 = ref nop in
															let code3 = ref nop in
													
															begin
																	code := label_jump ("while" ^ string_of_int(!contador_loop)) ++ newline ++
																	compile_expr e1 ++
																	compile_expr e2 ++
																	popq rax ++ newline ++
																	popq rbx ++ newline ++
																	cmp_reg_reg rax rbx ++ newline ++ 
																	je ("exit" ^ string_of_int(!contador_loop)) ++ newline;
																	
																	for j=0 to ((List.length i)-1) do code2 := !code2 ++ compile_instr (List.nth i j) done; 
																	
																	code3 := jmp ("while" ^ string_of_int(!contador_loop)) ++ newline ++
																	label_jump ("exit" ^ string_of_int(!contador_loop)) ++ newline;
																	
																	contador_loop := !contador_loop + 1;
																	(!code ++ !code2 ++ !code3)
															end
														end

										| Big (e1,e2) -> compile_instr (While (SmallEqual(e1,e2),i))

										| BigEqual (e1,e2) -> compile_instr (While (Small(e1,e2),i))

										| Small (e1,e2) -> compile_instr (While (BigEqual(e1,e2),i))

										| SmallEqual (e1,e2) -> compile_instr (While (Big(e1,e2),i))
	
                                end
                        
                        | B true -> begin
											let code = label_jump ("while" ^ string_of_int(!contador_loop)) in
											let code2 = ref nop in
											let code3 = ref nop in

											begin
													for k=0 to ((List.length i)-1) do code2 := !code2 ++ compile_instr (List.nth i k) done;
									
													code3 := jmp ("while" ^ string_of_int(!contador_loop)) ++
													label_jump ("exit" ^ string_of_int(!contador_loop));
													contador_loop := !contador_loop + 1;
													(code ++ !code2 ++ !code3)
											end
									end

                        | B false -> nop (* não fazer nada *)

                        | Comp (e1, e2) -> (* a==b *)
											begin
												let code = ref nop in
												let code2 = ref nop in
												let code3 = ref nop in
										
												begin
														code := label_jump ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														compile_expr e1 ++
														compile_expr e2 ++
														popq rax ++ newline ++
														popq rbx ++ newline ++
														cmp_reg_reg rax rbx ++ newline ++ 
														jne ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														for j=0 to ((List.length i)-1) do code2 := !code2 ++ compile_instr (List.nth i j) done; 
														
														code3 := jmp ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														label_jump ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														contador_loop := !contador_loop + 1;
														(!code ++ !code2 ++ !code3)
												end
											end

                        | Big (e1, e2) -> (* a>b *)
											begin
												let code = ref nop in
												let code2 = ref nop in
												let code3 = ref nop in
										
												begin
														code := label_jump ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														compile_expr e1 ++
														compile_expr e2 ++
														popq rax ++ newline ++
														popq rbx ++ newline ++
														cmp_reg_reg rax rbx ++ newline ++ 
														jle ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														for j=0 to ((List.length i)-1) do code2 := !code2 ++ compile_instr (List.nth i j) done; 
														
														code3 := jmp ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														label_jump ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														contador_loop := !contador_loop + 1;
														(!code ++ !code2 ++ !code3)
												end
											end
                        
                        | BigEqual (e1, e2) -> (* a>=b *)
											begin
												let code = ref nop in
												let code2 = ref nop in
												let code3 = ref nop in
										
												begin
														code := label_jump ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														compile_expr e1 ++
														compile_expr e2 ++
														popq rax ++ newline ++
														popq rbx ++ newline ++
														cmp_reg_reg rax rbx ++ newline ++ 
														jl ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														for j=0 to ((List.length i)-1) do code2 := !code2 ++ compile_instr (List.nth i j) done; 
														
														code3 := jmp ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														label_jump ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														contador_loop := !contador_loop + 1;
														(!code ++ !code2 ++ !code3)
												end
											end

                        | Small (e1, e2) -> (* a<b *)
											begin
												let code = ref nop in
												let code2 = ref nop in
												let code3 = ref nop in
										
												begin
														code := label_jump ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														compile_expr e1 ++
														compile_expr e2 ++
														popq rax ++ newline ++
														popq rbx ++ newline ++
														cmp_reg_reg rax rbx ++ newline ++ 
														jge ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														for j=0 to ((List.length i)-1) do code2 := !code2 ++ compile_instr (List.nth i j) done; 
														
														code3 := jmp ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														label_jump ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														contador_loop := !contador_loop + 1;
														(!code ++ !code2 ++ !code3)
												end
											end

                        | SmallEqual (e1, e2) -> (* a<=b *)
											begin
												let code = ref nop in
												let code2 = ref nop in
												let code3 = ref nop in
										
												begin
														code := label_jump ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														compile_expr e1 ++
														compile_expr e2 ++
														popq rax ++ newline ++
														popq rbx ++ newline ++
														cmp_reg_reg rax rbx ++ newline ++ 
														jg ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														for j=0 to ((List.length i)-1) do code2 := !code2 ++ compile_instr (List.nth i j) done; 
														
														code3 := jmp ("while" ^ string_of_int(!contador_loop)) ++ newline ++
														label_jump ("exit" ^ string_of_int(!contador_loop)) ++ newline;
														
														contador_loop := !contador_loop + 1;
														(!code ++ !code2 ++ !code3)
												end
											end
					end
					
	| For (c, e1, e2, i) -> 
							begin
								let code = ref nop in
								let code2 = ref nop in
								let code3 = ref nop in
						
								begin
										code := compile_expr e1 ++
										compile_expr e2 ++
										popq rbp ++ newline ++
										popq_var c ++ newline ++
										label_jump ("for" ^ string_of_int(!contador_loop)) ++ newline ++
										cmp_var_reg c rbp ++ newline ++ 
										jl ("exit" ^ string_of_int(!contador_loop)) ++ newline;
										
										for j=0 to ((List.length i)-1) do code2 := !code2 ++ compile_instr (List.nth i j) done; 
										
										code3 := add_val_var 1 c ++ newline ++ jmp ("for" ^ string_of_int(!contador_loop)) ++ newline ++
										label_jump ("exit" ^ string_of_int(!contador_loop)) ++ newline;
										
										contador_loop := !contador_loop + 1;
										(!code ++ !code2 ++ !code3)
								end
							end

    | Nop -> nop (* não fazer nada *)

let compile_program p ofile = (* compilar o programa "p" gerando um fichero .s com o equivalente em assembly x86 *)

    let code = List.map compile_instr p in
    let code = List.fold_right (++) code nop in
    
    let p =
	{ text = start ".text\n.globl main\n" 
		++ glabel "main" ++ newline ++
			code ++
			comment "\tsaída" ++ newline ++
			mov_val_reg 0 rax ++ newline ++
			ret ++ newline ++
			label "print_int" ++ comment "função que imprime o conteúdo de %rsi" ++ newline ++
			movabs "message" rdi ++ newline ++
			call "printf" ++ newline ++
			mov_val_reg 0 rax ++ newline ++
			ret ++ newline;
data = data_definition ".data\n" ++ (data_variables variables)
    }
    in
    let f = open_out ofile in
    let fmt = formatter_of_out_channel f in
    X86.print_program fmt p;
    fprintf fmt "@?";
    close_out f