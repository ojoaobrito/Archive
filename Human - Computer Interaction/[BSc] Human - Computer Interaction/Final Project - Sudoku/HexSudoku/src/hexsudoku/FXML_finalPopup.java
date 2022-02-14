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
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author joaobrito
 */
public class FXML_finalPopup implements Initializable {

    /**
     * Initializes the controller class.
     */
    
    @FXML
    private Button voltar;
    
    @FXML
    private void onClick(ActionEvent e){
    
        try{
            // fechar a janela atual
            Stage stage = (Stage) voltar.getScene().getWindow();
            stage.close();

            // criar a janela de menu
            Stage anotherStage = new Stage();

            Parent root2 = FXMLLoader.load(getClass().getResource("FXML_menu.fxml"));

            Scene scene2 = new Scene(root2);

            anotherStage.setScene(scene2);
            anotherStage.show();
        }
        
        catch(Exception i){
        
            System.out.println(i.getMessage());
        }
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
