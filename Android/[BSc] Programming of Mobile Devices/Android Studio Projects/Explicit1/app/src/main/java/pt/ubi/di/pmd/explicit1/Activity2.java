package pt.ubi.di.pmd.explicit1;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class Activity2 extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.main2);

        TextView oTV = (TextView) findViewById(R.id.textview1);

        Intent iCameFromActivity1 = getIntent();

        oTV.setText(iCameFromActivity1.getStringExtra("string1"));
    }

    public void endActivity(View v){

        super.finish();
    }
}

