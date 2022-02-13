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
import java.io.*;

public class Aula4 {

    /**
     * @param args the command line arguments
     * @throws java.io.IOException
     */
    public static void main(String[] args) throws IOException {
        
        Contador c1;
        int i;
        
        c1=new Contador();
        
        c1.changeConta();
        
        i=c1.getConta();
        
        c1.toString();
        System.out.println(+i);
    }
    
}
