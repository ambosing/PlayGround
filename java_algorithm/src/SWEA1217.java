import java.util.Scanner;


public class SWEA1217 {
	public static int mul(int a, int b)
	{
		if(b <= 0) return 1;
		return mul(a, b-1) * a;
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int test = 0;
		int res = 0;
		int cnt = 0;
		int num = 0;
		
		while(test != 10)
		{
			test = sc.nextInt();
			num = sc.nextInt();
			cnt = sc.nextInt();
			
			res = mul(num, cnt);
			
			System.out.println("#"+ test + " " + res);
			
		}
		
	}
}
