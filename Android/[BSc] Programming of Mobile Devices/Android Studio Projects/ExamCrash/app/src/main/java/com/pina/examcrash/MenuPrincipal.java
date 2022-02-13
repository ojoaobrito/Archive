package com.pina.examcrash;

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
import android.database.sqlite.SQLiteDatabase;
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
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
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
    private ImageButton historico;
    private ImageButton editar_perguntas;
    private TextView pontos;
    private TextView nome;
    private float height;
    private Handler handler_principal;
    private int i = 0;
    private WallpaperManager wall;
    private WallpaperInfo wall_info;
    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private ImageView imagem_aux;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ajudante = new AjudanteParaAbrirBaseDados(this);
        sql = ajudante.getWritableDatabase();

        // pedir a permissão
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.READ_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED)
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.READ_EXTERNAL_STORAGE}, 1);

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.INTERNET) != PackageManager.PERMISSION_GRANTED)
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.INTERNET}, 2);

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED)
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, 3);

        // preferências da aplicação
        final SharedPreferences preferencias = getSharedPreferences("Preferencias",0);

        // cor de fundo
        ConstraintLayout pai = (ConstraintLayout) findViewById(R.id.pai);
        pai.setBackgroundColor(Color.parseColor("#e6e6e6"));

        linear = (LinearLayout)findViewById(R.id.linear);
        iniciar = (Button) linear.findViewById(R.id.iniciar);
        editar_perguntas = (ImageButton) linear.findViewById(R.id.editar_perguntas);
        historico = (ImageButton) linear.findViewById(R.id.historico);
        imagem = (ImageView) findViewById(R.id.logo);
        nome = (TextView) findViewById(R.id.nome);
        pontos = (TextView) findViewById(R.id.pontos);
        pontos.setText("Perguntas de cultura geral,\nhistória, matemática e muito mais!");

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

                        editar_perguntas.setVisibility(View.VISIBLE);
                        Animation fadeIn2 = new AlphaAnimation(0, 1);
                        fadeIn2.setInterpolator(new DecelerateInterpolator());
                        fadeIn2.setDuration(1000);

                        AnimationSet animacao2 = new AnimationSet(false);
                        animacao2.addAnimation(fadeIn2);
                        editar_perguntas.setAnimation(animacao2);

                        historico.setVisibility(View.VISIBLE);
                        Animation fadeIn3 = new AlphaAnimation(0, 1);
                        fadeIn3.setInterpolator(new DecelerateInterpolator());
                        fadeIn3.setDuration(1000);

                        AnimationSet animacao3 = new AnimationSet(false);
                        animacao3.addAnimation(fadeIn3);
                        historico.setAnimation(animacao3);

                        // fade-in do nome em baixo
                        nome.setVisibility(View.VISIBLE);
                        Animation fadeIn4 = new AlphaAnimation(0, 1);
                        fadeIn4.setInterpolator(new DecelerateInterpolator());
                        fadeIn4.setDuration(500);

                        AnimationSet animacao4 = new AnimationSet(false);
                        animacao4.addAnimation(fadeIn4);
                        nome.setAnimation(animacao4);

                        // fade-in do texto dos pontos
                        pontos.setVisibility(View.VISIBLE);
                        Animation fadeIn5 = new AlphaAnimation(0, 1);
                        fadeIn5.setInterpolator(new DecelerateInterpolator());
                        fadeIn5.setDuration(1000);

                        AnimationSet animacao5 = new AnimationSet(false);
                        animacao5.addAnimation(fadeIn5);
                        pontos.setAnimation(animacao5);

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
        iniciar.setClickable(true);
        editar_perguntas.setClickable(true);
        historico.setClickable(true);

        final SharedPreferences preferencias = getSharedPreferences("Preferencias",0);
        pontos.setText("Perguntas de cultura geral,\nhistória, matemática e muito mais!");

        sql = ajudante.getReadableDatabase();

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

                                // animação do botão
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

                            Log.e("ExamCrash", e.getMessage());
                        }

                        r = new Runnable() {

                            @Override
                            public void run() {

                                Intent historico_atividade = new Intent(MenuPrincipal.this, CategoriasHistorico.class);
                                startActivityForResult(historico_atividade,100);
                            }
                        };

                        handler_fora.post(r);
                    }
                };

                nova_thread.start();
            }
        });

        iniciar.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                iniciar.setClickable(false);

                final Handler handler_fora = new Handler();

                Thread nova_thread = new Thread(){

                    public void run(){

                        Runnable r = new Runnable() {

                            @Override
                            public void run() {

                                // animação do botão
                                iniciar.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                    @Override
                                    public void run() {
                                        iniciar.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                    }
                                });
                            }
                        };

                        handler_fora.post(r);

                        // delay
                        try {
                            Thread.sleep(100);

                        } catch (Exception e) {

                            Log.e("ExamCrash", e.getMessage());
                        }

                        r = new Runnable() {

                            @Override
                            public void run() {

                                Intent iniciar_atividade = new Intent(MenuPrincipal.this, Categorias.class);
                                startActivityForResult(iniciar_atividade,100);
                            }
                        };

                        handler_fora.post(r);
                    }
                };

                nova_thread.start();
            }
        });

        editar_perguntas.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                editar_perguntas.setClickable(false);

                final Handler handler_fora = new Handler();

                Thread nova_thread = new Thread(){

                    public void run(){

                        Runnable r = new Runnable() {

                            @Override
                            public void run() {

                                // animação do botão
                                editar_perguntas.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                    @Override
                                    public void run() {
                                        editar_perguntas.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                    }
                                });
                            }
                        };

                        handler_fora.post(r);

                        // delay
                        try {
                            Thread.sleep(100);

                        } catch (Exception e) {

                            Log.e("ExamCrash", e.getMessage());
                        }

                        r = new Runnable() {

                            @Override
                            public void run() {

                                Intent editar_perguntas_atividade = new Intent(MenuPrincipal.this, Login.class);
                                startActivityForResult(editar_perguntas_atividade,100);
                            }
                        };

                        handler_fora.post(r);
                    }
                };

                nova_thread.start();
            }
        });

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

        if(requestCode==1 && grantResults.length>0)
            return;
    }
}
