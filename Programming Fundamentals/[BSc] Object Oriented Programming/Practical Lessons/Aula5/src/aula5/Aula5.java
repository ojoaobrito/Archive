/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula5;

/**
 *
 * @author a37880
 */

import java.util.*;
import myinputs.Ler.*;
public class Aula5 {

    /**
     * @param args the command line arguments
     * @return 
     */
    public static void main(String[] args) {
        
        Jogador[] j1=new Jogador[30];
        int controlo=0, j=0, k=0, i=0, aux=0;
        String nome="";
        double salario=0.0;
        
       while(true){
           
           System.out.println();
           System.out.println(" >> FEDERAÇÃO PORTUGUESA DE FUTEBOL << ");
           System.out.println();
           System.out.println("(" +k +"/30) jogadores registados");
           System.out.println();
           System.out.println("1. LISTAR TODOS OS JOGADORES");
           System.out.println("2. CONSULTAR JOGADOR ESPECÍFICO E RESPETIVOS DADOS");
           System.out.println("3. ALTERAR DADOS EXISTENTES");
           System.out.println("4. CRIAR NOVOS DADOS DE JOGADOR");
           System.out.println("5. EXIT");
           System.out.println();
           System.out.print("> ");
           controlo=myinputs.Ler.umInt();
       
           switch(controlo){
               
               case 1: if(k!=0){
                   
                        System.out.println();
                        
                        for(i=0; i<k; i++){
                            
                            System.out.println(j1[i].toString());
                        }
                        
                        System.out.println();
               }
               
               else{
                   
                   System.out.println();
                   System.out.print("A BASE DE DADOS ESTÁ VAZIA!");
                   System.out.println();
               }
               
               break;
               
      
               case 2: 
                        if(k!=0){
                            
                       System.out.println();
                       System.out.print("INTRODUZA O NOME DO JOGADOR A PROCURAR: ");
                       nome=myinputs.Ler.umaString();
                       
                       for(i=0; i<k; i++){
                           
                           if(Objects.equals(j1[i].getNome(), nome)){
                               
                               System.out.println(j1[i].toString());
                               break;
                           }
                           
                           else if(i==(k-1)){
                               
                               System.out.println();
                               System.out.println("NÃO EXISTE NENHUM JOGADOR COM ESSE NOME...");
                               System.out.println();
                               break;
                           }
                       }
                       
                       }
                        
                        else{
                            
                        System.out.println();
                        System.out.println("A BASE DE DADOS ESTÁ VAZIA!");
                        System.out.println();
                            
                        }
                            
                            
                       break;
                       
               case 3: 
                       if(k!=0){
                           
                       System.out.println();
                       System.out.print("INTRODUZA O NOME DO JOGADOR A PROCURAR: ");
                       nome=myinputs.Ler.umaString();
                       
                       for(i=0; i<k; i++){
                           
                           if(Objects.equals(j1[i].getNome(), nome)){
                               
                               System.out.println();
                               System.out.println("O QUE PRETENDE ALTERAR?");
                               System.out.println();
                               
                               while(true){
                                   
                               if (aux==1){break;}
                               
                               System.out.println("1- NOME");
                               System.out.println("2- SALÁRIO");
                               System.out.println("3- GOLOS");
                               System.out.println();
                               System.out.println("4- VOLTAR");
                               System.out.println();
                               System.out.print("> ");
                               j=myinputs.Ler.umInt();
                                   
                                    switch(j){
                                        
                                        case 1:  System.out.println();
                                                 System.out.print("INTRODUZA O NOVO NOME: ");
                                                 nome=myinputs.Ler.umaString();
                                                 j1[i].setNome(nome);
                                                 break;
                                    
                                        case 2: System.out.println();
                                                System.out.print("INTRODUZA A PERCENTAGEM COM QUE ATUALIZAR O SALÁRIO (%): ");
                                                double percentagem=myinputs.Ler.umDouble();
                                                j1[i].alteraSalario(percentagem);
                                                break;
                                    
                                        case 3: System.out.println();
                                                System.out.print("QUAL JORNADA QUER ALTERAR? ");
                                                int jornada=myinputs.Ler.umInt();
                                                System.out.print("QUANTOS GOLOS MARCOU? ");
                                                int golos=myinputs.Ler.umInt();
                                                j1[i].alteraGolos(jornada,golos);
                                                break;
                                                
                                        case 4: aux=1;
                                    
                                        default: System.out.println();
                                                 System.out.println("POR FAVOR INTRODUZA UM VALOR VÁLIDO!");
                                                 System.out.println();
                                    }
                               }
                           
                                break;
                           }
                           
                           else if(i==(k-1)){
                               
                               System.out.println();
                               System.out.println("NÃO EXISTE NENHUM JOGADOR COM ESSE NOME...");
                               System.out.println();
                               break;
                           }
                       }
                           
                       }
                       
                       else{
                           
                        System.out.println();
                        System.out.println("A BASE DE DADOS ESTÁ VAZIA!");
                        System.out.println();
                           
                       }
                   
                       
                       break;
                   
               case 4:  if(k<30){
                            
                       j1[k]=new Jogador();
                   
                       System.out.println();
                       System.out.print("INTRODUZA O NOME DO JOGADOR: ");
                       nome=myinputs.Ler.umaString();
                       j1[k].setNome(nome);
                       
                       System.out.println();
                       System.out.print("INTRODUZA O SALÁRIO DO JOGADOR: ");
                       salario=myinputs.Ler.umDouble();
                       j1[k].setSalario(salario);
                       
                       k++;
                       }
               
                    else{
                       
                        System.out.println();
                        System.out.println("A BASE DE DADOS ENCHEU!");
                        System.out.println();
                        k=30;
                    }
                       
                       break;
            
                       
               case 5: System.out.println();
                       System.out.println("ADEUS!");
                       System.out.println();
                       System.exit(0);
                   
               default: System.out.println();
                        System.out.println("POR FAVOR INTRODUZA UM VALOR VÁLIDO!");
                        System.out.println();
           }
       
       
       
       
       
       }
        
        
    }
    
}
