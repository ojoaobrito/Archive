
package escoladeconducao;
import java.util.*;
import java.io.*;

public class Pessoa implements Serializable{
    
    protected String nome;
    protected int numero;
    protected ArrayList <Horario> horario;

    public Pessoa(String Nome, int numero) {
        this.nome = Nome;
        this.numero = numero;
        horario=new ArrayList <Horario>();
    }    
    public Pessoa(String Nome) {
        this.nome = Nome;
        horario=new ArrayList <Horario>();
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
    public void setHorario(ArrayList<Horario> Horario) {   
        this.horario=(ArrayList<Horario>)horario.clone();   
    }
     public boolean checkHorario(Horario horario){
       return(this.horario.contains(horario));
    }
    public void addHorario(Horario horario){
        if(checkHorario(horario)==false){
            this.horario.add(horario);
        }
    }
    public void removeHorario(Horario horario){
        if(checkHorario(horario)==true){
            this.horario.remove(horario);
        }
    }  

    @Override
    public String toString() {
        return "Pessoa{" + "nome=" + nome + ", numero=" + numero + '}';
    }
    public String toFile() {
        return (numero + " " + nome); //FALTA PASSAR O HORARIO!!!!!!!!!!!!!!!!!
    }
            
    public boolean equals(Object obj){
    
        if(obj!=null && this.getClass()==obj.getClass()){
        Pessoa x=(Pessoa) obj;
        return(this.nome==(x.nome)&& this.horario.equals(x.horario)&&this.numero==(x.numero));
        }else{
        return false;
        }
    }
    
    public Object clone(){
    Pessoa copia=new Pessoa(this.nome,this.numero);
    copia.horario=(ArrayList<Horario>)this.horario.clone();
    
    return copia;
    }
    
    


}
