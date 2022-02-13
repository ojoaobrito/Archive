package sd_browser;

public class tab extends Thread{

    private int id;
    private int current;

    public tab( int id ){

        super();

        this.id = id;

        System.out.println( "Tab: " + id );

        start();

    }

    public synchronized void run(){

        while(true){
            while(current != id){
                try{
                    wait();
                }catch( InterruptedException e ){
                    System.out.println( e.getMessage() );
                }
            }

            try{
                wait(1000);
            }catch( Exception e ){
                System.out.println( e.getMessage() );
            }

            System.out.println("Im " + id);

        }

    }

    public synchronized void change_active_tab( int current ){

        this.current = current;
        
        try{
            notifyAll();
        }catch( Exception e ){
            System.out.println( e.getMessage() );
        }
    
    }

    public void close(){
        interrupt();
    }

    public int get_id(){
    
        return id;
    
    }

}