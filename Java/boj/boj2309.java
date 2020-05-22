import java.util.*;
import java.io.*;

class Main {
    /**
     * @param args
     * @throws IOException
     */
    public static void main(String args[]) throws IOException{
    	 BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	 ArrayList<Integer> arr = new ArrayList<Integer>();
    	 int sum = 0;
    	 int check;
    	 int x, y;
    	 
    	 for (int i = 0; i < 9; i++) {
    		 arr.add(Integer.parseInt(bf.readLine()));
    		 sum += arr.get(i);
    	 }
    	 for (int i = 0; i < 9; i++) {
    		 check = 0;
    		 for (int j = 0; j < 9; j++) {
    			 if (i == j)
    				 continue;
    			 x = arr.get(i);
    			 y = arr.get(j);
    			 if (sum - (x + y) == 100) {
    				 check = 1;
    				 arr.remove((Integer)x);
    				 arr.remove((Integer)y);
    				 break;
    			 }
    		 }
    		 if (check == 1)
    			 break;
    	 }
    	 Collections.sort(arr);
    	 for (int i : arr)
    		 System.out.println(i);
    }
}