/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sd_browser;

import static java.lang.Thread.sleep;
import java.net.URL;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.ResourceBundle;
import javafx.application.Platform;
import javafx.collections.ObservableList;
import javafx.concurrent.Worker;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Menu;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebHistory;
import javafx.scene.web.WebView;
import javafx.stage.Stage;
import javax.swing.text.Document;

/**
 *
 * @author joaobrito
 */
public class FXMLDocumentController implements Initializable{
    
    @FXML
    private TabPane abas;
    
    @FXML
    private Tab aba_atual;
    
    private ArrayList threads;
    private ArrayList ids;
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        
        threads = new ArrayList<Thread>();
        ids = new ArrayList<Integer>();
        
        abas.setTabClosingPolicy(TabPane.TabClosingPolicy.ALL_TABS);
        
        // thread que monitoriza a aba/thread selecionada
        Thread thread = new Thread(){
        
            public void run(){
                
                while(true){
                    
                    try{
                        
                        if(abas!=null){
                            
                            aba_atual = abas.getSelectionModel().getSelectedItem();

                                // nova aba
                                if(aba_atual.getText().equals("+")){
                                    
                                    Platform.runLater(new Runnable() {

                                        @Override 
                                        public void run() {

                                            // objetos que carregam a página
                                            final WebView browser = new WebView();
                                            final WebEngine webEngine = browser.getEngine();
                                            
                                            abas.getTabs().remove(abas.getTabs().size()-1);

                                            // nova aba
                                            Tab nova = new Tab("Nova Aba");
                                            
                                            VBox vertical = new VBox();
                                            HBox horizontal = new HBox();

                                            TextField texto_url = new TextField("");
                                            
                                            webEngine.getLoadWorker().stateProperty().addListener((observable, oldValue, newValue) -> {
                                                
                                                if (Worker.State.SUCCEEDED.equals(newValue)) {
                                                    
                                                    String aux = webEngine.getTitle();
                                                    
                                                    if(aux.length()>15)
                                                        nova.setText(aux.substring(0, 15) + "...");
                                                    
                                                    else
                                                        nova.setText(aux);
                                                    
                                                    aux = webEngine.getLocation();
                                                    texto_url.setText(aux);
                                                }
                                            });
                                            
                                            Button go = new Button("Pesquisar");
                                            Button go2 = new Button("<");
                                            Button go3 = new Button(">");
                                            
                                            
                                            go.setOnAction(new EventHandler<ActionEvent>() {
                                                @Override 
                                                public void handle(ActionEvent e) {

                                                    webEngine.load(texto_url.getText());
                                                    Tab aba_atual = abas.getSelectionModel().getSelectedItem();
                                                    aba_atual.setText(texto_url.getText());
                                                }
                                            });
                                            
                                            go2.setOnAction(new EventHandler<ActionEvent>() {
                                                @Override 
                                                public void handle(ActionEvent e) {
                                                    
                                                    WebHistory historico = webEngine.getHistory();
                                                    ObservableList<WebHistory.Entry> entryList = historico.getEntries();
                                                    
                                                    if(historico.getCurrentIndex()!=0){
                                                    
                                                        webEngine.getHistory().go(-1);
                                                    }
                                                }
                                            });
                                            
                                            go3.setOnAction(new EventHandler<ActionEvent>() {
                                                @Override 
                                                public void handle(ActionEvent e) {
                                                    
                                                    WebHistory historico = webEngine.getHistory();
                                                    ObservableList<WebHistory.Entry> entryList = historico.getEntries();
                                                    
                                                    if(historico.getCurrentIndex()!=(entryList.size()-1)){
                                                    
                                                        webEngine.getHistory().go(1);
                                                    }
                                                }
                                            });

                                            // barra de pesquisa e botão
                                            horizontal.getChildren().addAll(go2,go3,texto_url,go);

                                            // buscar as dimensões da janela e dá-las à webview
                                            Stage atual = ((Stage)abas.getScene().getWindow());
                                            browser.prefHeightProperty().bind(atual.heightProperty());
                                            horizontal.setHgrow(texto_url, Priority.ALWAYS);

                                            ScrollPane scroll = new ScrollPane();
                                            scroll.setFitToWidth(true);
                                            scroll.setFitToHeight(true);

                                            scroll.setContent(browser);

                                            vertical.getChildren().addAll(horizontal, scroll);
                                            nova.setContent(vertical);

                                            // acrescentar as abas novas
                                            abas.getTabs().add(nova);
                                            abas.getSelectionModel().selectLast();

                                            Tab mais = new Tab("+");
                                            mais.setClosable(false);
                                            abas.getTabs().add(mais);
                                        }
                                    });
                                        
                                    }
                                }
                            
                            sleep(500);
                            
                        } catch(InterruptedException e){
                    
                        System.out.println(e.getMessage());
                    }
                
                }
                
            }
        };
        
        thread.start();
    }
    
}
