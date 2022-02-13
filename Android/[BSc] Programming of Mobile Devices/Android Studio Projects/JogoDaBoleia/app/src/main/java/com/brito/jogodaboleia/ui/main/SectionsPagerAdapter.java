package com.brito.jogodaboleia.ui.main;

import android.content.Context;
import android.content.SharedPreferences;
import android.util.Log;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import com.brito.jogodaboleia.R;

/**
 * A [FragmentPagerAdapter] that returns a fragment corresponding to
 * one of the sections/tabs/pages.
 */
public class SectionsPagerAdapter extends FragmentPagerAdapter {

    private static String[] TAB_TITLES = new String[]{""};
    private final Context mContext;

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
        return PlaceholderFragment.newInstance(position + 1);
    }

    @Nullable
    @Override
    public CharSequence getPageTitle(int position) {
        return (TAB_TITLES[position]);
    }

    @Override
    public int getCount() {

        SharedPreferences preferencias = mContext.getSharedPreferences("Preferencias",0);
        if(preferencias.getInt("Estado",0)==6)
            return(26);
        else
            return(preferencias.getInt("Estado",0)*5);
    }
}