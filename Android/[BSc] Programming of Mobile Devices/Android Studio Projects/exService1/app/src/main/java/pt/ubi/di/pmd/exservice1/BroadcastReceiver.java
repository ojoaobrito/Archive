package pt.ubi.di.pmd.exservice1;

import android.content.Intent;

public class BroadcastReceiver extends android.content.BroadcastReceiver{

    @Override
    public void onReceive(Intent intent){

        startService(intent);
    }
}
