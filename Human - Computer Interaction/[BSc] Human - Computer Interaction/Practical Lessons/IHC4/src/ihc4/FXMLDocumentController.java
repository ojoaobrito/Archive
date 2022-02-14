/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ihc4;

import java.awt.event.MouseEvent;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.input.KeyEvent;
import registadora.Registadora;

/**
 *
 * @author joaobrito
 */
public class FXMLDocumentController implements Initializable {
    
    @FXML
    private Button n0;
    
    @FXML
    private Button n1;
    
    @FXML
    private Button n2;
    
    @FXML
    private Button n3;
    
    @FXML
    private Button n4;
    
    @FXML
    private Button n5;
    
    @FXML
    private Button n6;
    
    @FXML
    private Button n7;
    
    @FXML
    private Button n8;
    
    @FXML
    private Button n9;
    
    @FXML
    private Button mais;
    
    @FXML
    private Button menos;
    
    @FXML
    private Button vezes;
    
    @FXML
    private Button dividir;
    
    @FXML
    private Button ponto;
    
    @FXML
    private Button clear;
    
    @FXML
    private Button resultado;
    
    @FXML
    private TextArea texto;
    
    @FXML
    private Label label_resultado;
    
    String numero = ""; // números que o utilizador vai introduzindo
    Registadora model = new Registadora(); //objeto que representa a nossa calculadora
    
    @FXML
    private void butClear(ActionEvent event) {
        
        numero = "";
        texto.setText("");
    }
    
    @FXML
    private void butDigito(ActionEvent event) {
        
        Button aux = (Button)event.getSource();
        System.out.println(aux.getText());
        numero = numero + aux.getText();
    }
    
    @FXML
    private void butDigitoTeclado(KeyEvent event) {
        
        String aux = event.getText();
        System.out.println(aux);
        numero = numero + aux;
    }
    
    @FXML
    private void butOperador(ActionEvent event){
        
        Button operador = (Button)event.getSource();
        model.regista(Double.parseDouble(numero));
        model.defineOperador(operador.getText().charAt(0));
        
        texto.setText(texto.getText() +numero +" " +operador.getText() +"\n");
        
        numero = "";
    }
    
    @FXML
    private void butOperadorTeclado(KeyEvent event){
        
        String operador = event.getText();
        model.regista(Double.parseDouble(numero));
        model.defineOperador(operador.charAt(0));
        
        System.out.println(operador);
        
        texto.setText(texto.getText() +numero +" " +operador +"\n");
        
        numero = "";
    }
    
    @FXML
    private void butResultado(ActionEvent event){
        
        texto.setText(texto.getText() +numero);
        label_resultado.setText("" +model.getResultado());
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        
    }    
    
}
