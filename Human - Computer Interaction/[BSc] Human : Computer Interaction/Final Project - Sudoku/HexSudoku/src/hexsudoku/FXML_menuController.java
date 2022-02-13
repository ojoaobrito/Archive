/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hexsudoku;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;
import java.util.Scanner;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.control.MenuButton;
import javafx.scene.control.RadioButton;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author joaobrito
 */
public class FXML_menuController implements Initializable  {

    /**
     * Initializes the controller class.
     */
    @FXML
    private Button jogo;

    @FXML
    private String player;
    
    @FXML
    private Label label1;
    @FXML
    private Label label2;
    @FXML
    private Label label3;
    @FXML
    private Label label4;
    @FXML
    private Label label5;
    @FXML
    private Label label6;
    @FXML
    private Label label7;
    @FXML
    private Label label8;
    @FXML
    private Label label9;
    @FXML
    private Label label10;
    @FXML
    private Label label11;
    @FXML
    private Label label12;
    @FXML
    private Label label13;
    @FXML
    private Label label14;
    @FXML
    private Label label15;
    @FXML
    private Label label16;
    @FXML
    private Label label17;
    @FXML
    private Label label18;
    @FXML
    private Label label19;
    @FXML
    private Label label20;
    @FXML
    private Label label21;
    @FXML
    private Label label22;
    @FXML
    private Label label23;
    @FXML
    private Label label24;
    @FXML
    private Label label25;
    @FXML
    private Label label26;
    @FXML
    private Label label27;
    @FXML
    private Label label28;
    @FXML
    private Label label29;
    @FXML
    private Label label30;
    
    @FXML
    private RadioButton facil;

    @FXML
    private RadioButton medio;

    @FXML
    private RadioButton dificil;

    @FXML
    private void facilAction(ActionEvent event) throws Exception{

        if(!facil.isSelected())
            jogo.setDisable(true);
        
        else
            jogo.setDisable(false);
        
        medio.setSelected(false);
        dificil.setSelected(false);
    }
    
    @FXML
    private void medioAction(ActionEvent event) throws Exception{

        if(!medio.isSelected())
            jogo.setDisable(true);
        
        else
            jogo.setDisable(false);
        
        facil.setSelected(false);
        dificil.setSelected(false);
    }
    
    @FXML
    private void dificilAction(ActionEvent event) throws Exception{

        if(!dificil.isSelected())
            jogo.setDisable(true);
        
        else
            jogo.setDisable(false);
        
        facil.setSelected(false);
        medio.setSelected(false);
    }
     
