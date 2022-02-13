package com.pina.examcrash.ui.main;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import com.pina.examcrash.AjudanteParaAbrirBaseDados;
import com.pina.examcrash.Historico;
import com.pina.examcrash.Perguntas;
import com.pina.examcrash.R;

import java.util.ArrayList;
import java.util.Random;

/**
 * A placeholder fragment containing a simple view.
 */
public class PlaceholderFragment extends Fragment {

    private static final String ARG_SECTION_NUMBER = "section_number";
    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private ArrayList<String> perguntas = new ArrayList<String>();
    private ArrayList<ArrayList<String>> respostas = new ArrayList<ArrayList<String>>();
    private ArrayList<Integer> certas = new ArrayList<Integer>();
    private ArrayList<Integer> desconta = new ArrayList<Integer>();
    private TextView pergunta;
    private static int id_categoria;
    private ArrayList<String> respostas_dadas = new ArrayList<String>();
    private Context contexto;
    private Button[] botoes_resposta = new Button[4];
    private String[] respostas_indices = {"A) ", "B) ", "C) ", "D) "};

    private PageViewModel pageViewModel;

    public static PlaceholderFragment newInstance(int index, String id_categoria_in, Context contexto) {

        id_categoria = Integer.parseInt(id_categoria_in);
        contexto = contexto;

        PlaceholderFragment fragment = new PlaceholderFragment();
        Bundle bundle = new Bundle();
        bundle.putInt(ARG_SECTION_NUMBER, index);
        fragment.setArguments(bundle);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        pageViewModel = ViewModelProviders.of(this).get(PageViewModel.class);
        int index = 1;
        if (getArguments() != null) {
            index = getArguments().getInt(ARG_SECTION_NUMBER);
        }
        pageViewModel.setIndex(index);
    }

    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_teste, container, false);
        final TextView textView_pergunta = root.findViewById(R.id.pergunta);

        final Button[] botoes_resposta = new Button[4];
        botoes_resposta[0] = (Button) root.findViewById(R.id.resposta1);
        botoes_resposta[1] = (Button) root.findViewById(R.id.resposta2);
        botoes_resposta[2] = (Button) root.findViewById(R.id.resposta3);
        botoes_resposta[3] = (Button) root.findViewById(R.id.resposta4);

        ajudante = new AjudanteParaAbrirBaseDados(getActivity().getApplicationContext());
        sql = ajudante.getReadableDatabase();

        Cursor cursor = sql.query(ajudante.TABLE_NAME2, new String []{"*"} ,"ID_Categoria='" + id_categoria + "'", null , null , null , null , null);
        boolean conteudo = cursor.moveToFirst();
        int contador = 0;

        SharedPreferences preferencias = getActivity().getApplicationContext().getSharedPreferences("Preferencias",0);

        Log.v("ExamCrash", "Fragment: " + id_categoria);

        while(conteudo){

            respostas_dadas.add(preferencias.getString(id_categoria + "+" + contador, "1"));

            perguntas.add(cursor.getString(2));
            String[] respostas_aux = cursor.getString(3).split("\n");
            ArrayList<String> respostas_aux_2 = new ArrayList<String>();

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
                    certas.add(j + 1);
                }

                if(codigo_resposta_aux[j].equals("P")){
                    desconta.add(j + 1);
                }

                else{
                    desconta.add(-1);
                }
            }

            contador++;
            conteudo = cursor.moveToNext();
        }

        pageViewModel.getText().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {

                int pergunta = Integer.parseInt(s);

                textView_pergunta.setText(perguntas.get(pergunta-1));
                botoes_resposta[0].setText(respostas.get(pergunta-1).get(0));
                botoes_resposta[1].setText(respostas.get(pergunta-1).get(1));
                botoes_resposta[2].setText(respostas.get(pergunta-1).get(2));
                botoes_resposta[3].setText(respostas.get(pergunta-1).get(3));

                // 1º botão
                if(botoes_resposta[0].getText().toString().replace(respostas_indices[0], "").equals(""))
                    botoes_resposta[0].setVisibility(View.INVISIBLE);
                else{
                    if(1==Integer.parseInt(respostas_dadas.get(pergunta-1)) &&
                            certas.get(pergunta-1)==1) {
                        botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_certo_escolhido);
                    }

                    else if(1==Integer.parseInt(respostas_dadas.get(pergunta-1)) &&
                            certas.get(pergunta-1)!=1) {

                        if(1==Integer.parseInt(respostas_dadas.get(pergunta-1)))
                            botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_errado_escolhido);

                        else
                            botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_neutro_escolhido);
                    }

                    else if(certas.get(pergunta-1)==1) {
                        botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_certo);
                    }
                }

                // 2º botão
                if(botoes_resposta[1].getText().toString().replace(respostas_indices[1], "").equals(""))
                    botoes_resposta[1].setVisibility(View.INVISIBLE);
                else{
                    if(2==Integer.parseInt(respostas_dadas.get(pergunta-1)) &&
                            certas.get(pergunta-1)==2){
                        botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_certo_escolhido);
                    }

                    else if(2==Integer.parseInt(respostas_dadas.get(pergunta-1)) &&
                            certas.get(pergunta-1)!=2){

                        if(2==Integer.parseInt(respostas_dadas.get(pergunta-1)))
                            botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_errado_escolhido);

                        else
                            botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_neutro_escolhido);
                    }

                    else if(2==botoes_resposta[1].getId()){
                        botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_certo);
                    }
                }

                // 3º botão
                if(botoes_resposta[2].getText().toString().replace(respostas_indices[2], "").equals(""))
                    botoes_resposta[2].setVisibility(View.INVISIBLE);
                else{
                    if(3==Integer.parseInt(respostas_dadas.get(pergunta-1)) &&
                            certas.get(pergunta-1)==3){
                        botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_certo_escolhido);
                    }

                    else if(3==Integer.parseInt(respostas_dadas.get(pergunta-1)) &&
                            certas.get(pergunta-1)!=3){

                        if(3==Integer.parseInt(respostas_dadas.get(pergunta-1)))
                            botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_errado_escolhido);

                        else
                            botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_neutro_escolhido);
                    }

                    else if(certas.get(pergunta-1)==3){
                        botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_certo);
                    }
                }

                // 4º botão
                if(botoes_resposta[3].getText().toString().replace(respostas_indices[3], "").equals(""))
                    botoes_resposta[3].setVisibility(View.INVISIBLE);
                else{
                if(4==Integer.parseInt(respostas_dadas.get(pergunta-1)) &&
                        certas.get(pergunta-1)==botoes_resposta[3].getId()) {
                    botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_certo_escolhido);
                }

                else if(4==Integer.parseInt(respostas_dadas.get(pergunta-1)) &&
                        certas.get(pergunta-1)!=4){

                    if(4==Integer.parseInt(respostas_dadas.get(pergunta-1)))
                        botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_errado_escolhido);

                    else
                        botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_neutro_escolhido);
                }

                else if(certas.get(pergunta-1)==4){
                    botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_certo);
                }
            }
            }
        });
        return root;
    }
}