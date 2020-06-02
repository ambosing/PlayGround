import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int []arr = new int[1000];
		int t = Integer.parseInt(br.readLine());
		int target, chk;
		
		arr[0] = 1;
		for (int i = 2; ; i++) {
			arr[i - 1] = arr[i - 2] + i;
			if (arr[i - 1] > 1000) 
				break;
		}
		for (int l = 0; l < t; l++) {
			target = Integer.parseInt(br.readLine());
			chk = 0;
			for (int i = 0; arr[i] < 1000; i++) {
				for (int j = 0; arr[j] < 1000; j++) {
					for (int k = 0; arr[k] < 1000; k++) {
						if (arr[i] + arr[j] + arr[k] == target) {
							chk = 1;
							break;
						}
					}
					if (chk == 1)
						break;
				}
				if (chk == 1)
					break;
			}
			if (chk == 1)
				bw.write("1\n");
			else
				bw.write("0\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
