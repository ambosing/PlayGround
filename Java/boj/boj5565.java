import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int result = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < 9; i++)
			result -= Integer.parseInt(br.readLine());
		bw.write(Integer.toString(result));
		bw.flush();
		bw.close();
		br.close();
	}
}
