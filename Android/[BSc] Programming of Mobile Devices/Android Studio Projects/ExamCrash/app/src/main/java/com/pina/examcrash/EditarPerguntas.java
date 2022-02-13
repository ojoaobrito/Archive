package com.pina.examcrash;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.Toast;

public class EditarPerguntas extends AppCompatActivity {

    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private LinearLayout linear;
    private EditText categoria;
    private EditText pergunta;
    private EditText resposta;
    private CheckBox check_certa;
    private CheckBox check_errada_nao_desconta;
    private CheckBox check_errada_desconta;
    private String nome_categoria = "";
    private String nome_pergunta = "";
    private int id_categoria = -1;
    private int id_pergunta = -1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_editar_perguntas);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getReadableDatabase();
    }

    public void guardarPergunta(View v){

        categoria = (EditText) findViewById(R.id.categoria_inserir);
        pergunta = (EditText) findViewById(R.id.pergunta_inserir);

        Cursor cursor = sql.query(ajudante.TABLE_NAME1, new String []{"*"} ,null , null , null , null , null , null);

        boolean conteudo = cursor.moveToFirst();
        boolean existente = false;
        while(conteudo) { // percorrer a base de dados

            nome_categoria = cursor.getString(1);
            id_categoria = cursor.getInt(0);

            if(nome_categoria.toLowerCase().equals(categoria.getText().toString().toLowerCase())){ // categoria já existente
                existente = true;
                break;
            }

            conteudo = cursor.moveToNext();
        }

        if(!existente)
            id_categoria += 1;

        cursor = sql.query(ajudante.TABLE_NAME2, new String []{"*"} ,null , null , null , null , null , null);

        conteudo = cursor.moveToFirst();
        existente = false;
        while(conteudo) { // percorrer a base de dados

            nome_pergunta = cursor.getString(2);
            id_pergunta = cursor.getInt(1);

            conteudo = cursor.moveToNext();
        }

        id_pergunta += 1;

        ContentValues valores_categoria = new ContentValues(); // usado para inserir os dados na nossa base de dados
        ContentValues valores_pergunta = new ContentValues(); // usado para inserir os dados na nossa base de dados

        if(categoria.getText().toString().equals("")) {
            Toast.makeText(this, "Introduza uma categoria!", Toast.LENGTH_SHORT).show();
            return;
        }

        if(pergunta.getText().toString().equals("")) {
            Toast.makeText(this, "Introduza uma pergunta!", Toast.LENGTH_SHORT).show();
            return;
        }

        valores_categoria.put(ajudante.COLUMN1, id_categoria);
        valores_categoria.put(ajudante.COLUMN2, categoria.getText().toString());
        valores_categoria.put(ajudante.COLUMN3, "");

        valores_pergunta.put(ajudante.COLUMN4, id_categoria);
        valores_pergunta.put(ajudante.COLUMN5, id_pergunta);
        valores_pergunta.put(ajudante.COLUMN6, pergunta.getText().toString());
        valores_pergunta.put(ajudante.COLUMN9, "");

        String texto_respostas = "";
        String codigo_respostas = "";
        int certas = 0;
        int contador_respostas = 0;

        for(int i = 0; i < 4; i++) {

            if(i == 0) {
                linear = (LinearLayout) findViewById(R.id.linear_perguntas_linha_1);
                resposta = (EditText) linear.findViewById(R.id.resposta_inserir_1);
                check_certa = (CheckBox) linear.findViewById(R.id.certa_1);
                check_errada_nao_desconta = (CheckBox) linear.findViewById(R.id.errada_nao_desconta_1);
                check_errada_desconta = (CheckBox) linear.findViewById(R.id.errada_desconta_1);
            }

            else if(i == 1) {
                linear = (LinearLayout) findViewById(R.id.linear_perguntas_linha_2);
                resposta = (EditText) linear.findViewById(R.id.resposta_inserir_2);
                check_certa = (CheckBox) linear.findViewById(R.id.certa_2);
                check_errada_nao_desconta = (CheckBox) linear.findViewById(R.id.errada_nao_desconta_2);
                check_errada_desconta = (CheckBox) linear.findViewById(R.id.errada_desconta_2);
            }

            else if(i == 2) {
                linear = (LinearLayout) findViewById(R.id.linear_perguntas_linha_3);
                resposta = (EditText) linear.findViewById(R.id.resposta_inserir_3);
                check_certa = (CheckBox) linear.findViewById(R.id.certa_3);
                check_errada_nao_desconta = (CheckBox) linear.findViewById(R.id.errada_nao_desconta_3);
                check_errada_desconta = (CheckBox) linear.findViewById(R.id.errada_desconta_3);
            }

            else{
                linear = (LinearLayout) findViewById(R.id.linear_perguntas_linha_4);
                resposta = (EditText) linear.findViewById(R.id.resposta_inserir_4);
                check_certa = (CheckBox) linear.findViewById(R.id.certa_4);
                check_errada_nao_desconta = (CheckBox) linear.findViewById(R.id.errada_nao_desconta_4);
                check_errada_desconta = (CheckBox) linear.findViewById(R.id.errada_desconta_4);
            }

            if(resposta.getText().toString().equals(""))
                continue;

            String codigo_aux = "";

            if(check_certa.isChecked()){
                codigo_aux += "C";
                certas++;
            }

            if(check_errada_nao_desconta.isChecked())
                codigo_aux += "E";

            if(check_errada_desconta.isChecked())
                codigo_aux += "P";

            if(codigo_aux.length() == 0){
                Toast.makeText(this, "Verifique se as respostas têm um tipo definido!", Toast.LENGTH_SHORT).show();
                return;
            }

            if(codigo_aux.length() > 1){
                Toast.makeText(this, "As respostas só podem ter 1 tipo!", Toast.LENGTH_SHORT).show();
                return;
            }

            if(i != 3){

                texto_respostas += resposta.getText().toString() + "\n";
                codigo_respostas += codigo_aux + "\n";
                contador_respostas++;
            }

            else{
                texto_respostas += resposta.getText().toString();
                codigo_respostas += codigo_aux;
                contador_respostas++;
            }
        }

        if(certas == 0){
            Toast.makeText(this, "Não existem respostas certas!", Toast.LENGTH_SHORT).show();
            return;
        }

        if(contador_respostas == 1){
            Toast.makeText(this, "Não pode existir apenas 1 resposta!", Toast.LENGTH_SHORT).show();
            return;
        }

        Log.v("ExamCrash", categoria.getText().toString() + " | " + pergunta.getText().toString() + ":\n" + texto_respostas + "\n" + codigo_respostas);

        valores_pergunta.put(ajudante.COLUMN7, texto_respostas);
        valores_pergunta.put(ajudante.COLUMN8, codigo_respostas);

        sql.insert(ajudante.TABLE_NAME1, null, valores_categoria);
        sql.insert(ajudante.TABLE_NAME2, null, valores_pergunta);

        categoria.setText("");
        pergunta.setText("");
        ((EditText) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_1)).findViewById(R.id.resposta_inserir_1)).setText("");
        ((EditText) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_2)).findViewById(R.id.resposta_inserir_2)).setText("");
        ((EditText) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_3)).findViewById(R.id.resposta_inserir_3)).setText("");
        ((EditText) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_4)).findViewById(R.id.resposta_inserir_4)).setText("");

        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_1)).findViewById(R.id.certa_1)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_2)).findViewById(R.id.certa_2)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_3)).findViewById(R.id.certa_3)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_4)).findViewById(R.id.certa_4)).setChecked(false);

        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_1)).findViewById(R.id.errada_nao_desconta_1)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_2)).findViewById(R.id.errada_nao_desconta_2)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_3)).findViewById(R.id.errada_nao_desconta_3)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_4)).findViewById(R.id.errada_nao_desconta_4)).setChecked(false);

        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_1)).findViewById(R.id.errada_desconta_1)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_2)).findViewById(R.id.errada_desconta_2)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_3)).findViewById(R.id.errada_desconta_3)).setChecked(false);
        ((CheckBox) ((LinearLayout) findViewById(R.id.linear_perguntas_linha_4)).findViewById(R.id.errada_desconta_4)).setChecked(false);

        Toast.makeText(this, "Pergunta guardada!", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onResume() {
        super.onResume();
    }

    @Override
    protected void onPause() {
        super.onPause();
        sql.close();
    }
}