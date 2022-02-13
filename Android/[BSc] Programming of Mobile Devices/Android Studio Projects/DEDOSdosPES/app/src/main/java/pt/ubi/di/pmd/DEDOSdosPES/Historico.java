//O histórico guarda o nivel, pergunta e resposta(correta/errada) do utilizador
package pt.ubi.di.pmd.DEDOSdosPES;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.util.Log;
import android.widget.LinearLayout;
import android.widget.TextView;

public class Historico extends AppCompatActivity {
    private SQLiteDatabase sql;
    private AjudanteParaAbrirBaseDados ajudante;
    private String id;
    private String nome;
    private String nivel;
    private String password;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_historico);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getReadableDatabase();

        try{
            Intent intento = getIntent();

            id = intento.getStringExtra("ID");
            nome = intento.getStringExtra("Nome");
            nivel = intento.getStringExtra("Nivel");
            password = intento.getStringExtra("Password");

        } catch (Exception e){
            Log.v("DEDOSdosPES",e.getMessage());}
    }

    protected void onResume(){
        super.onResume();
        sql = ajudante.getReadableDatabase();

        LinearLayout linear = (LinearLayout)findViewById(R.id.linear);
        linear.removeAllViews();
        Cursor cursor = sql.query(ajudante.TABLE_NAME2, new String[]{"*"},"ID='"+id+"'",null,null,null,null,null );

        boolean conteudo = cursor.moveToFirst();
        int id = 1;

        while (conteudo == true){

            Log.v("DEDOSdosPES",cursor.getString(2));
            int num1 = Integer.parseInt(cursor.getString(2).split(" ")[0]);
            int num2 = Integer.parseInt(cursor.getString(2).split(" ")[2]);
            int resultado = Integer.parseInt(cursor.getString(2).split(" ")[4]);

            if(num1 * num2 == resultado){

                //Texto de uma linha
                ConstraintLayout secundario = (ConstraintLayout)getLayoutInflater().inflate(R.layout.linha_historico,null);

                secundario.setId(id);
                id++;

                TextView tvNivel = (TextView)secundario.findViewById(R.id.Nivel);
                tvNivel.setText(cursor.getString(3));
                tvNivel.setId(id);
                id++;

                TextView tvTexto = (TextView)secundario.findViewById(R.id.Texto);
                tvTexto.setText(num1 + " x " + num2 + " = " + resultado );
                tvTexto.setId(id);
                id++;

                linear.addView(secundario);

            }else{

                //Texto de uma linha
                ConstraintLayout secundario = (ConstraintLayout)getLayoutInflater().inflate(R.layout.linha_historico_errado,null);

                secundario.setId(id);
                id++;

                TextView tvNivel = (TextView)secundario.findViewById(R.id.Nivel);
                tvNivel.setText(cursor.getString(3));
                tvNivel.setId(id);
                id++;

                TextView tvTexto = (TextView)secundario.findViewById(R.id.Texto);
                tvTexto.setText(num1 + " x " + num2 + " = " + resultado );
                tvTexto.setId(id);
                id++;

                linear.addView(secundario);

            }

            conteudo = cursor.moveToNext();
            Log.v("DEDOSdosPES","1");

        }


    }
}
