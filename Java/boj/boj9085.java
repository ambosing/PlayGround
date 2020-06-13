import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int n, limit, numSum;
		
		for (int i = 0; i < t; i++) {
			n = Integer.parseInt(br.readLine());
			String []strs = br.readLine().split(" ");
			limit = strs.length;
			numSum = 0;
			for (int j = 0; j < limit; j++)
				numSum += Integer.parseInt(strs[j]);
			bw.write(Integer.toString(numSum) + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}