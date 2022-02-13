/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ihc1;

import java.io.*;
import java.util.*;

/**
 *
 * @author joaobrito
 */
public class IHC1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException{
        
        Scanner leitura = new Scanner(new File("/Users/joaobrito/Desktop/IHC/nutrition.txt"));
        ArrayList<String> frases = new ArrayList<String>();
    
        while(leitura.hasNext())
            frases.add(leitura.nextLine()); // ler uma linha
        
        String[] categorias; //categorias
        float[] medias = new float[5]; //media de cada categoria
        int k=0;
        float a = 0;
        String s = "";
    
        for(int i=0; i<frases.size(); i++){ //imprimir os dados
        
            categorias = frases.get(i).split("[|]"); //dividir cada linha em porções (representam cada categoria); usa-se "[|]" porque se for só "|" os cortes vão ser mal feitos
            
            for(int j=0; j<7; j++){
                
                if(j==0)//nome da comida
                    System.out.printf("%-40s", categorias[j]);
                
                else if(j==6 && i==0){ //primeira linha da nova categoria (Energy/100g)
                    
                    s = "Energy/100g [kcal/100]";
                    System.out.printf("%26s", s);
                }
                
                else if(j==6 && i!=0){ //nova categoria (Energy/100g)
                    
                    a = (100*(Float.parseFloat(categorias[5])))/(Float.parseFloat(categorias[3]));
                    System.out.printf("%26.1f", a);
                    medias[k] = medias[k] + a;
                    k=0;
                }
                
                else{ //restantes categorias
                    
                    System.out.printf("%18s", categorias[j]);
                    
                    if(i==0) //ignorar a primeira linha
                        continue;
                    
                    if(j!=2){ //se não for a categoria das doses
                        
                        medias[k] = medias[k] + Float.parseFloat(categorias[j]);
                        k++;
                        
                    }
                    
                }
               
            }
            
            System.out.print("\n");
        }
        
        medias[0] = medias[0]/181;
        medias[1] = medias[1]/181;
        medias[2] = medias[2]/181;
        medias[3] = medias[3]/181;
        medias[4] = medias[4]/181;
        
        System.out.printf("\n%-40s","MÉDIAS");
        System.out.printf("%18.2f                     %15.2f  %16.2f  %16.2f %25.2f\n", medias[0], medias[1], medias[2], medias[3], medias[4]);
    
    }
    
}
