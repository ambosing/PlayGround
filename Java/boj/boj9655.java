import java.util.*;
import java.io.*;

class Main {
    public static void main(String args[]) throws IOException{
    	 BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	 int t = Integer.parseInt(bf.readLine());
    	 int i;
    	 for (i = 0; t > 0; i++) {
    		 if (t % 3 == 0)
    			 t -= 3;
    		 else
    			 t -= 1;
    	 }
    	 if (i % 2 == 1)
    		 System.out.println("SK");
    	 else
    		 System.out.println("CY");
    }
}