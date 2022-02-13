/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bases1;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.util.ArrayList;

/**
 *
 * @author britovski
 */
public class ListaRegistos implements Serializable {
    
    public ArrayList <Registo> lista;
    
    public ListaRegistos() {
        
        lista = new ArrayList <Registo>();
    
    }

    public ArrayList<Registo> getLista() {
        return lista;
    }

    public void setLista(ArrayList<Registo> lista) {
        this.lista = lista;
    }
    
    public boolean checkRegisto(Registo r){
        
        for(int i=0; i<lista.size(); i++){
            
            if(lista.get(i).getNome().equals(r.getNome()) && lista.get(i).getNumero()==(r.getNumero())){
                
                return(true);
            }
        }
        
        return(false);
    }
    
    
    public Registo getRegisto(String n, int num){
        
        if(n.equals("") == false && num == 0){
            
            for(int i=0; i<lista.size(); i++){
            
                if(lista.get(i).getNome().equals(n)){
                
                    return(lista.get(i));
                }
            }
        
            return(null);
        }
        
        else if (n.equals("") == true){
            
            for(int i=0; i<lista.size(); i++){
            
                if(lista.get(i).getNumero() == num){
                
                    return(lista.get(i));
                }
            }
        
            return(null);
            
        }
        
        else{
            
            for(int i=0; i<lista.size(); i++){
            
                if(lista.get(i).getNome().equals(n) == true && lista.get(i).getNumero() == num){
                
                    return(lista.get(i));
                }
            }
        
            return(null);
        }
        
    }
    
    
    public void addRegisto(Registo r){
        
        lista.add(r);
    }
}
