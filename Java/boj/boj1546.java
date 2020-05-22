import java.util.*;
import java.io.*;

class Main {
    /**
     * @param args
     * @throws IOException
     */
    public static void main(String args[]) throws IOException{
    	 BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	 int t = Integer.parseInt(bf.readLine());
    	 String[] strs = bf.readLine().split(" ");
    	 int []arr = new int[t];
    	 int m = -1, res;
    	 int sum = 0, cnt = 0;
    	 
    	 for (int i = 0; i < t; i++) {
    		 arr[i] = Integer.parseInt(strs[i]);
    		 if (m < arr[i])
    			 m = arr[i];
    		 sum += arr[i];
    		 cnt++;
    	 }
    	 double avg = sum * 100.0 / m / cnt ;
    	 System.out.println(avg);
    }
}