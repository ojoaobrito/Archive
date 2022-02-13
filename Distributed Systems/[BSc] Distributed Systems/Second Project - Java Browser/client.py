from multiprocessing.connection import Client
import threading
import time
import re
import os

class abas( threading.Thread ) :

    def __init__( self, id, lock, conn ) :

        threading.Thread.__init__( self )
        self.id = id
        self.current = 0
        self.lock = lock
        self.webpage = ""
        self.new_webpage = ""
        self.order_to_kill = False
        self.conn = conn


    def run( self ) :
        while True :

            while self.id == self.current :

                if self.new_webpage != self.webpage :

                    if not self.new_webpage == "" :

                        self.conn.send( self.new_webpage )
                        print( self.conn.recv( ) )
                        self.webpage = self.new_webpage
                    
            if self.order_to_kill :
                    break

    def get_id( self ) :
        return self.id
    
    def execute_order( self ) :
        self.order_to_kill = True

    def change_aba( self, id ) :
                
        if self.id == id:
            if self.webpage != "" :
                self.conn.send( self.webpage )
                print( self.conn.recv( ) )

        self.current = id

    def change_url( self, url ) :
        self.new_webpage = url


class browser( threading.Thread ) :

    def __init__( self, port ) :

        threading.Thread.__init__( self )
        self.threadLock = threading.Lock( )
        self.list_abas = []
        self.nm_abas = 0
        self.current = -1

        try :
            self.conn = Client( 
                ( 'localhost', 6000 ),
                authkey=bytes('secret password', 'utf-8' )
            )
        except :
            print( "No connection" )
            exit( 0 )

        if self.conn.recv( ) != "--open" :
            print( "--error" )
            exit()


    def run ( self ) :

        while True :

            command = input( "Insert new command: " ).strip()

            if command == "--new" :
                self.nm_abas += 1
                x = abas( self.nm_abas, self.threadLock, self.conn )
                x.start()
                self.list_abas.append( x )

                print( len(self.list_abas) )


            if command[0:7] == "--close" :
                for x in self.list_abas :
                    if x.get_id() == int( command[8:] ) :
                        x.execute_order()
                        self.list_abas.remove( x )


            if command[0:4] == "--go" :

                url = re.findall(r'(w.*)', command[5:])[0]

                for x in self.list_abas :
                    if x.get_id() == self.current :
                        x.change_url( "https://" + url )


            if command[0:8] == "--change" :
                self.current = int( command[9:] )
                for x in self.list_abas :
                    x.change_aba( self.current )


            if command[0:6] == "--exit" :
                for x in self.list_abas :
                    x.execute_order()
                self.conn.send("--close")
                print( self.conn.recv( ) )
                self.conn.close()
                for t in self.list_abas : t.join()


            if command == "--list" :
                l = []
                
                for x in self.list_abas :
                    l.append( x.get_id() )
                
                print( l )

            os.system( "\n" )


if __name__ == "__main__" :
    x = browser( 6000 )
    x.start()