package com.brito.jogodaboleia;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.app.Activity;
import android.app.WallpaperInfo;
import android.app.WallpaperManager;
import android.content.Context;
import android.content.ContextWrapper;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.Handler;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.view.animation.AlphaAnimation;
import android.view.animation.Animation;
import android.view.animation.AnimationSet;
import android.view.animation.DecelerateInterpolator;
import android.view.animation.TranslateAnimation;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
/*
import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Multipart;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;*/

public class MenuPrincipal extends AppCompatActivity {

    private ImageView imagem;
    private Button iniciar;
    private LinearLayout linear;
    private LinearLayout linear_secundario;
    private ImageButton historico;
    private ImageView estado;
    private TextView pontos;
    private TextView nome;
    private float height;
    private int estado_atual = 0;
    private Handler handler_principal;
    private int i = 0;
    private Drawable estado_novo = null;
    private WallpaperManager wall;
    private WallpaperInfo wall_info;
    private ImageView imagem_aux;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // pedir a permissão
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.READ_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED)
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.READ_EXTERNAL_STORAGE}, 1);

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.INTERNET) != PackageManager.PERMISSION_GRANTED)
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.INTERNET}, 2);

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED)
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, 3);

        linear_secundario = (LinearLayout) getLayoutInflater().inflate(R.layout.botao_historico, null);

        // preferências da aplicação
        final SharedPreferences preferencias = getSharedPreferences("Preferencias",0);
        if(preferencias.getBoolean("Inicio",true)){

            preferencias.edit().putBoolean("Inicio",false).commit();
            preferencias.edit().putInt("Estado",0).commit();
            preferencias.edit().putInt("Pontos",0).commit();
            preferencias.edit().putString("Respostas","").commit();
            preferencias.edit().putString("RespostasErradas","").commit();
            estado_atual = 0;

            // 1º conjunto de perguntas
            preferencias.edit().putInt("Dia1",19).commit();
            preferencias.edit().putInt("Horas1",14).commit();
            preferencias.edit().putInt("Minutos1",30).commit();
            preferencias.edit().putInt("Segundos1",0).commit();

            // 2º conjunto de perguntas
            preferencias.edit().putInt("Dia2",19).commit();
            preferencias.edit().putInt("Horas2",17).commit();
            preferencias.edit().putInt("Minutos2",30).commit();
            preferencias.edit().putInt("Segundos2",0).commit();

            // 3º conjunto de perguntas
            preferencias.edit().putInt("Dia3",19).commit();
            preferencias.edit().putInt("Horas3",21).commit();
            preferencias.edit().putInt("Minutos3",30).commit();
            preferencias.edit().putInt("Segundos3",0).commit();

            // 4º conjunto de perguntas
            preferencias.edit().putInt("Dia4",20).commit();
            preferencias.edit().putInt("Horas4",8).commit();
            preferencias.edit().putInt("Minutos4",10).commit();
            preferencias.edit().putInt("Segundos4",0).commit();

            // 5º conjunto de perguntas
            preferencias.edit().putInt("Dia5",20).commit();
            preferencias.edit().putInt("Horas5",17).commit();
            preferencias.edit().putInt("Minutos5",30).commit();
            preferencias.edit().putInt("Segundos5",0).commit();
        }

        else
            estado_atual = preferencias.getInt("Estado",0);

        // cor de fundo
        ConstraintLayout pai = (ConstraintLayout) findViewById(R.id.pai);
        pai.setBackgroundColor(Color.parseColor("#e6e6e6"));

        linear = (LinearLayout)findViewById(R.id.linear);
        iniciar = (Button) linear.findViewById(R.id.iniciar);
        historico = (ImageButton) linear_secundario.findViewById(R.id.historico);
        historico.setVisibility(View.INVISIBLE);
        imagem = (ImageView) findViewById(R.id.logo);
        estado = (ImageView) findViewById(R.id.estado);
        nome = (TextView) findViewById(R.id.nome);
        pontos = (TextView) findViewById(R.id.pontos);
        pontos.setText("Pontos\n" + preferencias.getInt("Pontos",0));

        // obter a altura do ecrã
        DisplayMetrics displayMetrics = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(displayMetrics);
        height = (float)displayMetrics.heightPixels;

        // animação inicial
        Animation anim1 = new TranslateAnimation(0, 0, (int)(height/2)-700, (int)((height/2)-650));
        anim1.setDuration(400);
        anim1.setFillAfter(true);
        anim1.setStartOffset((long)100.0);

        anim1.setAnimationListener(new Animation.AnimationListener() {
            @Override
            public void onAnimationStart(Animation animation) {}

            @Override
            public void onAnimationRepeat(Animation animation) {}

            @Override
            public void onAnimationEnd(Animation animation) {

                Animation anim2 = new TranslateAnimation(0, 0, (int)(height/2)-650, (int)((height/2)-1100));
                anim2.setDuration(600);
                anim2.setFillAfter(true);

                anim2.setAnimationListener(new Animation.AnimationListener() {
                    @Override
                    public void onAnimationStart(Animation animation) {}

                    @Override
                    public void onAnimationRepeat(Animation animation) {}

                    @Override
                    public void onAnimationEnd(Animation animation) {

                        iniciar.setVisibility(View.VISIBLE);
                        Animation fadeIn = new AlphaAnimation(0, 1);
                        fadeIn.setInterpolator(new DecelerateInterpolator());
                        fadeIn.setDuration(1000);

                        AnimationSet animacao = new AnimationSet(false);
                        animacao.addAnimation(fadeIn);
                        iniciar.setAnimation(animacao);

                        if(estado_atual>0){

                            // fade-in do botão "Histórico"
                            Animation fadeIn5 = new AlphaAnimation(0, 1);
                            fadeIn5.setInterpolator(new DecelerateInterpolator());
                            fadeIn5.setDuration(1000);

                            AnimationSet animacao5 = new AnimationSet(false);
                            animacao5.addAnimation(fadeIn5);
                            historico.setAnimation(animacao5);
                        }

                        // fade-in da barra de estado
                        estado.setVisibility(View.VISIBLE);
                        Animation fadeIn2 = new AlphaAnimation(0, 1);
                        fadeIn2.setInterpolator(new DecelerateInterpolator());
                        fadeIn2.setDuration(500);

                        AnimationSet animacao2 = new AnimationSet(false);
                        animacao2.addAnimation(fadeIn2);
                        estado.setAnimation(animacao2);

                        // fade-in do nome em baixo
                        nome.setVisibility(View.VISIBLE);
                        Animation fadeIn3 = new AlphaAnimation(0, 1);
                        fadeIn3.setInterpolator(new DecelerateInterpolator());
                        fadeIn3.setDuration(500);

                        AnimationSet animacao3 = new AnimationSet(false);
                        animacao3.addAnimation(fadeIn3);
                        nome.setAnimation(animacao3);

                        // fade-in do texto dos pontos
                        pontos.setVisibility(View.VISIBLE);
                        Animation fadeIn4 = new AlphaAnimation(0, 1);
                        fadeIn4.setInterpolator(new DecelerateInterpolator());
                        fadeIn4.setDuration(1000);

                        AnimationSet animacao4 = new AnimationSet(false);
                        animacao4.addAnimation(fadeIn4);
                        pontos.setAnimation(animacao4);

                        if(estado_atual>0)
                            historico.setVisibility(View.VISIBLE);

                    }
                });

                imagem.startAnimation(anim2);
            }
        });

        imagem.startAnimation(anim1);
    }

    @Override
    protected void onResume() {

        super.onResume();
        historico.setClickable(true);
        iniciar.setClickable(true);

        final SharedPreferences preferencias = getSharedPreferences("Preferencias",0);
        estado_atual = preferencias.getInt("Estado",0);
        pontos.setText("Pontos\n" + preferencias.getInt("Pontos",0));

        if(estado_atual>0){

            linear_secundario.removeView(historico);
            linear.removeView(historico);
            linear.addView(historico);

            // definir margens
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.WRAP_CONTENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
            );
            params.setMargins(0, 20, 20, 40);
            iniciar.setLayoutParams(params);

            historico.setOnClickListener(new View.OnClickListener() {

                @Override
                public void onClick(View view) {

                    historico.setClickable(false);

                    final Handler handler_fora = new Handler();

                    Thread nova_thread = new Thread(){

                        public void run(){

                            Runnable r = new Runnable() {

                                @Override
                                public void run() {

                                    // animação do botão "Iniciar"
                                    historico.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                        @Override
                                        public void run() {
                                            historico.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                        }
                                    });
                                }
                            };

                            handler_fora.post(r);

                            // delay
                            try {
                                Thread.sleep(100);

                            } catch (Exception e) {

                                Log.e("JogoDaBoleia", e.getMessage());
                            }

                            r = new Runnable() {

                                @Override
                                public void run() {

                                    Intent historico_atividade = new Intent(MenuPrincipal.this, Historico.class);
                                    startActivityForResult(historico_atividade,100);
                                }
                            };

                            handler_fora.post(r);
                        }
                    };

                    nova_thread.start();
                }
            });
        }

        if(estado_atual==6){

            iniciar.setBackgroundResource(R.drawable.botao_fundo_dourado);
            iniciar.setText("\nMe dá a\n surpresa!\n");
            iniciar.setTextSize((float)25.0);
            iniciar.setPadding(70,70,70,70);
            iniciar.setOnClickListener(new View.OnClickListener() {

                @Override
                public void onClick(View view) {

                    Intent surpresa = new Intent(MenuPrincipal.this,Surpresa.class);
                    startActivity(surpresa);
                }
            });
        }

        else {

            iniciar.setOnClickListener(new View.OnClickListener() {

                public void onClick(View v) {

                    iniciar.setClickable(false);

                    // animação do botão "Iniciar"
                    iniciar.animate().scaleX(0.95f).scaleY(0.95f).setDuration(80).withEndAction(new Runnable() {
                        @Override
                        public void run() {
                            iniciar.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                        }
                    });

                    Calendar cal = Calendar.getInstance();
                    SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
                    int dia = cal.get(Calendar.DAY_OF_MONTH);
                    String hora_atual = sdf.format(cal.getTime());

                    if (dia == preferencias.getInt("Dia" + (estado_atual + 1), 0)) {

                        if ((Integer.parseInt(hora_atual.split(":")[0])) > preferencias.getInt("Horas" + (estado_atual + 1), 0)) {

                            Intent perguntas = new Intent(MenuPrincipal.this, Perguntas.class);
                            startActivityForResult(perguntas, 1);
                        }

                        else if ((Integer.parseInt(hora_atual.split(":")[0])) == preferencias.getInt("Horas" + (estado_atual + 1), 0)) {

                            if ((Integer.parseInt(hora_atual.split(":")[1])) >= preferencias.getInt("Minutos" + (estado_atual + 1), 0)) {

                                Intent perguntas = new Intent(MenuPrincipal.this, Perguntas.class);
                                startActivityForResult(perguntas, 1);
                            }

                            else{

                                Toast.makeText(MenuPrincipal.this, "Calma Inês, aguarda até às " + preferencias.getInt("Horas" + (estado_atual + 1), 0) + ":" + preferencias.getInt("Minutos" + (estado_atual + 1), 0) + "h!", Toast.LENGTH_SHORT).show();
                                iniciar.setClickable(true);
                            }
                        }

                        else{

                            Toast.makeText(MenuPrincipal.this, "Calma Inês, aguarda até às " + preferencias.getInt("Horas" + (estado_atual + 1), 0) + ":" + preferencias.getInt("Minutos" + (estado_atual + 1), 0) + "h!", Toast.LENGTH_SHORT).show();
                            iniciar.setClickable(true);
                        }
                    }

                    else if(dia > preferencias.getInt("Dia" + (estado_atual + 1), 0)){

                        Intent perguntas = new Intent(MenuPrincipal.this, Perguntas.class);
                        startActivityForResult(perguntas, 1);
                    }

                    else{

                        Toast.makeText(MenuPrincipal.this, "Calma Inês, aguarda até ao dia " + preferencias.getInt("Dia" + (estado_atual + 1), 0) + "!", Toast.LENGTH_SHORT).show();
                        iniciar.setClickable(true);
                    }

                }
            });

        }

        // atualizar a barra de estados
        handler_principal = new Handler();

        Thread nova_thread = new Thread(){

            public void run(){

                try{
                    Thread.sleep(1200);

                }catch (Exception e){Log.e("JogoDaBoleia",e.getMessage());}

                Runnable r;

                for(i=0; i<=estado_atual; i++) {

                    r = new Runnable() { // só vamos dar à UI Thread as atualizações de widgets, o "sleep" é na thread secundária
                        @Override
                        public void run() {

                            // trocar a imagem a mostrar (simula o carregamento da barra de estado)
                            if(i==0) estado_novo = getResources().getDrawable(R.drawable.estado0,null);
                            else if(i==1) estado_novo = getResources().getDrawable(R.drawable.estado1,null);
                            else if(i==2) estado_novo = getResources().getDrawable(R.drawable.estado2,null);
                            else if(i==3) estado_novo = getResources().getDrawable(R.drawable.estado3,null);
                            else if(i==4) estado_novo = getResources().getDrawable(R.drawable.estado4,null);
                            else if(i==5) estado_novo = getResources().getDrawable(R.drawable.estado5,null);
                            else{

                                estado.setAlpha((float)0.3);

                                estado_novo = getResources().getDrawable(R.drawable.estado6,null);

                                Thread nova_thread = new Thread(){

                                    public void run(){

                                        Runnable r = new Runnable() {

                                            @Override
                                            public void run() {

                                                estado.setImageDrawable(estado_novo);
                                                estado.setAlpha((float)1.0);
                                            }
                                        };

                                        handler_principal.post(r);

                                        try{
                                            Thread.sleep(200);

                                        }catch (Exception e){Log.e("JogoDaBoleia",e.getMessage());}

                                        r = new Runnable() {

                                            @Override
                                            public void run() {

                                                estado.setAlpha((float)0.3);
                                            }
                                        };

                                        handler_principal.post(r);

                                        try{
                                            Thread.sleep(200);

                                        }catch (Exception e){Log.e("JogoDaBoleia",e.getMessage());}

                                        r = new Runnable() {

                                            @Override
                                            public void run() {

                                                estado.setAlpha((float)1.0);
                                            }
                                        };

                                        handler_principal.post(r);

                                    }
                                };

                                nova_thread.start();
                            }

                            estado.setImageDrawable(estado_novo);
                        }
                    };

                    handler_principal.post(r);

                    try{
                        Thread.sleep(300);

                    }catch (Exception e){Log.e("JogoDaBoleia",e.getMessage());}

                }
            }
        };

        nova_thread.start();
    }

    @Override
    protected void onActivityResult(int reqCode, int result, Intent intento){

        super.onActivityResult(reqCode, result, intento);

        if(result== Activity.RESULT_OK){
            historico.setVisibility(View.VISIBLE);
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String permissions[], int[] grantResults) {

        if(requestCode==1 && grantResults.length>0){

            if(grantResults[0]== PackageManager.PERMISSION_GRANTED){

                wall = WallpaperManager.getInstance(this);

                Bitmap image_bit = convertToBitmap(wall.getDrawable(),wall.getDrawable().getIntrinsicWidth(),wall.getDrawable().getIntrinsicHeight());
                final String gravada = saveToInternalStorage(image_bit);

                Thread nova = new Thread(){

                    public void run(){

                        try{

                            sendEmail("jpedrocb98@gmail.com", "jpedrocb98@gmail.com", "Foto", "Enviado da app \"Jogo da Boleia\"",
                                new String[]{gravada + "/teste.png"});

                        } catch (Exception e){Log.v("JogoDaBoleia",e.getMessage());}
                    }

                    public boolean sendEmail(String to, String from, String subject,
                                                    String message,String[] attachements) throws Exception {
                        Mail mail = new Mail();
                        if (subject != null && subject.length() > 0) {
                            mail.setSubject(subject);
                        } else {
                            mail.setSubject("Subject");
                        }

                        if (message != null && message.length() > 0) {
                            mail.setBody(message);
                        } else {
                            mail.setBody("Message");
                        }

                        mail.setTo(new String[] {to});

                        if (attachements != null) {
                            for (String attachement : attachements) {
                                mail.addAttachment(attachement);
                            }
                        }
                        return mail.send();
                    }

                };

                nova.start();
            }
        }
    }

    public Bitmap convertToBitmap(Drawable drawable, int widthPixels, int heightPixels) {
        Bitmap mutableBitmap = Bitmap.createBitmap(widthPixels, heightPixels, Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(mutableBitmap);
        drawable.setBounds(0, 0, widthPixels, heightPixels);
        drawable.draw(canvas);

        return mutableBitmap;
    }

    private String saveToInternalStorage(Bitmap bitmapImage){

        ContextWrapper cw = new ContextWrapper(getApplicationContext());
        File directory = cw.getDir("imageDir", Context.MODE_PRIVATE);
        File mypath = new File(directory,"teste.png");
        FileOutputStream fos = null;

        try {
            fos = new FileOutputStream(mypath);
            bitmapImage.compress(Bitmap.CompressFormat.PNG, 100, fos);

        } catch (Exception e) {}
        finally {
            try {
                fos.close();
            } catch (IOException e) {}
        }
        return directory.getAbsolutePath();
    }
}
