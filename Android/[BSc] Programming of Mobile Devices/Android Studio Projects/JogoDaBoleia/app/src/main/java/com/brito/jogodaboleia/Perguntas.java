package com.brito.jogodaboleia;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.view.animation.AlphaAnimation;
import android.view.animation.Animation;
import android.view.animation.AnimationSet;
import android.view.animation.DecelerateInterpolator;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.Random;

public class Perguntas extends AppCompatActivity implements View.OnClickListener {

    private ImageView estado;
    private int estado_atual = 0;
    private Handler handler_principal;
    private int i = 0;
    private Drawable estado_novo = null;
    private String[] perguntas = new String[26];
    private String[][] respostas = new String[26][4];
    private long[] certas = new long[25];
    private TextView pergunta;
    private Button[] botoes_resposta = new Button[4];
    private int pergunta_atual;
    private int contador_botao;
    private int acertos = 0;
    private long[] desconta = new long[25];

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_perguntas);

        pergunta = (TextView) findViewById(R.id.pergunta);

        botoes_resposta[0] = (Button) findViewById(R.id.resposta1);
        botoes_resposta[0].setOnClickListener(this);
        botoes_resposta[1] = (Button) findViewById(R.id.resposta2);
        botoes_resposta[1].setOnClickListener(this);
        botoes_resposta[2] = (Button) findViewById(R.id.resposta3);
        botoes_resposta[2].setOnClickListener(this);
        botoes_resposta[3] = (Button) findViewById(R.id.resposta4);
        botoes_resposta[3].setOnClickListener(this);

        // 1ª pergunta
        //--------------------------------------------------------------
        perguntas[0] = "1. De que cor era a fita que me escreveste?";
        respostas[0][0] = "A) Fita? Que fita?";
        respostas[0][1] = "B) Branca";
        respostas[0][2] = "C) Cor de tijolo";
        respostas[0][3] = "D) Nem reparei";
        certas[0] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        long[] array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[0] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 2ª pergunta
        //--------------------------------------------------------------
        perguntas[1] = "2. Em que dia e mês faço anos?";
        respostas[1][0] = "A) 19 de Agosto";
        respostas[1][1] = "B) 18 de Agosto";
        respostas[1][2] = "C) 9 de Agosto";
        respostas[1][3] = "D) 20 de Setembro";
        certas[1] = botoes_resposta[0].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[1].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[1] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 3ª pergunta
        //--------------------------------------------------------------
        perguntas[2] = "3. Qual é a tua alcunha na nossa conversa?";
        respostas[2][0] = "A) Inês";
        respostas[2][1] = "B) Inês França";
        respostas[2][2] = "C) Inês Lagosta";
        respostas[2][3] = "D) Inês Neves";
        certas[2] = botoes_resposta[3].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[2].getId();
        desconta[2] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 4ª pergunta
        //--------------------------------------------------------------
        perguntas[3] = "4. Na primeira vez que te dei boleia, fui jantar onde?";
        respostas[3][0] = "A) Merendola";
        respostas[3][1] = "B) Casa do Benfica";
        respostas[3][2] = "C) Yokozo";
        respostas[3][3] = "D) Serra Shopping";
        certas[3] = botoes_resposta[1].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[3] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 5ª pergunta
        //--------------------------------------------------------------
        perguntas[4] = "5. Qual a sequência da primeira vez que fomos passear?";
        respostas[4][0] = "A) Gelado, Jardim do Lago e Ponte Branca";
        respostas[4][1] = "B) Gelado e Ponte Branca";
        respostas[4][2] = "C) Gelado, Mural com vista para a cidade e Ponte Branca";
        respostas[4][3] = "D) Mural com vista para a cidade, gelado e Ponte Branca";
        certas[4] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[4] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 6ª pergunta
        //--------------------------------------------------------------
        perguntas[5] = "6. Antes de uma curva de visibilidade reduzida é proibido parar:";
        respostas[5][0] = "A) A 30 metros da mesma";
        respostas[5][1] = "B) A 50 metros da mesma";
        respostas[5][2] = "C) A 100 metros da mesma";
        respostas[5][3] = "D) Parar? Para a frente é que é o caminho!";
        certas[5] = botoes_resposta[0].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[1].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[5] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 7ª pergunta
        //--------------------------------------------------------------
        perguntas[6] = "7. Quantas vezes fomos comer gelado?";
        respostas[6][0] = "A) 1";
        respostas[6][1] = "B) Poucas vezes";
        respostas[6][2] = "C) 2";
        respostas[6][3] = "D) Demasiadas vezes";
        certas[6] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[6] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 8ª pergunta
        //--------------------------------------------------------------
        perguntas[7] = "8. Como se chama o meu irmão (aka teu amigo do Facebook)?";
        respostas[7][0] = "A) Pedro";
        respostas[7][1] = "B) José";
        respostas[7][2] = "C) Miguel";
        respostas[7][3] = "D) André";
        certas[7] = botoes_resposta[3].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[2].getId();
        desconta[7] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 9ª pergunta
        //--------------------------------------------------------------
        perguntas[8] = "9. Aprox. quantas vezes já perguntámos um ao outro se estávamos bem?";
        respostas[8][0] = "A) 10";
        respostas[8][1] = "B) Umas 200, coisa pouca!";
        respostas[8][2] = "C) Nenhuma";
        respostas[8][3] = "D) Estás bem Inês?";
        certas[8] = botoes_resposta[1].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[8] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 10ª pergunta
        //--------------------------------------------------------------
        perguntas[9] = "10. Qual é a tua frase mais \"usada\"?";
        respostas[9][0] = "A) \"Não é preciso\"";
        respostas[9][1] = "B) \"Oh, (...)\"";
        respostas[9][2] = "C) \"Estou sim\"";
        respostas[9][3] = "D) \"Tas bem?\"";
        certas[9] = botoes_resposta[0].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[1].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[9] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 11ª pergunta
        //--------------------------------------------------------------
        perguntas[10] = "11. Completa: \"Se tu estás bem, ...";
        respostas[10][0] = "A) ... tudo bem!\"";
        respostas[10][1] = "B) ... ainda bem!\"";
        respostas[10][2] = "C) ... eu estou bem\"";
        respostas[10][3] = "D) ... eu também!\"";
        certas[10] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[10] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 12ª pergunta
        //--------------------------------------------------------------
        perguntas[11] = "12. Como se chama o jogo das perguntas?";
        respostas[11][0] = "A) Perguntados";
        respostas[11][1] = "B) Quiz";
        respostas[11][2] = "C) O Teste";
        respostas[11][3] = "D) Sei lá!";
        certas[11] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[11] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 13ª pergunta
        //--------------------------------------------------------------
        perguntas[12] = "13. Na foto do instituto, qual é a ordem?";
        respostas[12][0] = "A) Tu, eu, Ana, Professora, Julien e Pedro";
        respostas[12][1] = "B) Tu, eu, Ana, Professora, Pedro e Julien";
        respostas[12][2] = "C) Eu, tu, Ana, Professora, Pedro e Julien";
        respostas[12][3] = "D) Eu, tu, Ana, Professora, Julien e Pedro";
        certas[12] = botoes_resposta[3].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[2].getId();
        desconta[12] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 14ª pergunta
        //--------------------------------------------------------------
        perguntas[13] = "14. Quantos filmes vi, obrigado (gentilmente) por ti?";
        respostas[13][0] = "A) 6";
        respostas[13][1] = "B) 5";
        respostas[13][2] = "C) 7";
        respostas[13][3] = "D) Eu não te obriguei a nada!";
        certas[13] = botoes_resposta[0].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[1].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[13] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 15ª pergunta
        //--------------------------------------------------------------
        perguntas[14] = "15. No jogo de nos descrever enquanto uma fruta, ambos somos...";
        respostas[14][0] = "A) ... uma banana!";
        respostas[14][1] = "B) ... um morango!";
        respostas[14][2] = "C) ... uma papaia!";
        respostas[14][3] = "D) ... um tomate!";
        certas[14] = botoes_resposta[1].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[14] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 16ª pergunta
        //--------------------------------------------------------------
        perguntas[15] = "16. Quantos seios cranianos existem?";
        respostas[15][0] = "A) 10";
        respostas[15][1] = "B) 9";
        respostas[15][2] = "C) 11";
        respostas[15][3] = "D) Pff estou de fériaaaasss!";
        certas[15] = botoes_resposta[0].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[1].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[15] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 17ª pergunta
        //--------------------------------------------------------------
        perguntas[16] = "17. No vídeo que gravei a passar de carro em tua casa, que banda ia a tocar?";
        respostas[16][0] = "A) Queen";
        respostas[16][1] = "B) Bon Jovi";
        respostas[16][2] = "C) Scorpions";
        respostas[16][3] = "D) U2";
        certas[16] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[16] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 18ª pergunta
        //--------------------------------------------------------------
        perguntas[17] = "18. A nossa conversa tem o seguinte gradiente de cores e emoji:";
        respostas[17][0] = "A) Vermelho para azul; emoji a sorrir";
        respostas[17][1] = "B) Azul para vermelho; emoji com a língua de fora";
        respostas[17][2] = "C) Azul para vermelho; emoji a sorrir";
        respostas[17][3] = "D) Vermelho para azul; emoji com a língua de fora";
        certas[17] = botoes_resposta[1].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[17] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 19ª pergunta
        //--------------------------------------------------------------
        perguntas[18] = "19. Como se chama a proposta de casa de banho feminina que me mandaste?";
        respostas[18][0] = "A) Women's Pink Toilet";
        respostas[18][1] = "B) 3Pees";
        respostas[18][2] = "C) Lapee";
        respostas[18][3] = "D) #PeeToo";
        certas[18] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[18] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 20ª pergunta
        //--------------------------------------------------------------
        perguntas[19] = "20. O Barça perdeu na Liga dos Campeões contra quem?";
        respostas[19][0] = "A) Manchester United";
        respostas[19][1] = "B) Tottenham";
        respostas[19][2] = "C) Roma";
        respostas[19][3] = "D) Liverpool";
        certas[19] = botoes_resposta[3].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[2].getId();
        desconta[19] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 21ª pergunta
        //--------------------------------------------------------------
        perguntas[20] = "21. Quem mandou mensagem primeiro?";
        respostas[20][0] = "A) Eu (João)";
        respostas[20][1] = "B) Sei lá!";
        respostas[20][2] = "C) Ai sou muito má a lembrar-me destas coisas!";
        respostas[20][3] = "D) Tu (Inês)";
        certas[20] = botoes_resposta[0].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[1].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[20] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 22ª pergunta
        //--------------------------------------------------------------
        perguntas[21] = "22. Que desculpa usei da primeira vez que te dei boleia?";
        respostas[21][0] = "A) Que estava mau tempo";
        respostas[21][1] = "B) Insistindo muito";
        respostas[21][2] = "C) Que estava mau tempo e podias ficar pior";
        respostas[21][3] = "D) Que estavas doentita";
        certas[21] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[21] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 23ª pergunta
        //--------------------------------------------------------------
        perguntas[22] = "23. Completa: \"Join me in my car, we...";
        respostas[22][0] = "A) ... 'll go real far away from here!\"";
        respostas[22][1] = "B) ... could go real far away from here!\"";
        respostas[22][2] = "C) ... can go real far away from here!\"";
        respostas[22][3] = "D) ... can go real far away, away from here!\"";
        certas[22] = botoes_resposta[3].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[2].getId();
        desconta[22] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 24ª pergunta
        //--------------------------------------------------------------
        perguntas[23] = "24. Que gelados comemos da 2ª vez?";
        respostas[23][0] = "A) Natas e Maracujá";
        respostas[23][1] = "B) Framboesa e Natas";
        respostas[23][2] = "C) Maracujá e Framboesa";
        respostas[23][3] = "D) Maracujá e Morango";
        certas[23] = botoes_resposta[1].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[2].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[23] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 25ª pergunta
        //--------------------------------------------------------------
        perguntas[24] = "25. Que palavra usei na pseudo-fita para te descrever?";
        respostas[24][0] = "A) Incrível";
        respostas[24][1] = "B) Máquina";
        respostas[24][2] = "C) Espetacular";
        respostas[24][3] = "D) Impecável";
        certas[24] = botoes_resposta[2].getId();

        // obter a resposta errada que desconta
        array_aux = new long[3];
        array_aux[0] = botoes_resposta[0].getId();
        array_aux[1] = botoes_resposta[1].getId();
        array_aux[2] = botoes_resposta[3].getId();
        desconta[24] = array_aux[new Random().nextInt(array_aux.length)];
        //--------------------------------------------------------------

        // 26ª pergunta
        //--------------------------------------------------------------
        perguntas[25] = "26. Gostaste destes 2 dias?";
        respostas[25][0] = "A) Sim";
        respostas[25][1] = "B) Óbvio que sim";
        respostas[25][2] = "C) Claro que não";
        respostas[25][3] = "D) Não";
        //--------------------------------------------------------------

        estado = (ImageView) findViewById(R.id.estado);

        // preferências da aplicação
        SharedPreferences preferencias = getSharedPreferences("Preferencias", 0);

        estado_atual = preferencias.getInt("Estado", 0);
        pergunta_atual = estado_atual*5;

        // cor de fundo
        ConstraintLayout pai = (ConstraintLayout) findViewById(R.id.pai);
        pai.setBackgroundColor(Color.parseColor("#e6e6e6"));

        // fade-in da barra de estado
        estado.setVisibility(View.VISIBLE);
        Animation fadeIn = new AlphaAnimation(0, 1);
        fadeIn.setInterpolator(new DecelerateInterpolator());
        fadeIn.setDuration(500);

        AnimationSet animacao = new AnimationSet(false);
        animacao.addAnimation(fadeIn);
        estado.setAnimation(animacao);

        handler_principal = new Handler();

        Thread nova_thread = new Thread() {

            public void run() {

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

                            estado.setImageDrawable(estado_novo);
                        }
                    };

                    handler_principal.post(r);

                    try {
                        Thread.sleep(300);

                    } catch (Exception e) {
                        Log.e("JogoDaBoleia", e.getMessage());
                    }

                }
            }
        };

        nova_thread.start();

        pergunta.setText(perguntas[pergunta_atual]);

        for(int i=0; i<4; i++){

            botoes_resposta[i].setText(respostas[pergunta_atual][i]);
        }
    }

    @Override
    protected void onResume(){

        super.onResume();
    }

    public void onClick(final View v){

        // desativar os botões
        botoes_resposta[0].setClickable(false);
        botoes_resposta[1].setClickable(false);
        botoes_resposta[2].setClickable(false);
        botoes_resposta[3].setClickable(false);

        SharedPreferences preferencias = getSharedPreferences("Preferencias",0);
        if(pergunta_atual==0)
            preferencias.edit().putString("Respostas",preferencias.getString("Respostas","") + v.getId()).commit();
        else
            preferencias.edit().putString("Respostas",preferencias.getString("Respostas","") + "-" + v.getId()).commit();


        if(pergunta_atual==0)
            preferencias.edit().putString("RespostasErradas",preferencias.getString("RespostasErradas","") + desconta[0]).commit();

        else if((pergunta_atual+1)!=26)
            preferencias.edit().putString("RespostasErradas",preferencias.getString("RespostasErradas","") + "-" + desconta[pergunta_atual]).commit();


        final Handler handler_fora = new Handler();

        Thread mudar_pergunta = new Thread(){

            public void run(){

                //ANIMAR OS BOTÕES
                //---------------------------------------------------------------------------------------------------------------------------------------------------------
                if ((pergunta_atual+1)!=26 && v.getId() == certas[pergunta_atual]) { // animar o botão da resposta certa

                    acertos++;

                    // mudar a cor de fundo
                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            v.setBackgroundResource(R.drawable.resposta_fundo_certo);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(10);

                    } catch (Exception e) {

                        Log.e("JogoDaBoleia", e.getMessage());
                    }

                    // fazer a animação
                    r = new Runnable() {

                        @Override
                        public void run() {

                            v.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                @Override
                                public void run() {
                                    v.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                }
                            });
                        }
                    };

                    handler_fora.post(r);
                }

                else if ((pergunta_atual+1)!=26 && v.getId() == desconta[pergunta_atual]) { // animar um dos botões de resposta errada, mas com desconto (perca de 1 ponto)

                    acertos--;

                    // mudar a cor de fundo
                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            v.setBackgroundResource(R.drawable.resposta_fundo_errado);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(10);

                    } catch (Exception e) {

                        Log.e("JogoDaBoleia", e.getMessage());
                    }

                    // fazer a animação
                    r = new Runnable() {

                        @Override
                        public void run() {

                            v.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                @Override
                                public void run() {
                                    v.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                }
                            });
                        }
                    };

                    handler_fora.post(r);
                }

                else if((pergunta_atual+1)!=26) { // animar um dos botões de resposta errada, mas sem desconto

                    // mudar a cor de fundo
                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            v.setBackgroundResource(R.drawable.resposta_fundo_neutro);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(10);

                    } catch (Exception e) {

                        Log.e("JogoDaBoleia", e.getMessage());
                    }

                    // fazer a animação
                    r = new Runnable() {

                        @Override
                        public void run() {

                            v.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                @Override
                                public void run() {
                                    v.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                }
                            });
                        }
                    };

                    handler_fora.post(r);
                }
                //---------------------------------------------------------------------------------------------------------------------------------------------------------

                //AVALIAR SE É PARA MUDAR DE PERGUNTA OU TERMINAR A ATIVIDADE
                //---------------------------------------------------------------------------------------------------------------------------------------------------------
                if (((pergunta_atual + 1) % 5) == 0 || (pergunta_atual+1)==26) { // terminar a atividade

                    SharedPreferences preferencias = getSharedPreferences("Preferencias", 0);

                    if((pergunta_atual+1)!=26)
                        preferencias.edit().putInt("Pontos", (preferencias.getInt("Pontos", 0)) + acertos).commit();

                    preferencias.edit().putInt("Estado", (preferencias.getInt("Estado", 0)) + 1).commit();

                    if((pergunta_atual+1)!=26){ // não é a pergunta final

                        // delay
                        try {
                            Thread.sleep(600);

                        } catch (Exception e) {

                            Log.e("JogoDaBoleia", e.getMessage());
                        }

                        Runnable r = new Runnable() {

                            @Override
                            public void run() {

                                if(botoes_resposta[0].getId()!=certas[pergunta_atual])
                                    botoes_resposta[0].animate().translationX(2000).setDuration(700);

                                if(botoes_resposta[1].getId()!=certas[pergunta_atual])
                                    botoes_resposta[1].animate().translationX(2000).setDuration(900);

                                if(botoes_resposta[2].getId()!=certas[pergunta_atual])
                                    botoes_resposta[2].animate().translationX(2000).setDuration(1100);

                                if(botoes_resposta[3].getId()!=certas[pergunta_atual])
                                    botoes_resposta[3].animate().translationX(2000).setDuration(1300);
                            }
                        };

                        handler_fora.post(r);

                        // delay
                        try {
                            Thread.sleep(1500);

                        } catch (Exception e) {

                            Log.e("JogoDaBoleia", e.getMessage());
                        }

                        Intent intento = new Intent();
                        setResult(Activity.RESULT_OK,intento);
                        Perguntas.super.finish();
                    }

                    else{ // pergunta final

                        // fazer a animação
                        Runnable r = new Runnable() {

                            @Override
                            public void run() {

                                v.animate().scaleX(0.93f).scaleY(0.93f).setDuration(80).withEndAction(new Runnable() {
                                    @Override
                                    public void run() {
                                        v.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                    }
                                });
                            }
                        };

                        handler_fora.post(r);

                        // delay
                        try {
                            Thread.sleep(600);

                        } catch (Exception e) {

                            Log.e("JogoDaBoleia", e.getMessage());
                        }

                        r = new Runnable() {

                            @Override
                            public void run() {

                                if(botoes_resposta[0].getId()!=v.getId())
                                    botoes_resposta[0].animate().translationX(2000).setDuration(700);

                                if(botoes_resposta[1].getId()!=v.getId())
                                    botoes_resposta[1].animate().translationX(2000).setDuration(900);

                                if(botoes_resposta[2].getId()!=v.getId())
                                    botoes_resposta[2].animate().translationX(2000).setDuration(1100);

                                if(botoes_resposta[3].getId()!=v.getId())
                                    botoes_resposta[3].animate().translationX(2000).setDuration(1300);
                            }
                        };

                        handler_fora.post(r);

                        // delay
                        try {
                            Thread.sleep(1500);

                        } catch (Exception e) {

                            Log.e("JogoDaBoleia", e.getMessage());
                        }

                        Intent intento = new Intent();
                        setResult(Activity.RESULT_OK,intento);
                        Perguntas.super.finish();
                    }

                }

                else { // mudar de pergunta

                    // delay
                    try {
                        Thread.sleep(600);

                    } catch (Exception e) {

                        Log.e("JogoDaBoleia", e.getMessage());
                    }

                    pergunta_atual++;

                    Runnable r = new Runnable() {

                        @Override
                        public void run() {

                            if(botoes_resposta[0].getId()!=certas[pergunta_atual-1])
                                botoes_resposta[0].animate().translationX(2000).setDuration(700);

                            if(botoes_resposta[1].getId()!=certas[pergunta_atual-1])
                                botoes_resposta[1].animate().translationX(2000).setDuration(900);

                            if(botoes_resposta[2].getId()!=certas[pergunta_atual-1])
                                botoes_resposta[2].animate().translationX(2000).setDuration(1100);

                            if(botoes_resposta[3].getId()!=certas[pergunta_atual-1])
                                botoes_resposta[3].animate().translationX(2000).setDuration(1300);
                        }
                    };

                    handler_fora.post(r);

                    // delay
                    try {
                        Thread.sleep(2000);

                        if(botoes_resposta[0].getId()==certas[pergunta_atual-1])
                            botoes_resposta[0].animate().translationX(2000).setDuration(1000);

                        else if(botoes_resposta[1].getId()==certas[pergunta_atual-1])
                            botoes_resposta[1].animate().translationX(2000).setDuration(1000);

                        else if(botoes_resposta[2].getId()==certas[pergunta_atual-1])
                            botoes_resposta[2].animate().translationX(2000).setDuration(1000);

                        else if(botoes_resposta[3].getId()==certas[pergunta_atual-1])
                            botoes_resposta[3].animate().translationX(2000).setDuration(1000);

                        Thread.sleep(750);

                    } catch (Exception e) {

                        Log.e("JogoDaBoleia", e.getMessage());
                    }

                    r = new Runnable() {

                        @Override
                        public void run() {

                            pergunta.animate().scaleX(0.95f).scaleY(0.95f).setDuration(80).withEndAction(new Runnable() {
                                @Override
                                public void run() {
                                    pergunta.animate().scaleX(1.0f).scaleY(1.0f).setDuration(80);
                                }
                            });
                            pergunta.setText(perguntas[pergunta_atual]);

                            // restaurar a cor original
                            botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo);
                            botoes_resposta[0].setText(respostas[pergunta_atual][0]);
                            botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo);
                            botoes_resposta[1].setText(respostas[pergunta_atual][1]);
                            botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo);
                            botoes_resposta[2].setText(respostas[pergunta_atual][2]);
                            botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo);
                            botoes_resposta[3].setText(respostas[pergunta_atual][3]);

                            // mudar a resposta
                            botoes_resposta[0].animate().translationX(0).setDuration(700);
                            botoes_resposta[1].animate().translationX(0).setDuration(900);
                            botoes_resposta[2].animate().translationX(0).setDuration(1100);
                            botoes_resposta[3].animate().translationX(0).setDuration(1300);

                            // reativar os botões
                            botoes_resposta[0].setClickable(true);
                            botoes_resposta[1].setClickable(true);
                            botoes_resposta[2].setClickable(true);
                            botoes_resposta[3].setClickable(true);
                        }
                    };

                    handler_fora.post(r);
                }
                //---------------------------------------------------------------------------------------------------------------------------------------------------------
            }
        };

        mudar_pergunta.start();
    }
}


