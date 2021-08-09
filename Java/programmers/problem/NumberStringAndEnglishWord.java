/*
일부 자릿수를 영단어를 원래의 숫자로 바꾸는 문제

풀이
0. 딕셔너리를 숫자와 숫자 영단어를 매핑시키기
1. 숫자는 그대로 쓰기
2. 영어가 나왔을 경우, 시작 인덱스와 끝 인덱스를 가지고
슬라이스 만들기
2-1. 만든 슬라이스 영단어가 딕셔너리에 있는지 확인하기
2-2. 있으면, 인덱스를 끝 인덱스로 변경
2-3. 없으면, 끝 인덱스만 + 1
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class NumberStringAndEnglishWord {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        System.out.println(solution(s));

        br.close();
    }

    static int solution(String s) {
        StringBuilder answer = new StringBuilder();
        HashMap<String, String> map = new HashMap<>();
        map.put("zero", "0");
        map.put("one", "1");
        map.put("two", "2");
        map.put("three", "3");
        map.put("four", "4");
        map.put("five", "5");
        map.put("six", "6");
        map.put("seven", "7");
        map.put("eight", "8");
        map.put("nine", "9");
        int len = s.length();
        for (int i = 0; i < len; i++) {
            if (Character.isDigit(s.charAt(i))) {
                answer.append(s.charAt(i));
            } else {
                int start = i;
                int end = i + 1;
                while (end <= len) {
                    String subs = s.substring(start, end);
                    if (map.containsKey(subs)) {
                        answer.append(map.get(subs));
                        break;
                    }
                    end += 1;
                }
                i = end - 1;
            }
        }

        return Integer.parseInt(answer.toString());
    }
}
