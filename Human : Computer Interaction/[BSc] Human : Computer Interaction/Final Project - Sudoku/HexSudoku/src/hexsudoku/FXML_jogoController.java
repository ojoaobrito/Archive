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
import java.util.Random;
import java.util.ResourceBundle;
import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.ProgressIndicator;
import javafx.scene.control.TextField;
import javafx.scene.input.InputMethodEvent;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Border;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

/**
 * FXML Controller class
 *
 * @author joaobrito
 */
public class FXML_jogoController implements Initializable {
    
    @FXML private ProgressBar progBar;
    @FXML private Label lblProg;
    @FXML private Button btnPause;
    @FXML
    private CheckBox help;
    
    @FXML
    private Label labelHelp;
     
    @FXML
    private GridPane grid ;
    @FXML
    private GridPane grid1 ;
  
    @FXML
    private GridPane grid2 ;
    @FXML
    private GridPane grid3 ;
    @FXML
    private GridPane grid4;
    @FXML
    private GridPane grid5 ;
    @FXML
    private GridPane grid6 ;
    @FXML
    private GridPane grid7 ;
    @FXML
    private GridPane grid8 ;
    @FXML
    private GridPane grid9 ;
    @FXML
    private GridPane grid10 ;
    @FXML
    private GridPane grid11 ;
    @FXML
    private GridPane grid12;
    @FXML
    private GridPane grid13 ;
    @FXML
    private GridPane grid14 ;
    @FXML
    private GridPane grid15 ;
    @FXML
    private GridPane grid16 ;
    
    @FXML
    private Label dificuldade;
    
    @FXML
    private Button desistir;
    
    
    private int num_ajudas;
    private int[][] TabInicial;
    private int tempo = 0;
    private String player;
    private String dificuldade_aux;
    int concluido=0;
    
    /**
     * Initializes the controller class.
     */
    
    @FXML
    private void desistirAction(ActionEvent event) throws Exception{
    
        // fechar a janela de jogo
        Stage stage = (Stage) desistir.getScene().getWindow();
        stage.close();
        
        // criar a janela de menu
        Stage anotherStage = new Stage();

        Parent root2 = FXMLLoader.load(getClass().getResource("FXML_menu.fxml"));

        Scene scene2 = new Scene(root2);

        anotherStage.setScene(scene2);
        anotherStage.show();
    }
    private int pausa=0;
    
    @FXML
    private void PauseAction(ActionEvent event) throws Exception{
        if(pausa==1){
            
            pausa=0;
            btnPause.setText("Pausar");
        }else{
            pausa=1;
            grid.setVisible(false);
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Informação");
            alert.setHeaderText(null);
            alert.setContentText("O jogo esta em pausa.");
            alert.showAndWait();
            grid.setVisible(true);
            pausa=0;
        }
    }
    
