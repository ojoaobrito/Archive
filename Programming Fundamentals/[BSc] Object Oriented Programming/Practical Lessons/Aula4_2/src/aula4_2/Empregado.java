/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula4_2;

/**
 *
 * @author a37880
 */
public class Empregado {
    
    private long nss;
    private String nome;
    private double salario;
    
    public Empregado(){
        
        nss=0;
        salario=0.0;
    }
    
    public long getNss(){
        
        return(nss);
    }
    
    public String getNome(){
        
        return(nome);
    }
    
    public double getSalario(){
        
        return(salario);
    }
    
    
}
