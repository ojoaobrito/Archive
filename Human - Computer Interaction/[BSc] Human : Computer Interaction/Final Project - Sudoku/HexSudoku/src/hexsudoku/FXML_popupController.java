/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hexsudoku;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author joaobrito
 */
public class FXML_popupController implements Initializable {

    /**
     * Initializes the controller class.
     */
    
    @FXML
    private Button voltar;
    
    @FXML
    private void onClick(ActionEvent e){
    
        // fechar a janela atual
        Stage stage = (Stage) voltar.getScene().getWindow();
        stage.close();
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
