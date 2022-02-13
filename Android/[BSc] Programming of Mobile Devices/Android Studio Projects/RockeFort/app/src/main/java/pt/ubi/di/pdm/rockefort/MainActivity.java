package pt.ubi.di.pdm.rockefort;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.constraintlayout.widget.ConstraintLayout;

import org.w3c.dom.Text;

import java.util.ArrayList;

public class MainActivity extends Activity {

    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private ArrayList<String> ids = new ArrayList<String>();
    private ArrayList<String> aux = new ArrayList<String>();
    private int id_aux = 0;
    private Context contexto = this;
    private Cursor cursor_main;
    private int count = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    protected void onResume(){

        super.onResume();

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getReadableDatabase();

        int id = 0;

        LinearLayout layout = (LinearLayout) findViewById(R.id.layout_Jogos);
        layout.removeAllViews();

        cursor_main = sql.query(ajudante.TABLE_NAME1, new String []{"*"} ,null , null , null , null , null , null);

        boolean conteudo = cursor_main.moveToFirst();

        while(conteudo){

            count++;
            conteudo = cursor_main.moveToNext();
        }

        cursor_main = sql.query(ajudante.TABLE_NAME1, new String []{"*"} ,null , null , null , null , null , null);

        conteudo = cursor_main.moveToFirst();

        while(conteudo){

            ConstraintLayout secundario = (ConstraintLayout) getLayoutInflater().inflate(R.layout.linha_jogo,null); // instanciar os objetos que estão em "linha_jogo.xml"
            ids.add(cursor_main.getString(0));
            secundario.setId(ids.size()-1);

            Button novo = (Button) secundario.findViewById(R.id.jogo);
            novo.setId(id);
            id += 1;

            novo.setText("JOGO: " + cursor_main.getString(1) + "\nNOME: " + cursor_main.getString(2) + "\nNÍVEL: " + cursor_main.getInt(3));

            Button edit = (Button) secundario.findViewById(R.id.edit);
            edit.setId(id);
            id += 1;

            Button trash = (Button) secundario.findViewById(R.id.trash);
            trash.setId(id);
            id += 1;

            TextView margem = (TextView) secundario.findViewById(R.id.margem);
            margem.setId(id);
            id += 1;

            LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);

            if(id==4)
                layoutParams.setMargins(37, 0, 37, 0);

            else if(count==1)
                layoutParams.setMargins(37, 0, 37, 55);

            else
                layoutParams.setMargins(37, 0, 37, 0);

            layout.addView(secundario, layoutParams);

            count--;
            conteudo = cursor_main.moveToNext();
        }
    }

    protected void onPause(){

        super.onPause();
        sql.close();
    }

    public void editarJogo(View v){

        final ConstraintLayout aux = (ConstraintLayout) v.getParent();
        Intent novo = new Intent(this,EditarJogo.class);
        Log.v("RockeFort",aux.getId() + "");

        Cursor cursor = sql.query(ajudante.TABLE_NAME1, new String []{"*"} ,"ID = '" + ids.get(aux.getId()) + "'" , null , null , null , null , null);

        boolean conteudo = cursor.moveToFirst();

        while(conteudo) {

            novo.putExtra("ID",cursor.getString(0));
            novo.putExtra("Nome",cursor.getString(1));
            novo.putExtra("Username",cursor.getString(2));
            novo.putExtra("Nivel",cursor.getString(3));
            conteudo = cursor.moveToNext();
        }

        startActivity(novo);
    }

    public void apagarJogo(View v){

        final ConstraintLayout aux = (ConstraintLayout) v.getParent();
        id_aux = aux.getId();
        AlertDialog.Builder builder = new AlertDialog.Builder(this);

        builder.setTitle("Deseja mesmo apagar este jogo?");
        builder.setMessage("Esta ação é irreversível");
        builder.setCancelable(true);

        builder.setPositiveButton("Sim", new DialogInterface.OnClickListener(){ // botão positivo

            @Override
            public void onClick(DialogInterface dialog, int which){

                sql.delete(ajudante.TABLE_NAME1,"ID='" + ids.get(id_aux) + "'", null);
                onResume();
            }
        });

        builder.setNegativeButton("Não", new DialogInterface.OnClickListener(){ // botão negativo

            @Override
            public void onClick(DialogInterface dialog, int which){

                dialog.dismiss();
            }
        });

        AlertDialog dialog = builder.create();
        dialog.show();

        // mudar a cor dos botões
        Button positivo = dialog.getButton(AlertDialog.BUTTON_POSITIVE);
        positivo.setTextColor(Color.parseColor("#006bb3"));

        Button negativo = dialog.getButton(AlertDialog.BUTTON_NEGATIVE);
        negativo.setTextColor(Color.parseColor("#006bb3"));
    }

    public void novoJogo(View v){

        Intent novo = new Intent(this, NovoJogo.class);
        startActivity(novo);
    }

    public void infoJogo(View v){

        final ConstraintLayout aux = (ConstraintLayout) v.getParent();
        Intent novo = new Intent(this,InfoJogo.class);
        Log.v("RockeFort",aux.getId() + "");

        Cursor cursor = sql.query(ajudante.TABLE_NAME1, new String []{"*"} ,"ID = '" + ids.get(aux.getId()) + "'" , null , null , null , null , null);

        boolean conteudo = cursor.moveToFirst();

        while(conteudo) {

            novo.putExtra("ID",cursor.getString(0));
            novo.putExtra("Nome",cursor.getString(1));
            novo.putExtra("Username",cursor.getString(2));
            novo.putExtra("Nivel",cursor.getString(3));
            conteudo = cursor.moveToNext();
        }

        startActivity(novo);
    }
}
