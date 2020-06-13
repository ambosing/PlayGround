import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		ArrayList<Integer> arr = new ArrayList<Integer>();
		String []strs = br.readLine().split(" ");
		int n, k;
		
		n = Integer.parseInt(strs[0]);
		k = Integer.parseInt(strs[1]);
		for (int i = 1; i <= n; i++) {
			if (n % i == 0)
				arr.add(i);
		}
		if (k - 1 >= arr.size())
			bw.write("0\n");
		else
			bw.write(Integer.toString(arr.get(k - 1)) + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}