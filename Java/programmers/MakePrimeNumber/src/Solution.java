import java.io.IOException;
import java.util.Arrays;

/*
3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하시오.

풀이
1. 3중 반복문으로 모든 경우 테스트
2. 그 수가 소수인지 확인
 */
public class Solution {
    public static void main(String args[]) throws IOException {
        int nums[] = {1, 2, 3, 4};
    }

    static int solution(int[] nums) {
        int answer = 0;
        boolean[] prime = new boolean[3001];
        int len = nums.length;

        // 소수 구하기
        for (int i = 2; i < 3001; i++) {
            if (prime[i])
                continue;
            for (int j = i + i; j < 3001; j += i) {
                prime[j] = true;
            }
        }

        for (int i = 0; i < len - 2; i++) {
            int val = 0;
            for (int j = i + 1; j < len - 1; j++)
                for (int k = j + 1; k < len; k++) {
                    val = nums[i] + nums[j] + nums[k];
                    if (!prime[val])
                        answer += 1;
                }

        }
        return answer;
    }
}
