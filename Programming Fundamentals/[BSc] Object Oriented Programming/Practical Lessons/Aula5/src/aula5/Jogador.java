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
public class Jogador {
    
    private String nome;
    private double salario;
    private int[] golos=new int[34];
    
    public Jogador(){
        
        this.nome="";
        this.salario=0.0;
    }
    
    public String getNome(){
        
        return(this.nome);
    }
    
    public double getSalario(){
        
        return(this.salario);
    }
    
    public int[] getGolos(){
        
        return(golos);
    }
     
    public void setNome(String nome){
        
        this.nome=nome;
    }
    
    public void setSalario(double salario){
        
        this.salario=salario;
    }
    
    public void alteraSalario(double percentagem){
        
        this.salario=((this.salario)+((this.salario)*(percentagem/100)));
    }
    
    public int totalGolos(){
        
        int soma =0;
        
        for(int i=0; i<34; i++){
            
           soma=soma+golos[i];
        }
        
        return(soma);
    }
    
    public void alteraGolos(int jornada, int golos){
        
        this.golos[jornada]=golos;
    }
    
    public String toString(){
        
        return("" +this.nome +" (SALARIO: " +this.salario +"€ / GOLOS:  " +totalGolos() +" golos).");
    }
    
    
    
    
    
}
