package pt.ubi.di.pmd.expermissions;

import android.app.Activity;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.provider.CallLog;
import android.widget.TextView;

public class LastCall extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState){

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_last_call);

        TextView oTV = (TextView) findViewById(R.id.texto);
        Uri uriCalls = Uri.parse("content://call_log/calls");
        Cursor curCalls = getContentResolver().query(uriCalls,null,null,null,null);
        String sInfo = "Last Call:";

        if(curCalls.moveToLast())
            sInfo += curCalls.getString(curCalls.getColumnIndex(CallLog.Calls.NUMBER)) + "\nDuration: " +curCalls.getString(curCalls.getColumnIndex(CallLog.Calls.DURATION));


        oTV.setText(sInfo);
    }
}
