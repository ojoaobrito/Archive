package escoladeconducao;

import java.io.*;
import java.util.*;

public class Horario implements Serializable {
    private int dia;
    private int hora;
    private String nomep;
    private String tipoAula;
    
    public Horario() {
        dia = 0;
        hora = 0;
        nomep = "";
        tipoAula = "";
    }

    public int getDia() {
        return(dia);
    }
    
    public String imprimeDia() {
       if(dia==1)
            return("Segunda-feira");
        else if(dia==2)
            return("Terça-feira");
        else if(dia==3)
            return("Quarta-feira");
        else if(dia==4)
            return("Quinta-feira");
        else if(dia==5)
            return("Sexta-feira");
       return("");
    }
    public void setDia(int dia) {
        this.dia=dia;
    }
    
    public int getHora() {
        return hora;
    }
    public void setHora(int hora) {
        this.hora = hora;
    }

    public String getnomeP() {
        return nomep;
    }
    public void setnomeP(String nomep) {
        this.nomep = nomep;
    }

    public String getTipoAula() {
        return tipoAula;
    }
    public void setTipoAula(String tipoAula) {
        this.tipoAula = tipoAula;
    }
    
    public boolean equals(Object obj){
        if(obj!=null && this.getClass()==obj.getClass()){
            Horario x=(Horario) obj;
            return(this.dia==(x.dia)&& this.hora==(x.hora)&&this.nomep.equals(x.nomep));
        }
        else{
            return (false);
        }
    }
    
    public Object clone(){
        Horario copia=new Horario();
        copia.setDia(this.dia);
        copia.setHora(this.hora);
        copia.setnomeP(nomep);
        copia.setTipoAula(tipoAula);
    
        return (copia);
    }
    
}
