package com.pina.examcrash;

import android.content.Intent;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import java.util.ArrayList;

public class CategoriasHistorico extends AppCompatActivity {

    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private int id;
    private ConstraintLayout aux;
    private boolean conteudo;
    private ArrayList<String> identificadores_categorias = new ArrayList<String>(); // relaciona os ID's de cada linha (botão de pomar + editar + apagar) com os ID's guardados na base de dados
    private int num__categorias;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_categorias_historico);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getWritableDatabase();

        ScrollView scroll = (ScrollView) findViewById(R.id.scroll_categorias);
        scroll.setFadingEdgeLength(25);
    }

    @Override
    protected void onResume() {

        super.onResume();
        sql = ajudante.getReadableDatabase();

        SharedPreferences preferencias = getSharedPreferences("Preferencias",0);

        LinearLayout layout = (LinearLayout) findViewById(R.id.layout_pomares);

        Cursor cursor = sql.query(ajudante.TABLE_NAME1, new String []{"*"} ,null , null , null , null , null , null);

        // fazer reset geral
        id = 1;
        num__categorias = 0;
        identificadores_categorias.clear();
        layout.removeAllViews();

        conteudo = cursor.moveToFirst();

        if(conteudo){

            TextView texto_inicial = (TextView) findViewById(R.id.texto_inicial);
            texto_inicial.setText("");
        }

        while(conteudo){ // listar as categorias guardados

            Cursor cursor2 = sql.query(ajudante.TABLE_NAME2, new String []{"*"} ,"ID_Categoria='" + (Integer.parseInt(cursor.getString(0))) + "'" , null , null , null , null , null);
            boolean conteudo2 = cursor2.moveToFirst();
            boolean mostrar = false;
            int contador = 0;

            while(conteudo2){

                if(!preferencias.getString((Integer.parseInt(cursor.getString(0))) + "+" + contador, "-1").equals("-1")){ // a pergunta foi respondida
                    mostrar = true;
                    break;
                }

                contador++;
                conteudo2 = cursor2.moveToNext();
            }

            if(!mostrar) {
                conteudo = cursor.moveToNext();
                continue;
            }

            ConstraintLayout secundario = (ConstraintLayout) getLayoutInflater().inflate(R.layout.linha_categoria,null); // instanciar os objetos que estão em "linha_pomar.xml"
            secundario.setId(id);
            id += 1;
            identificadores_categorias.add(cursor.getString(0));

            Button novo = (Button) secundario.findViewById(R.id.categoria);
            novo.setText(cursor.getString(1));
            novo.setId(id);
            id += 1;

            TextView margem = (TextView) secundario.findViewById(R.id.margem);
            margem.setId(id+10);

            LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);

            if(id==4)
                layoutParams.setMargins(37, 5, 37, 0);

            else
                layoutParams.setMargins(37, 30, 37, 0);

            layout.addView(secundario, layoutParams);
            conteudo = cursor.moveToNext();
        }

        if(id==1){ // a variável "id" nunca foi atualizada, logo não há categorias guardadas

            TextView texto_inicial = (TextView) findViewById(R.id.texto_inicial);
            texto_inicial.setText("Não existem categorias com respostas dadas...");
        }
    }

    public void fazerPerguntas(View v){

        Intent perguntas = new Intent(this, Historico.class);

        // o ID do pai do botão (um layout secundário) é apenas um mecanismo para obter o real ID da categoria com que estamos a trabalhar
        aux = (ConstraintLayout) v.getParent();
        int button_id = (int)(((int)aux.getId() - 1) / 2);

        Log.v("ExamCrash", "Button ID: " + button_id);

        perguntas.putExtra("ID_Categoria", "" + button_id);

        startActivity(perguntas);
    }
}