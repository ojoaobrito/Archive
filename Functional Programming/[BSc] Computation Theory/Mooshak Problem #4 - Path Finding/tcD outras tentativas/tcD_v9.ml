type comando = Add of int*int | Del of int*int | Link of int*int;; (* tipo próprio para os comandos "LINK", "ADD" e "DEL" *)
    
let rec existeCaminho (apagados, fim, vizinhos, vizinhosAux, lista) = (* função que verifica se há um caminho entre as colónias "a" e "b" *)

                                    let contador = ref 0 in (* variável auxiliar *)
                                    let tamanhoApagados = ref (Array.length !apagados) in
                                    let controlo = ref "YES" in (* variável auxiliar *)
                                    let numVizinhos = ref 0 in (* número de vizinhos de uma dada colónia *)
                                    let tamanhoVizinhos = ref (Array.length !vizinhos) in (* número de colónias a avaliar *)
                                    let resposta = ref "NO" in (* resposta à pergunta de haver caminho entre "a" e "b" *)
                                    let temp = ref !tamanhoVizinhos in (* variável auxiliar *)

                                    for j=0 to !temp-1 do
                                        
                                        if((!vizinhos.(j))>0) then begin
                                            numVizinhos:=(Array.length !(!lista.((!vizinhos.(j))-1))); (* número de vizinhos de determinada colónia *)
                                            for i=0 to !numVizinhos-1 do begin
                                                for k=0 to !tamanhoApagados-1 do
                                                    match !apagados.(k) with
                                                    | (a,b) -> if(((!vizinhos.(j))=a && ((!(!lista.(!vizinhos.(j)-1))).(i))=b) || (!vizinhos.(j))=b && ((!(!lista.(!vizinhos.(j)-1))).(i))=a) then controlo:="NO";
                                                done;
                                                if(!controlo="YES") then begin
                                                    if(((!(!lista.(!vizinhos.(j)-1))).(i))=fim) then begin resposta:="YES"; numVizinhos:=i; temp:=j end
                                                    else if(!vizinhosAux.(((!(!lista.(!vizinhos.(j)-1))).(i))-1)=1)then vizinhos:=(Array.append !vizinhos [|((!(!lista.(!vizinhos.(j)-1))).(i))|])
                                                end;
                                                controlo:="YES";
                                            end;
                                            done;
                                            controlo:="YES";
                                            !vizinhosAux.(!vizinhos.(j)-1)<-0;
                                            !vizinhos.(j)<-(-(!vizinhos.(j)));
                                        end

                                        else contador:=(!contador+1)
                                    done;

                                    if((!contador)=(!tamanhoVizinhos)) then resposta:="NO";

                                    if(!resposta="NO" && (!contador)!=(!tamanhoVizinhos)) then resposta:=existeCaminho(apagados,fim,vizinhos,vizinhosAux,lista);
                                    
                                    !resposta;; 

let lerComando () = (* função para ler os comandos *)
  
                let a,b,c = Scanf.sscanf (read_line ()) " %s %d %d" (fun a b c -> a,b,c) in
  
                match a with
                | "ADD" -> Add (b,c)
                | "DEL" -> Del (b,c)            
                | _ -> Link (b,c);;

let n,p = Scanf.sscanf (read_line ()) " %d %d" (fun a b -> a,b);; (* número de colónias e de condições *)

let apagados = ref (Array.make 0 (-1,-1));; (* vetor dos caminhos apagados *)
let lista = ref (Array.make n (ref [||]));; (* lista de adjacência das colónias *)

let final = ref "";; (* resposta final *)

let com = ref (Add (0,0)) in
        
for i=0 to p-1 do
    com:=lerComando();
    match !com with
    | Add (a,b) -> !lista.(a-1)<-(ref(Array.append !(!lista.(a-1)) [|b|])); !lista.(b-1)<-(ref(Array.append !(!lista.(b-1)) [|a|]));
    | Link (a,b) -> final:=(!final ^ existeCaminho(apagados,b,(ref [|a|]),(ref(Array.make n 1)),lista) ^ "\n");
    | Del (a,b) -> apagados:=(Array.append !apagados [|(a,b)|]); 
done;
;;

let() = Printf.printf "%s" !final;;