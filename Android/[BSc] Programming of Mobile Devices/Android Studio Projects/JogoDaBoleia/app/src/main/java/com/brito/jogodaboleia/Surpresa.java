package com.brito.jogodaboleia;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;

public class Surpresa extends AppCompatActivity {

    private ImageView imagem;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_surpresa);

        imagem = (ImageView) findViewById(R.id.final_imagem);

        // cor de fundo
        ConstraintLayout pai = (ConstraintLayout) findViewById(R.id.pai);
        pai.setBackgroundColor(Color.parseColor("#e6e6e6"));
    }

    public void guardar(View v){

        Log.v("JogoDaBoleia","Guardar");

        Bitmap imagem = BitmapFactory.decodeResource(this.getResources(),
                R.drawable.final_imagem);

        File file = new File(new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS).getPath() + "/"), "JogoDaBoleia.jpg");
        if (file.exists()) {
            file.delete();
        }
        try {
            FileOutputStream out = new FileOutputStream(file);
            imagem.compress(Bitmap.CompressFormat.JPEG, 100, out);
            out.flush();
            out.close();
        } catch (Exception e) {

            Log.v("JogoDaBoleia",e.getMessage());
        }

        Toast.makeText(this,"A imagem foi guardada nas transferências!",Toast.LENGTH_LONG).show();
    }
}

