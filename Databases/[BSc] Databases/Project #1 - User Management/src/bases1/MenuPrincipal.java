/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bases1;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.NotSerializableException;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;
import javax.swing.event.*;

/**
 *
 * @author britovski
 */
public class MenuPrincipal extends JFrame implements Serializable {

    public MenuPrincipal(ListaRegistos lista, SqlManager sql) throws IOException {               
    
    GridBagLayout painel = new GridBagLayout(); //layout do painel
    GridBagConstraints c = new GridBagConstraints(); //constraints, ou seja
    //os limites e formato de cada componente
          
    this.setTitle("Registos 2.0"); 
    this.setSize(500,400);  
    this.setVisible(true);
    this.setDefaultCloseOperation(EXIT_ON_CLOSE);
 
    JTabbedPane tp = new JTabbedPane(); 
    
    JPanel p1 = new JPanel();
    p1.setBackground(new Color(216, 229, 243));
    p1.setLayout(painel);
    tp.add("Novo Registo",p1);
    
    tp.setIconAt(0, createImageIcon("1.png", ""));
    
    JPanel p2 = new JPanel();
    p2.setBackground(new Color(216, 229, 243));
    p2.setLayout(painel);
    tp.add("Consultar Registo",p2);
    
    tp.setIconAt(1, createImageIcon("2.png", ""));
    
    JPanel p3 = new JPanel();
    p3.setBackground(new Color(216, 229, 243));
    p3.setLayout(painel);
    tp.add("Listar Registos",p3);
    
    tp.setIconAt(2, createImageIcon("3.png", ""));
      
    tp.setBounds(1,1,this.getWidth(),this.getHeight());
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 0;
    c.gridy = 1;
    c.insets = new Insets(1,1,50,1);
    c.weightx = 0;
    JLabel rotulo2 = new JLabel("Nome ");
    
    p1.add(rotulo2,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 1;
    c.gridy = 1;
    c.insets = new Insets(1,1,50,1);
    JTextField nome = new JTextField();
    
    p1.add(nome,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 0;
    c.gridy = 2;
    c.insets = new Insets(1,1,50,1);
    c.weightx = 0;
    JLabel rotulo3 = new JLabel("Número ");
    
    p1.add(rotulo3,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 1;
    c.gridy = 2;
    c.insets = new Insets(1,1,50,1);
    JTextField numero = new JTextField();
    
    p1.add(numero,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 1;
    c.gridy = 3;
    c.gridwidth = 1;
    JButton botao = new JButton("Adicionar");
    
    botao.addActionListener(new ActionListener(){
        
        public void actionPerformed(ActionEvent e){
            
            if(nome.getText().equals("") || numero.getText().equals("")){
                
                JOptionPane.showMessageDialog(null, "Preencha os 2 campos corretamente!");
            }
            
            else{
                
                Registo novo = null; 
                int k = 0;
                
                try{
                    
                    novo = new Registo(nome.getText(),Integer.parseInt(numero.getText()));
            
                }
                
                catch(NumberFormatException n){
                    
                    JOptionPane.showMessageDialog(null, "Número inválido!");
                    k=1;
                }
                
                if(lista.checkRegisto(novo) == false && k == 0){
                    
                    sql.saveRegisto(novo);
                    JOptionPane.showMessageDialog(null, "Registo adicionado com sucesso!");
                    lista.lista=sql.getRegistos();
                    
                    tp.revalidate();
                    
                    p3.revalidate();
                    p3.repaint();
                }
            
                else if(lista.checkRegisto(novo) == true && k == 0){
                
                    JOptionPane.showMessageDialog(null, "Registo já adicionado!");
                }
            }
        }
    });
    
    p1.add(botao,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 0;
    c.gridy = 1;
    c.insets = new Insets(1,1,50,1);
    c.weightx = 0;
    JLabel rotulo4 = new JLabel("Nome ");
    
    p2.add(rotulo4,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 1;
    c.gridy = 1;
    c.insets = new Insets(1,1,50,1);
    JTextField nome2 = new JTextField();
    
    p2.add(nome2,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 1;
    c.gridy = 2;
    c.insets = new Insets(1,1,50,1);
    JLabel rotulo5 = new JLabel("/     ou     /");
    
    p2.add(rotulo5,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 0;
    c.gridy = 3;
    c.insets = new Insets(1,1,50,1);
    JLabel rotulo6 = new JLabel("Número ");
    
    p2.add(rotulo6,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 1;
    c.gridy = 3;
    c.insets = new Insets(1,1,50,1);
    JTextField numero2 = new JTextField();
    
    p2.add(numero2,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 1;
    c.gridy = 4;
    c.insets = new Insets(1,1,50,1);
    JButton botao2 = new JButton("Consultar");
    
    p2.add(botao2,c);
    
    botao2.addActionListener(new ActionListener(){
        
        public void actionPerformed(ActionEvent e){
           
            if(nome2.getText().equals("")==true && numero2.getText().equals("")==true){
                //nenhum campo preenchido 
               
                JOptionPane.showMessageDialog(null, "Preencha pelo menos 1 campo!");
            }
           
            else{
               
                if(numero2.getText().equals("") == true && nome2.getText().equals("") == false){
                   //pesquisa pelo nome
                   
                   Registo aux = lista.getRegisto(nome2.getText(), 0);
                   
                   if(aux != null){
                       
                       JOptionPane.showMessageDialog(null, aux.getNome() + "\n" + aux.getNumero() + "\n");
                   }
                   
                   else{
                       
                       JOptionPane.showMessageDialog(null, "Não existe nenhum registo correspondente!");
                   }
                }
               
                else if (numero2.getText().equals("") == false && nome2.getText().equals("") == true){ 
                    //pesquisa pelo número
                   
                    Registo aux = null;
                    int k=0;
                    
                    try{
                        
                        aux = lista.getRegisto("", Integer.parseInt(numero2.getText()));
                    }
                    
                    catch(NumberFormatException n){
                        
                        JOptionPane.showMessageDialog(null, "Número inválido!");
                        k=1;
                    }
                    
                    if(aux != null){
                       
                        JOptionPane.showMessageDialog(null, "Nome: " + aux.getNome() + "\n" + "Número: " +aux.getNumero() + "\n");
                    }
                   
                    else if(aux == null && k==0){
                       
                        JOptionPane.showMessageDialog(null,"Não existe nenhum registo correspondente!");
                    }
                }
                
                else{ //pesquisa pelos 2 parâmetros
                    
                    Registo aux = null;
                    
                    aux = lista.getRegisto(nome2.getText(), Integer.parseInt(numero2.getText()));
                    
                    if(aux != null){
                        
                        JOptionPane.showMessageDialog(null, "Nome: " + aux.getNome() + "\n" + "Número: " +aux.getNumero() + "\n");
                    }
                    
                    else{
                        
                        JOptionPane.showMessageDialog(null, "Não existe nenhum registo correspondente!");
                    }
                }
            } 
        }
    });
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 0;
    c.gridy = 0;
    c.insets = new Insets(1,50,20,50);
    c.weightx = 0;
    JLabel rotulo7 = new JLabel("Registos");
    
    p3.add(rotulo7,c);
    
    c.fill = GridBagConstraints.HORIZONTAL;
    c.gridx = 0;
    c.gridy = 1;
    c.insets = new Insets(1,1,1,1);
    c.weightx = 0;
    
    DefaultListModel list = new DefaultListModel();
        
    for(int i=0; i<lista.lista.size(); i++){
            
        list.addElement(lista.lista.get(i).getNome());
    }
        
    JList regList  = new JList(list);
        
    regList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
    regList.setVisibleRowCount(10);
        
    regList.addListSelectionListener( new ListSelectionListener() {
            
        public void valueChanged(ListSelectionEvent e) {
   
            if (e.getValueIsAdjusting() == false) {

                JOptionPane.showMessageDialog(null, "Nome: " + lista.lista.get(regList.getSelectedIndex()).getNome() + "\nNúmero: " + lista.lista.get(regList.getSelectedIndex()).getNumero());
                
                revalidate();
                repaint();
            }
        }
    });
        
    JScrollPane listScrollPane = new JScrollPane(regList);
    p3.add(listScrollPane,c);

    this.add(tp);  
    
    revalidate();
    repaint();
        
    }

    protected ImageIcon createImageIcon(String path, String description) {
        
    java.net.URL imgURL = getClass().getResource(path);
    if (imgURL != null) {
        return new ImageIcon(imgURL, description);
    } else {
        System.err.println("Couldn't find file: " + path);
        return null;
    }
}
    
}
