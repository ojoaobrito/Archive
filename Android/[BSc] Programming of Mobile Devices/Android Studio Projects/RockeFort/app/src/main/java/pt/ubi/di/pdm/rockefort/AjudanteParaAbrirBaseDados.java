package pt.ubi.di.pdm.rockefort;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class AjudanteParaAbrirBaseDados extends SQLiteOpenHelper{

    // informação da base de dados
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "RockeFortDatabase";

    // tabela dos jogos
    protected static final String TABLE_NAME1 = "Jogos";
    protected static final String COLUMN1 = "ID"; // valor MD5 do nome do jogo
    protected static final String COLUMN2 = "NomeJogo";
    protected static final String COLUMN3 = "NomeUser";
    protected static final String COLUMN4 = "NivelUser";

    // comandos SQL para criação das tabelas
    private static final String JOGOS_TABLE_CREATE =
            "CREATE TABLE " + TABLE_NAME1 + "(" + COLUMN1 + " CHAR(32) PRIMARY KEY, " + COLUMN2 + " VARCHAR(30), "
                    + COLUMN3 + " VARCHAR(30), " + COLUMN4 + " INTEGER)";

    // comandos SQL para remoção das tabelas
    private static final String JOGOS_TABLE_DROP = "DROP TABLE " + TABLE_NAME1 + ";";

    private static final String JOGOS_AUX_TABLE_DROP = "DROP TABLE JogosAux;";

    // comandos SQL para criação de tabelas temporárias (usados no método "onUpdate(...)")
    private static final String JOGOS_TABLE_TEMP = "CREATE TEMP TABLE JogosAux AS SELECT * FROM " + TABLE_NAME1 + ";";
    private static final String JOGOS_TABLE_INSERT = "INSERT INTO " + TABLE_NAME1 + "(" + COLUMN1 + ", " + COLUMN2 + ", "
            + COLUMN3 + ", " + COLUMN4 + ") SELECT * FROM JogosAux;";

    public AjudanteParaAbrirBaseDados(Context context){

        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {

        db.execSQL(JOGOS_TABLE_CREATE);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion){

        // remoção da tabela de jogos já existente e criação da nova, mantendo os dados já guardados
        db.execSQL(JOGOS_TABLE_TEMP);
        db.execSQL(JOGOS_TABLE_DROP);
        db.execSQL(JOGOS_TABLE_CREATE);
        db.execSQL(JOGOS_TABLE_INSERT);
        db.execSQL(JOGOS_AUX_TABLE_DROP);
    }
}
