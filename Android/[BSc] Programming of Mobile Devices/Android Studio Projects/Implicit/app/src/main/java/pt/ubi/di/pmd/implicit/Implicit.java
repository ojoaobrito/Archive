package pt.ubi.di.pmd.implicit;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.*;
import android.view.*;

public class Implicit extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.activity_implicit);
    }

    public void sendMessage(View v){

        Intent iSendMessage = new Intent(Intent.ACTION_SEND);
        iSendMessage.putExtra(Intent.EXTRA_TEXT,"Hello World!");
        iSendMessage.setType("text/plain");
        startActivity(iSendMessage);
    }
}
