import java.util.Scanner;

public class SWEA1221 {
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int[] num = new int[10];
		String inp = new String();
		String[] inp2;
		String temp1;
		String[] temp2 = new String[2];
		int temp;
		int n, t;
		
		temp = Integer.parseInt(sc.nextLine());
		System.out.println(temp);
		
		while(temp != 0)
		{
			temp--;
		
			temp1 = sc.nextLine();
			temp2 = temp1.split(" ");
			n = Integer.parseInt(temp2[1]);
			inp2 = new String[n];
			
			inp = sc.nextLine();
			
			inp2 = inp.split(" ");
			
			for(int i = 0; i < n; i++)
			{
				if(inp2[i].contentEquals("ZRO"))
					num[0]++;
				else if(inp2[i].contentEquals("ONE"))
					num[1]++;
				else if(inp2[i].contentEquals("TWO"))
					num[2]++;
				else if(inp2[i].contentEquals("THR"))
					num[3]++;
				else if(inp2[i].contentEquals("FOR"))
					num[4]++;
				else if(inp2[i].contentEquals("FIV"))
					num[5]++;
				else if(inp2[i].contentEquals("SIX"))
					num[6]++;
				else if(inp2[i].contentEquals("SVN"))
					num[7]++;
				else if(inp2[i].contentEquals("EGT"))
					num[8]++;
				else if(inp2[i].contentEquals("NIN"))
					num[9]++;
				
			}
			
			
			System.out.println(temp2[0]);
			
			t = 0;
			while(t != 10)
			{
				while(num[t] != 0)
				{
					switch(t)
					{
						case 0: System.out.print("ZRO ");
								num[t]--;
								break;
						case 1: System.out.print("ONE ");
								num[t]--;
								break;
						case 2: System.out.print("TWO ");
								num[t]--;
								break;
						case 3: System.out.print("THR ");
								num[t]--;
								break;
						case 4: System.out.print("FOR ");
								num[t]--;
								break;
						case 5: System.out.print("FIV ");
								num[t]--;
								break;
						case 6: System.out.print("SIX ");
								num[t]--;
								break;
						case 7: System.out.print("SVN ");
								num[t]--;
								break;
						case 8: System.out.print("EGT ");
								num[t]--;
								break;
						case 9: System.out.print("NIN ");
								num[t]--;
								break;
				
							
					}
				}
				t++;
			}
		}
	}
}
