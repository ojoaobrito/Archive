/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bases1;

import java.io.IOException;
import java.io.NotSerializableException;
import java.io.Serializable;
import java.util.*;

/**
 *
 * @author britovski
 */
public class Registo implements Serializable {
    
    private int numero;
    private String nome;
    
    
    public Registo(String n, int num){
        
        nome = n;
        numero = num;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int num) {
        
        numero = num;
    }

    public String getNome() {
        
        return nome;
    }

    public void setNome(String nome) {
        
        this.nome = nome;
    }
    
}
