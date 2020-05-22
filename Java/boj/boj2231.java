import java.util.*;
import java.io.*;

class Main {
    /**
     * @param args
     * @throws IOException
     */
    public static void main(String args[]) throws IOException {
    	 BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	 int n = Integer.parseInt(bf.readLine());
    	 int i = 1;
    	 int temp;
    	 int res = 0;
    	 
    	 while (i < n) {
    		 res = 0;
    		 temp = i;
    		 res += temp;
    		 while (temp > 0) {
    			 res += temp % 10;
    			 temp /= 10;
    		 }
    		 if (res == n)
    			 break;
    		 i++;
    	 }
    	 if (i == n)
    		 i = 0;
    	 System.out.println(i);
    }
}