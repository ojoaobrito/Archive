from multiprocessing.connection import Client
import threading
import time
import os

host_server = '192.168.43.15'
rest = []

class bd_con( threading.Thread ) :
    def __init__( self, port , query) :
        threading.Thread.__init__( self )
        self.threadLock = threading.Lock()
        self.query = query

        try :
            self.con = Client(
                ( host_server, port ),
                authkey=bytes( 'secret password', 'utf-8' )
            )
        except :
            print( "#---- Can't Establish a Connection ----" )
            exit( 0 )

        if self.con.recv() != '1' :
            print( '#---- Error in Establishing a Connection ----' )
            exit( 0 )

    def run( self ) :

        global rest
        __user__ = 'policia'
        __pass__ = 'policia12345'
        __query__ = self.query

        self.con.send(
            __user__ + "$" +
            __pass__ + "$" +
            __query__
        )
   
        if self.con.recv() != '1':
            print("#---- Can't Establish a Connection ----")
        
        res = self.con.recv()
        self.con.send(res)

        self.threadLock.acquire()
        rest = res.copy()
        self.threadLock.release()

        # os.system( '\n' )

def get_query_result(query):
    bd_conn = bd_con( 6000, query )
    bd_conn.start()
    time.sleep(5)
    return(rest)
