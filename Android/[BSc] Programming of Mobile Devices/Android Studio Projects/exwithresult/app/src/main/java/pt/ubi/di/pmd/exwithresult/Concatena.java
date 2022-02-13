package pt.ubi.di.pmd.exwithresult;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

public class Concatena extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState){

        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.activity_concatenar);
    }


    public void handleButton(View v){

        this.finish();
    }

    @Override
    public void finish(){

        Log.d("Concatena","Concatenar");

        try{

            Intent intent = getIntent(); // recuperar o intento que veio da primeira atividade
            String concatenada = intent.getStringExtra("nome") +" " +intent.getStringExtra("ultimo");

            Intent enviar = new Intent();
            enviar.putExtra("resultado",concatenada);
            setResult(RESULT_OK, enviar); // correu tudo bem

            super.finish();
        }

        catch(Exception e) {} // não vamos fazer nada
    }
}
