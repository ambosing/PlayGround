import java.util.*;

public class boj2941 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = new String();
		String pattern[] = { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
		Scanner sc = new Scanner(System.in);
		int len_s, check, len_p, len_pp = 0;
		int i, j, k;
		int result;
		
		s = sc.nextLine();
		len_s = s.length();
		len_p = pattern.length;
		result = len_s;
		for (i = 0; i < len_s; i++)
		{
			check = 0;
			for (j = 0; j < len_p; j++)
			{
				len_pp = pattern[j].length();
				for (k = 0; k < len_pp; k++)
				{
					if (i + k < len_s && s.charAt(i + k) == pattern[j].charAt(k))
						continue;
					else
						break;
				}
				if (k == len_pp)
					check = 1;
			}
			if (check == 1)
				result -= len_pp - 1;
		}
		System.out.println(result);
	}
}