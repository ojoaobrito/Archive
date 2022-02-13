import java.io.*;

public class aula1{

    public static void main(String[] args){

        BufferedWriter bw;

        try{

            bw = new BufferedWriter(new FileWriter("teste1.txt"));
            bw.write("1");
            bw.newLine();
            bw.write("2");
            bw.flush();
            bw.close();
        
        } catch (IOException e){

            System.out.println(e.getMessage());
        }
    }
}