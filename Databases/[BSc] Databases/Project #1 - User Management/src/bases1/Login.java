/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bases1;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.util.ArrayList;
import javax.swing.*;

/**
 *
 * @author britovski
 */
public class Login extends JFrame{
    
    public Login(ListaRegistos lista, SqlManager sql) {  
    
        GridBagLayout painel = new GridBagLayout(); //layout do painel
        GridBagConstraints c = new GridBagConstraints(); //constraints, ou seja
        //os limites e formato de cada componente
           
        this.setTitle("LOGIN"); 
        this.setLayout(painel); //adicionar o layout ao painel
        
        setSize(300, 300);  
        setVisible(true);  
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        c.fill = GridBagConstraints.HORIZONTAL;
        c.gridx = 0; //posição no eixo x
        c.gridy = 0; //posição no eixo y
        c.insets = new Insets(3,3,3,0);
        JTextField utilizador = new JTextField();
    
        this.add(utilizador, c);
    
        c.fill = GridBagConstraints.HORIZONTAL;
        c.gridx = 0; //posição no eixo x
        c.gridy = 1; //posição no eixo y
        c.insets = new Insets(1,6,10,0);

        this.add(new JLabel("username"),c);
    
        c.fill = GridBagConstraints.HORIZONTAL;
        c.gridx = 0;
        c.gridy = 2;
        c.insets = new Insets(3,3,3,0);
        JPasswordField password = new JPasswordField();
    
        this.add(password, c);
    
        c.fill = GridBagConstraints.HORIZONTAL;
        c.gridx = 0; //posição no eixo x
        c.gridy = 3; //posição no eixo y
        c.insets = new Insets(1,6,10,0);

        this.add(new JLabel("password"),c);
    
        c.fill = GridBagConstraints.HORIZONTAL;  
        c.gridx= 0;  
        c.gridy = 4;
        c.insets = new Insets(10,3,3,0);
        JButton botao = new JButton("LOGIN");
        
        botao.addActionListener( new ActionListener() {
            
            public void actionPerformed(ActionEvent e) {
                
                if(utilizador.getText().equals("Bases") == false || String.valueOf(password.getPassword()).equals("Dados") == false){
                
                    JOptionPane.showMessageDialog(null, "Dados Incorretos");
                }
           
                else{
            
                    try{
                        
                        MenuPrincipal menu = new MenuPrincipal(lista,sql);
                    }
                    
                    catch(IOException o){
                        
                        System.out.println(o.getMessage());
                    }
                    dispose();
                }
            }
        });
    
        this.add(botao, c);
        
        revalidate();
        repaint();
    }  
   
}
