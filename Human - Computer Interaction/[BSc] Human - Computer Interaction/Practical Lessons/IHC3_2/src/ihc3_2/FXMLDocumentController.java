/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ihc3_2;

import javafx.scene.input.MouseEvent;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.layout.Pane;

/**
 *
 * @author joaobrito
 */
public class FXMLDocumentController implements Initializable {
    
    @FXML
    private Label red;
    
    @FXML
    private Label green;
    
    @FXML
    private Label blue;
    
    @FXML
    private Label red_value;
    
    @FXML
    private Label green_value;
    
    @FXML
    private Label blue_value;
    
    @FXML
    private Slider red_slider;
    
    @FXML
    private Slider green_slider;
    
    @FXML
    private Slider blue_slider;
    
    @FXML
    private Pane painel;
    
    @FXML
    private void handleSlider(MouseEvent event) {
           
        int vermelho = (int)red_slider.getValue();
        int verde = (int)green_slider.getValue();
        int azul = (int)blue_slider.getValue();
        
        String hexadecimal = "" +Integer.toHexString(vermelho);
        String hexadecimal2 = "" +Integer.toHexString(verde);
        String hexadecimal3 = "" +Integer.toHexString(azul);
        
        if(red_slider.isFocused())
            red_value.setText("" +vermelho +" " +hexadecimal.toUpperCase());
        
        else if(green_slider.isFocused())
            green_value.setText("" +verde +" " +hexadecimal2.toUpperCase());
       
        
        else if(blue_slider.isFocused())
            blue_value.setText("" +azul +" " +hexadecimal3.toUpperCase());
               
        
        if(hexadecimal.length()==1)
            hexadecimal = "0" +hexadecimal;
        
        if(hexadecimal2.length()==1)
            hexadecimal2 = "0" +hexadecimal2;
        
        if(hexadecimal3.length()==1)
            hexadecimal3 = "0" +hexadecimal3;
        
        painel.setStyle("-fx-background-color: #" +hexadecimal.toLowerCase() +hexadecimal2.toLowerCase() +hexadecimal3.toLowerCase() +"; ");
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
