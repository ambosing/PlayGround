import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int limit;
		
		for (int i = 0; i < t; i++) {
			limit = i + 1;
			for (int j = 0; j < limit; j++)
				bw.write("*");
			limit = 2 * (t - (i + 1));
			for (int j = 0; j < limit; j++)
				bw.write(" ");
			limit = i + 1;
			for (int j = 0; j < limit; j++)
				bw.write("*");
			bw.write("\n");
		}
		t--;
		for (int i = 0; i < t; i++) {
			for (int j = i; j < t; j++)
				bw.write("*");
			limit = 2 * (i + 1);
			for (int j = 0; j < limit; j++)
				bw.write(" ");
			for (int j = i; j < t; j++)
				bw.write("*");
			bw.write("\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}