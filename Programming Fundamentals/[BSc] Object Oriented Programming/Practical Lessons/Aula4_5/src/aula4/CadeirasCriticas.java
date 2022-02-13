package aula4;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author a37880
 */
public class CadeirasCriticas {
    
    private String curso;
    private String disciplinas[]=new String[3];
    
    public CadeirasCriticas(){
    
        curso="";
}
    
    public String getCurso(){
        
        return(curso);
    }
    
    public void setCurso(String curso){
        
        this.curso=curso;
    }
    
    public String getDisciplinas1(){
        
        return(disciplinas[0]);
    }
    
    public String getDisciplinas2(){
        
        return(disciplinas[1]);
    }
    
    public String getDisciplinas3(){
        
        return(disciplinas[2]);
    }
    
    public void setDisciplinas(String[] disciplinas){
        
        this.disciplinas[0]=disciplinas[0];
        this.disciplinas[1]=disciplinas[1];
        this.disciplinas[2]=disciplinas[2];
        
    }
    
    public String toString(){
        
        return("O curso é o de " +curso +", sendo que as disciplinas críticas são " +disciplinas[0] + ", " +disciplinas[1] +" e " +disciplinas[2] +".");
    }
}
