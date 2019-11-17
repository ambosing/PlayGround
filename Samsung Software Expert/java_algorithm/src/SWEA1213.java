import java.util.Scanner;

public class SWEA1213 {
	public static void main(String args[])
	{
		int test = 0;
		String str ;
		String input;
		Scanner sc = new Scanner(System.in);
		String temp;
		int cnt = 0;
		
		while(test != 10)
		{
			test = sc.nextInt();
			
			str = new String();
			input = new String();
			temp = new String();
			
			input = sc.next();
			
			str = sc.next();
			
			
			for(int i = 0; i < str.length()-input.length()+1; i++)
			{
				temp = str.substring(i, i+input.length());
				if(input.contentEquals(temp))
					cnt++;
			}
			
			System.out.println("#"+test+" "+cnt);
			cnt = 0;
		}
	}
}
