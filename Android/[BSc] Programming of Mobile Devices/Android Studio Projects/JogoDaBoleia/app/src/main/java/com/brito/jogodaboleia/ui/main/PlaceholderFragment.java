package com.brito.jogodaboleia.ui.main;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;

import com.brito.jogodaboleia.R;

import java.util.Random;

/**
 * A placeholder fragment containing a simple view.
 */
public class PlaceholderFragment extends Fragment {

    private static final String ARG_SECTION_NUMBER = "section_number";

    private PageViewModel pageViewModel;

    public static PlaceholderFragment newInstance(int index) {
        PlaceholderFragment fragment = new PlaceholderFragment();
        Bundle bundle = new Bundle();
        bundle.putInt(ARG_SECTION_NUMBER, index);
        fragment.setArguments(bundle);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        pageViewModel = ViewModelProviders.of(this).get(PageViewModel.class);
        int index = 1;
        if (getArguments() != null) {
            index = getArguments().getInt(ARG_SECTION_NUMBER);
        }
        pageViewModel.setIndex(index);
    }

    @Override
    public View onCreateView(
            @NonNull LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_teste, container, false);
        final TextView textView_pergunta = root.findViewById(R.id.pergunta);

        final Button[] botoes_resposta = new Button[4];
        botoes_resposta[0] = (Button) root.findViewById(R.id.resposta1);
        botoes_resposta[1] = (Button) root.findViewById(R.id.resposta2);
        botoes_resposta[2] = (Button) root.findViewById(R.id.resposta3);
        botoes_resposta[3] = (Button) root.findViewById(R.id.resposta4);
        pageViewModel.getText().observe(this, new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {

                int pergunta = Integer.parseInt(s);

                String[] perguntas = new String[26];
                String[][] respostas = new String[26][4];
                long[] certas = new long[25];

                // 1ª pergunta
                //--------------------------------------------------------------
                perguntas[0] = "1. De que cor era a fita que me escreveste?";
                respostas[0][0] = "A) Fita? Que fita?";
                respostas[0][1] = "B) Branca";
                respostas[0][2] = "C) Cor de tijolo";
                respostas[0][3] = "D) Nem reparei";
                certas[0] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 2ª pergunta
                //--------------------------------------------------------------
                perguntas[1] = "2. Em que dia e mês faço anos?";
                respostas[1][0] = "A) 19 de Agosto";
                respostas[1][1] = "B) 18 de Agosto";
                respostas[1][2] = "C) 9 de Agosto";
                respostas[1][3] = "D) 20 de Setembro";
                certas[1] = botoes_resposta[0].getId();
                //--------------------------------------------------------------

                // 3ª pergunta
                //--------------------------------------------------------------
                perguntas[2] = "3. Qual é a tua alcunha na nossa conversa?";
                respostas[2][0] = "A) Inês";
                respostas[2][1] = "B) Inês França";
                respostas[2][2] = "C) Inês Lagosta";
                respostas[2][3] = "D) Inês Neves";
                certas[2] = botoes_resposta[3].getId();
                //--------------------------------------------------------------

                // 4ª pergunta
                //--------------------------------------------------------------
                perguntas[3] = "4. Na primeira vez que te dei boleia, fui jantar onde?";
                respostas[3][0] = "A) Merendola";
                respostas[3][1] = "B) Casa do Benfica";
                respostas[3][2] = "C) Yokozo";
                respostas[3][3] = "D) Serra Shopping";
                certas[3] = botoes_resposta[1].getId();
                //--------------------------------------------------------------

                // 5ª pergunta
                //--------------------------------------------------------------
                perguntas[4] = "5. Qual a sequência da primeira vez que fomos passear?";
                respostas[4][0] = "A) Gelado, Jardim do Lago e Ponte Branca";
                respostas[4][1] = "B) Gelado e Ponte Branca";
                respostas[4][2] = "C) Gelado, Mural com vista para a cidade e Ponte Branca";
                respostas[4][3] = "D) Mural com vista para a cidade, gelado e Ponte Branca";
                certas[4] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 6ª pergunta
                //--------------------------------------------------------------
                perguntas[5] = "6. Antes de uma curva de visibilidade reduzida é proibido parar:";
                respostas[5][0] = "A) A 30 metros da mesma";
                respostas[5][1] = "B) A 50 metros da mesma";
                respostas[5][2] = "C) A 100 metros da mesma";
                respostas[5][3] = "D) Parar? Para a frente é que é o caminho!";
                certas[5] = botoes_resposta[0].getId();
                //--------------------------------------------------------------

                // 7ª pergunta
                //--------------------------------------------------------------
                perguntas[6] = "7. Quantas vezes fomos comer gelado?";
                respostas[6][0] = "A) 1";
                respostas[6][1] = "B) Poucas vezes";
                respostas[6][2] = "C) 2";
                respostas[6][3] = "D) Demasiadas vezes";
                certas[6] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 8ª pergunta
                //--------------------------------------------------------------
                perguntas[7] = "8. Como se chama o meu irmão (aka teu amigo do Facebook)?";
                respostas[7][0] = "A) Pedro";
                respostas[7][1] = "B) José";
                respostas[7][2] = "C) Miguel";
                respostas[7][3] = "D) André";
                certas[7] = botoes_resposta[3].getId();
                //--------------------------------------------------------------

                // 9ª pergunta
                //--------------------------------------------------------------
                perguntas[8] = "9. Aprox. quantas vezes já perguntámos um ao outro se estávamos bem?";
                respostas[8][0] = "A) 10";
                respostas[8][1] = "B) Umas 200, coisa pouca!";
                respostas[8][2] = "C) Nenhuma";
                respostas[8][3] = "D) Estás bem Inês?";
                certas[8] = botoes_resposta[1].getId();
                //--------------------------------------------------------------

                // 10ª pergunta
                //--------------------------------------------------------------
                perguntas[9] = "10. Qual é a tua frase mais \"usada\"?";
                respostas[9][0] = "A) \"Não é preciso\"";
                respostas[9][1] = "B) \"Oh, (...)\"";
                respostas[9][2] = "C) \"Estou sim\"";
                respostas[9][3] = "D) \"Tas bem?\"";
                certas[9] = botoes_resposta[0].getId();
                //--------------------------------------------------------------

                // 11ª pergunta
                //--------------------------------------------------------------
                perguntas[10] = "11. Completa: \"Se tu estás bem, ...";
                respostas[10][0] = "A) ... tudo bem!\"";
                respostas[10][1] = "B) ... ainda bem!\"";
                respostas[10][2] = "C) ... eu estou bem\"";
                respostas[10][3] = "D) ... eu também!\"";
                certas[10] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 12ª pergunta
                //--------------------------------------------------------------
                perguntas[11] = "12. Como se chama o jogo das perguntas?";
                respostas[11][0] = "A) Perguntados";
                respostas[11][1] = "B) Quiz";
                respostas[11][2] = "C) O Teste";
                respostas[11][3] = "D) Sei lá!";
                certas[11] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 13ª pergunta
                //--------------------------------------------------------------
                perguntas[12] = "13. Na foto do instituto, qual é a ordem?";
                respostas[12][0] = "A) Tu, eu, Ana, Professora, Julien e Pedro";
                respostas[12][1] = "B) Tu, eu, Ana, Professora, Pedro e Julien";
                respostas[12][2] = "C) Eu, tu, Ana, Professora, Pedro e Julien";
                respostas[12][3] = "D) Eu, tu, Ana, Professora, Julien e Pedro";
                certas[12] = botoes_resposta[3].getId();
                //--------------------------------------------------------------

                // 14ª pergunta
                //--------------------------------------------------------------
                perguntas[13] = "14. Quantos filmes vi, obrigado (gentilmente) por ti?";
                respostas[13][0] = "A) 6";
                respostas[13][1] = "B) 5";
                respostas[13][2] = "C) 7";
                respostas[13][3] = "D) Eu não te obriguei a nada!";
                certas[13] = botoes_resposta[0].getId();
                //--------------------------------------------------------------

                // 15ª pergunta
                //--------------------------------------------------------------
                perguntas[14] = "15. No jogo de nos descrever enquanto uma fruta, ambos somos...";
                respostas[14][0] = "A) ... uma banana!";
                respostas[14][1] = "B) ... um morango!";
                respostas[14][2] = "C) ... uma papaia!";
                respostas[14][3] = "D) ... um tomate!";
                certas[14] = botoes_resposta[1].getId();
                //--------------------------------------------------------------

                // 16ª pergunta
                //--------------------------------------------------------------
                perguntas[15] = "16. Quantos seios cranianos existem?";
                respostas[15][0] = "A) 10";
                respostas[15][1] = "B) 9";
                respostas[15][2] = "C) 11";
                respostas[15][3] = "D) Pff estou de fériaaaasss!";
                certas[15] = botoes_resposta[0].getId();
                //--------------------------------------------------------------

                // 17ª pergunta
                //--------------------------------------------------------------
                perguntas[16] = "17. No vídeo que gravei a passar de carro em tua casa, que banda ia a tocar?";
                respostas[16][0] = "A) Queen";
                respostas[16][1] = "B) Bon Jovi";
                respostas[16][2] = "C) Scorpions";
                respostas[16][3] = "D) U2";
                certas[16] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 18ª pergunta
                //--------------------------------------------------------------
                perguntas[17] = "18. A nossa conversa tem o seguinte gradiente de cores e emoji:";
                respostas[17][0] = "A) Vermelho para azul; emoji a sorrir";
                respostas[17][1] = "B) Azul para vermelho; emoji com a língua de fora";
                respostas[17][2] = "C) Azul para vermelho; emoji a sorrir";
                respostas[17][3] = "D) Vermelho para azul; emoji com a língua de fora";
                certas[17] = botoes_resposta[1].getId();
                //--------------------------------------------------------------

                // 19ª pergunta
                //--------------------------------------------------------------
                perguntas[18] = "19. Como se chama a proposta de casa de banho feminina que me mandaste?";
                respostas[18][0] = "A) Women's Pink Toilet";
                respostas[18][1] = "B) 3Pees";
                respostas[18][2] = "C) Lapee";
                respostas[18][3] = "D) #PeeToo";
                certas[18] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 20ª pergunta
                //--------------------------------------------------------------
                perguntas[19] = "20. O Barça perdeu na Liga dos Campeões contra quem?";
                respostas[19][0] = "A) Manchester United";
                respostas[19][1] = "B) Tottenham";
                respostas[19][2] = "C) Roma";
                respostas[19][3] = "D) Liverpool";
                certas[19] = botoes_resposta[3].getId();
                //--------------------------------------------------------------

                // 21ª pergunta
                //--------------------------------------------------------------
                perguntas[20] = "21. Quem mandou mensagem primeiro?";
                respostas[20][0] = "A) Eu (João)";
                respostas[20][1] = "B) Sei lá!";
                respostas[20][2] = "C) Ai sou muito má a lembrar-me destas coisas!";
                respostas[20][3] = "D) Tu (Inês)";
                certas[20] = botoes_resposta[0].getId();
                //--------------------------------------------------------------

                // 22ª pergunta
                //--------------------------------------------------------------
                perguntas[21] = "22. Que desculpa usei da primeira vez que te dei boleia?";
                respostas[21][0] = "A) Que estava mau tempo";
                respostas[21][1] = "B) Insistindo muito";
                respostas[21][2] = "C) Que estava mau tempo e podias ficar pior";
                respostas[21][3] = "D) Que estavas doentita";
                certas[21] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 23ª pergunta
                //--------------------------------------------------------------
                perguntas[22] = "23. Completa: \"Join me in my car, we...";
                respostas[22][0] = "A) ... 'll go real far away from here!\"";
                respostas[22][1] = "B) ... could go real far away from here!\"";
                respostas[22][2] = "C) ... can go real far away from here!\"";
                respostas[22][3] = "D) ... can go real far away, away from here!\"";
                certas[22] = botoes_resposta[3].getId();
                //--------------------------------------------------------------

                // 24ª pergunta
                //--------------------------------------------------------------
                perguntas[23] = "24. Que gelados comemos da 2ª vez?";
                respostas[23][0] = "A) Natas e Maracujá";
                respostas[23][1] = "B) Framboesa e Natas";
                respostas[23][2] = "C) Maracujá e Framboesa";
                respostas[23][3] = "D) Maracujá e Morango";
                certas[23] = botoes_resposta[1].getId();
                //--------------------------------------------------------------

                // 25ª pergunta
                //--------------------------------------------------------------
                perguntas[24] = "25. Que palavra usei na pseudo-fita para te descrever?";
                respostas[24][0] = "A) Incrível";
                respostas[24][1] = "B) Máquina";
                respostas[24][2] = "C) Espetacular";
                respostas[24][3] = "D) Impecável";
                certas[24] = botoes_resposta[2].getId();
                //--------------------------------------------------------------

                // 26ª pergunta
                //--------------------------------------------------------------
                perguntas[25] = "26. Gostaste destes 2 dias?";
                respostas[25][0] = "A) Sim";
                respostas[25][1] = "B) Óbvio que sim";
                respostas[25][2] = "C) Claro que não";
                respostas[25][3] = "D) Não";
                //--------------------------------------------------------------

                textView_pergunta.setText(perguntas[pergunta-1]);
                botoes_resposta[0].setText(respostas[pergunta-1][0]);
                botoes_resposta[1].setText(respostas[pergunta-1][1]);
                botoes_resposta[2].setText(respostas[pergunta-1][2]);
                botoes_resposta[3].setText(respostas[pergunta-1][3]);

                // colorir os botões consoante as respostas dadas
                SharedPreferences preferencias = textView_pergunta.getContext().getSharedPreferences("Preferencias",0);
                String aux = (preferencias.getString("Respostas",""));
                String[] respostas_dadas = aux.split("-");

                String aux2 = (preferencias.getString("RespostasErradas",""));
                String[] respostas_erradas = aux2.split("-");

                if(pergunta==26){

                    // 1º botão
                    if(botoes_resposta[0].getId()==Integer.parseInt(respostas_dadas[pergunta-1])) {
                        botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_escolhido);
                    }

                    // 2º botão
                    else if(botoes_resposta[1].getId()==Integer.parseInt(respostas_dadas[pergunta-1])) {
                        botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_escolhido);
                    }

                    // 3º botão
                    else if(botoes_resposta[2].getId()==Integer.parseInt(respostas_dadas[pergunta-1])) {
                        botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_escolhido);
                    }

