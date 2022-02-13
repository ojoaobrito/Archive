type comando = Add of int*int | Del of int*int | Link of int*int;; (* tipo próprio para os comandos "LINK", "ADD" e "DEL" *)

let rec existeCaminho (colonias, fim, vizinhos, vizinhosAux, lista, n) = (* função que verifica se há um caminho entre as colónias "a" e "b" *)

                                    let contador = ref 0 in (* variável auxiliar *)
                                    let numVizinhos = ref 0 in (* número de vizinhos de uma dada colónia *)
                                    let tamanhoV = ref (Array.length !vizinhos) in (* número de colónias a avaliar *)
                                    let resposta = ref "NO" in (* resposta à pergunta de haver caminho entre "a" e "b" *)
                                    let temp = ref !tamanhoV in (* variável auxiliar *)

                                    for j=0 to !temp-1 do
                                        if((!vizinhos.(j))>0) then begin
                                            numVizinhos:=(Array.length !(!lista.((!vizinhos.(j))-1)));
                                            for i=0 to !numVizinhos-1 do
                                                if((!colonias.(!vizinhos.(j)-1).((!(!lista.(!vizinhos.(j)-1)).(i))-1))=true) then begin
                                                    if(((!(!lista.(!vizinhos.(j)-1))).(i))=fim) then begin resposta:="YES"; numVizinhos:=i; temp:=j end
                                                    else if(!vizinhosAux.(((!(!lista.(!vizinhos.(j)-1))).(i))-1)=1)then vizinhos:=(Array.append !vizinhos [|((!(!lista.(!vizinhos.(j)-1))).(i))|])
                                                end;
                                            done;
                                            !vizinhosAux.(!vizinhos.(j)-1)<-0;
                                            !vizinhos.(j)<-(-(!vizinhos.(j)));
                                        end
                                        else contador:=(!contador+1)
                                    done;

                                    if((!contador)=(!tamanhoV)) then resposta:="NO";

                                    if(!resposta="NO" && (!contador)!=(!tamanhoV)) then resposta:=existeCaminho(colonias,fim,vizinhos,vizinhosAux,lista,n);

                                    !resposta;;

let lerComando () = (* função para ler os comandos *)

                let a,b,c = Scanf.sscanf (read_line ()) " %s %d %d" (fun a b c -> a,b,c) in

                match a with
                | "ADD" -> Add (b,c)
                | "DEL" -> Del (b,c)
                | _ -> Link (b,c);;

let n,p = Scanf.sscanf (read_line ()) " %d %d" (fun a b -> a,b);; (* número de colónias e de condições *)

let colonias = Array.make_matrix n n false;; (* matriz de adjacência das colónias *)
let lista = ref (Array.make n (ref [||]));; (* lista de adjacência das colónias, auxiliar da matriz "colonias" *)

let final = ref "";; (* resposta final *)

let com = ref (Add (0,0)) in

for i=0 to p-1 do
    com:=lerComando();
    match !com with
    | Add (a,b) -> begin colonias.(a-1).(b-1)<-true; colonias.(b-1).(a-1)<-true; !lista.(a-1)<-(ref(Array.append !(!lista.(a-1)) [|b|])); !lista.(b-1)<-(ref(Array.append !(!lista.(b-1)) [|a|])) end;
    | Del (a,b) -> begin colonias.(a-1).(b-1)<-false; colonias.(b-1).(a-1)<-false end;
    | Link (a,b) -> final:=(!final ^ existeCaminho((ref colonias),b,(ref [|a|]),(ref(Array.make n 1)),lista,n) ^ "\n");
done;
;;

let() = Printf.printf "%s" !final;;
