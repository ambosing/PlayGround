import java.io.*;
import java.util.*;

public class SWEA1222 {
	public static void main(String args[]) throws Exception
	{
		int n;
		int test = 0;
		String inp = new String();
		String[] inp_arr;
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int result;
		
		while(test != 10)
		{
			n = Integer.parseInt(bf.readLine());
			inp = bf.readLine();
			inp_arr = inp.split("\\+");
			result = 0;
			
			for(int i = 0; i < inp_arr.length; i++)
				result += Integer.parseInt(inp_arr[i]);
			
			
			test++;
			
			System.out.println("#"+test+" "+result);
		}
	}
}
