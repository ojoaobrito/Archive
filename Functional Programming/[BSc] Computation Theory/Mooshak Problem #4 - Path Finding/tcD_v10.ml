type comando = Add of int*int | Del of int*int | Link of int*int;; (* tipo próprio para os comandos "LINK", "ADD" e "DEL" *)

exception Sair;; (* parar de avaliar colónias na função "existeCaminho" *)

let existeCaminho (apagados, origem, fim, vizinhos, vizinhosAux, lista, resposta) = (* função que verifica se há um caminho entre as colónias "a" e "b" *)

									(* vizinhosAux - vetor que indica quais as colónias que já foram visitadas, neste pedido de "LINK" *)

                                    let controlo = ref "YES" in (* variável auxiliar *)
                                    let correr = ref true in (* variável que determina se é para continuar ou não a função *)
                                    let temp = ref [||] in (* variável auxiliar *)
                                    let tamanhoVizinhos = ref (Array.length !vizinhos) in (* número de colónias a avaliar *)
                                    let tamanhoApagados = ref (Array.length !apagados) in (* múmero de caminhos diretos apagados *)
                                    let numVizinhos = ref 0 in (* número de vizinhos de uma dada colónia *)

                                    !vizinhosAux.(origem-1)<-0; (* a colónia de "origem" não é para ser considerada *)

                                    try begin
                                        while (!correr)=true do begin
                                            for j=0 to !tamanhoVizinhos-1 do begin (* percorrer os vizinhos *)
                                                numVizinhos:=(Array.length !(!lista.((!vizinhos.(j))-1))); (* vizinhos dos vizinhos *)
                                                for i=0 to !numVizinhos-1 do begin
                                                    for k=0 to !tamanhoApagados-1 do (* ver se alguma colónia foi afetada pelos caminhos apagados *)
                                                        match !apagados.(k) with
                                                        | (a,b) -> if(((!vizinhos.(j))=a && ((!(!lista.(!vizinhos.(j)-1))).(i))=b) || (!vizinhos.(j))=b && ((!(!lista.(!vizinhos.(j)-1))).(i))=a || (origem=a && (!vizinhos.(j))=b) || (origem=b && (!vizinhos.(j))=a)) then controlo:="NO";
                                                    done;
                                                    if(!controlo="YES") then begin
                                                        if(((!(!lista.(!vizinhos.(j)-1))).(i))=fim || (!vizinhos.(j))=fim) then begin resposta:="YES"; raise Sair end (* caso ideal *)
                                                        else if(!vizinhosAux.(((!(!lista.(!vizinhos.(j)-1))).(i))-1)=1)then temp:=(Array.append !temp [|((!(!lista.(!vizinhos.(j)-1))).(i))|]) (* mais uma colónia a considerar *)
                                                    end;
                                                    controlo:="YES";
                                                end;
                                                done;
                                                !vizinhosAux.(!vizinhos.(j)-1)<-0; (* marcar a colónia como visitada *)
                                            end
                                        done;
                                        vizinhos:=(Array.copy (!temp)); (* guardar os novos vizinhos, ou seja, as novas colónias a considerar *)
                                        tamanhoVizinhos:=(Array.length !vizinhos);
                                        if((!tamanhoVizinhos)=0) then begin resposta:="NO"; raise Sair end (* não há mais nada a fazer *)
                                        else temp:=[||];
                                    end
                                    done;
                                    end

                                    with Sair -> ();;

let lerComando () = (* função para ler os comandos *)

                let a,b,c = Scanf.sscanf (read_line ()) " %s %d %d" (fun a b c -> a,b,c) in
                match a with
                | "ADD" -> Add (b,c)
                | "DEL" -> Del (b,c)
                | _ -> Link (b,c);;

let n,p = Scanf.sscanf (read_line ()) " %d %d" (fun a b -> a,b);; (* número de colónias e de condições *)

let apagados = ref (Array.make 0 (-1,-1));; (* vetor dos caminhos diretos apagados *)
let lista = ref (Array.make n (ref [||]));; (* vetor/lista de adjacência das colónias *)

let final = ref "";; (* resposta final *)
let resposta = ref "";; (* respostas intermédias *)

let com = ref (Add (0,0)) in (* comandos introduzidos *)

for i=0 to p-1 do
    com:=lerComando();
    match !com with
    | Add (a,b) -> !lista.(a-1)<-(ref(Array.append !(!lista.(a-1)) [|b|])); !lista.(b-1)<-(ref(Array.append !(!lista.(b-1)) [|a|]));
    | Link (a,b) -> if(a=b) then resposta:="YES" else existeCaminho(apagados,a,b,(ref(Array.copy (!(!lista.(a-1))))),(ref(Array.make n 1)),lista,resposta); final:=(!final ^ !resposta ^ "\n");
    | Del (a,b) -> apagados:=(Array.append !apagados [|(a,b)|]);
done;
;;

let() = Printf.printf "%s" !final;;
