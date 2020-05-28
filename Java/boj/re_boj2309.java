import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int []heights = new int[9];
		int sum = 0;
		int check = 0;
		
		for (int i = 0; i < 9; i++) {
			heights[i] = Integer.parseInt(br.readLine());
			sum += heights[i];
		}
		
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (i == j)
					continue;
				if (sum - (heights[i] + heights[j]) == 100) {
					heights[i] = -1;
					heights[j] = -1;
					check = 1;
					break;
				}
			}
			if (check == 1)
				break;
		}
		Arrays.sort(heights);
		for (int i : heights) {
			if (i != -1)
				bw.write(Integer.toString(i) + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}

}
