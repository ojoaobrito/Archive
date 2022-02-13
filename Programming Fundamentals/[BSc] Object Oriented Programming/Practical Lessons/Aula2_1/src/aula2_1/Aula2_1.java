/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula2_1;

/**
 *
 * @author a37880
 */

import java.io.*;
public class Aula2_1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        
        BufferedReader canal;
        canal=new BufferedReader (new InputStreamReader(System.in));
        
        System.out.println("Escreva um inteiro: ");
        
        String s=canal.readLine();
        int i= Integer.parseInt(s);
        
        System.out.println("O inteiro foi: "+i);
        
        
    }
    
}