    public String[][] insereSudoku(String[][] Sudoku, String[] x,int id){
                int xmin=0,xmax=0,ymin=0,ymax=0;
                if(id==1){xmin=0;xmax=4;ymin=0;ymax=4;}
                if(id==2){xmin=0;xmax=4;ymin=4;ymax=8;}
                if(id==3){xmin=0;xmax=4;ymin=8;ymax=12;}
                if(id==4){xmin=0;xmax=4;ymin=12;ymax=16;}
                if(id==5){xmin=4;xmax=8;ymin=0;ymax=4;}
                if(id==6){xmin=4;xmax=8;ymin=4;ymax=8;}
                if(id==7){xmin=4;xmax=8;ymin=8;ymax=12;}
                if(id==8){xmin=4;xmax=8;ymin=12;ymax=16;}
                if(id==9){xmin=8;xmax=12;ymin=0;ymax=4;}
                if(id==10){xmin=8;xmax=12;ymin=4;ymax=8;}
                if(id==11){xmin=8;xmax=12;ymin=8;ymax=12;}
                if(id==12){xmin=8;xmax=12;ymin=12;ymax=16;}
                if(id==13){xmin=12;xmax=16;ymin=0;ymax=4;}
                if(id==14){xmin=12;xmax=16;ymin=4;ymax=8;}
                if(id==15){xmin=12;xmax=16;ymin=8;ymax=12;}
                if(id==16){xmin=12;xmax=16;ymin=12;ymax=16;}
                
                int l=0;
                for (int m=xmin;m<xmax;m++){

                    for (int j=ymin;j<ymax;j++){
                       Sudoku[m][j]=x[l];
                       l++;
                               
                    }
                }
                
                
        return Sudoku;
    
    
    }
    public boolean VerificaSudo(String[][] Sudo){
        if(!VerificaArr(getSudokuUtil(grid1))){return false;}
        if(!VerificaArr(getSudokuUtil(grid2))){return false;}
        if(!VerificaArr(getSudokuUtil(grid3))){return false;}
        if(!VerificaArr(getSudokuUtil(grid4))){return false;}
        if(!VerificaArr(getSudokuUtil(grid5))){return false;}
        if(!VerificaArr(getSudokuUtil(grid6))){return false;}
        if(!VerificaArr(getSudokuUtil(grid7))){return false;}
        if(!VerificaArr(getSudokuUtil(grid8))){return false;}
        if(!VerificaArr(getSudokuUtil(grid9))){return false;}
        if(!VerificaArr(getSudokuUtil(grid10))){return false;}
        if(!VerificaArr(getSudokuUtil(grid11))){return false;}
        if(!VerificaArr(getSudokuUtil(grid12))){return false;}
        if(!VerificaArr(getSudokuUtil(grid13))){return false;}
        if(!VerificaArr(getSudokuUtil(grid14))){return false;}
        if(!VerificaArr(getSudokuUtil(grid15))){return false;}
        if(!VerificaArr(getSudokuUtil(grid16))){return false;}
        
        
        
        for (int m=0;m<16;m++){
            for (int i=0;i<16;i++){

                for (int j=i+1;j<16;j++){
                    
                    if(Sudo[m][i].equalsIgnoreCase(Sudo[m][j]) || Sudo[m][i].equalsIgnoreCase("") ){
                        System.out.println("m: "+ m+" i:"+i);
                        return false;
                    }
                }
                for (int j=m+1;j<16;j++){
                    
                    if(Sudo[m][i].equalsIgnoreCase(Sudo[j][i]) || Sudo[m][i].equalsIgnoreCase("")){
                        System.out.println("m: "+ m+" i:"+i);
                        return false;
                    }
                }
                
                

            }

        } 
        
        
    return true;
    } 
    
    
    public boolean VerificaArr(String[] arr){
        for (int i=0;i<16;i++){
        
            for (int j=i+1;j<16;j++){
        
                if(arr[i].equalsIgnoreCase(arr[j])){return false;}
        
            }
            
        
        }
    return true;
    }
    
    
    @FXML
    private void SubmitAction(ActionEvent event) throws Exception{
            pausa=1;
            
            String[][] SudokuUtil= new String[16][16];
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid1),1);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid2),2);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid3),3);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid4),4);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid5),5);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid6),6);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid7),7);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid8),8);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid9),9);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid10),10);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid11),11);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid12),12);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid13),13);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid14),14);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid15),15);
            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid16),16);
            
            
            
            
            if(VerificaSudo(SudokuUtil)){
                
                concluido=1;
                // objeto ideal para escrita em ficheiros .txt
                PrintWriter writer = new PrintWriter(new FileOutputStream("games_data.txt", true));
                
                writer.println(dificuldade_aux + " // " + player + " " + tempo);
                writer.close();
                
                
                 // fechar a janela de menu
                Stage stage = (Stage) grid.getScene().getWindow();
                stage.close();

                // criar a janela de jogo
                Stage anotherStage = new Stage();

                Parent root2 = FXMLLoader.load(getClass().getResource("FXML_menu.fxml"));

                Scene scene2 = new Scene(root2);

                anotherStage.setScene(scene2);
                anotherStage.setResizable(false);
                anotherStage.show();
                
            }
            
            else{
            
                // criar um popup a informar que o tabuleiro está errado
                Stage anotherStage = new Stage();

                Parent root2 = FXMLLoader.load(getClass().getResource("FXML_popup.fxml"));

                Scene scene2 = new Scene(root2);

                anotherStage.setScene(scene2);
                anotherStage.show();
                
                System.out.println(timer.toString());
                
                pausa = 0;
            }
    }
    
    private int mode = 10;
    private boolean work = true;
    
    Timer timer;
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        concluido=0;
        try{
            
            File ficheiro = new File("current_player.txt");
            Scanner leitura = new Scanner(ficheiro);
            String aux = leitura.nextLine();
            
            String dif = aux.split(" - ")[1];
            dificuldade_aux = dif;
            player = aux.split(" - ")[0];
            dificuldade.setText("Dificuldade: " + dif);
            
            if(dif.equals("Fácil")){
                mode = 15*60;
                num_ajudas = 4;
            }

            if(dif.equals("Médio")){
                mode = 10*60;
                num_ajudas = 2;
            }

            if(dif.equals("Difícil")){
                mode = 7*60;
            }
        }
       
        
        catch(IOException e){
            
            System.out.println(e.getMessage());
        }
        
        int[][] Sudoku=genSudoku();
        Sudoku=baralhaSudoku(Sudoku);
        TabInicial=TabuleiroInicial(Sudoku);
        //int[][] SudokuTable;
        genLayout(grid1,partSudoku(TabInicial,1));
        genLayout(grid2,partSudoku(TabInicial,2));
        genLayout(grid3,partSudoku(TabInicial,3));
        genLayout(grid4,partSudoku(TabInicial,4));
        genLayout(grid5,partSudoku(TabInicial,5));
        genLayout(grid6,partSudoku(TabInicial,6));
        genLayout(grid7,partSudoku(TabInicial,7));
        genLayout(grid8,partSudoku(TabInicial,8));
        genLayout(grid9,partSudoku(TabInicial,9));
        genLayout(grid10,partSudoku(TabInicial,10));
        genLayout(grid11,partSudoku(TabInicial,11));
        genLayout(grid12,partSudoku(TabInicial,12));
        genLayout(grid13,partSudoku(TabInicial,13));
        genLayout(grid14,partSudoku(TabInicial,14));
        genLayout(grid15,partSudoku(TabInicial,15));
        genLayout(grid16,partSudoku(TabInicial,16));
        
        timer = new Timer();
        timer.schedule(new RepetidorAux(), 0, 1000);
        
        Thread thread = new Thread(){ //thread para contar o tempo passado
        
            public void run(){
            
                try{
                    
                    while(work){
                        
                        sleep(1000);
                        
                        if (pausa==0){
                            tempo++;
                            continue;
                        }
                        if (concluido==1){
                            break;
                        }
                        
                        if((dificuldade_aux.equals("Fácil") && tempo==900) || (dificuldade_aux.equals("Médio") && tempo==600)
                                || (dificuldade_aux.equals("Difícil") && tempo==420)){
                            
                            work = false;
                        
                            Platform.runLater(new Runnable() { // informar a UIThread
                                @Override public void run() {
                                    
                                    try{
                                        
                                        // fechar a janela atual
                                        Stage stage = (Stage) desistir.getScene().getWindow();
                                        stage.close();
                                    
                                        // criar a janela de jogo
                                        Stage anotherStage = new Stage();

                                        Parent root2 = FXMLLoader.load(getClass().getResource("FXML_finalPopup.fxml"));

                                        Scene scene2 = new Scene(root2);

                                        anotherStage.setScene(scene2);
                                        anotherStage.setResizable(false);
                                        anotherStage.show();
                                    }
                                    
                                    catch(Exception e){
                                    
                                        System.out.println(e.getMessage());
                                    }
                                }
                            });
                        }
                    }
                }
                
                catch(Exception e){
                
                    System.out.println(e.getMessage());
                }
            }
        };
        
        thread.start();
        
        
    }
    
    public int[][] TabuleiroInicial(int[][] Sudoku){
         
        int[][] Tab=new int[16][16];
         
        for (int i=0;i<16;i++){
            int n=new Random().nextInt(3);
            int[] arrpos= new int[16];

            for (int j=0;j<6+n+num_ajudas;j++){

                int pos=new Random().nextInt(16);
                if(arrpos[pos]==0){

                    arrpos[pos]=1;
                }else{j--;}


           }
           Tab=atualiza(Sudoku,Tab,i,arrpos);
        }
        
        return Tab;
    }
    
    public int[][] atualiza(int[][] Sudoku , int[][] aux,int nr,int[] arr){
        
        int xmin=0,xmax=0,ymin=0,ymax=0,id=-1;
        
        for (int i=0;i<16;i++){
        
            if(arr[i]==1){
                id=i+1;
                if(id==1){xmin=0;xmax=4;ymin=0;ymax=4;}
                if(id==2){xmin=0;xmax=4;ymin=4;ymax=8;}
                if(id==3){xmin=0;xmax=4;ymin=8;ymax=12;}
                if(id==4){xmin=0;xmax=4;ymin=12;ymax=16;}
                if(id==5){xmin=4;xmax=8;ymin=0;ymax=4;}
                if(id==6){xmin=4;xmax=8;ymin=4;ymax=8;}
                if(id==7){xmin=4;xmax=8;ymin=8;ymax=12;}
                if(id==8){xmin=4;xmax=8;ymin=12;ymax=16;}
                if(id==9){xmin=8;xmax=12;ymin=0;ymax=4;}
                if(id==10){xmin=8;xmax=12;ymin=4;ymax=8;}
                if(id==11){xmin=8;xmax=12;ymin=8;ymax=12;}
                if(id==12){xmin=8;xmax=12;ymin=12;ymax=16;}
                if(id==13){xmin=12;xmax=16;ymin=0;ymax=4;}
                if(id==14){xmin=12;xmax=16;ymin=4;ymax=8;}
                if(id==15){xmin=12;xmax=16;ymin=8;ymax=12;}
                if(id==16){xmin=12;xmax=16;ymin=12;ymax=16;}

                for (int m=xmin;m<xmax;m++){

                    for (int j=ymin;j<ymax;j++){
                        if(Sudoku[m][j]==nr){
                            aux[m][j]=nr;
                            break;
                        }   
                    }
                }
            }else{
            
                id=i+1;
                if(id==1){xmin=0;xmax=4;ymin=0;ymax=4;}
                if(id==2){xmin=0;xmax=4;ymin=4;ymax=8;}
                if(id==3){xmin=0;xmax=4;ymin=8;ymax=12;}
                if(id==4){xmin=0;xmax=4;ymin=12;ymax=16;}
                if(id==5){xmin=4;xmax=8;ymin=0;ymax=4;}
                if(id==6){xmin=4;xmax=8;ymin=4;ymax=8;}
                if(id==7){xmin=4;xmax=8;ymin=8;ymax=12;}
                if(id==8){xmin=4;xmax=8;ymin=12;ymax=16;}
                if(id==9){xmin=8;xmax=12;ymin=0;ymax=4;}
                if(id==10){xmin=8;xmax=12;ymin=4;ymax=8;}
                if(id==11){xmin=8;xmax=12;ymin=8;ymax=12;}
                if(id==12){xmin=8;xmax=12;ymin=12;ymax=16;}
                if(id==13){xmin=12;xmax=16;ymin=0;ymax=4;}
                if(id==14){xmin=12;xmax=16;ymin=4;ymax=8;}
                if(id==15){xmin=12;xmax=16;ymin=8;ymax=12;}
                if(id==16){xmin=12;xmax=16;ymin=12;ymax=16;}

                for (int m=xmin;m<xmax;m++){

                    for (int j=ymin;j<ymax;j++){
                        if(Sudoku[m][j]==nr){
                            aux[m][j]=-1;
                            break;
                        }   
                    }
                }
            }
        }
    return aux;
    }
    
    public int[][] genSudoku(){
    
        Random random = new Random();
            final int n = 4;//aqui vai o numero de elementos do seu sudoku(4 vai ser um sudoku 4x4
            final int [][] field = new int[n * n][n * n];//matriz onde será armazenado o sudoku
            int x = random.nextInt(130);//semente aleatória para não gerar o mesmo sudoku
            System.out.println(x);
            for (int i = 0; i < n; i++, x++)
            {
                for (int j = 0; j < n; j++, x += n)
                {
                    for (int k = 0; k < n * n; k++, x++)
                    {
                        
                        field[n * i + j][k] = (x % (n * n)) ;
                       
                    }
                }
            }
    
        return(field);
    }
    
    public int[][] baralhaSudoku(int[][] Sudoku){
        Sudoku=trocaLinhas(Sudoku,0,2);
        Sudoku=trocaLinhas(Sudoku,0,3);
        Sudoku=trocaLinhas(Sudoku,4,6);
        Sudoku=trocaLinhas(Sudoku,4,7);
        Sudoku=trocaLinhas(Sudoku,4,5);
        Sudoku=trocaLinhas(Sudoku,8,9);
        Sudoku=trocaLinhas(Sudoku,8,10);
        Sudoku=trocaLinhas(Sudoku,13,15);
        Sudoku=trocaLinhas(Sudoku,13,14);
        Sudoku=trocaColunas(Sudoku,0,3);
        Sudoku=trocaColunas(Sudoku,0,2);
        Sudoku=trocaColunas(Sudoku,4,6);
        Sudoku=trocaColunas(Sudoku,4,7);
        Sudoku=trocaColunas(Sudoku,4,5);
        Sudoku=trocaColunas(Sudoku,8,9);
        Sudoku=trocaColunas(Sudoku,8,10);
        Sudoku=trocaColunas(Sudoku,13,15);
        Sudoku=trocaColunas(Sudoku,13,14);
    
        
        
    return(Sudoku);
    }
    
    
    public int[] partSudoku(int[][] Sudo, int id){
        int xmin=0,xmax=0,ymin=0,ymax=0;
        int[] aux = new int[16];
        if(id==1){xmin=0;xmax=4;ymin=0;ymax=4;}
        if(id==2){xmin=0;xmax=4;ymin=4;ymax=8;}
        if(id==3){xmin=0;xmax=4;ymin=8;ymax=12;}
        if(id==4){xmin=0;xmax=4;ymin=12;ymax=16;}
        if(id==5){xmin=4;xmax=8;ymin=0;ymax=4;}
        if(id==6){xmin=4;xmax=8;ymin=4;ymax=8;}
        if(id==7){xmin=4;xmax=8;ymin=8;ymax=12;}
        if(id==8){xmin=4;xmax=8;ymin=12;ymax=16;}
        if(id==9){xmin=8;xmax=12;ymin=0;ymax=4;}
        if(id==10){xmin=8;xmax=12;ymin=4;ymax=8;}
        if(id==11){xmin=8;xmax=12;ymin=8;ymax=12;}
        if(id==12){xmin=8;xmax=12;ymin=12;ymax=16;}
        if(id==13){xmin=12;xmax=16;ymin=0;ymax=4;}
        if(id==14){xmin=12;xmax=16;ymin=4;ymax=8;}
        if(id==15){xmin=12;xmax=16;ymin=8;ymax=12;}
        if(id==16){xmin=12;xmax=16;ymin=12;ymax=16;}
        int l=0;
        for (int i=xmin;i<xmax;i++){
        
            for (int j=ymin;j<ymax;j++){
                aux[l]=Sudo[i][j];
                l++;
            }
            
        }
    
    return(aux);
    }
    public String translate(int j){
        if(j<0){
            return "";
        }else if(j<10&&j>=0){
              return(Integer.toString(j));
        }else if(j==10){
              return("A");
        }else if(j==11){
              return("B");
        }else if(j==12){
              return("C");
        }else if(j==13){
              return("D");
        }else if(j==14){
              return("E");
        }else if(j==15){
              return("F");
        }
    return("");
    }
    
    public int[][] trocaLinhas(int[][] Sudoku, int i , int j){
        int aux=-1;
        for(int m=0;m<16;m++){
            aux=Sudoku[i][m];
            Sudoku[i][m]=Sudoku[j][m];
            Sudoku[j][m]=aux;
        }
    
    return(Sudoku);
    }
    
    public int[][] trocaColunas(int[][] Sudoku, int i , int j){
        int aux=-1;
        for(int m=0;m<16;m++){
            aux=Sudoku[m][i];
            Sudoku[m][i]=Sudoku[m][j];
            Sudoku[m][j]=aux;
        }
    
    return(Sudoku);
    }
    
    
    public String[] getSudokuUtil(GridPane gp) {
    String[] i=new String[16];
    int count=0,l=0;
    
    for (Node node :gp.getChildren()  ) {
        if(l!=16){
            Pane pane=(Pane)node;
            int w=0;
            for(Node panenode : pane.getChildren()){
                if(w==0){
                TextField text= (TextField) panenode;
                i[count]=text.getText();


                w++;
                }

            }
            count++;
        } 
        l++;
    
    
    }
    
    return i;
    }
    public boolean Verifica(String str){
    
            if(str.equalsIgnoreCase("0")){return true;}
            if(str.equalsIgnoreCase("1")){return true;}
            if(str.equalsIgnoreCase("2")){return true;}
            if(str.equalsIgnoreCase("3")){return true;}
            if(str.equalsIgnoreCase("4")){return true;}
            if(str.equalsIgnoreCase("5")){return true;}
            if(str.equalsIgnoreCase("6")){return true;}
            if(str.equalsIgnoreCase("7")){return true;}
            if(str.equalsIgnoreCase("8")){return true;}
            if(str.equalsIgnoreCase("9")){return true;}
            if(str.equalsIgnoreCase("A")){return true;}
            if(str.equalsIgnoreCase("B")){return true;}
            if(str.equalsIgnoreCase("C")){return true;}
            if(str.equalsIgnoreCase("D")){return true;}
            if(str.equalsIgnoreCase("E")){return true;}
            if(str.equalsIgnoreCase("F")){return true;}
            
    return false;
    }
    
    String pos="";
    int grids=1;
    public void genLayout(GridPane gp,int[] sudoku){
        
        int i=0;
        for (Node node :gp.getChildren()  ) {
            if(i!=16){
                TextField text = new TextField();
                if (translate(sudoku[i]).equals("")){
                    text.setText("");
                    text.setEditable(true);
                    text.setFont(Font.font("Normal", FontWeight.NORMAL, 16));
                }else{
                    text.setText(translate(sudoku[i])+"\n");
                    text.setEditable(false);
                    
                    text.setFont(Font.font("Normal", FontWeight.BOLD, 16));

                }

                Pane pane =(Pane)node;
                pane.setStyle("-fx-background-color:#ffffff;");
                text.setStyle("-fx-border-color:#ffffff;");

                text.setMaxWidth(Double.MAX_VALUE);
                text.setMaxHeight(Double.MAX_VALUE);


                text.setId(Integer.toString(grids)+"-"+Integer.toString(i));
                 i=i+1;
                 text.setOnMouseClicked((MouseEvent t) -> {
                    if(text.isEditable()){
                     if(help.isSelected()){
                           pos=text.getId();
                           System.out.println("OI " + pos);
                            String[][] SudokuUtil= new String[16][16];
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid1),1);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid2),2);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid3),3);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid4),4);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid5),5);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid6),6);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid7),7);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid8),8);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid9),9);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid10),10);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid11),11);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid12),12);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid13),13);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid14),14);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid15),15);
                            SudokuUtil=insereSudoku(SudokuUtil, getSudokuUtil(grid16),16);
                           int[] help=getAjuda(Integer.parseInt(pos.split("-")[0]),Integer.parseInt(pos.split("-")[1]),SudokuUtil);
                           String helps="";
                           for(int m=0;m<16;m++){
                               if(help[m]==0){
                                   if(m<10){
                           
                                    helps= helps + Integer.toString(m)+", ";
                                    }else if(m==10){
                                    helps= helps + "A" +", ";
                                    }else if (m==11){
                                    helps= helps + "B" +", ";
                                    }else if(m==12){
                                    helps= helps + "C" +", ";
                                    }else if (m==13){
                                    helps= helps + "D" +", ";
                                    }else if(m==14){
                                    helps= helps + "E" +", ";
                                    }else if (m==15){
                                    helps= helps + "F" +", ";
                                    }else{
                                    }
                               }
                            }
                           
                            String[] aux = helps.split(", ");
                            String final_string = "";
                            
                            if(aux.length==1)
                                final_string = aux[0];
                            
                            else{
                            
                                for(int j=0; j<aux.length; j++){

                                    if(j==(aux.length-2)){

                                        final_string += aux[j] + " ou " + aux[j+1];
                                        break;
                                    }

                                    final_string += aux[j] + ", ";
                                }
                            }
                            
                           labelHelp.setText(final_string);
                     }else{
                         labelHelp.setText("");
                     }}  
                    });


              text.setOnKeyReleased((KeyEvent t) -> {
                       if(!Verifica(text.getText())){
                           text.setText("");
                       }

                });

               //text.setOnMouseClicked();
                pane.getChildren().add(text);
            }
        }
      grids++;
    }
    
    public int[] getAjuda(int id,int pos,String[][] Sudo){
      int[] r=new int[16];
      int xmin=0,xmax=0,ymin=0,ymax=0;
        if(id==1){xmin=0;xmax=4;ymin=0;ymax=4;}
        if(id==2){xmin=0;xmax=4;ymin=4;ymax=8;}
        if(id==3){xmin=0;xmax=4;ymin=8;ymax=12;}
        if(id==4){xmin=0;xmax=4;ymin=12;ymax=16;}
        if(id==5){xmin=4;xmax=8;ymin=0;ymax=4;}
        if(id==6){xmin=4;xmax=8;ymin=4;ymax=8;}
        if(id==7){xmin=4;xmax=8;ymin=8;ymax=12;}
        if(id==8){xmin=4;xmax=8;ymin=12;ymax=16;}
        if(id==9){xmin=8;xmax=12;ymin=0;ymax=4;}
        if(id==10){xmin=8;xmax=12;ymin=4;ymax=8;}
        if(id==11){xmin=8;xmax=12;ymin=8;ymax=12;}
        if(id==12){xmin=8;xmax=12;ymin=12;ymax=16;}
        if(id==13){xmin=12;xmax=16;ymin=0;ymax=4;}
        if(id==14){xmin=12;xmax=16;ymin=4;ymax=8;}
        if(id==15){xmin=12;xmax=16;ymin=8;ymax=12;}
        if(id==16){xmin=12;xmax=16;ymin=12;ymax=16;}
        int l=0,x=0,y=0;
        for (int i=xmin;i<xmax;i++){
        
            for (int j=ymin;j<ymax;j++){
                if(!Sudo[i][j].equals("")){
                     if(Sudo[i][j].equalsIgnoreCase("A")){
                        r[10]=1;
                     }else if(Sudo[i][j].equalsIgnoreCase("B")){
                        r[11]=1;
                     }else if(Sudo[i][j].equalsIgnoreCase("C")){
                        r[12]=1;
                     }else if(Sudo[i][j].equalsIgnoreCase("D")){
                        r[13]=1;
                     }else if(Sudo[i][j].equalsIgnoreCase("E")){
                        r[14]=1;
                     }else if(Sudo[i][j].equalsIgnoreCase("F")){
                        r[15]=1;
                     }else {
                         r[Integer.parseInt(Sudo[i][j])]=1;
                     }
                }
                if(l==pos){
                    x=i;
                    y=j;
                }
                l++;
            }
            
        }
        for(int i=0;i<16;i++){
            
            if(!Sudo[i][y].equals("")){
                if(Sudo[i][y].equalsIgnoreCase("A")){
                   r[10]=1;
                }else if(Sudo[i][y].equalsIgnoreCase("B")){
                   r[11]=1;
                }else if(Sudo[i][y].equalsIgnoreCase("C")){
                   r[12]=1;
                }else if(Sudo[i][y].equalsIgnoreCase("D")){
                   r[13]=1;
                }else if(Sudo[i][y].equalsIgnoreCase("E")){
                   r[14]=1;
                }else if(Sudo[i][y].equalsIgnoreCase("F")){
                   r[15]=1;
                }else{
                    r[Integer.parseInt(Sudo[i][y])]=1;
                }
            }
            if(!Sudo[x][i].equals("")){
                if(Sudo[x][i].equalsIgnoreCase("A")){
                   r[10]=1;
                }else if(Sudo[x][i].equalsIgnoreCase("B")){
                   r[11]=1;
                }else if(Sudo[x][i].equalsIgnoreCase("C")){
                   r[12]=1;
                }else if(Sudo[x][i].equalsIgnoreCase("D")){
                   r[13]=1;
                }else if(Sudo[x][i].equalsIgnoreCase("E")){
                   r[14]=1;
                }else if(Sudo[x][i].equalsIgnoreCase("F")){
                   r[15]=1;
                }else{
                    r[Integer.parseInt(Sudo[x][i])]=1;
                }
            }
            
        }
        
       return r;
    }
    
    private int reps2;
    class RepetidorAux extends TimerTask{
            int reps = mode;
            int sec = 0;
            
            public void rekt(double perct) {
                Platform.runLater(new Runnable() {
                    @Override
                    public void run() {
                        progBar.setProgress(perct);
                        lblProg.setText(reps/60+" min "+reps%60 +" seg" );
                    }
                });
                
            }

            public void run(){
                if(pausa==1){
                
                    rekt((mode - reps) / new Double(mode));
                
                }else{
                    if (reps > -1){
                    reps--;
                    sec++;
                    reps2=mode -reps;
                    rekt((mode - reps) / new Double(mode));
                    if (reps == 0){
                    
                        timer.cancel();
                        
                    }
                    }
                }
                
                
            }
        }
}    
    

