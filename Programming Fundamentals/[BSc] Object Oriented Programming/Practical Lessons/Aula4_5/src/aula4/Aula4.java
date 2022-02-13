/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula4;

/**
 *
 * @author a37880
 */

import myinputs.Ler.*;

public class Aula4 {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        
        CadeirasCriticas c1;
        String curso="";
        String [] disciplinas= new String[3];
        
        c1=new CadeirasCriticas();
        
        System.out.println();
        System.out.println("Escreva o seu curso, por favor: ");
        curso=myinputs.Ler.umaString();
                
        c1.setCurso(curso);
        
        System.out.println();
        System.out.println("Agora, diga quais as disciplinas mais difíceis no seu curos: ");
        
        for(int i=0; i<3; i++){
            
        disciplinas[i]=myinputs.Ler.umaString();
        
        }
        
        c1.setDisciplinas(disciplinas);
        
        System.out.println();
        System.out.println(c1.toString());
        
    }
    
}
