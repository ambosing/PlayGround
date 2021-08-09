/*
absolutes는 정수
sign이 참이면 양수, sign이 거짓이면 음수

풀이
1. absolutes를 하나씩 뽑는다.
2. sign이 거짓이면 음수로 더해준다.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static void main(String args[]) throws IOException {
        int[] absolutes = {4,7,12};
        boolean[] signs = {true,false,true};

        System.out.println(solution(absolutes, signs));
    }

    static int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int len = absolutes.length;

        for (int i = 0; i < len; i++) {
            int val = absolutes[i];
            if (!signs[i])
                val *= -1;
            answer += val;
        }

        return answer;
    }
}
