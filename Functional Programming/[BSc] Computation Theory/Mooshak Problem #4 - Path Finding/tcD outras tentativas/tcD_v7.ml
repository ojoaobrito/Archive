type comando = Add of int*int | Del of int*int | Link of int*int;;

let adicionaVizinho (vizinhos, elemento) = 

                    let tamanho = ref (Array.length !vizinhos) in
                    let resposta = ref "YES" in

                    for i=0 to !tamanho-1 do
                        if(!vizinhos.(i)=elemento || !vizinhos.(i)=(-elemento)) then begin resposta:="NO"; tamanho:=i end
                    done;

                    !resposta;;

let existeCaminho (colonias, origem, fim, vizinhos, n) = (* função que verifica se há um caminho entre as colónias "a" e "b" *)

                                    let contador = ref 0 in
                                    let numColonias = ref n in
                                    let tamanhoV = ref (Array.length !vizinhos) in
                                    let resposta = ref "NO" in
                                    let correr = ref true in

                                    while (!correr)=true do begin
                                        for j=0 to !tamanhoV-1 do
                                            if((!vizinhos.(j))>0) then begin
                                                for i=0 to !numColonias-1 do
                                                    if(!colonias.((!vizinhos.(j))-1).(i)=1 && (i+1)=fim) then begin resposta:="YES"; numColonias:=i; tamanhoV:=(j-2); correr:=false end
                                                    else if(!colonias.(!vizinhos.(j)-1).(i)=1) then if(adicionaVizinho(vizinhos,(i+1))="YES") then vizinhos:=(Array.append !vizinhos [|(i+1)|])
                                                done;
                                                !vizinhos.(j)<-(-(!vizinhos.(j)))
                                            end
                                            else contador:=(!contador+1)
                                        done;
                                        if((!contador)!=(!tamanhoV)) then begin tamanhoV:=(Array.length !vizinhos); contador:=0 end
                                        else begin resposta:="NO"; correr:=false end;
                                        end;
                                    done;

                                    !resposta;; 

let n,p = Scanf.sscanf (read_line ()) " %d %d" (fun a b -> a,b);;

let ler_comando () =
  let a,b,c = Scanf.sscanf (read_line ()) " %s %d %d" (fun a b c -> a,b,c) in
  match a with
  | "ADD" -> Add (b,c)
  | "DEL" -> Del (b,c)            
  | _ -> Link (b,c);;

let colonias = Array.make_matrix n n 0;; (* matriz de adjacência das colónias *)

let final = ref "";; (* resposta final *)

let com = ref (Add (0,0)) in
        
    for i=0 to p-1 do
        Printf.printf "%d\n" (i+1);
        com:=ler_comando();
        match !com with
        | Add (a,b) -> begin colonias.(a-1).(b-1)<-1; colonias.(b-1).(a-1)<-1 end;
        | Del (a,b) -> begin colonias.(a-1).(b-1)<-0; colonias.(b-1).(a-1)<-0 end;
        | Link (a,b) -> final:=(!final ^ existeCaminho((ref colonias),a,b,(ref [|a|]),n) ^ "\n"); 
    done;
;;

let() = Printf.printf "%s" !final;;