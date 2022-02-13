package aula4;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author a37880
 * @throws IOException
 */

import java.io.IOException;

public class Contador {
    
    private int conta;
    
    public Contador() {
        
        conta=0;
    }
    
    public void changeConta() throws IOException{
        
        int i;
        
        i=System.in.read();
       
        conta=i;   
   
    }
    
    public int incConta(){
        
        conta++;
        return conta;
    }
    
    public int getConta(){
        
        return conta;
    }
    
    public String toString(){
        
       return("O valor de conta é: ");
    }
}
