import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
	static void swap_row(char[][] board, int i, int j) {
		char temp = board[i][j];
		board[i][j] = board[i + 1][j];
		board[i + 1][j] = temp;
	}
	
	static void swap_col(char[][] board, int i, int j) {
		char temp = board[i][j];
		board[i][j] = board[i][j + 1];
		board[i][j + 1] = temp;
	}
	
	static int find_max(int x, int y) {
		return (x > y ? x : y);
	}
	
	static int return_max_result(char board[][], int n) {
		int []results = new int[2];
		int num, num2;
		
		for (int i = 0; i < n; i++) {
			num = 1;
			num2 = 1;
			for (int j = 1; j < n; j++) {
				if (board[i][j - 1] == board[i][j])
					num++;
				else {
					if (results[0] < num)
						results[0] = num;
					num = 1;
				}
				if (board[j - 1][i] == board[j][i])
					num2++;
				else {
					if (results[1] < num2)
						results[1] = num2;
					num2 = 1;
				}
			}
			if (results[0] < num)
				results[0] = num;
			if (results[1] < num2)
				results[1] = num2;
		}
		return (find_max(results[0], results[1]));
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		char [][]board = new char[n][n];
		int []results = new int[2];
		int answer = 0;
		
		for (int i = 0; i < n; i++) 
			board[i] = br.readLine().toCharArray();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (j < n - 1) {
					swap_col(board, i , j);
					results[0] = return_max_result(board, n);
					swap_col(board, i , j);
				}
				if (i < n - 1) {
					swap_row(board, i, j);
					results[1] = return_max_result(board, n);
					swap_row(board, i, j);
				}
				if (answer < find_max(results[0], results[1]))
					answer = find_max(results[0], results[1]);
			}
		}
		bw.write(Integer.toString(answer));
		bw.flush();
		br.close();
		bw.close();
	}
}
