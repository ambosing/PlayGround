/*

 */

import java.util.Arrays;

public class Solution {
    public String solution(int[][] scores) {
        StringBuilder answer = new StringBuilder();

        int len = scores.length;
        int sum[] = new int[len];
        int cnt[] = new int[len];
        Arrays.fill(cnt, len);
        for (int i = 0; i < len; i++) {
            int[] max = {-1, -2, -1, 1};
            int[] min = {-1, -2, 200, 1};
            for (int j = 0; j < len; j++) {
                if (max[2] < scores[j][i]) {
                    max[0] = i;
                    max[1] = j;
                    max[2] = scores[j][i];
                    max[3] = 1;
                } else if (max[2] == scores[j][i])
                    max[3] += 1;
                if (min[2] > scores[j][i]) {
                    min[0] = i;
                    min[1] = j;
                    min[2] = scores[j][i];
                    min[3] = 1;
                } else if (min[2] == scores[j][i])
                    min[3] += 1;
                sum[i] += scores[j][i];
            }
            if (max[0] == max[1] && max[3] == 1) {
                sum[max[0]] -= max[2];
                cnt[max[0]] -= 1;
            }
            if (min[0] == min[1] && min[3] == 1) {
                sum[min[0]] -= min[2];
                cnt[min[0]] -= 1;
            }
            int avg = sum[i] / cnt[i];
            if (avg >= 90)
                answer.append("A");
            else if (avg >= 80)
                answer.append("B");
            else if (avg >= 70)
                answer.append("C");
            else if (avg >= 50)
                answer.append("D");
            else
                answer.append("F");
        }

        return answer.toString();
    }
}
