import java.util.Scanner;

public class SWEA1216 {
	public static void main(String args[])
	{
		int test = 0;
		int len = 0;
		String temp1 = new String();
		int cnt = 0;
		String str3 = new String();
		String rev = new String();
		String str2 = new String();
		StringBuffer temp = new StringBuffer();
		char[][] str = new char[101][101];
		Scanner sc = new Scanner(System.in);
		
		while(test != 10)
		{
			
			temp1 = sc.nextLine();
			test = Integer.parseInt(temp1);
			
			
			
			
			for(int i = 0; i < 100; i++)
			{
				
				temp1 = sc.nextLine();
				for(int j = 0; j < 100; j++)
				{	
					str[i][j] = temp1.charAt(j);
					
				}
				
			}
			for(int k = 2; k < 100; k++)
			{
				for(int i = 0; i < 100; i++)
				{
					for(int j = 0; j < 100; j++)
					{
						temp.append(str[i][j]);
					}
					str2 = temp.toString();
					temp = null;
					temp = new StringBuffer();
					
					for(int t = 0; t < 100-k+1; t++)
					{
						str3 = str2.substring(t, t+k);
						temp.append(str3);
						temp = temp.reverse();
						rev = temp.toString();
						if(str3.contentEquals(rev))
						{
							if(cnt <= k)
								cnt = k;
						}
								
						temp = null;
						temp = new StringBuffer();
					}
				
				}
				
				for(int i = 0; i < 100; i++)
				{
					for(int j = 0; j < 100; j++)
					{
						temp.append(str[j][i]);
					}
					str2 = temp.toString();
					temp = null;
					temp = new StringBuffer();
					
					for(int t = 0; t < 100-k+1; t++)
					{
						str3 = str2.substring(t, t+k);
						temp.append(str3);
						temp = temp.reverse();
						rev = temp.toString();
						if(str3.contentEquals(rev))
						{
							if(cnt <= k)
								cnt = k;
						}
						temp = null;
						temp = new StringBuffer();
					}
				}
			}
			System.out.println("#"+test+" "+cnt);
			cnt = 0;
			
		}
	}
}
