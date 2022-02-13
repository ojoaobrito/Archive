package pt.ubi.di.pmd.DEDOSdosPES;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Random;


public class Tabuada extends AppCompatActivity {

    private SQLiteDatabase sql;
    private AjudanteParaAbrirBaseDados ajudante;
    private String id;
    private String nome;
    private String nivel;
    private String password;
    private int resultado;
    private int num1;
    private int num2;
    private SharedPreferences pref;
    private int r_certas=0,r_erradas=0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tabuada);

        nivel = "Fácil"; // no caso de erro e por padrão, deixamos o nível inicializado a "Fácil"

        try{
            Intent intento = getIntent();

            id = intento.getStringExtra("ID");
            nome = intento.getStringExtra("Nome");
            nivel = intento.getStringExtra("Nivel");
            password = intento.getStringExtra("Password");

        } catch (Exception e){Log.v("DEDOSdosPES",e.getMessage());}

        Random r = new Random();
        int low = 0, high = 6;

        if(nivel.equals("Fácil")){

            low = 0;
            high = 6;
        }

        else if(nivel.equals("Médio")){

            low = 1;
            high = 11;
        }

        else if(nivel.equals("Especialista")){

            low = 3;
            high = 13;
        }

        else if(nivel.equals("Épico")){

            low = 3;
            high = 101;
        }

        else if(nivel.equals("Lendário")){

            low = 10;
            high = 1000;
        }

        num1 = r.nextInt(high-low)+low;
        num2 = r.nextInt(high-low)+low;
        resultado = num1*num2;

        TextView num_1 = (TextView)findViewById(R.id.num1);
        TextView num_2 = (TextView)findViewById(R.id.num2);
        num_1.setText(""+num1); //convert int to String
        num_2.setText(""+num2);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getWritableDatabase();
        TextView texto = (TextView)findViewById(R.id.Nivel);
        texto.setText("Nivel: " + nivel);

        TextView nome_aux = (TextView)findViewById(R.id.user);
        nome_aux.setText(nome);

    }

    public void switch_levels(View v){
        // mudar de nível
        TextView texto = (TextView)findViewById(R.id.Nivel);
        ContentValues contVal = new ContentValues();
        contVal.put(ajudante.COLUMN1, id);
        contVal.put(ajudante.COLUMN2, nome);
        contVal.put(ajudante.COLUMN3, password);

        if(nivel.equals("Fácil")){
            contVal.put(ajudante.COLUMN4, "Médio");
            nivel = "Médio";
            texto.setText("Nivel: Médio");
        }
        else if(nivel.equals("Médio")){
            contVal.put(ajudante.COLUMN4, "Especialista");
            nivel = "Especialista";
            texto.setText("Nivel: Especialista");
        }
        else if(nivel.equals("Especialista")){
            contVal.put(ajudante.COLUMN4, "Épico");
            nivel = "Épico";
            texto.setText("Nivel: Épico");
        }
        else if(nivel.equals("Épico")){
            contVal.put(ajudante.COLUMN4, "Lendário");
            nivel = "Lendário";
            texto.setText("Nivel: Lendário");
        }
        else if(nivel.equals("Lendário")){
            contVal.put(ajudante.COLUMN4, "Fácil");
            nivel = "Fácil";
            texto.setText("Nivel: Fácil");
        }
        contVal.put(ajudante.COLUMN5, 0);
        contVal.put(ajudante.COLUMN12, 0);

        Random r = new Random();
        int low = 0, high = 6;

        if(nivel.equals("Fácil")){

            low = 0;
            high = 6;
        }

        else if(nivel.equals("Médio")){

            low = 1;
            high = 11;
        }

        else if(nivel.equals("Especialista")){

            low = 3;
            high = 13;
        }

        else if(nivel.equals("Épico")){

            low = 3;
            high = 101;
        }

        else if(nivel.equals("Lendário")){

            low = 10;
            high = 1000;
        }

        num1 = r.nextInt(high-low)+low;
        num2 = r.nextInt(high-low)+low;
        resultado = num1*num2;

        TextView num_1 = (TextView)findViewById(R.id.num1);
        TextView num_2 = (TextView)findViewById(R.id.num2);
        num_1.setText(""+num1); //convert int to String
        num_2.setText(""+num2);

        sql.update(ajudante.TABLE_NAME1,contVal,"ID =" + id +"",null );

    }

    public void definicoes(View v){

        Intent intento = new Intent(this,Definicoes.class);
        startActivity(intento);
    }

    public void historico(View v){

        Intent intento = new Intent(this,Historico.class);

        intento.putExtra("ID", id);
        intento.putExtra("Nome",nome);
        intento.putExtra("Password",password);
        intento.putExtra("Nivel",nivel);


        startActivity(intento);


    }

    public void Resposta(View v){


        EditText respostaUser = (EditText)findViewById(R.id.resposta);
        TextView tvNum1 = (TextView)findViewById(R.id.num1);
        TextView tvNum2 = (TextView)findViewById(R.id.num2);

        if(respostaUser.getText().toString().equals("") || !respostaUser.getText().toString().matches("[0-9]+")){

            Toast.makeText(this,"Resposta Inválida!",Toast.LENGTH_LONG ).show();
            respostaUser.setText("");
            return;
        }

        // vamos contar o número de entradas no histórico
        int num_registos = 0;
        Cursor cursor = sql.query(ajudante.TABLE_NAME2, new String[]{"COUNT(*)"},null,null,null,null,null,null );

        boolean conteudo = cursor.moveToFirst();

        while (conteudo == true){

            num_registos = cursor.getInt(0);
            break;
        }

        ContentValues contVal = new ContentValues();
        contVal.put(ajudante.COLUMN6, num_registos+1);
        contVal.put(ajudante.COLUMN7, id);
        contVal.put(ajudante.COLUMN8,tvNum1.getText().toString()+ " * " +tvNum2.getText().toString()+ " = " +respostaUser.getText().toString());

        //respondeu bem
        if(Integer.parseInt(respostaUser.getText().toString())== resultado){
            Toast.makeText(this,"Resposta Certa!",Toast.LENGTH_LONG ).show();
            contVal.put(ajudante.COLUMN11,1);

            Cursor cursor2 = sql.query(ajudante.TABLE_NAME1,new String[] {"*"}, "ID='" + id + "'", null,null,null,null,null);

            conteudo = cursor2.moveToFirst();

            while(conteudo== true){
                r_certas = Integer.parseInt(cursor2.getString(4));
                r_erradas = Integer.parseInt(cursor2.getString(5));
                break;
            }

            Log.v("DEDOSdosPES","" + r_certas);
            Log.v("DEDOSdosPES","" + r_certas);
            ImageButton botao = (ImageButton) findViewById(R.id.nivel);

        //10 respostas certas seguidas
            if(r_certas+1 == 10 && !botao.isEnabled()){

                if(nivel.equals("Fácil")){
                    contVal.put(ajudante.COLUMN10,"Fácil"); // atualiza o nivel na BD
                    TextView texto = (TextView)findViewById(R.id.Nivel);
                    texto.setText("Nivel: Médio" );
                    nivel = "Médio";
                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );


                }else if(nivel.equals("Médio")){
                    contVal.put(ajudante.COLUMN10,"Médio"); // atualiza o nivel na BD
                    TextView texto = (TextView)findViewById(R.id.Nivel);
                    texto.setText("Nivel: Especialista" );
                    nivel = "Especialista";
                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );

                }else if(nivel.equals("Especialista")){
                    contVal.put(ajudante.COLUMN10,"Especialista"); // atualiza o nivel na BD
                    TextView texto = (TextView)findViewById(R.id.Nivel);
                    texto.setText("Nivel: Épico" );
                    nivel = "Épico";
                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );

                }
                else if(nivel.equals("Épico")){
                    contVal.put(ajudante.COLUMN10,"Épico"); // atualiza o nivel na BD
                    TextView texto = (TextView)findViewById(R.id.Nivel);
                    texto.setText("Nivel: Lendário" );
                    nivel = "Lendário";
                    //dar update na tabela dos Alunos com o novo nivel do aluno
                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );

                }

        //quando responde bem mas nao é a 10.o resposta certa
            }else {
                contVal.put(ajudante.COLUMN10,nivel);
                ContentValues contVal2 = new ContentValues();
                contVal2.put(ajudante.COLUMN1,id);
                contVal2.put(ajudante.COLUMN2, nome);
                contVal2.put(ajudante.COLUMN3,password );
                contVal2.put(ajudante.COLUMN4, nivel);
                contVal2.put(ajudante.COLUMN5, r_certas+1);
                contVal2.put(ajudante.COLUMN12, 0);
                sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );
            }


        }else{
            Toast.makeText(this,"Resposta Errada!",Toast.LENGTH_LONG ).show();
            contVal.put(ajudante.COLUMN11,0);

            Cursor cursor2 = sql.query(ajudante.TABLE_NAME1,new String[] {"*"}, "ID='" + id + "'", null,null,null,null,null);

            conteudo = cursor2.moveToFirst();

            while(conteudo== true){
                r_certas = Integer.parseInt(cursor2.getString(4));
                r_erradas = Integer.parseInt(cursor2.getString(5));
                break;
            }

            ImageButton botao = (ImageButton) findViewById(R.id.nivel);

            if(r_erradas+1 == 5 && !botao.isEnabled()){

                if(nivel.equals("Fácil")){
                    contVal.put(ajudante.COLUMN10,"Fácil"); // atualiza/mantem o nivel na BD
                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );

                }else if(nivel.equals("Médio")){
                    contVal.put(ajudante.COLUMN10,"Médio"); // atualiza o nivel na BD
                    TextView texto = (TextView)findViewById(R.id.Nivel);
                    texto.setText("Nivel: Fácil" );
                    nivel = "Fácil";

                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );

                }else if(nivel.equals("Especialista")){
                    contVal.put(ajudante.COLUMN10,"Especialista"); // atualiza o nivel na BD
                    TextView texto = (TextView)findViewById(R.id.Nivel);
                    texto.setText("Nivel: Médio" );
                    nivel = "Médio";
                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );

                }
                else if(nivel.equals("Épico")){
                    contVal.put(ajudante.COLUMN10,"Épico"); // atualiza o nivel na BD
                    TextView texto = (TextView)findViewById(R.id.Nivel);
                    texto.setText("Nivel: Especialista" );
                    nivel = "Especialista";

                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );

                }

                else if(nivel.equals("Lendário")){
                    contVal.put(ajudante.COLUMN10,"Lendário"); // atualiza o nivel na BD
                    TextView texto = (TextView)findViewById(R.id.Nivel);
                    texto.setText("Nivel: Épico" );
                    nivel = "Épico";

                    ContentValues contVal2 = new ContentValues();
                    contVal2.put(ajudante.COLUMN1,id);
                    contVal2.put(ajudante.COLUMN2, nome);
                    contVal2.put(ajudante.COLUMN3,password );
                    contVal2.put(ajudante.COLUMN4, nivel);
                    contVal2.put(ajudante.COLUMN5, 0);
                    contVal2.put(ajudante.COLUMN12, 0);
                    sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );

                }



                //quando responde mal mas nao é a 5.o resposta errada
            }else {
                contVal.put(ajudante.COLUMN10,nivel);
                ContentValues contVal2 = new ContentValues();
                contVal2.put(ajudante.COLUMN1,id);
                contVal2.put(ajudante.COLUMN2, nome);
                contVal2.put(ajudante.COLUMN3,password );
                contVal2.put(ajudante.COLUMN4, nivel);
                contVal2.put(ajudante.COLUMN5, 0);
                contVal2.put(ajudante.COLUMN12, r_erradas+1);
                sql.update(ajudante.TABLE_NAME1,contVal2,"ID ='" + id +"'",null );
            }


        }


        sql.insert(ajudante.TABLE_NAME2,null,contVal);

        Random r = new Random();
        int low = 0, high = 6;

        if(nivel.equals("Fácil")){

            low = 0;
            high = 6;
        }

        else if(nivel.equals("Médio")){

            low = 1;
            high = 11;
        }

        else if(nivel.equals("Especialista")){

            low = 3;
            high = 13;
        }

        else if(nivel.equals("Épico")){

            low = 3;
            high = 101;
        }

        else if(nivel.equals("Lendário")){

            low = 10;
            high = 1000;
        }

        num1 = r.nextInt(high-low)+low;
        num2 = r.nextInt(high-low)+low;
        resultado = num1*num2;

        TextView num_1 = (TextView)findViewById(R.id.num1);
        TextView num_2 = (TextView)findViewById(R.id.num2);
        num_1.setText(""+num1); //convert int to String
        num_2.setText(""+num2);

        respostaUser.setText("");


    }

    protected void onResume(){

        super.onResume();

        ImageButton btn_nivel=(ImageButton)findViewById(R.id.nivel);
        pref = getApplicationContext().getSharedPreferences("Definicoes",0);
        String modo_avancado = pref.getString("modo_avancado", "");

        //ativar/desativar botao nivel

        if(modo_avancado.equals("On")){
            btn_nivel.setEnabled(false);
            //opacidade do botao/cor
            btn_nivel.setAlpha((float)0.5);
            SharedPreferences.Editor editor = pref.edit();
            editor.putString("modo_avancado", "On");
            editor.apply();
        }else{
            btn_nivel.setEnabled(true);
            btn_nivel.setAlpha((float)1.0);
            SharedPreferences.Editor editor = pref.edit();
            editor.putString("modo_avancado", "Off");
            editor.apply();
        }

    }
}
