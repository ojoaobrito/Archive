package pt.ubi.di.pmd.DEDOSdosPES;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class AjudanteParaAbrirBaseDados extends SQLiteOpenHelper{

    // informação da base de dados
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "DedosDOSpesBD";

    // tabela dos Alunos
    protected static final String TABLE_NAME1 = "Alunos";
    protected static final String COLUMN1 = "ID";
    protected static final String COLUMN2 = "Nome";
    protected static final String COLUMN3 = "Password";
    protected static final String COLUMN4 = "NivelAtual";
    protected static final String COLUMN5 = "RespostasCertas";
    protected static final String COLUMN12 = "RespostasErradas";

    // tabela do historico
    protected static final String TABLE_NAME2 = "Historico";
    protected static final String COLUMN6 = "IDHistorico";
    protected static final String COLUMN7 = "ID";
    protected static final String COLUMN8 = "PerguntaResposta";
    protected static final String COLUMN10 = "Nivel";
    protected static final String COLUMN11 = "certoOUerrado";


    // comandos SQL para criação das tabelas
    private static final String ALUNOS_TABLE_CREATE =
            "CREATE TABLE " + TABLE_NAME1 + "(" + COLUMN1 + " INTEGER PRIMARY KEY, " + COLUMN2 + " VARCHAR(50), "
                    + COLUMN3 + " CHAR(32), "+ COLUMN4+ " VARCHAR(15)," + COLUMN5+ " INTEGER, " + COLUMN12 + " INTEGER);";

    private static final String HISTORICO_TABLE_CREATE =
            "CREATE TABLE " + TABLE_NAME2 + "(" + COLUMN6 + " INTEGER PRIMARY KEY, " + COLUMN7 + " INTEGER, " + COLUMN8 + " VARCHAR(20), "
             + COLUMN10 + " INTEGER, " + COLUMN11 + " INTEGER);";


    // comandos SQL para remoção das tabelas
    private static final String ALUNOS_TABLE_DROP = "DROP TABLE " + TABLE_NAME1 + ";";
    private static final String HISTORICO_TABLE_DROP = "DROP TABLE " + TABLE_NAME2 + ";";

    private static final String ALUNOS_AUX_TABLE_DROP = "DROP TABLE AlunosAux;";
    private static final String HISTORICO_AUX_TABLE_DROP = "DROP TABLE HistoricoAux;";

    // comandos SQL para criação de tabelas temporárias (usados no método "onUpdate(...)")
    private static final String ALUNOS_TABLE_TEMP = "CREATE TEMP TABLE AlunosAux AS SELECT * FROM " + TABLE_NAME1 + ";";
    private static final String ALUNOS_TABLE_INSERT = "INSERT INTO " + TABLE_NAME1 + "(" + COLUMN1 + ", " + COLUMN2 + ", "
            + COLUMN3 +"," + COLUMN4+ ", "+ COLUMN5+ "," +COLUMN12+ ") SELECT * FROM AlunosAux;";

    private static final String HISTORICO_TABLE_TEMP = "CREATE TEMP TABLE HistoricoAux AS SELECT * FROM " + TABLE_NAME2 + ";";
    private static final String HISTORICO_TABLE_INSERT = "INSERT INTO " + TABLE_NAME2 + "(" + COLUMN6 + ", " + COLUMN7 + ", " + COLUMN8 + ", "
             + COLUMN10 + ", " + COLUMN11 + ") SELECT * FROM HistoricoAux;";


    public AjudanteParaAbrirBaseDados(Context context){

        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {

        db.execSQL(ALUNOS_TABLE_CREATE);
        db.execSQL(HISTORICO_TABLE_CREATE);

    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion){

        // remoção da tabela de alunos já existente e criação da nova, mantendo os dados já guardados
        db.execSQL(ALUNOS_TABLE_TEMP);
        db.execSQL(ALUNOS_TABLE_DROP);
        db.execSQL(ALUNOS_TABLE_CREATE);
        db.execSQL(ALUNOS_TABLE_INSERT);
        db.execSQL(ALUNOS_AUX_TABLE_DROP);

        // remoção da tabela de historico já existente e criação da nova, mantendo os dados já guardados
        db.execSQL(HISTORICO_TABLE_TEMP);
        db.execSQL(HISTORICO_TABLE_DROP);
        db.execSQL(HISTORICO_TABLE_CREATE);
        db.execSQL(HISTORICO_TABLE_INSERT);
        db.execSQL(HISTORICO_AUX_TABLE_DROP);

    }
}
