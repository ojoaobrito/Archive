package pt.ubi.di.pdm.rockefort;

import android.app.Activity;

import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class PrefsJogo extends Activity {

    private ImageView background;
    private String ID;
    private String nome_jogo;
    private String username;
    private int nivel;
    private TextView titulo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_prefs_jogo);

        try {

            Intent intento = getIntent();

            ID = intento.getStringExtra("ID");
            nome_jogo = intento.getStringExtra("Nome");
            username = intento.getStringExtra("Username");
            nivel = Integer.parseInt(intento.getStringExtra("Nivel"));
            titulo = (TextView) findViewById(R.id.titulo);

            // mudar o wallpaper consoante o jogo
            background = (ImageView) findViewById(R.id.background);

            if(nome_jogo.equals("Minecraft")) {
                background.setBackgroundResource(R.drawable.mn2);
                titulo.setTextColor(Color.parseColor("#006bb3"));
                background.setAlpha((float)0.6);
            }

            else if(nome_jogo.equals("Assassin's Creed")) {
                background.setBackgroundResource(R.drawable.ass1);
                titulo.setTextColor(Color.parseColor("#006bb3"));
                background.setAlpha((float)0.6);
            }

            else if(nome_jogo.equals("League Of Legends")) {
                background.setBackgroundResource(R.drawable.lol2);
                titulo.setTextColor(Color.parseColor("#006bb3"));
                background.setAlpha((float)0.6);
            }

            else if(nome_jogo.equals("Rocket League")) {
                background.setBackgroundResource(R.drawable.rl1);
                titulo.setTextColor(Color.parseColor("#FFFFFF"));
                background.setAlpha((float)0.6);
            }

            else if(nome_jogo.equals("CS:GO")) {
                background.setBackgroundResource(R.drawable.cs2);
                titulo.setTextColor(Color.parseColor("#FFFFFF"));
                background.setAlpha((float)0.6);
            }

            else if(nome_jogo.equals("Fortnite")) {
                background.setBackgroundResource(R.drawable.ft2);
                titulo.setTextColor(Color.parseColor("#FFFFFF"));
                background.setAlpha((float)0.6);
            }

        } catch (Exception e) {

            Log.e("RockeFort", e.getMessage());
            super.finish();
        }
    }

    public void reddit(View v) {

        String link = "";

        if(nome_jogo.equals("Minecraft"))
            link = "https://www.reddit.com/r/Minecraft/";
        else if(nome_jogo.equals("CS:GO"))
            link = "https://www.reddit.com/r/GlobalOffensive/comments/1qze76/how_to_link_reddit_account_to_steam/";
        else if(nome_jogo.equals("Assassin's Creed"))
            link = "https://www.reddit.com/r/assassinscreed/";
        else if(nome_jogo.equals("League Of Legends"))
            link = "https://www.reddit.com/r/leagueoflegends/comments/34iiz7/linking_league_account_to_reddit_account/";
        else if(nome_jogo.equals("Rocket League"))
            link = "https://www.reddit.com/r/RocketLeague/comments/awufp2/link_accounts/";
        else if(nome_jogo.equals("Fortnite"))
            link = "https://www.reddit.com/r/FortNiteBR/";

        try {

            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(link));
            startActivity(browserIntent);

        } catch(Exception e){Log.e("RockeFort",e.getMessage());}

    }

    public void youtube(View v) {

        String link = "";

        if(nome_jogo.equals("Minecraft"))
            link = "https://www.youtube.com/user/TeamMojang";
        else if(nome_jogo.equals("CS:GO"))
            link = "https://www.youtube.com/channel/UCWF9XFFp_jVxGWvFmPZY70Q";
        else if(nome_jogo.equals("Assassin's Creed"))
            link = "https://www.youtube.com/channel/UCrniLr5HDebHfskhSSAAt0A";
        else if(nome_jogo.equals("League Of Legends"))
            link = "https://www.youtube.com/user/RiotGamesInc";
        else if(nome_jogo.equals("Rocket League"))
            link = "https://www.youtube.com/user/RocketLeagueGame";
        else if(nome_jogo.equals("Fortnite"))
            link = "https://www.youtube.com/user/epicfortnite";


        try {

            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(link));
            startActivity(browserIntent);

        } catch(Exception e){Log.e("RockeFort",e.getMessage());}

    }

    public void news(View v) {

        String link = "";

        if(nome_jogo.equals("Minecraft"))
            link = "https://www.tecmundo.com.br/minecraft";
        else if(nome_jogo.equals("CS:GO"))
            link = "https://steamcommunity.com/app/730/allnews/";
        else if(nome_jogo.equals("Assassin's Creed"))
            link = "https://news.ubisoft.com/en-us/category/assassins-creed";
        else if(nome_jogo.equals("League Of Legends"))
            link = "https://euw.leagueoflegends.com/en/news/";
        else if(nome_jogo.equals("Rocket League"))
            link = "https://www.rocketleague.com/news/";
        else if(nome_jogo.equals("Fortnite"))
            link = "https://www.epicgames.com/fortnite/en-US/news";

        try {

            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(link));
            startActivity(browserIntent);

        } catch(Exception e){Log.e("RockeFort",e.getMessage());}

    }

    public void tips(View v) {

        String link = "";

        if(nome_jogo.equals("Minecraft"))
            link = "https://www.wondershare.com/game-tips/minecraft-tips.html";
        else if(nome_jogo.equals("CS:GO"))
            link = "https://www.killping.com/blog/how-to-get-better-cs-go/";
        else if(nome_jogo.equals("Assassin's Creed"))
            link = "https://www.gamesradar.com/assassins-creed-odyssey-tips/";
        else if(nome_jogo.equals("League Of Legends"))
            link = "https://lolriotguide.com/league-of-legends-tips/";
        else if(nome_jogo.equals("Rocket League"))
            link = "https://www.cnet.com/how-to/tips-to-help-you-get-better-at-rocket-league/";
        else if(nome_jogo.equals("Fortnite"))
            link = "https://www.pcgamesn.com/fortnite/fortnite-battle-royale-download-tips-gameplay-weapons-map-loot-items";

        try {

            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(link));
            startActivity(browserIntent);

        } catch(Exception e){Log.e("RockeFort",e.getMessage());}

    }

    public void InfoJogo(View v) {

        super.finish();

    }

}
