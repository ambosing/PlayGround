import java.util.*;
import java.io.*;

class Main {
    public static void main(String args[]) throws IOException{
    	BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	String[] str_arr = bf.readLine().split("");
    	Arrays.sort(str_arr, Collections.reverseOrder());
    	for (String i : str_arr)
    		System.out.print(i);
    	
    }
}