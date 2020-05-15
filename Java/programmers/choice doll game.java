import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int move_len = moves.length;
        int board_len = board.length;
        int lst_idx = -1;
        int idx = 0;
        ArrayList<Integer> lst = new ArrayList<Integer>();
        
        for (int i = 0; i < move_len; i++) {
            for (int j = 0; j < board_len; j++) {
                idx = moves[i] - 1;
                if (board[j][idx] != 0) {
                    lst_idx += 1;
                    lst.add(lst_idx, board[j][idx]);
                    board[j][idx] = 0;
                    if (lst_idx >= 1 && lst.get(lst_idx) == lst.get(lst_idx - 1)) {
                        lst.remove(lst_idx--);
                        lst.remove(lst_idx--);
                        answer += 2;
                    }
                    break;
                }
            }
        }
        return answer;
    }
}