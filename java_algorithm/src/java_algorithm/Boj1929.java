package java_algorithm;
import java.util.StringTokenizer;
import java.io.*;

public class Boj1929 {
	public static void main(String args[]) throws Exception
	{
		int prnum1, prnum2;
		int i,j;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String s = br.readLine();
		
		StringTokenizer st = new StringTokenizer(s);
		
		prnum1 = Integer.parseInt(st.nextToken());
		prnum2 = Integer.parseInt(st.nextToken());
		
		for(i = prnum1; i <= prnum2; i++)
		{
			if(i == 2)
			{
				bw.write(String.valueOf(i));
				bw.newLine();
				bw.flush();
				continue;
			}
			for(j = 2; j < i; j++)
			{
				if(i % j == 0)
					break;
			}
			
			if(j == i) 
			{
				bw.write(String.valueOf(i));
				bw.newLine();
				bw.flush();

			}
		}

	}
}
