import java.util.*;

public class boj15947 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t;
		int	div, mod;
		int len_s;
		String res = new String();
		String temp = new String();
		String s[] = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan".split(" ");
		
		t = sc.nextInt() - 1;
		len_s = s.length;
		div = t / len_s;
		mod = t % len_s;
		if (s[mod].equals("tururu"))
		{
			if (div > 2)
				res = "tu+ru*" + Integer.toString(div + 2);
			else
			{
				for (int i = 0; i < div; i++)
					temp += "ru";
				res = "tururu" + temp;
			}
		}
		else if (s[mod].equals("turu"))
		{
			if (div > 3)
				res = "tu+ru*" + Integer.toString(div + 3);
			else
			{
				for (int i = 0; i < div; i++)
					temp += "ru";
				res = "turu" + temp;
			}
		}
		else
			res = s[mod];
		System.out.print(res);
		sc.close();
	}
}
