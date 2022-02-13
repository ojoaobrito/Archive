package com.pina.examcrash;

import android.content.ContentValues;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Color;
import android.os.Bundle;

import com.google.android.material.tabs.TabLayout;

import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.coordinatorlayout.widget.CoordinatorLayout;
import androidx.viewpager.widget.ViewPager;
import androidx.appcompat.app.AppCompatActivity;

import android.util.Log;
import android.widget.Button;

import com.pina.examcrash.ui.main.SectionsPagerAdapter;

public class Historico extends AppCompatActivity {

    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private int id_categoria = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_historico);

        // cor de fundo
        CoordinatorLayout pai = (CoordinatorLayout) findViewById(R.id.pai);
        pai.setBackgroundColor(Color.parseColor("#e6e6e6"));

        try{

            Intent intento = getIntent();
            id_categoria = Integer.parseInt(intento.getStringExtra("ID_Categoria"));
        }

        catch(Exception e){

            Log.e("ExamCrash", "Erro ao receber o intento!");
            super.finish();
        }

        SharedPreferences preferencias = getSharedPreferences("Preferencias",0);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getReadableDatabase();

        Cursor cursor = sql.query(ajudante.TABLE_NAME2, new String []{"*"} ,"ID_Categoria='" + id_categoria + "'" , null , null , null , null , null);

        boolean conteudo = cursor.moveToFirst();
        Log.v("ExamCrash", "Conteudo: " + conteudo);
        int contador = 0;

        while(conteudo){

            if(!preferencias.getString(id_categoria + "+" + contador, "-1").equals("-1")) // a pergunta foi respondida
                contador += 1;

            conteudo = cursor.moveToNext();
        }

        SharedPreferences.Editor editor = preferencias.edit();
        editor.putInt("Num_perguntas", contador);
        editor.putString("ID_Categoria", "" + id_categoria);
        editor.apply();

        Log.v("ExamCrash", "" + contador);
        Log.v("ExamCrash", "" + id_categoria);

        SectionsPagerAdapter sectionsPagerAdapter = new SectionsPagerAdapter(this, getSupportFragmentManager());

        String[] aux;

        aux = new String[contador];

        for(int i=0; i<aux.length; i++){

            aux[i] = "Pergunta " + (i+1);
        }

        sectionsPagerAdapter.mudar(aux);

        ViewPager viewPager = findViewById(R.id.view_pager);
        viewPager.setAdapter(sectionsPagerAdapter);
        viewPager.setOffscreenPageLimit(1);
        TabLayout tabs = findViewById(R.id.tabs);
        tabs.setupWithViewPager(viewPager);
        tabs.setSelectedTabIndicatorColor(getIntFromColor(255,255,255));
    }

    public int getIntFromColor(int Red, int Green, int Blue){
        Red = (Red << 16) & 0x00FF0000; //Shift red 16-bits and mask out other stuff
        Green = (Green << 8) & 0x0000FF00; //Shift Green 8-bits and mask out other stuff
        Blue = Blue & 0x000000FF; //Mask out anything not blue.

        return 0xFF000000 | Red | Green | Blue; //0xFF000000 for 100% Alpha. Bitwise OR everything together.
    }
}