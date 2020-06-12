import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int line_limit;
		
		for (int i = 0; i < t; i++) {
			for (int j = t - i - 1; j > 0; j--)
				bw.write(" ");
			line_limit = i % t + 1;
			for (int j = 0; j < line_limit; j++)
				bw.write("*");
			bw.write("\n");
		}
		t--;
		for (int i = 0; i < t; i++) {
			line_limit = i % t + 1;
			for (int j = 0; j < line_limit; j++)
				bw.write(" ");
			for (int j = t - i; j > 0; j--)
				bw.write("*");
			bw.write("\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}