                    // 4º botão
                    else if(botoes_resposta[3].getId()==Integer.parseInt(respostas_dadas[pergunta-1])) {
                        botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_escolhido);
                    }
                }

                else{

                    // 1º botão
                    if(botoes_resposta[0].getId()==Integer.parseInt(respostas_dadas[pergunta-1]) &&
                            certas[pergunta-1]==botoes_resposta[0].getId()) {
                        botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_certo_escolhido);
                    }

                    else if(botoes_resposta[0].getId()==Integer.parseInt(respostas_dadas[pergunta-1]) &&
                            certas[pergunta-1]!=botoes_resposta[0].getId()) {

                        if(botoes_resposta[0].getId()==Integer.parseInt(respostas_erradas[pergunta-1]))
                            botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_errado_escolhido);

                        else
                            botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_neutro_escolhido);
                    }

                    else if(certas[pergunta-1]==botoes_resposta[0].getId()) {
                        botoes_resposta[0].setBackgroundResource(R.drawable.resposta_fundo_certo);
                    }

                    // 2º botão
                    if(botoes_resposta[1].getId()==Integer.parseInt(respostas_dadas[pergunta-1]) &&
                            certas[pergunta-1]==botoes_resposta[1].getId()){
                        botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_certo_escolhido);
                    }

                    else if(botoes_resposta[1].getId()==Integer.parseInt(respostas_dadas[pergunta-1]) &&
                            certas[pergunta-1]!=botoes_resposta[1].getId()){

                        if(botoes_resposta[1].getId()==Integer.parseInt(respostas_erradas[pergunta-1]))
                            botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_errado_escolhido);

                        else
                            botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_neutro_escolhido);
                    }

                    else if(certas[pergunta-1]==botoes_resposta[1].getId()){
                        botoes_resposta[1].setBackgroundResource(R.drawable.resposta_fundo_certo);
                    }

                    // 3º botão
                    if(botoes_resposta[2].getId()==Integer.parseInt(respostas_dadas[pergunta-1]) &&
                            certas[pergunta-1]==botoes_resposta[2].getId()){
                        botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_certo_escolhido);
                    }

                    else if(botoes_resposta[2].getId()==Integer.parseInt(respostas_dadas[pergunta-1]) &&
                            certas[pergunta-1]!=botoes_resposta[2].getId()){

                        if(botoes_resposta[2].getId()==Integer.parseInt(respostas_erradas[pergunta-1]))
                            botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_errado_escolhido);

                        else
                            botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_neutro_escolhido);
                    }

                    else if(certas[pergunta-1]==botoes_resposta[2].getId()){
                        botoes_resposta[2].setBackgroundResource(R.drawable.resposta_fundo_certo);
                    }

                    // 4º botão
                    if(botoes_resposta[3].getId()==Integer.parseInt(respostas_dadas[pergunta-1]) &&
                            certas[pergunta-1]==botoes_resposta[3].getId()) {
                        botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_certo_escolhido);
                    }

                    else if(botoes_resposta[3].getId()==Integer.parseInt(respostas_dadas[pergunta-1]) &&
                            certas[pergunta-1]!=botoes_resposta[3].getId()){

                        if(botoes_resposta[3].getId()==Integer.parseInt(respostas_erradas[pergunta-1]))
                            botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_errado_escolhido);

                        else
                            botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_neutro_escolhido);
                    }

                    else if(certas[pergunta-1]==botoes_resposta[3].getId()){
                        botoes_resposta[3].setBackgroundResource(R.drawable.resposta_fundo_certo);
                    }
                }
            }
        });
        return root;
    }
}