    @FXML
    private void handlerButton(ActionEvent event) throws Exception{
        
        PrintWriter writer = new PrintWriter(new FileOutputStream("games_data.txt", true));
        PrintWriter writer2 = new PrintWriter(new FileOutputStream("current_player.txt", false));
        writer.println();
   
        if(facil.isSelected())
            writer2.print(player + " - Fácil");
        
        else if(medio.isSelected())
            writer2.print(player + " - Médio");
        
        else if(dificil.isSelected())
            writer2.print(player + " - Difícil");
        
        writer2.close();
        
        // fechar a janela de menu
        Stage stage = (Stage) jogo.getScene().getWindow();
        stage.close();
        
        // criar a janela de jogo
        Stage anotherStage = new Stage();
            
        Parent root2 = FXMLLoader.load(getClass().getResource("FXML_jogo.fxml"));
        
        Scene scene2 = new Scene(root2);
        
        anotherStage.setScene(scene2);
        anotherStage.setResizable(false);
        anotherStage.show();
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
       
        int contador1 = 1;
        int contador2 = 1;
        int contador3 = 1;
        ArrayList<Integer> array1 = new ArrayList<Integer>();
        ArrayList<String> array1_nome = new ArrayList<String>();
        ArrayList<Integer> array2 = new ArrayList<Integer>();
        ArrayList<String> array2_nome = new ArrayList<String>();
        ArrayList<Integer> array3 = new ArrayList<Integer>();
        ArrayList<String> array3_nome = new ArrayList<String>();
        
        try{
            File ficheiro = new File("games_data.txt");
            Scanner leitura = new Scanner(ficheiro);
            
            File ficheiro2 = new File("current_player.txt");
            Scanner leitura2 = new Scanner(ficheiro2);
            player = leitura2.nextLine().split(" ")[0];
            
            String aux = "";

            while(leitura.hasNextLine()){

                aux = leitura.nextLine();
                
                if(aux.split(" ")[0].equals("Fácil")){
                    
                    array1.add(Integer.parseInt(aux.split(" ")[3]));
                    array1_nome.add(aux.split(" ")[2]);
                }
                
                else if(aux.split(" ")[0].equals("Médio")){
                    
                    array2.add(Integer.parseInt(aux.split(" ")[3]));
                    array2_nome.add(aux.split(" ")[2]);
                }
                
                else if(aux.split(" ")[0].equals("Difícil")){
                    
                    array3.add(Integer.parseInt(aux.split(" ")[3]));
                    array3_nome.add(aux.split(" ")[2]);
                }
            }
            
            ArrayList<Integer> array1_aux = new ArrayList<Integer>();
            ArrayList<String> array1_aux_string = new ArrayList<String>();
            ArrayList<Integer> array2_aux = new ArrayList<Integer>();
            ArrayList<String> array2_aux_string = new ArrayList<String>();
            ArrayList<Integer> array3_aux = new ArrayList<Integer>();
            ArrayList<String> array3_aux_string = new ArrayList<String>();
            int max = 200000;
            String max_string = "";
            int tamanho1 = array1.size();
            int tamanho2 = array2.size();
            int tamanho3 = array3.size();
            int k = 0;
            
            while(tamanho1>=1){
                
                for(int i=0; i<array1.size(); i++){

                    if(array1.get(i)<max){
                        
                        max = array1.get(i);
                        max_string = array1_nome.get(i);
                        k=i;
                    }
                }
                
                array1_aux.add(max);
                array1_aux_string.add(max_string);
                array1.remove(k);
                array1_nome.remove(k);
                tamanho1 = array1.size();
                max = 200000;
            }
            
            
            max = 200000;
            k = 0;
            max_string = "";
            
            while(tamanho2>=1){
                
                for(int i=0; i<array2.size(); i++){

                    if(array2.get(i)<max){
                        
                        max = array2.get(i);
                        max_string = array2_nome.get(i);
                        k=i;
                    }
                }
                
                array2_aux.add(max);
                array2_aux_string.add(max_string);
                array2.remove(k);
                array2_nome.remove(k);
                tamanho2 = array2.size();
                max = 200000;
            }
            
            max = 200000;
            k = 0;
            max_string = "";
            
            while(tamanho3>=1){
                
                for(int i=0; i<array3.size(); i++){

                    if(array3.get(i)<max){
                        
                        max = array3.get(i);
                        max_string = array3_nome.get(i);
                        k=i;
                    }
                }
                
                array3_aux.add(max);
                array3_aux_string.add(max_string);
                array3.remove(k);
                array3_nome.remove(k);
                tamanho3 = array3.size();
                max = 200000;
            }
            
            for(int i=1; i<=array1_aux.size(); i++){
            
                if(i==1){label1.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==2){label2.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==3){label3.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==4){label4.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==5){label5.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==6){label6.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==7){label7.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==8){label8.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==9){label9.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
                if(i==10){label10.setText(array1_aux_string.get(i-1) + " // " + array1_aux.get(i-1) + " seg.");}
            }
            
            for(int i=1; i<=array2_aux.size(); i++){
            
                if(i==1){label11.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==2){label12.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==3){label13.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==4){label14.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==5){label15.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==6){label16.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==7){label17.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==8){label18.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==9){label19.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
                if(i==10){label20.setText(array2_aux_string.get(i-1) + " // " + array2_aux.get(i-1) + " seg.");}
            }
            
            for(int i=1; i<=array3_aux.size(); i++){
            
                if(i==1){label21.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==2){label22.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==3){label23.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==4){label24.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==5){label25.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==6){label26.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==7){label27.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==8){label28.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==9){label29.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
                if(i==10){label30.setText(array3_aux_string.get(i-1) + " // " + array3_aux.get(i-1) + " seg.");}
            }
            
            if(array1_aux.size()==0)
                label5.setText("Sem dados");
            
            if(array2_aux.size()==0)
                label15.setText("Sem dados");
            
            if(array3_aux.size()==0)
                label25.setText("Sem dados");
            
        }
        
        catch(Exception e){
        
            System.out.println(e.getMessage());
        }
    }    
    
}
                   