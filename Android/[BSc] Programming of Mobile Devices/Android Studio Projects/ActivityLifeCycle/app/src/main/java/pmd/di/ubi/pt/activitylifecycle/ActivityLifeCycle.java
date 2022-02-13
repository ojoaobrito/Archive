package pmd.di.ubi.pt.activitylifecycle;

import android.app.Activity;
import android.os.Bundle;
import android.util.*;

public class ActivityLifeCycle extends Activity
{
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        super.setContentView(R.layout.activity_life_cycle);
        Log.d("ActivityLifeCycle","onCreate() was called!");

    }

    @Override
    public void onStart()
    {
        super.onStart();
        Log.d("ActivityLifeCycle","onStart() was called!");
    }

    @Override
    public void onResume()
    {
        super.onResume();
        Log.d("ActivityLifeCycle","onResume() was called!");
    }

    @Override
    public void onRestart()
    {
        super.onRestart();
        Log.d("ActivityLifeCycle","onRestart() was called!");
    }

    @Override
    public void onPause()
    {
        super.onPause();
        Log.d("ActivityLifeCycle","onPause() was called!");
    }

    @Override
    public void onStop()
    {
        super.onStop();
        Log.d("ActivityLifeCycle","onStop() was called!");
    }

    @Override
    public void onDestroy()
    {
        super.onDestroy();
        Log.d("ActivityLifeCycle","onDestroy() was called!");
    }

}

