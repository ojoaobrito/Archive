/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ihc2;

import java.net.URL;
import java.text.DecimalFormat;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.image.ImageView;

/**
 *
 * @author joaobrito
 */
public class FXMLDocumentController implements Initializable {
    
    @FXML
    private ImageView imagem;
    @FXML
    private Label a;
    @FXML
    private Label b;
    @FXML
    private Label c;
    @FXML
    private Label resultado;
    @FXML
    private Label valor;
    @FXML
    private TextField txt_a;
    @FXML
    private TextField txt_b;
    @FXML
    private TextField txt_c;
    @FXML
    private Button calcular;
    
    @FXML
    private void handleButtonAction(ActionEvent event) {
        
        double a = Double.parseDouble(txt_a.getText());
        double b = Double.parseDouble(txt_b.getText());
        double c = Double.parseDouble(txt_c.getText());
        
        DecimalFormat df = new DecimalFormat("#.#######"); //formatar o valor final
        
        double s = (a+b+c)/2;
        
        valor.setText("" +df.format(Math.sqrt(s*(s-a)*(s-b)*(s-c))));
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
