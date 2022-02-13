/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package numeros;

/**
 *
 * @author a37880
 */
public class Numeros {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int i, soma=0;
        
        for(i=1; i<10; i++){
            
            int a=myinputs.Ler.umInt();
            soma=soma+i;
        }
        
        System.out.println("A soma é: "+soma);
    }
    
    
}
