/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ihc3;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

/**
 *
 * @author joaobrito
 */
public class FXMLDocumentController implements Initializable {
    
    @FXML
    private TextArea texto;
    
    @FXML
    private Label palavra;
    
    @FXML
    private Label contagem;
    
    @FXML
    private Label numero;
    
    @FXML
    private TextField pesquisa;
    
    @FXML
    private CheckBox maiusculas;
    
    @FXML
    private Button botao;
    
    @FXML
    private void handleButtonAction(ActionEvent event) {
        
        String[] conteudo = texto.getText().split("[ ,.;!?]+"); //dividir o texto em palavras
        String palavra = "";
        String escolhida = pesquisa.getText();
        int contador = 0;
        
        for(int i=0; i<conteudo.length; i++){
             
            if(escolhida.equals(conteudo[i]) || (maiusculas.isSelected() && escolhida.equalsIgnoreCase(conteudo[i]))) //exatamente igual ou igual mas com maiúsculas/minúsculas
                contador++;
            
        }
     
        numero.setText("" +contador);
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
