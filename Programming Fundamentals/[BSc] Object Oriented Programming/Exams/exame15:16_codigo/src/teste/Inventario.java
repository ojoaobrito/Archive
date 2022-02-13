/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package teste;

import java.time.LocalDate;
import java.util.ArrayList;

/**
 *
 * @author joaobrito
 */
public class Inventario {
    
    private ArrayList<Produto> produtos;
    
    public Inventario (){
        
        produtos = new ArrayList<Produto>();
    }
    
    public ArrayList<Produto> getProdutos(){
    
        return(produtos);
    }
    
    public void setProdutos(ArrayList<Produto> produtos){ // não basta fazer "this.produtos = produtos", isso seria apenas atribuir apontadores
    
        if(this.produtos.size()==produtos.size()){
        
            for(int i=0; i<produtos.size(); i++){
            
                this.produtos.get(i).setCodigo(produtos.get(i).getCodigo());
                this.produtos.get(i).setNome(produtos.get(i).getNome());
                this.produtos.get(i).setQuantidade(produtos.get(i).getQuantidade());
                this.produtos.get(i).setPreco(produtos.get(i).getPreco());
            }
        }
    }
    
    public double foraDePrazo(ArrayList<ProdutoAlimentar> lista){
    
        double total = 0.0; 
       
        for(int i=0; i<lista.size(); i++){
            
            if(lista.get(i).getDataValidade().compareTo(LocalDate.now())<0)
                total += lista.get(i).getPreco();
        }
        
        return(total);
    }
}
