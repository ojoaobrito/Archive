from multiprocessing.connection import Listener
import threading
import os
import time
import psycopg2

file_logs = "logs.txt"
host_server = '192.168.241.155'
host = 'localhost'


class dispatcher( threading.Thread ) :
    def __init__( self ) :
        threading.Thread.__init__( self )
        self.queue = []
    def run( self ) :
        print( '#---- Dispatcher is on ----' )
        while True :
            
            if not len( self.queue ) :
                print( "#---- No Requests in the Queue ----" )
            
            else :
                for i in self.queue :
                    try :
                        self.send_result_of_query( i[0], i[1], i[2], i[3] )
                        i[3].close()
                        print( '#---- Request Dispatched... Connection Closed ----' )
                    except :
                        print( '#---- Invalid Request ----' )

            self.queue.clear()
            time.sleep( 5 )
    def send_result_of_query( self, user, passw, query, con ) :
        try :
            conn = None
            params = {
                'host' : host,
                'database' : database,
                'user' : user,
                'password' : passw
            }
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute( query )
            result = cur.fetchall()

            con.send( result )
            
            cur.close()

            handler = open( file_logs, "a" )
            handler.write(
                user + "$" + 
                query + "$" +
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + "\n"
            )
            handler.close()

        except (Exception, psycopg2.DatabaseError) as error :
            print( error )
        finally :
            if con is not None :
                conn.close()


class connection( threading.Thread ) :
    def __init__( self, newCon ) :
        threading.Thread.__init__( self )
        self.con = newCon
    def run( self ) :
        print( "#---- New connection attached: ", Listener.last_accepted, " ----" )
        self.con.send( "1" )
        
        try :
            __query_params__ = self.con.recv()

            if __query_params__ == '69' :
                self.con.send( '0' )
                return

            self.con.send( '1' )
            
            aux = __query_params__.split( '$' )
            user, pwd, query = aux[0], aux[1], aux[2]

            thread_lock_gl.acquire()
            dsp.queue.append(( user, pwd, query, self.con ))
            thread_lock_gl.release()

        except Exception as e :
            #print( "#---- Connection Lost ----" )
            print( e )


class listener( threading.Thread ) :
    def __init__( self, port='6000' ) :
        threading.Thread.__init__( self )
        self.Listener = Listener(
            ( host_server, port ),
            authkey = bytes( 'secret password', 'utf-8' )
        )
        self.threadLock = threading.Lock()
    def run( self ) :
        while True :
            conn = self.Listener.accept()
            self.threadLock.acquire()

            x_con = connection( conn )
            x_con.start()
            connection_list.append( x_con )
            
            self.threadLock.release()


if __name__ == '__main__' :

    database = 'dados_acidentes'

    lstr = listener( 6000 )
    lstr.start()

    connection_list = []

    thread_lock_gl = threading.Lock()

    dsp = dispatcher()
    dsp.start()

    while True :

        time.sleep( 10 )
        print( "Active Connection: ", len( connection_list ) )

        for c in connection_list :
            if not c.is_alive() :
                connection_list.remove( c )

        for c in connection_list :
            c.join
        
    print("#---- Server Closing ----")