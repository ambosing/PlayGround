import java.util.Scanner;

public class SWEA1215 {
	public static void main(String args[])
	{
		int test = 0;
		int len = 0;
		String temp1 = new String();
		int k=0, cnt =0, cnt_ = 0;
		String str3 = new String();
		String rev = new String();
		String str2 = new String();
		StringBuffer temp = new StringBuffer();
		char[][] str = new char[9][9];
		Scanner sc = new Scanner(System.in);
		
		while(test != 10)
		{
			test++;
			temp1 = sc.nextLine();
			len = Integer.parseInt(temp1);
			
			
			
			
			for(int i = 0; i < 8; i++)
			{
				k = 0;
				temp1 = sc.nextLine();
				for(int j = 0; j < 8; j++)
				{	
					str[i][j] = temp1.charAt(j);
					
				}
				
			}
			
			for(int i = 0; i < 8; i++)
			{
				for(int j = 0; j < 8; j++)
				{
					temp.append(str[i][j]);
				}
				str2 = temp.toString();
				temp = null;
				temp = new StringBuffer();
				
				for(int t = 0; t < 8-len+1; t++)
				{
					str3 = str2.substring(t, t+len);
					temp.append(str3);
					temp = temp.reverse();
					rev = temp.toString();
					if(str3.contentEquals(rev))
						cnt++;
					temp = null;
					temp = new StringBuffer();
				}
			
			}
			
			for(int i = 0; i < 8; i++)
			{
				for(int j = 0; j < 8; j++)
				{
					temp.append(str[j][i]);
				}
				str2 = temp.toString();
				temp = null;
				temp = new StringBuffer();
				
				for(int t = 0; t < 8-len+1; t++)
				{
					str3 = str2.substring(t, t+len);
					temp.append(str3);
					temp = temp.reverse();
					rev = temp.toString();
					if(str3.contentEquals(rev))
						cnt++;
					temp = null;
					temp = new StringBuffer();
				}
			}
			System.out.println("#"+test+" "+cnt);
			cnt = 0;
			
		}
	}
}
