package escoladeconducao;
import java.io.*;

import java.util.ArrayList;
import myinputs.Ler;

public class Professor extends Pessoa implements Serializable {
    private static int ult = 0;
    private float salario;
    
    
    public Professor(String nome){
       super(nome, ult);
       ult++;
    }
    public Professor(String nome, float salario){
       super(nome, ult);
       this.salario = salario;
       ult++;
    }
    
    public void setUlt(int ultimo) {
        this.ult = ultimo;
    }
    public int getUlt() {
        return(ult);
    }
    
    public float getSalario() {
        return salario;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }

    public ArrayList<Horario> getHorario() {
        return horario;
    }
    public void setHorario(ArrayList<Horario> horario) {
        this.horario = horario;
    }
    public void addHorario(Horario horario) {
        super.addHorario(horario);
    }
    public void removeHorario(Horario horario) {
        super.removeHorario(horario);
    }
    public boolean checkHorario(Horario horario) {
        return(super.checkHorario(horario));
    }
    
    public int mostrarHorarioDisponivel(int dia) {
        int h9=0,h11=0,h14=0,h16=0,f=0;
        for(int i=0;i<super.horario.size();i++) {
            if(super.horario.get(i).getDia() == dia) {
                if(super.horario.get(i).getHora()==9){
                    h9=1;
                }
                if(super.horario.get(i).getHora()==11){
                    h11=1;
                }
                if(super.horario.get(i).getHora()==14){
                    h14=1;
                }
                if(super.horario.get(i).getHora()==16){
                    h16=1;
                }
            }
        }
       
        if(h9==0){
           
            f++;
            System.out.println(f+") 9h-11h");
        }
        if(h11==0){
             
            f++;
            System.out.println(f+") 11h-13h");
        }
        if(h14==0){
            
            f++;
            System.out.println(f+") 14h-16h");
        }
        if(h16==0){
             
            f++;
            System.out.println(f+") 16h-18h");
        }
        if(f!=0) {
            System.out.print("Opção: ");
            int hora=Ler.umInt();
            int d=0;
            if(h9==0){
                d++;
                if(d==hora)
                    return 9;
            }
            if(h11==0){
                d++;
                if(d==hora)
                    return 11;
            }
            if(h14==0){
                d++;
                if(d==hora)
                    return 14;
            }
            if(h16==0){
                d++;
                if(d==hora)
                    return 16;
            }
        }
      return 0;  
    }
    public boolean existeDia(ArrayList<Horario> h,int dia){
        for(int i=0;i<h.size();i++){
            if(h.get(i).getDia()==dia)
                return true;     
        
        }  
        return false;
    }
    
    
    @Override
    public String toString() {
        return "Professor{" + "salario=" + salario + '}' + super.toString();
    }
    
}
