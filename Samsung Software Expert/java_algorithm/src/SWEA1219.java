import java.util.Scanner;


public class SWEA1219 {
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int test =0;
		int len =0;
		int[] size = new int[100];
		int[] size2 = new int[100];
		int inp1 = 0;
		int inp2 = 0, next =0;
		int past = 0;
		int[] route = new int[100];
		int[] route2 = new int[100];
		int valid = 1;
		
		
		while(test != 10)
		{
			test = sc.nextInt();
			len = sc.nextInt();
			
			for(int i=0; i<len; i++)
			{
				inp1 = sc.nextInt();
				inp2 = sc.nextInt();
				if(size[inp1] == 0)
					size[inp1] = inp2;
				else
					size2[inp1] = inp2;
			}
			
			for(int i =0; i <len; i++)
			{
				if (i == 0)
				{
					next = size[i];
				}
				if(size[next] == 99 || size2[next] == 99) break;
				
				System.out.println(next + " " + size[next]);
				if(size[next] != 0 &&(route[next] != size[next] && route2[next] != size[next]))
				{
					past = next;
					next = size[next];
					if(route[past] == 0)
						route[past] = next;
					else if(route2[past] == 0)
						route2[past] = next;
				}
				
				else 
				{
					if(size2[past] != 0 &&(route[past] != size2[past] && route2[past] != size2[past]) )
					{
						next = size2[past];
						if(route[past] == 0)
							route[past] = next;
						else if(route2[past] == 0)
							route2[past] = next;
					}
					
					else if(size2[next] != 0 && (route[next] != size2[next] && route2[next] != size2[next]))
					{
						past = next;
						next = size2[next];
						if(route[past] == 0)
							route[past] = next;
						else if(route2[past] == 0)
							route2[past] = next;
						
					}
						
					else
					{
						valid =0;
						break;
					}
				}
				
				
				
				
			
				
			}
			System.out.println("#"+test+" "+valid);
			
			valid = 1;
			
			for(int i = 0; i < 100; i++)
			{
				size[i] = 0;
				size2[i] = 0;
				route[i] = 0;
				route2[i] = 0;
			}
				
		}
	}

}
