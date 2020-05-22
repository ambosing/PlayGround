import java.util.*;
import java.io.*;

class Main {
   
    public static void main(String args[]) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int t = Integer.parseInt(br.readLine());
    	int[] arr = new int[100];
    	int n, j;
    	int temp;
    	
    	temp = 0;
    	arr[1] = 1;
    	j = 2;
    	while (true) {
    		arr[j] = arr[j - 1] + j;
    		if (arr[j] > 1000)
    			break;
    		j++;
    	}
    	for (int i = 0; i < t; i++) {
    		n = Integer.parseInt(br.readLine());
    		for (int k = 1; arr[k] < 1000; k++) {
    			for (int r = 1; arr[r] < 1000; r++) {
    				for (int u = 1; arr[u] < 1000; u++) {
    					temp = arr[k] + arr[r] + arr[u];
    					if (temp == n)
    						break;
    				}
    				if (temp == n)
						break;
    			}
    			if (temp == n)
					break;
    		}
    		if (temp == n)
    			System.out.println(1);
    		else
    			System.out.println(0);
    	}
    }
}