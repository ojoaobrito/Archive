package escoladeconducao;
import java.io.*;

public class Aluno extends Pessoa implements Serializable {
    
    private static int ult = 0;
    private String categoria;
    //private Aulas aulas;
    
    public  Aluno (String nome){
       super(nome,ult);
       ult++;
    }
    
    public void setUlt(int ultimo) {
        this.ult = ultimo;
    }
    public int getUlt() {
        return(ult);
    }
    
    @Override
    public String toString() {
        return "Aluno{" + "categoria=" + categoria + ", aulas=" + super.toString() + '}';
    }
    

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(int categoria) {
        if(categoria==1)
            this.categoria = "A";
        else if(categoria==2)
            this.categoria = "B";
        else if(categoria==3)
            this.categoria = "A+B";
        else if(categoria==4)
            this.categoria = "C";
        else if(categoria==5)
            this.categoria = "D";
    }
    
    public void setNome(String nome){
    
    super.nome=nome;
    }
   public String getNome(){
    
    return(super.nome);
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
    
}
