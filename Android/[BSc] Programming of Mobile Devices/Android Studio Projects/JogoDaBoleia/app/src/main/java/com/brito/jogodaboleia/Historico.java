package com.brito.jogodaboleia;

import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;

import com.google.android.material.tabs.TabLayout;

import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.coordinatorlayout.widget.CoordinatorLayout;
import androidx.viewpager.widget.ViewPager;
import androidx.appcompat.app.AppCompatActivity;

import android.util.Log;

import com.brito.jogodaboleia.ui.main.SectionsPagerAdapter;

public class Historico extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_historico);

        // cor de fundo
        CoordinatorLayout pai = (CoordinatorLayout) findViewById(R.id.pai);
        pai.setBackgroundColor(Color.parseColor("#e6e6e6"));

        SectionsPagerAdapter sectionsPagerAdapter = new SectionsPagerAdapter(this, getSupportFragmentManager());

        SharedPreferences preferencias = getSharedPreferences("Preferencias",0);
        String[] aux;

        if(preferencias.getInt("Estado",0)==6){

            Log.v("JogoDaBoleia","Teste1");
            aux = new String[26];

            for(int i=0; i<aux.length; i++){

                aux[i] = "Pergunta " + (i+1);
            }
        }

        else{

            Log.v("JogoDaBoleia","Historico");

            aux = new String[preferencias.getInt("Estado",0)*5];

            for(int i=0; i<aux.length; i++){

                aux[i] = "Pergunta " + (i+1);
            }
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