/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hexsudoku;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.net.URL;
import java.security.MessageDigest;
import java.util.ResourceBundle;
import java.util.Scanner;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author joaobrito
 */
public class FXML_registarController implements Initializable {

    /**
     * Initializes the controller class.
     */
    
    @FXML
    private TextField username;
    
    @FXML
    private PasswordField password;
    
    @FXML
    private PasswordField confirmar_password;
    
    @FXML
    private Button voltar;
    
    @FXML
    private Button confirmar;
    
    @FXML
    private Label password_incorreta;
    
    @FXML
    private Label username_incorreto;
    
    @FXML
    private Label confirmar_password_incorreta;
    
    @FXML
    private void handlerButton(ActionEvent event) throws Exception{
        
        int controlo = 1;
        
        if(username.getText().equals("")){
        
            username_incorreto.setOpacity(1.0);
            username_incorreto.setText("introduza o username");
            username.setStyle("-fx-border-color: red");
            controlo = 0;
        }
        
        else{ // fazer reset ao label e textfield do username
        
            username.setStyle("");
            username_incorreto.setOpacity(0.0);
        }
        
        if(password.getText().equals("")){
        
            password_incorreta.setOpacity(1.0);
            password_incorreta.setText("introduza a password");
            password.setStyle("-fx-border-color: red");
            controlo = 0;
        }
        
        else{ // fazer reset ao label e textfield da password
        
            password.setStyle("");
            password_incorreta.setOpacity(0.0);
        }
        
        if(confirmar_password.getText().equals("")){
        
            confirmar_password_incorreta.setOpacity(1.0);
            confirmar_password_incorreta.setText("confirme a password");
            confirmar_password.setStyle("-fx-border-color: red");
            controlo = 0;
        }
        
        else{ // fazer reset ao label e textfield da confirmação de password
        
            confirmar_password.setStyle("");
            confirmar_password_incorreta.setOpacity(0.0);
        }
        
        if(controlo==1){
            
            if(!password.getText().equals(confirmar_password.getText())){ // passwords diferentes
            
                password_incorreta.setOpacity(1.0);
                password_incorreta.setText("passwords diferentes");
                password.setStyle("-fx-border-color: red");
                
                confirmar_password_incorreta.setOpacity(1.0);
                confirmar_password_incorreta.setText("passwords diferentes");
                confirmar_password.setStyle("-fx-border-color: red");
            }
            
            else{
                
                // criar o ficheiro de autenticação se for preciso
                PrintWriter writer1 = new PrintWriter(new FileOutputStream("authentication_data.txt", true));
                
                File ficheiro = new File("authentication_data.txt");
                Scanner leitura = new Scanner(ficheiro);

                while(leitura.hasNextLine()){

                    String aux[] = leitura.nextLine().split(" // ");
                    
                    if(aux[0].equals(username.getText())){
                        
                        username_incorreto.setOpacity(1.0);
                        username_incorreto.setText("username já existente");
                        username.setStyle("-fx-border-color: red");
                        controlo = 0;
                    }
                }
                
                if(controlo==1){
                
                    // escrever dados de autenticação no ficheiro adequado
                    try {

                        // objeto ideal para escrita em ficheiros .txt
                        PrintWriter writer = new PrintWriter(new FileOutputStream("authentication_data.txt", true));

                        // obter o valor MD5 da password
                        MessageDigest md = MessageDigest.getInstance("MD5");
                        byte[] resultado = md.digest(password.getText().getBytes());

                        BigInteger aux = new BigInteger(1, resultado);

                        String hexadecimal = aux.toString(16);

                        while(hexadecimal.length() < 32)
                            hexadecimal = "0" + hexadecimal;

                        // guardar no ficheiro de autenticação
                        writer.println(username.getText() + " // " + hexadecimal);
                        writer.close();
                    }
                    catch (IOException e){
                        System.out.println(e.getMessage());
                    }

                    // fechar a janela de registar
                    Stage stage = (Stage) confirmar.getScene().getWindow();
                    stage.close();

                    // criar a janela de menu
                    Stage anotherStage = new Stage();

                    Parent root2 = FXMLLoader.load(getClass().getResource("FXML_menu.fxml"));

                    Scene scene2 = new Scene(root2);

                    anotherStage.setScene(scene2);
                    anotherStage.show();
                }
            }
        }
    }
    
    @FXML
    private void voltar(ActionEvent event) throws Exception{
    
        // fechar a janela de registar
        Stage stage = (Stage) voltar.getScene().getWindow();
        stage.close();
        
        // voltar à janela de login
        Stage anotherStage = new Stage();
            
        Parent root2 = FXMLLoader.load(getClass().getResource("FXMLDocument.fxml"));
        
        Scene scene2 = new Scene(root2);
        
        anotherStage.setScene(scene2);
        anotherStage.show();
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        
        // TODO
    }    
    
}
