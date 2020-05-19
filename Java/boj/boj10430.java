import java.util.*;
import java.io.*;

class Main {
    public static void main(String args[]) throws IOException{
    	BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	String[] line = bf.readLine().split(" ");
    	int[] arr = new int[3];
    	for (int i = 0; i < 3; i++)
    		arr[i] = Integer.parseInt(line[i]);
    	System.out.println((arr[0] + arr[1]) % arr[2]);
    	System.out.println(((arr[0] % arr[2]) + (arr[1] % arr[2])) % arr[2]);
    	System.out.println((arr[0] * arr[1]) % arr[2]);
    	System.out.println(((arr[0] % arr[2]) * (arr[1] % arr[2])) % arr[2]);
    }
}