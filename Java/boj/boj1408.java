import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String [][]times = new String[2][3];
		int [][]timeInt = new int[3][3];
		String print = new String();
		final int last = 3;

		times[0] = br.readLine().split(":");
		times[1] = br.readLine().split(":");
		for (int i = 0; i < last; i++) {
			timeInt[0][i] = Integer.parseInt(times[0][i]);
			timeInt[1][i] = Integer.parseInt(times[1][i]);
		}
		if (timeInt[0][0] > timeInt[1][0])
			timeInt[1][0] += 24;
		else if (timeInt[0][0] == timeInt[1][0]) {
			if (timeInt[0][1] > timeInt[1][1])
				timeInt[1][0] += 24;
			else if (timeInt[0][1] == timeInt[1][1])
				if (timeInt[0][2] > timeInt[1][2])
					timeInt[1][0] += 24;
		}
		for (int i = last - 1; i >= 0; i--) {
			if (i != 0 && timeInt[1][i] < timeInt[0][i]) {
				timeInt[1][i - 1]--;
				if (timeInt[1][i - 1] == -1) {
					timeInt[1][i - 1] = 59;
					timeInt[1][i - 2]--;
				}
				timeInt[2][i] = Math.abs(60 + timeInt[1][i] - timeInt[0][i]);
				continue;
			}
			timeInt[2][i] = Math.abs(timeInt[0][i] - timeInt[1][i]);
		}
		for (int i = 0; i < last; i++) {
			print = Integer.toString(timeInt[2][i]);
			if (timeInt[2][i] == 0)
				bw.write("00");
			else if (timeInt[2][i] < 10)
				bw.write("0" + print);
			else
				bw.write(print);
			if (i != last - 1)
				bw.write(":");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
