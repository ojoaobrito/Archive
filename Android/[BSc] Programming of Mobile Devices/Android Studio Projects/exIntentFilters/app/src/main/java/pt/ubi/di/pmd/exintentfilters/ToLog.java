package pt.ubi.di.pmd.exintentfilters;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.*;

public class ToLog extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.activity_tolog);

        try {

            Intent intento = getIntent();
            Log.i("ToLog",intento.getStringExtra(Intent.EXTRA_TEXT));
        }

        catch(Exception e){

            Log.i("ToLog","Ainda não chegou");
        }
    }

    private void partilha(View v){

        Intent intento = new Intent(Intent.ACTION_SEND);
        intento.putExtra(Intent.EXTRA_TEXT,"Vim de outra aplicação");
        startActivity(intento);
    }
}
