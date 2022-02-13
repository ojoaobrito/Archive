package pt.ubi.di.pdm.rockefort;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.ContentValues;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class NovoJogo extends Activity {

    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private String escolha_jogo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_novo_jogo);
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

    public void novoJogo(View v){

        ContentValues valores = new ContentValues();
        EditText username = (EditText)findViewById(R.id.novo_username);
        EditText nivel = (EditText)findViewById(R.id.novo_nivel);

        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] resultado = md.digest(escolha_jogo.getBytes());

            BigInteger aux = new BigInteger(1, resultado);

            String id_final = aux.toString(16);

            while (id_final.length() < 32)
                id_final = "0" + id_final;

            valores.put(ajudante.COLUMN1, id_final);
            valores.put(ajudante.COLUMN2, escolha_jogo);
            valores.put(ajudante.COLUMN3, username.getText().toString());
            valores.put(ajudante.COLUMN4, nivel.getText().toString());

            sql.insert(ajudante.TABLE_NAME1, null, valores);
            super.finish();
        }

        catch(NoSuchAlgorithmException e){ Log.v("RockeFort",e.getMessage()); }
    }

    public void escolha(View v){

        escolha_jogo = ((Button)v).getText().toString();

        ((Button)v).setTypeface(((Button)v).getTypeface(), Typeface.BOLD);
        ((Button)v).getBackground().setAlpha(255);

        LinearLayout linear = (LinearLayout) findViewById(R.id.linear1);

        for(int i=0; i<linear.getChildCount(); i++){

            View aux_view = linear.getChildAt(i);
            Button aux = (Button) aux_view;
            if(aux_view.getId()!=((Button)v).getId()) {

                aux.getBackground().setAlpha(125);
                aux.setTypeface(null, Typeface.NORMAL);
            }
        }

        linear = (LinearLayout) findViewById(R.id.linear2);

        for(int i=0; i<linear.getChildCount(); i++){

            View aux_view = linear.getChildAt(i);
            Button aux = (Button) aux_view;
            if(aux_view.getId()!=((Button)v).getId()) {

                aux.getBackground().setAlpha(125);
                aux.setTypeface(null, Typeface.NORMAL);
            }
        }
    }
}
