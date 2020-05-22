import java.util.*;
import java.io.*;

class Main {
	static int find_max(int a, int b) {
		return a > b ? a : b;
	}
	
	static void swap_row(char [][]b, int i, int j) {
		char temp;
		
		temp = b[i + 1][j];
		b[i + 1][j] = b[i][j];
		b[i][j] = temp;
	}
	
	static void swap_col(char [][]b, int i, int j) {
		char temp;
		
		temp = b[i][j + 1];
		b[i][j + 1] = b[i][j];
		b[i][j] = temp;
	}
	
	static int return_max(char[][] b, int t) {
		int m;
		int cnt;
		
		m = 0;
		for (int i = 0; i < t; i++) {
			cnt = 1;
			for (int j = 1; j < t; j++) {
				if (b[i][j - 1] == b[i][j])
					cnt++;
				else {
					if (m < cnt)
						m = cnt;
					cnt = 1;
				}
			}
			if (m < cnt)
				m = cnt;
			cnt = 1;
			for (int j = 1; j < t; j++) {
				if (b[j - 1][i] == b[j][i])
					cnt++;
				else {
					if (m < cnt)
						m = cnt;
					cnt = 1;
				}
			}
			if (m < cnt)
				m = cnt;
		}
		return m;
	}
   
    public static void main(String args[]) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int t = Integer.parseInt(br.readLine());
    	char [][]board = new char[t][t];
    	int res;
    	
    	res = 0;
    	for (int i = 0; i < t; i++)
    		board[i] = br.readLine().toCharArray();
    	for (int i = 0; i < t; i++) {
    		for (int j = 0; j < t; j++) {
    			if (i < t - 1) {
    				swap_row(board, i, j);
        			res = find_max(return_max(board, t), res);
        			swap_row(board, i, j);
    			}
    			if (j < t - 1) {
    				swap_col(board, i, j);
        			res = find_max(return_max(board, t), res);
        			swap_col(board, i, j);
    			}
    		}
    	}
    	System.out.print(res);
    }
}