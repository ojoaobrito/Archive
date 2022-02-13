/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package teste;

import java.time.LocalDate;
import java.time.Month;

/**
 *
 * @author joaobrito
 */
public class ProdutoAlimentar extends Produto{
    
    private LocalDate data_validade;
    
    public ProdutoAlimentar(Produto produto, LocalDate data_validade){
    
        super(produto.getNome());
        super.setPreco(produto.getPreco());
        super.setQuantidade(produto.getQuantidade());
        super.setCodigo(produto.getCodigo()); // o código deste ProdutoAlimentar deve ser o mesmo do Produto dado como parâmetro
        this.data_validade = data_validade;
    }

    public LocalDate getDataValidade() {
        return data_validade;
    }

    public void setDataValidade(LocalDate data_validade) {
        this.data_validade = data_validade;
    }
    
    public boolean equals(ProdutoAlimentar p){
    
        if(p!=null && p.getClass()==this.getClass()){
        
            if(this.data_validade.compareTo(p.getDataValidade())!=0)
                return(false);
            
            if(!this.getNome().equals(p.getNome()) || this.getPreco()!=p.getPreco()
                    || this.getQuantidade()!=p.getQuantidade() || this.getCodigo()!=p.getCodigo())
                return(false);
            
            return(true);
        }
        
        return(false); // se for impossível comparar "p" ao objeto atual, devolvemos false
    }
}
