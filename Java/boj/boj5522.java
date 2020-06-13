import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		final int GAME_ROUND = 5;
		int totalScore = 0;
		
		for (int i = 0; i < GAME_ROUND; i++)
			totalScore += Integer.parseInt(br.readLine());
		bw.write(totalScore + "\n");
		bw.flush();
		bw.close();
		br.close();
	}
}