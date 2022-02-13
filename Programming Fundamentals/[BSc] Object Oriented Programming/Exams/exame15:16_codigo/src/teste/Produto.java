/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package teste;

/**
 *
 * @author joaobrito
 */
public class Produto {
    
    private int codigo;
    private static int ultimo;
    private String nome;
    private double preco;
    private int quantidade;

    public Produto(String nome){

        this.nome = nome;
        ultimo++;
        codigo = ultimo;
        preco = 0.0;
        quantidade = 1;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade){
        this.quantidade = quantidade;
    }
    
    public void subirProduto(int percentagem) throws ValorInvalido{
    
        if(percentagem<0 || percentagem>100)
            throw new ValorInvalido("O valor introduzido, " + percentagem + ", não está entre 0 e 100");
        
        preco += preco*(percentagem/100.0);
    }
    
    public String toString(){
    
        return("código: " + codigo + " nome: " + nome + " preço:" + preco + " quandidade: " + quantidade);
    }
}
