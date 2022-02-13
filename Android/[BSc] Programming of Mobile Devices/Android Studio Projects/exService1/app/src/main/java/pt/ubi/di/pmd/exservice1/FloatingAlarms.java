package pt.ubi.di.pmd.exservice1;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class FloatingAlarms extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_floating_alarms);
    }

    public void onButtonClick(View v){

        Intent intento = new Intent(this,ServiceAlarms.class);
        startService(intento);
    }
}
