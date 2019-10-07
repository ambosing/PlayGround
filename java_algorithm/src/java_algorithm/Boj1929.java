package java_algorithm;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Boj1929 {
	public static void main(String args[])
	{
		int m, n;
		int i, j;
		Scanner sc = new Scanner(System.in);
		ArrayList<Boolean> Array;
		
		
		m = sc.nextInt();
		n = sc.nextInt();
		Array = new ArrayList<Boolean>(n+1);
		
		
		Array.add(false);
		Array.add(false);
		
		for(i = 2; i <= n; i++)
		{
			Array.add(true);
			
		}
		
		for(i = 2; (i*i) <= n; i++) {
			if(Array.get(i))
			{
				for(j = i*2; j<=n; j+=i) Array.set(j,false);
			}
		}
		
		for(i = m; i<=n; i++)
		{
			if(Array.get(i) == true)
				System.out.println(i);
		}
	}
}
