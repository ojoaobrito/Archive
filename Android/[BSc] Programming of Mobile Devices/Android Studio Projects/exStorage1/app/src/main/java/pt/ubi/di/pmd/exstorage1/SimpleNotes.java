package pt.ubi.di.pmd.exstorage1;

import android.app.Activity;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

public class SimpleNotes extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.activity_simple_notes);

        SharedPreferences oSP = getPreferences(0);

        if(!oSP.getBoolean("recover",false)){ // é a primeira vez que a app é aberta, temos de mostrar as instruções

            try {

                // como abrir um ficheiro em Android
                InputStream ficheiro = getResources().openRawResource(R.raw.instructions);

                EditText texto = (EditText) findViewById(R.id.campo);

                byte[] buffer = new byte[ficheiro.available()]; // criar um array de bytes com espaço suficiente para guardar o conteúdo do ficheiro

                ficheiro.read(buffer);
                ficheiro.close();

                texto.setText(new String(buffer)); // transformar o buffer (em bytes) numa string usável

                // criar um editor que permite gerir as preferências da aplicação
                SharedPreferences.Editor editor = oSP.edit();
                editor.putBoolean("recover", true);
                editor.commit();

            } catch (FileNotFoundException f){

                Log.e("SimpleNotes", "File not found!");
                super.finish();
            }

            catch(IOException i){

                Log.e("SimpleNotes", "Problems while loading file!");
                super.finish();
            }
        }

        else {

            EditText texto = (EditText) findViewById(R.id.campo);
            texto.setText("");
        }
    }

    public void sendSave(View v){ // guardar as notas

        SharedPreferences oSP = getPreferences(0);
        SharedPreferences.Editor editor = oSP.edit();
        editor.putBoolean("recover", true);
        editor.commit();
    }

    public void exitNotSave(View v){ // sair da app e não guardar

        SharedPreferences oSP = getPreferences(0);
        SharedPreferences.Editor editor = oSP.edit();
        editor.putBoolean("recover", false);
        editor.commit();
    }
}
