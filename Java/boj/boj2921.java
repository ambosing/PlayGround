import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int []num = new int[1000];
		int start, end, sum;
		
		for (int i = 0; i < 1000; i++) {
			start = i + 1;
			end = 2 * (i + 1);
			sum = 0;
			for (int j = start; j <= end; j++)
				sum += j;
			if (i == 0)
				num[i] = sum;
			else
				num[i] = num[i - 1] + sum;
		}
		bw.write(Integer.toString(num[t - 1]) + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}