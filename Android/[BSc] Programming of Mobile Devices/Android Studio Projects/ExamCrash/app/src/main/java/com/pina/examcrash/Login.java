package com.pina.examcrash;

import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.widget.EditText;
import android.widget.Toast;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Login extends Activity {

    private EditText nome;
    private EditText password;
    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase bd;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setContentView(R.layout.activity_login);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        bd = ajudante.getWritableDatabase();
    }

    @Override
    protected void onStop(){

        super.onStop();
        bd.close();
    }

    @Override
    protected void onResume(){

        super.onResume();
        bd = ajudante.getWritableDatabase();
    }

    public void fazerLogin(View v){

        nome = (EditText) findViewById(R.id.nome_texto);
        password = (EditText) findViewById(R.id.pass_texto);

        try{

            String hash_esperado = "aa1bf4646de67fd9086cf6c79007026c";

            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] resultado = md.digest(password.getText().toString().getBytes());

            BigInteger aux = new BigInteger(1, resultado);

            String hexadecimal = aux.toString(16);

            while (hexadecimal.length() < 32)
                hexadecimal = "0" + hexadecimal;

            //verificar se a autenticação está correta
            if(nome.getText().toString().equals("admin") && hexadecimal.equals(hash_esperado)) {

                //passar parametros no intento
                Intent login = new Intent(this, EditarPerguntas.class);
                startActivity(login);

            }else{
                Toast.makeText(this,"Username ou password incorretos!", Toast.LENGTH_SHORT).show();
            }

        }

        catch(NoSuchAlgorithmException n){}
    }
}
