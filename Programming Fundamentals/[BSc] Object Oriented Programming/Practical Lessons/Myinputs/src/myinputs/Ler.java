/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package myinputs;

/**
 *
 * @author a37880
 */

import java.io.*;
public class Ler {
    
    public static String umaString(){
        
        String s="";
        try{
            BufferedReader in= new BufferedReader(new InputStreamReader(System.in));
            s=in.readLine();
        }
        catch(IOException e){
            
            System.out.println("Erro ao ler fluxo de entrada. ");
        }
        
        return s;
    }
    

    public static int umInt(){
    
        while(true){
            
            try{
                return Integer.valueOf(umaString().trim()).intValue();
            }
            catch(Exception e){
                
                System.out.println("Não é um valor válido!!!");
            }
        }

}
    
    public static float umFloat(){
    
        while(true){
            
            try{
                return Float.valueOf(umaString());     
            }
            catch(Exception e){
                
                System.out.println("Não é um valor válido!!!");
            }
        }

} 
    
    public static char umChar() {
        while(true) {
            try {
                return umaString().trim().charAt(0);
            }
            catch (Exception e){  
                System.out.println("Não é um valor valido!!!");
            }
        }
}
    
    
    public static double umDouble(){
    
        while(true){
            
            try{
                return Double.valueOf(umaString());     
            }
            catch(Exception e){
                
                System.out.println("Não é um valor válido!!!");
            }
        }

} 
    
    
    public static boolean umBoolean(){
    
        while(true){
            
            try{
                return Boolean.valueOf(umaString());     
            }
            catch(Exception e){
                
                System.out.println("Não é um valor válido!!!");
            }
        }

} 
    
    
   public static short umShort(){
    
        while(true){
            
            try{
                return Short.valueOf(umaString());     
            }
            catch(Exception e){
                
                System.out.println("Não é um valor válido!!!");
            }
        }

} 
   
   
   public static long umLong(){
    
        while(true){
            
            try{
                return Long.valueOf(umaString());     
            }
            catch(Exception e){
                
                System.out.println("Não é um valor válido!!!");
            }
        }

} 

}



 