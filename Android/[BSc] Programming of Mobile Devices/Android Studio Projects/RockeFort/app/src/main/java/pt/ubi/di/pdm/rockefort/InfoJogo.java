package pt.ubi.di.pdm.rockefort;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.app.Activity;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import org.w3c.dom.Text;

public class InfoJogo extends Activity {

    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;
    private TextView nome_jogo;
    private TextView username;
    private TextView nivel;
    private ImageView background;
    private String ID;
    private String jogo;
    private String jogador;
    private String nivel_string;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info_jogo);

        nome_jogo = (TextView) findViewById(R.id.nome_jogo);
        username = (TextView)findViewById(R.id.nome_jogador);

        try {

            Intent intento = getIntent();

            ID = intento.getStringExtra("ID");
            jogador = intento.getStringExtra("Username");
            jogo = intento.getStringExtra("Nome");
            nivel_string = intento.getStringExtra("Nivel");

            // informação atual, mostrar ao utilizador apenas a título informativo
            username.setText(intento.getStringExtra("Username"));
            nome_jogo.setText(intento.getStringExtra("Nome") + " | " + intento.getStringExtra("Nivel"));

            // mudar o wallpaper consoante o jogo
            background = (ImageView) findViewById(R.id.background);

            if(intento.getStringExtra("Nome").equals("Minecraft")) {
                background.setBackgroundResource(R.drawable.mn2);
                background.setAlpha((float)0.6);
            }

            else if(intento.getStringExtra("Nome").equals("Assassin's Creed")) {
                background.setBackgroundResource(R.drawable.ass1);
                background.setAlpha((float)0.6);
            }

            else if(intento.getStringExtra("Nome").equals("League Of Legends")) {
                background.setBackgroundResource(R.drawable.lol2);
                background.setAlpha((float)0.6);
            }

            else if(intento.getStringExtra("Nome").equals("Rocket League")) {
                background.setBackgroundResource(R.drawable.rl1);
                nome_jogo.setTextColor(Color.parseColor("#FFFFFF"));
                username.setTextColor(Color.parseColor("#FFFFFF"));
                background.setAlpha((float)0.6);
            }

            else if(intento.getStringExtra("Nome").equals("CS:GO")) {
                background.setBackgroundResource(R.drawable.cs2);
                nome_jogo.setTextColor(Color.parseColor("#FFFFFF"));
                username.setTextColor(Color.parseColor("#FFFFFF"));
                background.setAlpha((float)0.6);
            }

            else if(intento.getStringExtra("Nome").equals("Fortnite")) {
                background.setBackgroundResource(R.drawable.ft2);
                nome_jogo.setTextColor(Color.parseColor("#FFFFFF"));
                username.setTextColor(Color.parseColor("#FFFFFF"));
                background.setAlpha((float)0.6);
            }

        } catch (Exception e) {

            Log.e("RockeFort", "Erro ao receber o intento!");
            super.finish();
        }
    }

    public void prefsJogo(View v) {

        Intent intento = new Intent(InfoJogo.this, PrefsJogo.class);
        intento.putExtra("ID",ID);
        intento.putExtra("Nome",jogo);
        intento.putExtra("Username",jogador);
        intento.putExtra("Nivel",nivel_string);
        startActivity(intento);

    }

    public void MainActivity(View v) {

        super.finish();

    }
}
