package pt.ubi.di.pdm.rockefort;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.ContentValues;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class EditarJogo extends Activity {

    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private EditText nome_jogo;
    private EditText username;
    private EditText nivel;
    private String ID;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_editar_jogo);

        nome_jogo = (EditText)findViewById(R.id.novo_nome);
        username = (EditText)findViewById(R.id.novo_username);
        nivel = (EditText)findViewById(R.id.novo_nivel);

        try {

            Intent intento = getIntent();

            ID = intento.getStringExtra("ID");

            // informação atual, mostrar ao utilizador apenas a título informativo
            nome_jogo.setHint(intento.getStringExtra("Nome"));
            username.setHint(intento.getStringExtra("Username"));
            nivel.setHint(intento.getStringExtra("Nivel"));

        } catch (Exception e) {

            Log.e("RockeFort", "Erro ao receber o intento!");
            super.finish();
        }
    }

    protected void onResume(){

        super.onResume();
        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getWritableDatabase();
    }

    protected void onPause(){

        super.onPause();
        sql.close();
    }

    public void editarJogo(View v){

        ContentValues valores = new ContentValues();
        EditText nome_jogo = (EditText)findViewById(R.id.novo_nome);
        EditText username = (EditText)findViewById(R.id.novo_username);
        EditText nivel = (EditText)findViewById(R.id.novo_nivel);

        valores.put(ajudante.COLUMN1, ID);

        if(!nome_jogo.getText().toString().equals(""))
            valores.put(ajudante.COLUMN2, nome_jogo.getText().toString());

        else
            valores.put(ajudante.COLUMN2, nome_jogo.getHint().toString());

        if(!username.getText().toString().equals(""))
            valores.put(ajudante.COLUMN3, username.getText().toString());

        else
            valores.put(ajudante.COLUMN3, username.getHint().toString());

        if(!nivel.getText().toString().equals(""))
            valores.put(ajudante.COLUMN4, nivel.getText().toString());

        else
            valores.put(ajudante.COLUMN4, nivel.getHint().toString());

        sql.update(ajudante.TABLE_NAME1, valores,"ID = '" + ID + "'",null);
        super.finish();

    }
}
