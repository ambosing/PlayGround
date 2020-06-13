import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int size = Integer.parseInt(br.readLine());
		String []strs = br.readLine().split(" ");
		int result = 0;
		int num, adder;
		
		adder = 0;
		for (int i = 0; i < size; i++) {
			num = Integer.parseInt(strs[i]);
			if (num == 1)
				adder++;
			else
				adder = 0;
			result += adder;
		}
		bw.write(result + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}