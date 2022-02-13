package pt.ubi.di.pmd.exservice1;

import android.app.Service;
import android.content.Intent;
import android.os.Handler;
import android.os.IBinder;
import android.util.Log;
import android.widget.Toast;

public class ServiceAlarms extends Service{

    Handler handler;

    @Override
    public int onStartCommand(Intent intento, int flags, int startId){

        handler = new Handler(); // como foi definido na UIThread, faz a ponte para a nova thread e através dele "enviamos" a toast para a UIThread

        new Thread(){ // esta thread cria a Toast, manda-a para a UIThread e adormece de seguida (repete o processo 10 vezes)

            public void run(){

                for(int i=0; i<10; i++){

                    Runnable runnable = new Runnable(){

                        @Override
                        public void run(){

                            Toast.makeText(ServiceAlarms.this, "Service Started!", Toast.LENGTH_SHORT).show();
                        }
                    };

                    handler.post(runnable); // enviar o objeto runnable para a UIThread

                    try{

                        Thread.sleep(5000);

                    } catch(InterruptedException e){

                        Log.e("ServiceAlarms", "Erro");
                    }
                }
            }
        }.start();

        return(START_NOT_STICKY);
    }

    @Override
    public IBinder onBind(Intent intento){

        return(null);
    }
}
