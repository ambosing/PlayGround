import java.util.Scanner;

public class SWEA1218 {
	public static void main(String args[])
	{
		int test = 0;
		int len = 0;
		String[] str;
		String temp = new String();
		Scanner sc = new Scanner(System.in);
		int valid = 1;
		int[] str2 = {0,0,0,0,0,0,0,0};
		
		while(test != 10)
		{
			test++;
			temp = sc.nextLine();
			len = Integer.parseInt(temp);
			temp = sc.nextLine();
			str = new String[len];
			
			str = temp.split("");
			
			for(int i = 0; i < str.length; i++)
			{
				if(str[i].equals("{"))
					str2[0]++;
				else if(str[i].equals("}"))
				{
					str2[1]++;
					if(str2[0] <str2[1])
						valid = 0;
				}
					
				else if(str[i].equals("["))
					str2[2]++;
				else if(str[i].equals("]"))
				{
					str2[3]++;
					if(str2[2] <str2[3])
						valid = 0;
				}
					
				else if(str[i].equals("("))
					str2[4]++;
				else if(str[i].equals(")"))
				{
					str2[5]++;
					if(str2[4] <str2[5])
						valid = 0;
				}
				else if(str[i].equals("<"))
					str2[6]++;
				else if(str[i].equals(">"))
				{
					str2[7]++;
					if(str2[6] <str2[7])
						valid = 0;
				}
			
				
			}
			
			
			
			for(int j = 0; j < 8; j = j+2)
			{
				if(str2[j] != str2[j+1])
					valid = 0;
				if(str2[j] != str2[j+1])
					valid = 0;
				if(str2[j] != str2[j+1])
					valid = 0;
				if(str2[j] != str2[j+1])
					valid = 0;
			}
			
			System.out.println("#"+test+" "+valid);
			valid = 1;
			
			for(int i = 0; i<8; i++)
				str2[i] = 0;
			
		}
	}
}
