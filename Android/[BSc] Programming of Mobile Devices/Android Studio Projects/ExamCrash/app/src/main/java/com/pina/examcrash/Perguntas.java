package com.pina.examcrash;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.app.Activity;
import android.content.ContentValues;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.view.animation.AlphaAnimation;
import android.view.animation.Animation;
import android.view.animation.AnimationSet;
import android.view.animation.DecelerateInterpolator;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Random;

public class Perguntas extends AppCompatActivity implements View.OnClickListener {

    private Handler handler_principal;
    private int i = 0;
    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private ArrayList<String> perguntas = new ArrayList<String>();
    private ArrayList<ArrayList<String>> respostas = new ArrayList<ArrayList<String>>();
    private ArrayList<Integer> certas = new ArrayList<Integer>();
    private ArrayList<Integer> desconta = new ArrayList<Integer>();
    private TextView pergunta;
    private Button[] botoes_resposta = new Button[4];
    private int pergunta_atual = 0;
    private int contador_botao;
    private int id_categoria;
    private int acertos = 0;
    private String[] respostas_indices = {"A) ", "B) ", "C) ", "D) "};

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_perguntas);

        botoes_resposta[0] = (Button) findViewById(R.id.resposta1);
        botoes_resposta[0].setOnClickListener(this);
        botoes_resposta[1] = (Button) findViewById(R.id.resposta2);
        botoes_resposta[1].setOnClickListener(this);
        botoes_resposta[2] = (Button) findViewById(R.id.resposta3);
        botoes_resposta[2].setOnClickListener(this);
        botoes_resposta[3] = (Button) findViewById(R.id.resposta4);
        botoes_resposta[3].setOnClickListener(this);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getReadableDatabase();

        try{

            Intent intento = getIntent();
            id_categoria = Integer.parseInt(intento.getStringExtra("ID_Categoria"));

            Log.v("ExamCrash", "Categoria ID: " + id_categoria);
        }

        catch(Exception e){

            Log.e("ExamCrash", "Erro ao receber o intento!");
            super.finish();
        }

        Cursor cursor = sql.query(ajudante.TABLE_NAME2, new String []{"*"} ,"ID_Categoria='" + id_categoria + "'", null , null , null , null , null);
        boolean conteudo = cursor.moveToFirst();
        int contador = 0;

        while(conteudo){

            perguntas.add(cursor.getString(2));
            String[] respostas_aux = cursor.getString(3).split("\n");
            ArrayList <String> respostas_aux_2 = new ArrayList<String>();

            for(int j = 0; j < 4; j++){

                try {
                    respostas_aux_2.add(respostas_indices[j] + respostas_aux[j]);
                }
                catch(Exception e){
                    respostas_aux_2.add(respostas_indices[j] + "");
                }
            }

            respostas.add(respostas_aux_2);

            String codigo_resposta = cursor.getString(4);
            String[] codigo_resposta_aux = codigo_resposta.split("\n");

            for(int j = 0; j < respostas_aux.length; j++){

                if(codigo_resposta_aux[j].equals("C")){
                    certas.add(botoes_resposta[j].getId());
                }

                if(codigo_resposta_aux[j].equals("P")){
                    desconta.add(botoes_resposta[j].getId());
                }

                else{
                    desconta.add(-1);
                }
            }

            contador++;
            conteudo = cursor.moveToNext();
        }

        pergunta = (TextView) findViewById(R.id.pergunta);

        // preferências da aplicação
        SharedPreferences preferencias = getSharedPreferences("Preferencias", 0);

        // cor de fundo
        ConstraintLayout pai = (ConstraintLayout) findViewById(R.id.pai);
        pai.setBackgroundColor(Color.parseColor("#e6e6e6"));

        pergunta.setText(perguntas.get(pergunta_atual));

        for(int i=0; i<4; i++){

            if(!respostas.get(pergunta_atual).get(i).replace(respostas_indices[i], "").equals(""))
                botoes_resposta[i].setText(respostas.get(pergunta_atual).get(i));

            else{
                botoes_resposta[i].setText("");
                botoes_resposta[i].setVisibility(View.INVISIBLE);
            }
        }
    }

    @Override
    protected void onResume(){

        super.onResume();
    }

    public void onClick(final View v){

        Button b = (Button) findViewById(v.getId());

        SharedPreferences preferencias = this.getSharedPreferences("Preferencias",0);
        SharedPreferences.Editor editor = preferencias.edit();

        if(b.getText().toString().contains("A) "))
            editor.putString(id_categoria + "+" + pergunta_atual, "1");
        else if(b.getText().toString().contains("B) "))
            editor.putString(id_categoria + "+" + pergunta_atual, "2");
        else if(b.getText().toString().contains("C) "))
            editor.putString(id_categoria + "+" + pergunta_atual, "3");
        else if(b.getText().toString().contains("D) "))
            editor.putString(id_categoria + "+" + pergunta_atual, "4");

        editor.apply();

        // desativar os botões
        botoes_resposta[0].setClickable(false);
        botoes_resposta[1].setClickable(false);
        botoes_resposta[2].setClickable(false);
        botoes_resposta[3].setClickable(false);

        final Handler handler_fora = new Handler();

        Thread mudar_pergunta = new Thread(){

            public void run(){

                //ANIMAR OS BOTÕES
                //---------------------------------------------------------------------------------------------------------------------------------------------------------
                if (v.getId() == certas.get(pergunta_atual)) { // animar o botão da resposta certa

                    acertos++;

                    // mudar a cor de fundo
                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            v.setBackgroundResource(R.drawable.resposta_fundo_certo);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(10);

                    } catch (Exception e) {

                        Log.e("ExamCrash", e.getMessage());
                    }

                    // fazer a animação
                    r = new Runnable() {

                        @Override
                        public void run() {

                            v.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                @Override
                                public void run() {
                                    v.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                }
                            });
                        }
                    };

                    handler_fora.post(r);
                }

                else if ((desconta.size() != 0) && v.getId() == desconta.get(pergunta_atual)) { // animar um dos botões de resposta errada, mas com desconto (perca de 1 ponto)

                    acertos--;

                    // mudar a cor de fundo
                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            v.setBackgroundResource(R.drawable.resposta_fundo_errado);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(10);

                    } catch (Exception e) {

                        Log.e("ExamCrash", e.getMessage());
                    }

                    // fazer a animação
                    r = new Runnable() {

                        @Override
                        public void run() {

                            v.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                @Override
                                public void run() {
                                    v.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                }
                            });
                        }
                    };

                    handler_fora.post(r);
                }

                else{ // animar um dos botões de resposta errada, mas sem desconto

                    // mudar a cor de fundo
                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            v.setBackgroundResource(R.drawable.resposta_fundo_neutro);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(10);

                    } catch (Exception e) {

                        Log.e("ExamCrash", e.getMessage());
                    }

                    // fazer a animação
                    r = new Runnable() {

                        @Override
                        public void run() {

                            v.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                @Override
                                public void run() {
                                    v.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                }
                            });
                        }
                    };

                    handler_fora.post(r);
                }
                //---------------------------------------------------------------------------------------------------------------------------------------------------------

                //AVALIAR SE É PARA MUDAR DE PERGUNTA OU TERMINAR A ATIVIDADE
                //---------------------------------------------------------------------------------------------------------------------------------------------------------
                if ((pergunta_atual + 1) == perguntas.size()) { // terminar a atividade

                    SharedPreferences preferencias = getSharedPreferences("Preferencias", 0);

                    // delay
                    try {
                        Thread.sleep(600);

                    } catch (Exception e) {

                        Log.e("ExamCrash", e.getMessage());
                    }

                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            if(botoes_resposta[0].getId()!=certas.get(pergunta_atual))
                                botoes_resposta[0].animate().translationX(-2000).setDuration(700);

                            if(botoes_resposta[1].getId()!=certas.get(pergunta_atual))
                                botoes_resposta[1].animate().translationX(-2000).setDuration(900);

                            if(botoes_resposta[2].getId()!=certas.get(pergunta_atual))
                                botoes_resposta[2].animate().translationX(-2000).setDuration(1100);

                            if(botoes_resposta[3].getId()!=certas.get(pergunta_atual))
                                botoes_resposta[3].animate().translationX(-2000).setDuration(1300);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(1500);

                    } catch (Exception e) {

                        Log.e("ExamCrash", e.getMessage());
                    }

                    Intent intento = new Intent();
                    setResult(Activity.RESULT_OK,intento);
                    Perguntas.super.finish();

                }

                else { // mudar de pergunta

                    // delay
                    try {
                        Thread.sleep(600);

                    } catch (Exception e) {

                        Log.e("ExamCrash", e.getMessage());
                    }

                    pergunta_atual++;

                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            if(botoes_resposta[0].getId()!=certas.get(pergunta_atual-1))
                                botoes_resposta[0].animate().translationX(-2000).setDuration(700);

                            if(botoes_resposta[1].getId()!=certas.get(pergunta_atual-1))
                                botoes_resposta[1].animate().translationX(-2000).setDuration(900);

                            if(botoes_resposta[2].getId()!=certas.get(pergunta_atual-1))
                                botoes_resposta[2].animate().translationX(-2000).setDuration(1100);

                            if(botoes_resposta[3].getId()!=certas.get(pergunta_atual-1))
                                botoes_resposta[3].animate().translationX(-2000).setDuration(1300);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(2000);

                        if(botoes_resposta[0].getId()==certas.get(pergunta_atual-1))
                            botoes_resposta[0].animate().translationX(-2000).setDuration(1000);

                        else if(botoes_resposta[1].getId()==certas.get(pergunta_atual-1))
                            botoes_resposta[1].animate().translationX(-2000).setDuration(1000);

                        else if(botoes_resposta[2].getId()==certas.get(pergunta_atual-1))
                            botoes_resposta[2].animate().translationX(-2000).setDuration(1000);

                        else if(botoes_resposta[3].getId()==certas.get(pergunta_atual-1))
                            botoes_resposta[3].animate().translationX(-2000).setDuration(1000);

                        Thread.sleep(750);

                    } catch (Exception e) {

                        Log.e("ExamCrash", e.getMessage());
                    }

                    r = new Runnable() {

                        @Override
                        public void run() {

                            pergunta.animate().scaleX(0.95f).scaleY(0.95f).setDuration(80).withEndAction(new Runnable() {
                                @Override
                                public void run() {
                                    pergunta.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                }
                            });
                            pergunta.setText(perguntas.get(pergunta_atual));

                            // restaurar a cor original
                            botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo);
                            botoes_resposta[0].setText(respostas.get(pergunta_atual).get(0));
                            botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo);
                            botoes_resposta[1].setText(respostas.get(pergunta_atual).get(1));
                            botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo);
                            botoes_resposta[2].setText(respostas.get(pergunta_atual).get(2));
                            botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo);
                            botoes_resposta[3].setText(respostas.get(pergunta_atual).get(3));

                            botoes_resposta[0].setVisibility(View.INVISIBLE);
                            botoes_resposta[1].setVisibility(View.INVISIBLE);
                            botoes_resposta[2].setVisibility(View.INVISIBLE);
                            botoes_resposta[3].setVisibility(View.INVISIBLE);

                            // mudar a resposta
                            botoes_resposta[0].animate().translationX(2000).setDuration(1000);
                            botoes_resposta[1].animate().translationX(2000).setDuration(1000);
                            botoes_resposta[2].animate().translationX(2000).setDuration(1000);
                            botoes_resposta[3].animate().translationX(2000).setDuration(1000);

                        }
                    };

                    handler_fora.post(r);

                    try {
                        Thread.sleep(1000);
                    }
                    catch(Exception e){
                        Log.e("ExamCrash", e.getMessage());
                    }

                    r = new Runnable() {

                        @Override
                        public void run() {

                            if(botoes_resposta[0].getText().toString().replace(respostas_indices[0], "").equals(""))
                                botoes_resposta[0].setVisibility(View.INVISIBLE);
                            else
                                botoes_resposta[0].setVisibility(View.VISIBLE);

                            if(botoes_resposta[1].getText().toString().replace(respostas_indices[1], "").equals(""))
                                botoes_resposta[1].setVisibility(View.INVISIBLE);
                            else
                                botoes_resposta[1].setVisibility(View.VISIBLE);

                            if(botoes_resposta[2].getText().toString().replace(respostas_indices[2], "").equals(""))
                                botoes_resposta[2].setVisibility(View.INVISIBLE);
                            else
                                botoes_resposta[2].setVisibility(View.VISIBLE);

                            if(botoes_resposta[3].getText().toString().replace(respostas_indices[3], "").equals(""))
                                botoes_resposta[3].setVisibility(View.INVISIBLE);
                            else
                                botoes_resposta[3].setVisibility(View.VISIBLE);

                            botoes_resposta[0].animate().translationX(0).setDuration(700);
                            botoes_resposta[1].animate().translationX(0).setDuration(900);
                            botoes_resposta[2].animate().translationX(0).setDuration(1100);
                            botoes_resposta[3].animate().translationX(0).setDuration(1300);

                            // reativar os botões
                            botoes_resposta[0].setClickable(true);
                            botoes_resposta[1].setClickable(true);
                            botoes_resposta[2].setClickable(true);
                            botoes_resposta[3].setClickable(true);
                        }
                    };

                    handler_fora.post(r);
                }
                //---------------------------------------------------------------------------------------------------------------------------------------------------------
            }
        };

        mudar_pergunta.start();
    }
}


