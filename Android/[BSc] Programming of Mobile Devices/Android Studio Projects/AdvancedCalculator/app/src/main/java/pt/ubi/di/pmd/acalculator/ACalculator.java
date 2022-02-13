package pt.ubi.di.pmd.acalculator;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.*;
import android.widget.*;
import android.support.design.widget.Snackbar;

public class ACalculator extends AppCompatActivity {

    TextView barra;
    TextView result;
    EditText number1;
    EditText number2;
    Button sum;
    Button sub;
    Button mul;
    Button div;
    Snackbar mensagem;

    @Override
    protected void onCreate(Bundle savedInstanceState) { //criar a aplicação

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_acalculator); //carrega o layout da aplicação

        // instanciar os objetos (a classe R contém os ID's dos recursos). Existem classes R para cada tipo de recurso
        barra = (TextView) findViewById(R.id.barra);
        result = (TextView) findViewById(R.id.result);
        number1 = (EditText) findViewById(R.id.number1);
        number2 = (EditText) findViewById(R.id.number2);
        sum = (Button) findViewById(R.id.sum);
        sub = (Button) findViewById(R.id.sub);
        mul = (Button) findViewById(R.id.mul);
        div = (Button) findViewById(R.id.div);

        sum.setOnClickListener(

            new View.OnClickListener(){

                @Override
                public void onClick(View v) {

                    double num1 = Double.parseDouble(number1.getText().toString());
                    double num2 = Double.parseDouble(number2.getText().toString());

                    double soma = num1 + num2;

                    result.setText("" +soma);
                }

            }
        );

        sub.setOnClickListener(

            new View.OnClickListener(){

                @Override
                public void onClick(View v) {

                    double num1 = Double.parseDouble(number1.getText().toString());
                    double num2 = Double.parseDouble(number2.getText().toString());

                    double sub = num1 - num2;

                    result.setText("" +sub);
                }

            }
        );

        mul.setOnClickListener(

            new View.OnClickListener(){

                @Override
                public void onClick(View v) {

                    double num1 = Double.parseDouble(number1.getText().toString());
                    double num2 = Double.parseDouble(number2.getText().toString());

                    double mul = num1 * num2;

                    result.setText("" +mul);
                }

            }
        );

        div.setOnClickListener(

            new View.OnClickListener(){

                @Override
                public void onClick(View v) {

                    double num1 = Double.parseDouble(number1.getText().toString());
                    double num2 = Double.parseDouble(number2.getText().toString());

                    if (num2<=0){


                    }

                    double div = num1 / num2;

                    result.setText("" +div);
                }

            }
        );

    }
}
