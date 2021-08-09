/*
놀이기구를 N번 이용하면, 이용료의 N배를 받는다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지
return하도록 solution 함수를 완성하라

풀이
1. 마지막 항을 구한다. last = price * count
2. 수열의 합을 구한다. Sn = (count * (price + last)) / 2
3. answer = money - sn;
 */

public class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        long last = price * count;
        long sn = (count * (price + last)) / 2;
        if (money > sn)
            return 0;
        answer = Math.abs(money - sn);
        return answer;
    }
}
