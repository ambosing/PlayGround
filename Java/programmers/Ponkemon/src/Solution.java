/*
폰켓몬은 N/2마리 가질 수 있다.
가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아 그 때의 폰켓몬 종류 번호의 개수를 구하라

풀이
1. 폰켓몬의 종류가 몇 개인지 세야한다.
2. 종류의 개수와 N/2중 둘 중 작은 것을 반환
 */

import java.util.HashMap;

public class Solution {
    public static void main(String[] args) {
        int nums[] = {3,1,2,3};
        System.out.println(solution(nums));
    }

    static int solution(int[] nums) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, 1);
        }
        answer = Math.min(map.size(), nums.length / 2);
        return answer;
    }
}
