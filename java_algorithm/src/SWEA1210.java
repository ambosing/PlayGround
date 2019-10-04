import java.util.Scanner;

public class Solution {
	public static void main(String args[])
	{
		int test = 0;
		int[][] x = new int[100][100];
		int i;
		int pos = 0, direc = 1;
		int height;
		Scanner sc = new Scanner(System.in);
		
		
		while(test != 10)
		{
			test = sc.nextInt();
			for( i = 0; i < 100; i++)
			{
				for(int j = 0; j < 100; j++)
				{
					x[i][j] = sc.nextInt();
					
				}
			}
			
			for(i = 0; i < 100; i++)
			{
				if(x[99][i] == 2 )
				{
					pos = i;
					break;
				}
			}
		
			height = 98;
			direc = 1;
			while(true)
			{
				if ( height  == 0) break;
				if(pos+1 < 100 && (direc == 1 || direc == 2) && x[height][pos+1] == 1)
				{
					pos += 1;
					direc = 2;
					continue;
				}
				if(pos-1 >= 0 && (direc == 1 || direc == 3) && x[height][pos-1] == 1)
				{
					pos -= 1;
					direc = 3;
					continue;
				}
				
				
				height -= 1;
				direc = 1;
				
				
			}
			System.out.println("#"+test + " " + pos);
			
		}
	}
}
