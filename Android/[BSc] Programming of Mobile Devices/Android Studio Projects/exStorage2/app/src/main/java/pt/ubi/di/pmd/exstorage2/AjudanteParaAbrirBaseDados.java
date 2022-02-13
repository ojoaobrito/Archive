package pt.ubi.di.pmd.exstorage2;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class AjudanteParaAbrirBaseDados extends SQLiteOpenHelper{

    protected static final int DB_VERSION = 1;
    protected static final String DB_NAME = "FavouriteMovies";

    protected static final String TABLE_NAME = "Movie";
    protected static final String COLUMN1 = "ID";
    protected static final String COLUMN2 = "Nome";
    protected static final String COLUMN3 = "Ano";

    // comandos SQL
    private static final String CREATE_MOVIE = "CREATE TABLE " + TABLE_NAME + "(" + COLUMN1 + " INTEGER PRIMARY KEY AUTOINCREMENT, " + COLUMN2 +
            " VARCHAR(50), " + COLUMN3 + " INTEGER);";

    public AjudanteParaAbrirBaseDados(Context context){

        super(context, DB_NAME, null, DB_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db){

        db.execSQL(CREATE_MOVIE);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int old_version, int new_version){

        db.execSQL("DROP TABLE " + TABLE_NAME + ";");
        db.execSQL(CREATE_MOVIE);
    }
}
