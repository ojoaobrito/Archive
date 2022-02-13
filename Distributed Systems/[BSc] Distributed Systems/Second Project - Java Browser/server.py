from urllib.request import urlopen
from multiprocessing.connection import Listener
import threading
import time
import os
import re

class connection( threading.Thread ) :

    def __init__( self, newCon ) :

        threading.Thread.__init__( self )
        self.con = newCon


    def run( self ) :

        print( "New connection attached: ", Listener.last_accepted )
        self.con.send( "--open" )

        while True :

            try :
                url = self.con.recv( )
            except :
                print( "---- connection lost ----" )
                break

            if url == "--close" :
                self.con.send( "--disconnected" )
                break            

            try :

                name = re.findall(r'https://(.*)', url)[0] + ".html"
                name_c =  os.getcwd() + "/records/" + name
                
                if name in os.listdir( os.getcwd( ) + "/records" ) :
                   
                    self.con.send( open( name_c, "r" ).read( ) )

                else :

                    html = urlopen( url ).read()
                    self.con.send( str(html) )

                    open( name_c, "w" ).write( str( html ) )

            except :

                print( "invalid" )
                self.con.send( "--error" )

        self.con.close()


class listener( threading.Thread ) :


    def __init__ (self, port) :
    
        threading.Thread.__init__( self )
        self.Listener = Listener( 
            ( 'localhost', port ), 
            authkey = bytes( 'secret password', 'utf-8' )
        )
        self.threadLock = threading.Lock( )


    def run( self ) :

        while True :

            conn = self.Listener.accept( )
            
            self.threadLock.acquire( )
            
            x = connection( conn )
            x.start( )
            connection_list.append( x )

            self.threadLock.release( )


if __name__ == "__main__" :

    if "records" not in os.listdir( ) :
        os.mkdir( "records" )

    list = listener( 6000 )
    list.start()

    connection_list = []


    while True :

        time.sleep( 1 )
        print( "Active Connections: ", len( connection_list ) )
        
        for c in connection_list : 
            if not c.is_alive() : 
                connection_list.remove( c )


    for c in connection_list :
        c.join()

    print( "Server closing" )