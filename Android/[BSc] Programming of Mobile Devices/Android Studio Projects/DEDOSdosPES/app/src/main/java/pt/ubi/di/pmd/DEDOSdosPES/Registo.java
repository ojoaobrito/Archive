//Registo do utilizador para que este consiga entrar na app

package pt.ubi.di.pmd.DEDOSdosPES;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Registo extends AppCompatActivity {

    private SQLiteDatabase sql;
    private AjudanteParaAbrirBaseDados ajudante;



    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registo);

        ajudante = new AjudanteParaAbrirBaseDados(this);

    }


    protected void onResume(){
        super.onResume();
        sql = ajudante.getWritableDatabase();

    }

    protected void onPause(){
        super.onPause();
        sql.close();
    }


    public void registar(View v){

        // registar
        EditText Nome = (EditText)findViewById(R.id.username);
        EditText Password = (EditText)findViewById(R.id.pass);

        if(Nome.getText().toString().equals("")){
            Toast.makeText(this, "Username inválido", Toast.LENGTH_LONG).show();
            return;
        }

        if(Password.getText().toString().equals("")){
            Toast.makeText(this, "Password inválida", Toast.LENGTH_LONG).show();
            return;
        }

        //fazer uma query à base de dados e obter conteudo
        Cursor cursor = sql.query(ajudante.TABLE_NAME1,new String[] {"*"}, null, null,null,null,null,null);

        boolean conteudo = cursor.moveToFirst();
        int cont=0;

        //contar o numero de alunos guardados
        while (conteudo==true){
            cont++;

            if(cursor.getString(1).equals(Nome.getText().toString())){

                Toast.makeText(this, "Utilizador já existente!", Toast.LENGTH_LONG).show();
                return;
            }

            conteudo = cursor.moveToNext();
        }

        String hexadecimal="";
        //calcular o hash da password
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] resultado = md.digest(Password.getText().toString().getBytes());

            BigInteger aux = new BigInteger(1, resultado);

            hexadecimal = aux.toString(16);

            while (hexadecimal.length() < 32)
                hexadecimal = "0" + hexadecimal;
        } catch (NoSuchAlgorithmException e) {}

        // guarda na BD
        ContentValues contVal = new ContentValues();
        contVal.put(ajudante.COLUMN1, cont+1);
        contVal.put(ajudante.COLUMN2,Nome.getText().toString());
        contVal.put(ajudante.COLUMN3, hexadecimal);
        contVal.put(ajudante.COLUMN4, "Fácil");
        contVal.put(ajudante.COLUMN5, 0);
        contVal.put(ajudante.COLUMN12, 0);
        sql.insert(ajudante.TABLE_NAME1,null, contVal);

        // lançar a atividade principal
        Intent intento = new Intent(this,Tabuada.class);
        intento.putExtra("ID",cont+1 + "");
        intento.putExtra("Nome",Nome.getText().toString());
        intento.putExtra("Password",hexadecimal);
        intento.putExtra("Nivel","Fácil");
        startActivity(intento);
    }
}
