import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		String []strs = new String[2];
		int	[]num = new int[2];
		
		for (int i = 0; i < t; i++) {
			strs = br.readLine().split(" ");
			num[0] = Integer.parseInt(strs[0]);
			num[1] = Integer.parseInt(strs[1]);
			bw.write("Case " + Integer.toString(i + 1) + ": " + Integer.toString(num[0] + num[1]) + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}