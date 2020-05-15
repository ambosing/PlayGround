import java.util.*;

public class boj16433 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n, r, c, check;
		
		n = sc.nextInt();
		r = sc.nextInt() - 1;
		c = sc.nextInt() - 1;
		check = (r + c) % 2;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if ((i + j) % 2 == check)
					System.out.print('v');
				else
					System.out.print('.');
			}
			System.out.println();
		}
	}

}
