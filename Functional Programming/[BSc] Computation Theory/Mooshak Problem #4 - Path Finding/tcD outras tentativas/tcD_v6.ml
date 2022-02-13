type comando = Add of int*int | Del of int*int | Link of int*int;; (* tipo próprio para os comandos "LINK", "ADD" e "DEL" *)

let adicionaVizinho (vizinhos, elemento) = (* função auxiliar à "existeCaminho", verifica se o elemento "elemento" deve ser, ou não, adicionado ao veotr "vizinhos" *)

                    let tamanho = ref (Array.length !vizinhos) in
                    let resposta = ref "YES" in

                    for i=0 to !tamanho-1 do
                        if(!vizinhos.(i)=elemento || !vizinhos.(i)=(-elemento)) then begin resposta:="NO"; tamanho:=i end
                    done;

                    !resposta;;

let rec existeCaminho (colonias, origem, fim, vizinhos, lista) = (* função que verifica se há um caminho entre as colónias "a" e "b" *)

                                    let contador = ref 0 in
                                    let numVizinhos = ref 0 in
                                    let tamanhoV = ref (Array.length !vizinhos) in
                                    let resposta = ref "NO" in
                                    let temp = ref !tamanhoV in

                                    for j=0 to !temp-1 do
                                        if((!vizinhos.(j))>0) then begin
                                            numVizinhos:=(Array.length !(!lista.((!vizinhos.(j))-1)));
                                            for i=0 to !numVizinhos-1 do
                                                if((!colonias.(!vizinhos.(j)-1).((!(!lista.(!vizinhos.(j)-1)).(i))-1))=1) && (((!(!lista.(!vizinhos.(j)-1))).(i))=fim) then begin resposta:="YES"; numVizinhos:=i; temp:=j end
                                                else if((!colonias.(!vizinhos.(j)-1).((!(!lista.(!vizinhos.(j)-1)).(i))-1))=1) then if((adicionaVizinho(vizinhos,((!(!lista.(!vizinhos.(j)-1))).(i))))="YES") then vizinhos:=(Array.append !vizinhos [|((!(!lista.(!vizinhos.(j)-1))).(i))|])
                                            done;
                                            !vizinhos.(j)<-(-(!vizinhos.(j)));
                                        end
                                        else contador:=(!contador+1)
                                    done;

                                    if((!contador)=(!tamanhoV)) then resposta:="NO";

                                    if(!resposta="NO" && (!contador)!=(!tamanhoV)) then resposta:=existeCaminho(colonias,origem,fim,vizinhos,lista);
                                    
                                    !resposta;; 

let n,p = Scanf.sscanf (read_line ()) " %d %d" (fun a b -> a,b);;

let ler_comando () =
  let a,b,c = Scanf.sscanf (read_line ()) " %s %d %d" (fun a b c -> a,b,c) in
  match a with
  | "ADD" -> Add (b,c)
  | "DEL" -> Del (b,c)            
  | _ -> Link (b,c);;

let colonias = Array.make_matrix n n 0;; (* matriz de adjacência das colónias *)
let lista = ref (Array.make n (ref [||]));; (* lista de adjacência das colónias, auxiliar da matriz "colonias" *)

let final = ref "";; (* resposta final *)

let com = ref (Add (0,0)) in
        
    for i=0 to p-1 do
        Printf.printf "%d\n" (i+1);
        com:=ler_comando();
        match !com with
        | Add (a,b) -> begin colonias.(a-1).(b-1)<-1; colonias.(b-1).(a-1)<-1; !lista.(a-1)<-(ref(Array.append !(!lista.(a-1)) [|b|])); !lista.(b-1)<-(ref(Array.append !(!lista.(b-1)) [|a|])) end;
        | Del (a,b) -> begin colonias.(a-1).(b-1)<-0; colonias.(b-1).(a-1)<-0 end;
        | Link (a,b) -> final:=(!final ^ existeCaminho((ref colonias),a,b,(ref [|a|]),lista) ^ "\n"); 
    done;
;;

let() = Printf.printf "%s" !final;;