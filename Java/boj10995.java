import java.util.*;

public class boj10995 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h, leng;
		
		h = sc.nextInt();
		for (int i = 0; i < h; i++)
		{
			if (i % 2 == 0)
				leng = h * 2 - 1;
			else
				leng = h * 2;
			for (int j = 0; j < leng; j++)
			{
				if ((i + j) % 2 == 0)
					System.out.print('*');
				else
					System.out.print(' ');
			}
			System.out.println();
		}
	}

}
