import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException; 
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;

public class sha1sum{

	static final String HEXES ="0123456789abcdef";

	public static String getHex(byte[] raw){

		if(raw == null)
			return(null);

		final StringBuilder hex = new StringBuilder(2*raw.length);
		
		for (final byte b : raw)
			hex.append(HEXES.charAt((b & 0xF0) >> 4)).append(HEXES.charAt((b & 0x0F)));
		
		return hex.toString();
	}

	public static void main(String args[]){

		FileReader ficheiro; // ficheiro a abrir
		MessageDigest message; // objeto que vai tratar de calcular o valor de hash

		try{

			ficheiro = new FileReader(args[0]);
			message = MessageDigest.getInstance("SHA1"); //instanciar com o algoritmo SHA1
		}
		
		catch(FileNotFoundException f){

			System.out.println("ERRO!!");
			return;
		}

		catch(NoSuchAlgorithmException n){

			System.out.println("ERRO!!");
			return;
		}

		char[] buff = new char[1];

		try{
			while(ficheiro.read(buff)>0)
				message.update((byte)buff[0]);
			
			System.out.println("SHA1(" +args[0] +")= " +getHex(message.digest()));

			ficheiro.close();
		}

		catch(IOException i){

			System.out.println("ERRO!!");
			return;
		}
	}
}