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
		int temp, sum, start, target;
		
		target = Integer.parseInt(br.readLine());
		start = 1;
		while (start != target) {
			sum = start;
			temp = start;
			while (temp > 0) {
				sum += temp % 10;
				temp /= 10;
			}
			if (sum == target)
				break;
			start++;
		}
		if (start == target)
			bw.write("0");
		else
			bw.write(Integer.toString(start));
		bw.flush();
		bw.close();
		br.close();
	}
}
