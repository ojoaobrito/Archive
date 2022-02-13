package pt.ubi.di.pmd.explicit1;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class Explicit1 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.activity_explicit1);
    }

    public void startCalculator(View v){

        Intent iCalc = new Intent();
        iCalc.setAction(Intent.ACTION_MAIN);
        iCalc.setComponent(new ComponentName("com.android.calculator2","com.android.calculator2.Calculator"));
        startActivity(iCalc);
    }

    public void startActivity(View v){

        Intent iActivity = new Intent(this, Activity2.class);
        iActivity.putExtra("string1","Sou fabulástico!");
        startActivity(iActivity);
    }
}
