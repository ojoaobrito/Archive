/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bases1;
import javax.swing.*;
import java.awt.*;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.NotSerializableException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
/**
 *
 * @author britovski
 */
public class Bases1 extends JFrame{
 
    public static void main(String[] args) throws IOException {  
            
        ListaRegistos lista = new ListaRegistos();
        SqlManager sql = new SqlManager();
        
        /*try{
            
         ObjectInputStream is = new ObjectInputStream(new FileInputStream("dataBase.dat"));
            
         lista.lista = (ArrayList<Registo>)is.readObject();
         
        }
        
        catch (IOException e){
            System.out.println(e.getMessage());
        }
        catch(ClassNotFoundException e) {
            System.out.println(e.getMessage());
        }*/
        
        //Login login = new Login(registos); //ecrã de LOGIN
        
        lista.lista=sql.getRegistos();
        
        MenuPrincipal menu = new MenuPrincipal(lista,sql);
                
    }     
    
}