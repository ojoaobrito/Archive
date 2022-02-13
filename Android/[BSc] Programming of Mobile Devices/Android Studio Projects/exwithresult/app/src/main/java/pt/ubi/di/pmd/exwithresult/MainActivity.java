package pt.ubi.di.pmd.exwithresult;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends Activity {

    private final int reqCode = 1; // código que identifica o pedido de intento
    private TextView texto;
    private EditText nome;
    private EditText ultimo;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.activity_main);

        texto = (TextView) findViewById(R.id.texto);
        nome = (EditText) findViewById(R.id.primeiro);
        ultimo = (EditText) findViewById(R.id.ultimo);
    }

    public void concatenar(View v){

        Intent intento = new Intent(this,Concatena.class);
        intento.putExtra("nome",nome.getText().toString());
        intento.putExtra("ultimo",ultimo.getText().toString());
        startActivityForResult(intento,reqCode);
    }

    // o Android chama automaticamente este método quando a segunda atividade acaba
    @Override
    protected void onActivityResult(int reqCodigo, int outcome, Intent retorno){

        if(reqCodigo==reqCode && outcome==RESULT_OK){ // estamos a falar do mesmo pedido e correu tudo bem

            String concatenada = retorno.getStringExtra("resultado");
            texto.setText(concatenada);
        }
    }
}
