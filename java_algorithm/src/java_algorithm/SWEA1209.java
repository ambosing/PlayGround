package java_algorithm;
import java.util.Scanner;


public class SWEA1209 {
	public static void main(String args[]) {
		int test = 0;
		int[][] xy = new int[100][100];
		int max = 0;
		int x = 0;
		int sum1 = 0, sum2 = 0;

		Scanner sc = new Scanner(System.in);
		
		
		while(test != 10)
		{
			test = sc.nextInt();
			for(int i = 0; i <100; i++)
			{
				
				for(int j=0; j < 100; j++)
				{
					xy[i][j] = sc.nextInt();
					x += xy[i][j];
					if(i == j)
					{
						// 대각선 오른쪽 합
						sum1 += xy[i][i];
					}
				}
				if( max < x)
				{
					max = x;
				}
				x = 0;
			}
			
			for(int i =99; i >=0; i--)
			{
				for(int j = 0; j < 100; j++)
				{
					x += xy[j][i];
					
					if(j == i)
					{
						sum2 += xy[j][j];
					}
				}
				if(max < x)
				{
					max = x;
				}
				x = 0;
			}
			if(max < sum1)
				max = sum1;
			if(max < sum2)
				max = sum2;
			
			System.out.println("#"+test+" "+max);
			max = 0;
			sum1 = 0;
			sum2 = 0;
			
			
		}
		
	}
}
