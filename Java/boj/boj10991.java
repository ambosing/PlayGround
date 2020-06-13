import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int limit;
		
		for (int i = 0; i < t; i++) {
			limit = t - i - 1;
			for (int j = 0; j < limit; j++)
				bw.write(" ");
			limit = 2 * (i + 1);
			for (int j = 0; j < limit; j++) {
				if (j % 2 == 0)
					bw.write("*");
				else
					bw.write(" ");
			}
			bw.write("\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}