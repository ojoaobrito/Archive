package sd_browser;

import java.util.ArrayList;
import java.time.Clock;

public class backbone{

    private int tab_id;
    private int running_tab;
    private ArrayList < tab > user_tabs;

    public backbone( ){
        tab_id = 0;

        user_tabs = new ArrayList < tab > ();

        System.out.println( "\nNew Instance of Browser" );

    }

    public void new_tab( ){

        tab_id ++;
        user_tabs.add( new tab( tab_id ) );
        
    }

    public void switch_tab( int id ){

        running_tab = id;

        for ( tab t : user_tabs ){

            t.change_active_tab( id );

        }

    }

    public synchronized void close_tab( int id ){

        int k = 0;

        for ( k = 0; k < user_tabs.size(); k++ )
            if ( user_tabs.get( k ).get_id() == id )
                break;

        user_tabs.get(k).close();
        user_tabs.remove( user_tabs.get(k) );

    }

    public void active_tabs( ){

        System.out.println("\nSub-routine to check open threads:");

        for ( tab t : user_tabs ){

            System.out.println( t.get_id() );

        }

        System.out.println("");

    }

}