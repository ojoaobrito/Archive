/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hexsudoku;

import java.awt.Color;
import java.awt.Paint;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
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
import javafx.scene.layout.Border;
import javafx.scene.layout.BorderStroke;
import javafx.scene.layout.BorderStrokeStyle;
import javafx.scene.layout.BorderWidths;
import javafx.scene.layout.CornerRadii;
import javafx.stage.Stage;

/**
 *
 * @author joaobrito
 */
public class FXMLDocumentController implements Initializable {
    
    @FXML
    private TextField username;
    
    @FXML
    private PasswordField password;
    
    @FXML
    private Button entrar;
    
    @FXML
    private Button registar;
    
    @FXML
    private Label password_incorreta;
    
    @FXML
    private Label username_incorreto;
    
    @FXML
    private void handlerButton(ActionEvent event) throws Exception{
        
        // fechar a janela de login
        Stage stage = (Stage) registar.getScene().getWindow();
        stage.close();
        
        // criar a janela de registar
        Stage anotherStage = new Stage();
            
        Parent root2 = FXMLLoader.load(getClass().getResource("FXML_registar.fxml"));
        
        Scene scene2 = new Scene(root2);
        
        anotherStage.setScene(scene2);
        anotherStage.show();
    }
    
    @FXML
    private void handlerMenu(ActionEvent event) throws Exception{
        
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
        
        if(controlo==1){
        
            controlo = 0;
            
            try{
        
                File ficheiro = new File("authentication_data.txt");
                Scanner leitura = new Scanner(ficheiro);

                while(leitura.hasNextLine()){

                    String aux[] = leitura.nextLine().split(" // ");
                    System.out.println(aux[0]);

                    if(username.getText().equals(aux[0])){

                        controlo = 1;

                        // fazer reset ao label e textfield do username
                        username.setStyle("");
                        username_incorreto.setOpacity(0.0);

                        // obter o valor MD5 da password
                        MessageDigest md = MessageDigest.getInstance("MD5");
                        byte[] resultado = md.digest(password.getText().getBytes());

                        BigInteger aux3 = new BigInteger(1, resultado);

                        String hexadecimal = aux3.toString(16);

                        while(hexadecimal.length() < 32)
                            hexadecimal = "0" + hexadecimal;

                        if(hexadecimal.equals(aux[1])){ // password correta
                            
                            try{
                                
                                PrintWriter writer = new PrintWriter(new FileOutputStream("current_player.txt", false));
                                writer.print(username.getText());
                                writer.close();
                                
                                // fechar a janela de login
                                Stage stage = (Stage) registar.getScene().getWindow();
                                stage.close();

                                // criar a janela de menu
                                Stage anotherStage = new Stage();

                                Parent root2 = FXMLLoader.load(getClass().getResource("FXML_menu.fxml"));

                                Scene scene2 = new Scene(root2);

                                anotherStage.setScene(scene2);
                                anotherStage.show();
                            
                            }
                            
                            catch(IOException e){
                            
                                System.out.println(e.getMessage());
                            }
                        }

                        else{ // password incorreta

                            password_incorreta.setOpacity(1.0);
                            username_incorreto.setText("password incorreta");
                            password.setStyle("-fx-border-color: red");
                        }
                    }

                    else if(!leitura.hasNextLine() && controlo==0){ // não há mais utilizadores registados ("username" incorreto)

                        username_incorreto.setOpacity(1.0);
                        username_incorreto.setText("username inexistente");
                        username.setStyle("-fx-border-color: red");
                    }
                }
            }

            catch(IOException e){
                System.out.println(e.getMessage());
            }
        }
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
