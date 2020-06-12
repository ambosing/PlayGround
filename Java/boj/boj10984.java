import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < t; i++) {
			int studentNum = Integer.parseInt(br.readLine());
			int gpSum = 0;
			double avgGpa = 0.0;
			for (int j = 0; j < studentNum; j++) {
				String []strs = new String[2];
				strs = br.readLine().split(" ");
				int gp = Integer.parseInt(strs[0]);
				gpSum += gp;
				avgGpa += gp * Double.parseDouble(strs[1]);
			}
			bw.write(Integer.toString(gpSum) + " " + 
					Double.toString(Math.round(avgGpa * 10 / gpSum) / 10.0) + "\n");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}
}