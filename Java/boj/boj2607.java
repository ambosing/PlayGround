import java.util.*;
import java.io.*;

class Main {
    public static void main(String args[]) throws IOException{
    	BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	String[] s = bf.readLine().split(" ");
    	int a = Integer.parseInt(s[0]);
    	int b = Integer.parseInt(s[1]);
    	int c = a;
    	int d = b;
    	int temp, gcd, lcm;
    	
    	while (b > 0) {
    		temp = a;
    		a = b;
    		b = temp % b;
    	}
    	gcd = a;
    	lcm = c * d / gcd;
    	System.out.print(gcd + "\n" + lcm);
    }
}