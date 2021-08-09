import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;

class Descendings implements Comparator<Integer> {
    public int compare(Integer a, Integer b) {
        return b.compareTo(a);
    }
}

class Ascendings implements Comparator<Integer> {
    public int compare(Integer a, Integer b) {
        return a.compareTo(b);
    }
}

class Solution1 {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int idx;
        int ans_idx = -1;
        ArrayList<Integer> lst;
        
        for (int i = 0; i < commands.length; i++) {
            lst = new ArrayList<Integer>();
            idx = -1;
            for (int j = commands[i][0] - 1; j <= commands[i][1] - 1; j++)
                lst.add(++idx, array[j]);
            Collections.sort(lst, new Ascending());
            answer[++ans_idx] = lst.get(commands[i][2] - 1);
        }
        return answer;
    }
}