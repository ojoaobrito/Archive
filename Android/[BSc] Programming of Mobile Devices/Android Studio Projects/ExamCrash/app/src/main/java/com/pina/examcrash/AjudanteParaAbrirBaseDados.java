package com.pina.examcrash;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class AjudanteParaAbrirBaseDados extends SQLiteOpenHelper{

    // informação da base de dados
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "ExamCrashDatabase";

    // tabela das categorias
    public static final String TABLE_NAME1 = "Categorias";
    public static final String COLUMN1 = "ID_Categoria";
    public static final String COLUMN2 = "Nome";
    public static final String COLUMN3 = "Icone";

    // tabela das perguntas
    public static final String TABLE_NAME2 = "Perguntas";
    public static final String COLUMN4 = "ID_Categoria";
    public static final String COLUMN5 = "ID_Pergunta";
    public static final String COLUMN6 = "Texto_Pergunta";
    public static final String COLUMN7 = "Texto_Respostas";
    public static final String COLUMN8 = "Código_Respostas";
    public static final String COLUMN9 = "Resposta";

    // comandos SQL para criação das tabelas
    private static final String CATEGORIA_TABLE_CREATE =
            "CREATE TABLE " + TABLE_NAME1 + "(" + COLUMN1 + " INTEGER PRIMARY KEY, " + COLUMN2 + " VARCHAR(30), "
                    + COLUMN3 + " VARCHAR(30))";

    private static final String PERGUNTAS_TABLE_CREATE =
            "CREATE TABLE " + TABLE_NAME2 + "(" + COLUMN4 + " INTEGER, " + COLUMN5 + " INTEGER, "
                    + COLUMN6 + " VARCHAR(30), " + COLUMN7 + " VARCHAR(30), " + COLUMN8 + " VARCHAR(30), " + COLUMN9 + " VARCHAR(30))";

    // comandos SQL para remoção das tabelas
    private static final String CATEGORIA_TABLE_DROP = "DROP TABLE " + TABLE_NAME1 + ";";
    private static final String CATEGORIA_AUX_TABLE_DROP = "DROP TABLE ExamCrashAux;";

    // comandos SQL para criação de tabelas temporárias (usados no método "onUpdate(...)")
    private static final String CATEGORIA_TABLE_TEMP = "CREATE TEMP TABLE ExamCrashAux AS SELECT * FROM " + TABLE_NAME1 + ";";
    private static final String CATEGORIA_TABLE_INSERT = "INSERT INTO " + TABLE_NAME1 + "(" + COLUMN1 + ", " + COLUMN2 + ", "
            + COLUMN3 + ") SELECT * FROM ExamCrashAux;";

    // comandos SQL para remoção das tabelas
    private static final String PERGUNTAS_TABLE_DROP = "DROP TABLE " + TABLE_NAME2 + ";";
    private static final String PERGUNTAS_AUX_TABLE_DROP = "DROP TABLE ExamCrashAux2;";

    // comandos SQL para criação de tabelas temporárias (usados no método "onUpdate(...)")
    private static final String PERGUNTAS_TABLE_TEMP = "CREATE TEMP TABLE ExamCrashAux2 AS SELECT * FROM " + TABLE_NAME2 + ";";
    private static final String PERGUNTAS_TABLE_INSERT = "INSERT INTO " + TABLE_NAME2 + "(" + COLUMN4 + ", " + COLUMN5 + ", "
            + COLUMN6 + ", " + COLUMN7 + ", " + COLUMN8 + ", " + COLUMN9 + ") SELECT * FROM ExamCrashAux2;";

    public AjudanteParaAbrirBaseDados(Context context){

        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {

        db.execSQL(CATEGORIA_TABLE_CREATE);
        db.execSQL(PERGUNTAS_TABLE_CREATE);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion){

        // remoção da tabela já existente e criação da nova, mantendo os dados já guardados
        db.execSQL(CATEGORIA_TABLE_TEMP);
        db.execSQL(CATEGORIA_TABLE_DROP);
        db.execSQL(CATEGORIA_TABLE_CREATE);
        db.execSQL(CATEGORIA_TABLE_INSERT);
        db.execSQL(CATEGORIA_AUX_TABLE_DROP);

        // remoção da tabela já existente e criação da nova, mantendo os dados já guardados
        db.execSQL(PERGUNTAS_TABLE_TEMP);
        db.execSQL(PERGUNTAS_TABLE_DROP);
        db.execSQL(PERGUNTAS_TABLE_CREATE);
        db.execSQL(PERGUNTAS_TABLE_INSERT);
        db.execSQL(PERGUNTAS_AUX_TABLE_DROP);
    }
}
