import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		int playerNum;
		int maxPrice;
		String bestPlayer;
		
		for (int i = 0; i < t; i++) {
			playerNum = Integer.parseInt(br.readLine());
			maxPrice  = 0;
			bestPlayer = new String();
			for (int j = 0; j < playerNum; j++) {
				String[] playerInfo = new String[2];
				playerInfo = br.readLine().split(" ");
				int price = Integer.parseInt(playerInfo[0]);
				if (maxPrice < price) {
					maxPrice = price;
					bestPlayer = playerInfo[1];
				}
			}
			bw.write(bestPlayer + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
