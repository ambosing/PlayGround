import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int []num = new int[3];
		int []cnt = new int[10];
		int limit = 3;
		int res;
		
		for (int i = 0; i < limit; i++)
			num[i] = Integer.parseInt(br.readLine());
		res = num[0] * num[1] * num[2];
		char []char_arr = Integer.toString(res).toCharArray();
		limit = char_arr.length;
		for (int i = 0; i < 10; i++) {
			char chk = (char)(i + 48);
			for (int j = 0; j < limit; j++)
				if (chk == char_arr[j])
					cnt[i]++;
		}
		for (int i : cnt)
			bw.write(i + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}
