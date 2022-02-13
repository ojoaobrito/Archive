/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package totoloto;

/**
 *
 * @author a37880
 */

import java.lang.Math;
import java.util.*;
public class Totoloto {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)  {
       
        int rand, i;
        
        Scanner teclado=new Scanner(System.in);
       System.out.println("");
       System.out.println(">> TOTOLOTO 1.0 <<");
       System.out.println("");
       
       System.out.println("Escolha a sua chave (de 1 a 49):");
       
       System.out.print("1º num: ");
       int a= teclado.nextInt();
       System.out.print("2º num: ");
       int b=teclado.nextInt();
       System.out.print("3º num: ");
       int c=teclado.nextInt();
       System.out.print("4º num: ");
       int d=teclado.nextInt();
       System.out.print("5º num: ");
       int e=teclado.nextInt();
       System.out.print("6º num: ");
       int f=teclado.nextInt();
    
     
       System.out.println("A chave certa é: ");
       System.out.println("");
               
       for(i=0; i<6; i++){
           
       rand=(int)((Math.random())*3+1);
       System.out.print(""+rand);
       System.out.print(" ");
       }
       
       System.out.println("");
 
    }
    
}
