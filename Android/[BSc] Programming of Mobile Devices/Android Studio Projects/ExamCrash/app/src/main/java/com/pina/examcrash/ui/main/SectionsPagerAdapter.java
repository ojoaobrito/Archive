package com.pina.examcrash.ui.main;

import android.content.Context;
import android.content.SharedPreferences;
import android.database.sqlite.SQLiteDatabase;
import android.util.Log;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import com.pina.examcrash.AjudanteParaAbrirBaseDados;
import com.pina.examcrash.R;

/**
 * A [FragmentPagerAdapter] that returns a fragment corresponding to
 * one of the sections/tabs/pages.
 */
public class SectionsPagerAdapter extends FragmentPagerAdapter {

    private static String[] TAB_TITLES = new String[]{""};
    private final Context mContext;
    private AjudanteParaAbrirBaseDados ajudante;
    private SQLiteDatabase sql;

    public SectionsPagerAdapter(Context context, FragmentManager fm) {
        super(fm);
        mContext = context;
    }

    public void mudar(String[] titulos){

        TAB_TITLES = titulos;
    }

    @Override
    public Fragment getItem(int position) {
        // getItem is called to instantiate the fragment for the given page.
        // Return a PlaceholderFragment (defined as a static inner class below).
        SharedPreferences preferencias = mContext.getSharedPreferences("Preferencias",0);
        return PlaceholderFragment.newInstance(position + 1, preferencias.getString("ID_Categoria", "10"), mContext);
    }

    @Nullable
    @Override
    public CharSequence getPageTitle(int position) {
        return (TAB_TITLES[position]);
    }

    @Override
    public int getCount() {

        SharedPreferences preferencias = mContext.getSharedPreferences("Preferencias",0);
        return(preferencias.getInt("Num_perguntas", 0));
    }
}