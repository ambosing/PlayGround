import java.util.Scanner;

public class SWEA1220 {
	public static void main(String args[])
	{
		int[][] t;
		int size, temp;
		int test = 0;
		Scanner sc = new Scanner(System.in);
		int dl = 0;
	
		
		while(test != 10)
		{
			test++;
			size = sc.nextInt();
			t = new int[size][size];
			
			temp = 0;
			for(int i = 0; i < 100; i++)
				for(int j = 0; j < 100; j++)
					t[i][j] = sc.nextInt();
			
			for(int i = 0; i < 100; i++)
			{
				temp = 0;
				for(int j = 0; j < 100; j++)
				{
					if(temp == 0 && t[j][i] == 1)
					{
						temp = t[j][i];
					}
					else if(temp == 1 && t[j][i] == 2)
					{
						dl++;
						temp = 0;
					}
					
				}
				
			}
				
			
			System.out.println("#"+test+" "+dl);
			dl = 0;
			
		}
	}
}
