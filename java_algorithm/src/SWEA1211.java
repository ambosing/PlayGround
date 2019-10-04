import java.util.Scanner;

public class SWEA1211 {
	public static void main(String args[])
	{
		int test = 0;
		int cnt = 0;
		int[][] ladder = new int[100][100];
		Scanner sc = new Scanner(System.in);
		int k = 0;
		int x= 0, min = 0, idx= 0;
		int drc = 1;
		
		while(test != 10)
		{
			test = sc.nextInt();
			
			for(int i = 0; i < 100; i++)
				for(int j = 0; j < 100; j++)
					ladder[i][j] = sc.nextInt();
			
			
		
			min = 1000;
			idx = 0;
			for(int i = 0; i < 100; i++)
			{
				k = 0; 
				x= i;
				cnt = 0;
				
				while(ladder[0][i] == 1)
				{
					
					if(x > 0 && (drc == 1 || drc == 2) && ladder[k][x-1] == 1)
					{
						x -= 1;
						drc = 2;
						cnt++;
						continue;
					}
					
					if(x != 99 && (drc == 1 || drc == 3) && ladder[k][x+1] == 1)
					{
						x += 1;
						drc = 3;
						cnt++;
						continue;
					}
					
					
					k += 1;
					drc = 1;
					cnt++;
					
					if(k ==  100) break;
				}
				
				if(k == 100 && cnt > 0 && min >= cnt)
				{
					min = cnt;
					idx = i;
				}
			}
			
			
			System.out.println("#"+test+" "+idx);
		}
	}
}
