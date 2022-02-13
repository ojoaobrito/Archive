package pt.ubi.di.pmd.exstorage2;

import android.app.Activity;
import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.support.constraint.ConstraintLayout;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;

import java.text.ParseException;

public class FavouriteMovies extends Activity{

    private SQLiteDatabase sql;
    private AjudanteParaAbrirBaseDados ajudante;

    @Override
    protected void onCreate(Bundle savedInstanceState){

        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.activity_favourite_movies);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getWritableDatabase();

    }

    @Override
    protected void onResume(){

        super.onResume();
        sql = ajudante.getWritableDatabase();

        LinearLayout layout = (LinearLayout) findViewById(R.id.llsv);
        Cursor oCursor = sql.query(ajudante.TABLE_NAME, new String []{"*"} ,null , null , null , null , null , null);

        boolean bCarryOn = oCursor.moveToFirst();

        while(bCarryOn){

            LinearLayout novo = (LinearLayout) getLayoutInflater().inflate(R.layout.line, null);
            novo.setId(oCursor.getInt( 0)*10+4);

            EditText oED1 = (EditText) novo.findViewById (R.id.ed1);
            oED1.setId(oCursor.getInt(0)*10+2);
            oED1.setText(oCursor.getString(1));
            oED1.layout(0,20,0,20);

            EditText oED2 = (EditText) novo.findViewById (R.id.ed2);
            oED2.setId(oCursor.getInt(0)*10+3);
            oED2.setText("" + oCursor.getInt(2));
            oED2.layout(0,20,0,20);

            Button oB1 = (Button) novo.findViewById(R.id.edit);
            oB1.setId(oCursor.getInt(0)*10+1);
            oB1.layout(0,20,0,20);

            Button oB2 = (Button) novo.findViewById(R.id.del);
            oB2.setId(oCursor.getInt(0)*10);
            oB1.layout(0,20,0,20);

            layout.addView(novo);

            bCarryOn = oCursor.moveToNext(); // andar para o próximo resultado/linha
        }
    }

    @Override
    protected void onPause(){

        super.onPause();
        ajudante.close();
    }

    public void onINSERTclick(View v){

        ContentValues oCV = new ContentValues ();
        EditText oED1 = (EditText) findViewById(R.id.nome);
        EditText oED2 = (EditText) findViewById (R.id.ano);
        oCV.put(ajudante.COLUMN2, oED1.getText().toString());

        try {

            oCV.put(ajudante.COLUMN3, Integer.parseInt(oED2.getText().toString()));

        } catch(Exception e){

            Log.e("PrunusApp", "Erro a inserir o ano (" + oED2.getText().toString() + ")!");
        }

        sql.insert(ajudante.TABLE_NAME, null, oCV);
        onResume();
    }

    public void onDELclick ( View v ){

        sql.delete(ajudante.TABLE_NAME,"ROWID= " + (v.getId()/10),null);
        LinearLayout oLL1 = (LinearLayout) findViewById(v.getId()+4);
        ((LinearLayout) oLL1.getParent()).removeView(oLL1);
    }
}
