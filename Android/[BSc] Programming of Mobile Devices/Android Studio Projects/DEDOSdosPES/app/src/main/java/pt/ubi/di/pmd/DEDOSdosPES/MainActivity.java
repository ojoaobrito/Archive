package pt.ubi.di.pmd.DEDOSdosPES;

import androidx.appcompat.app.AppCompatActivity;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.view.animation.AlphaAnimation;
import android.view.animation.Animation;
import android.view.animation.AnimationSet;
import android.view.animation.DecelerateInterpolator;
import android.view.animation.TranslateAnimation;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MainActivity extends AppCompatActivity {

    private float height;
    private TextView username_texto;
    private TextView pass_texto;
    private TextView registar;
    private EditText username;
    private EditText pass;
    private LinearLayout linear;
    private Button botao;
    private Button botao2;
    private Context contexto = this;
    private SQLiteDatabase sql;
    private AjudanteParaAbrirBaseDados ajudante;
    private int controlo = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getReadableDatabase();

        /*

        MediaPlayer som= MediaPlayer.create(MainActivity.this,R.raw.som);
        som.start();

        Tentei colocar som na app de modo a ficar mais apelativa, uma vez que é feita para crianças.
        No entanto não ficou corretamente implementada.

        */

    }

    public void iniciar(View v){

        username_texto = (TextView) findViewById(R.id.username_texto);
        pass_texto = (TextView) findViewById(R.id.pass_texto);
        registar = (TextView) findViewById(R.id.registar);
        username = (EditText) findViewById(R.id.username);
        pass = (EditText) findViewById(R.id.pass);
        linear = (LinearLayout) findViewById(R.id.linear);
        botao = (Button) findViewById(R.id.botao);
        botao2 = (Button) findViewById(R.id.botao2);

        if(controlo == 1 && username.getText().toString().equals("")){
            //pequena notificação/pop-up com a mensagem "username inválido" de 3.5 segundos
            Toast.makeText(this, "Username inválido", Toast.LENGTH_LONG).show();
            return;
        }

        if(controlo == 1 && pass.getText().toString().equals("")){
            //pequena notificação/pop-up com a mensagem "password inválida" de 3.5 segundos
            Toast.makeText(this, "Password inválida", Toast.LENGTH_LONG).show();
            return;
        }

        // obter a altura do ecrã
        DisplayMetrics displayMetrics = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(displayMetrics);
        height = (float)displayMetrics.heightPixels;

        // animação inicial
        Animation anim1 = new TranslateAnimation(0, 0, 0, (int)((height/2)-((int)((height/2))-50)));
        anim1.setDuration(400);
        anim1.setFillAfter(true);
        anim1.setStartOffset((long)100.0);

        anim1.setAnimationListener(new Animation.AnimationListener() {
            @Override
            public void onAnimationStart(Animation animation) {

                // animação para o botão
                Animation anim = new TranslateAnimation(0, 0, 0, (int)((height/2)-((int)((height/2))+100)));
                anim.setDuration(700);
                anim.setFillAfter(true);

                anim.setAnimationListener(new Animation.AnimationListener() {
                    @Override
                    public void onAnimationStart(Animation animation) {}

                    @Override
                    public void onAnimationRepeat(Animation animation) {}

                    @Override
                    public void onAnimationEnd(Animation animation) {

                        Animation fadeIn = new AlphaAnimation(1, 0);
                        fadeIn.setInterpolator(new DecelerateInterpolator());
                        fadeIn.setDuration(500);

                        AnimationSet animacao = new AnimationSet(false);
                        animacao.addAnimation(fadeIn);
                        botao.setAnimation(animacao);
                    }
                });

                botao.setAnimation(anim);
            }

            @Override
            public void onAnimationRepeat(Animation animation) {}

            @Override
            public void onAnimationEnd(Animation animation) {

                // animação para o texto
                Animation anim2 = new TranslateAnimation(0, 0, (int)((height/2)-((int)((height/2))-50)), (int)((height/2)-((int)((height/2))+200)));
                anim2.setDuration(600);
                anim2.setFillAfter(true);

                anim2.setAnimationListener(new Animation.AnimationListener() {
                    @Override
                    public void onAnimationStart(Animation animation) {}

                    @Override
                    public void onAnimationRepeat(Animation animation) {}

                    @Override
                    public void onAnimationEnd(Animation animation) {
                        controlo = 1;
                        botao2.setVisibility(View.VISIBLE);
                        registar.setVisibility(View.VISIBLE);
                        botao.setVisibility(View.INVISIBLE);

                        Animation fadeIn0 = new AlphaAnimation(0, 1);
                        fadeIn0.setInterpolator(new DecelerateInterpolator());
                        fadeIn0.setDuration(500);

                        AnimationSet animacao0 = new AnimationSet(false);
                        animacao0.addAnimation(fadeIn0);
                        botao2.setAnimation(animacao0);

                        Animation fadeInregistar = new AlphaAnimation(0, 1);
                        fadeInregistar.setInterpolator(new DecelerateInterpolator());
                        fadeInregistar.setDuration(500);

                        AnimationSet animacaoregistar = new AnimationSet(false);
                        animacaoregistar.addAnimation(fadeInregistar);
                        registar.setAnimation(animacaoregistar);

                        username_texto.setVisibility(View.VISIBLE);
                        Animation fadeIn = new AlphaAnimation(0, 1);
                        fadeIn.setInterpolator(new DecelerateInterpolator());
                        fadeIn.setDuration(1000);

                        AnimationSet animacao = new AnimationSet(false);
                        animacao.addAnimation(fadeIn);
                        username_texto.setAnimation(animacao);

                        // fade-in do EditText do username
                        username.setVisibility(View.VISIBLE);
                        Animation fadeIn3 = new AlphaAnimation(0, 1);
                        fadeIn3.setInterpolator(new DecelerateInterpolator());
                        fadeIn3.setDuration(500);

                        AnimationSet animacao3 = new AnimationSet(false);
                        animacao3.addAnimation(fadeIn3);
                        username.setAnimation(animacao3);

                        // fade-in do TextView da password
                        pass_texto.setVisibility(View.VISIBLE);
                        Animation fadeIn4 = new AlphaAnimation(0, 1);
                        fadeIn4.setInterpolator(new DecelerateInterpolator());
                        fadeIn4.setDuration(1000);

                        AnimationSet animacao4 = new AnimationSet(false);
                        animacao4.addAnimation(fadeIn4);
                        pass_texto.setAnimation(animacao4);

                        // fade-in do EditText do username
                        pass.setVisibility(View.VISIBLE);
                        Animation fadeIn5 = new AlphaAnimation(0, 1);
                        fadeIn3.setInterpolator(new DecelerateInterpolator());
                        fadeIn3.setDuration(500);

                        AnimationSet animacao5 = new AnimationSet(false);
                        animacao3.addAnimation(fadeIn5);
                        pass.setAnimation(animacao5);

                    }
                });

                linear.startAnimation(anim2);
            }
        });

        linear.startAnimation(anim1);
    }


    protected void onResume(){
        super.onResume();
        sql = ajudante.getReadableDatabase();

    }
    protected void onPause(){
        super.onPause();
        sql.close();
    }


    public void tabuada(View v){

        if(controlo == 1 && username.getText().toString().equals("")){
            Toast.makeText(this, "Username inválido", Toast.LENGTH_LONG).show();
            return;
        }

        if(controlo == 1 && pass.getText().toString().equals("")){
            Toast.makeText(this, "Password inválida", Toast.LENGTH_LONG).show();
            return;
        }

        EditText nome = (EditText)findViewById(R.id.username);
        EditText pass = (EditText)findViewById(R.id.pass);
        int controlo = 0;

        String hexadecimal="";
        //calcular o hash da password
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] resultado = md.digest(pass.getText().toString().getBytes());

            BigInteger aux = new BigInteger(1, resultado);

            hexadecimal = aux.toString(16);

            while (hexadecimal.length() < 32)
                hexadecimal = "0" + hexadecimal;
        } catch (NoSuchAlgorithmException e) {}


        //fazer uma query à base de dados e obter conteudo
        Cursor cursor = sql.query(ajudante.TABLE_NAME1,new String[] {"*"}, null, null,null,null,null,null);

        boolean conteudo = cursor.moveToFirst();

        while(conteudo== true){
            String nomeAUX = cursor.getString(1);
            String passAUX = cursor.getString(2);

            if(nome.getText().toString().equals(nomeAUX)){
                if(hexadecimal.equals(passAUX)){

                    controlo=1;

                    Intent intento = new Intent(this,Tabuada.class);
                    intento.putExtra("ID",cursor.getString(0));
                    intento.putExtra("Nome",nomeAUX);
                    intento.putExtra("Password",passAUX);
                    intento.putExtra("Nivel",cursor.getString(3));
                    startActivity(intento);

                }

            }

        conteudo = cursor.moveToNext();
        }
        if(controlo == 0){


            AlertDialog.Builder builder = new AlertDialog.Builder(this);

            builder.setTitle("Utilizador não registado");
            builder.setMessage("Faz o teu registo");
            builder.setCancelable(true);

            builder.setPositiveButton("Registar", new DialogInterface.OnClickListener(){// botão registar

                @Override
                public void onClick(DialogInterface dialog, int which){
                    Intent intento = new Intent(contexto,Registo.class);
                    startActivity(intento);

                }
            });

            builder.setNegativeButton("OK", new DialogInterface.OnClickListener(){ // botão ok

                @Override
                public void onClick(DialogInterface dialog, int which){

                    dialog.dismiss();
                }
            });

            AlertDialog dialog = builder.create();
            dialog.show();

    }}

    public void registar(View v){

        Intent intento = new Intent(this,Registo.class);
        Log.v("DEDOSdosPES","1");
        startActivity(intento);
    }
}
