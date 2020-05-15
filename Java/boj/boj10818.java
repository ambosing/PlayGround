import java.util.Scanner;

public class boj10818 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t;
		int max;
		int	temp;
		int min;
		
		max = Integer.MIN_VALUE;
		min = Integer.MAX_VALUE;
		t = scan.nextInt();
		for (int i = 0; i < t; i++)
		{
			temp = scan.nextInt();
			if (temp > max)
				max = temp;
			if (temp < min)
				min = temp;
		}
		System.out.println(max + " " + min);
		scan.close();
	}

}
