//O modo avançado ajusta o nivel de forma automatica (10 respostas corretas -> sobe de nivel, 10 respostas erradas -> desce de nivel)
package pt.ubi.di.pmd.DEDOSdosPES;

import androidx.appcompat.app.AppCompatActivity;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.CompoundButton;
import android.widget.RadioGroup;
import android.widget.Switch;

public class Definicoes extends AppCompatActivity {
    private SharedPreferences pref;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_definicoes);

        //vai buscar o ficheiro
        pref = getApplicationContext().getSharedPreferences("Definicoes", 0);

        //primeira entrada do ficheiro
        String modo_avancado = pref.getString("modo_avancado", "");

        //buscar o botao(switch)
        Switch btn_switch = (Switch)findViewById(R.id.modo);

        if(modo_avancado.equals("On")){
            btn_switch.setChecked(true);
        }else{
            btn_switch.setChecked(false);
        }

        //mudança de estado do switch(on off modo avançado)
        btn_switch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked == true){
                    SharedPreferences.Editor editor = pref.edit();
                    editor.putString("modo_avancado", "On");
                    editor.apply();

                } else{
                    SharedPreferences.Editor editor = pref.edit();
                    editor.putString("modo_avancado", "Off");
                    editor.apply();

                }
            }
        });



    }
}
