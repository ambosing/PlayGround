import java.util.Scanner;

public class boj1912 {
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n, temp = 0;
		int i;
		int max= 0;
		n = sc.nextInt();
		
		int[] arr = new int[n];
		
		for(i = 0; i < n; i++)
		{
			arr[i] = sc.nextInt();
			
		}
		
		for(int j = 0; j < n; j++)
		{
			if(arr[j] >= 0)
			{
				temp += arr[j];
				
				if(max < temp)
					max = temp;
			}

			
			else
			{
				if(arr[j] + temp < max && max < temp)
				{
					max = temp;
					temp += arr[j];
					if(temp <0)
						temp = 0;
				}
				
				else if(max > temp && temp > 0)
				{
					temp += arr[j];
				}
				else 
					temp = 0;
				
			}
			
		}
		
		System.out.println(max);
		

	}
}
