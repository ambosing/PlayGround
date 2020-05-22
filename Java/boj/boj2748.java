import java.util.*;
import java.io.*;

class Main {
    public static void main(String args[]) throws IOException{
    	 BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	 int n = Integer.parseInt(bf.readLine());
    	 long []pibo = new long[91];
    	 pibo[0] = 0;
    	 pibo[1] = 1;
    	 for (int i = 2; i <= n; i++)
    		 pibo[i] = pibo[i - 1] + pibo[i - 2];
    	 System.out.println(pibo[n]);
    }
}