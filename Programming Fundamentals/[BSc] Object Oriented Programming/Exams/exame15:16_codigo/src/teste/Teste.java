/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package teste;

import java.time.LocalDate;
import java.time.Month;
import java.util.ArrayList;

/**
 *
 * @author joaobrito
 */
public class Teste {

    public static String produtoMaisCaro(ArrayList<Produto> lista){
    
        double mais_caro = 0.0;
        String nome = "";
        
        for(int i=0; i<lista.size(); i++){
        
            if(lista.get(i).getPreco()>mais_caro){
            
                mais_caro = lista.get(i).getPreco();
                nome = lista.get(i).getNome();
            }
        }
        
        return(nome);
    }
    
    public static int produtosIguais(ArrayList<Produto> lista, String nome){
    
        int iguais = 0;
        
        for(int i=0; i<lista.size(); i++){
        
            if(lista.get(i).getNome().equals(nome))
                iguais++;
        }
        
        return(iguais);
    }
    
    public static void main(String[] args) {
        
        // TESTAR A CLASSE Produto
        // -----------------------------------------------------
        Produto p1 = new Produto("Portátil Asus");
        Produto p2 = new Produto("Portátil HP");
        
        p1.setPreco(600.0);
        p2.setPreco(800.0);
        
        ArrayList<Produto> lista = new ArrayList<Produto>();
        
        lista.add(p1);
        lista.add(p2);
       
        try{
            
            p1.subirProduto(10);
        }
        catch(ValorInvalido v){
        
            System.out.println(v.getMessage());
        }
        
        System.out.println(p1.getPreco());
        System.out.println(produtoMaisCaro(lista));
        System.out.println(produtosIguais(lista,"Portátil HP"));
        // -----------------------------------------------------
        
        // TESTAR AS CLASSES ProdutoAlimentar E Inventario
        // -----------------------------------------------------------------------------------------------------------------------
        // produto alimentar - alface
        LocalDate data = LocalDate.of(2019, Month.DECEMBER, 12);
        Produto p3_produto = new Produto("Alface");
        ProdutoAlimentar p3 = new ProdutoAlimentar(p3_produto,data);
        p3.setPreco(1.0);
        
        // produto alimentar - tomate
        LocalDate data2 = LocalDate.of(2019, Month.DECEMBER, 12);
        Produto p4_produto = new Produto("Tomate");
        ProdutoAlimentar p4 = new ProdutoAlimentar(p4_produto,data2);
        p4.setPreco(2.0);
        
        ArrayList<ProdutoAlimentar> lista_alimentar = new ArrayList<ProdutoAlimentar>();
        
        lista_alimentar.add(p3);
        lista_alimentar.add(p4);
        
        System.out.println(p3.equals(p4));
        
        Inventario inventario = new Inventario();
        System.out.println(inventario.foraDePrazo(lista_alimentar)); // ambos os produtos (tomate e alface) estão fora da validade
        // -----------------------------------------------------------------------------------------------------------------------
    }
    
}
