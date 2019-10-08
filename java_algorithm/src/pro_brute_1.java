
public class pro_brute_1 {
	class Solution {
	    public int[] solution(int[] answers) {
	        int[] answer = {};
	        int[] cnt = {0, 0, 0};
	        int[] num1 = {1,2,3,4,5};
	        int[] num2 = {2,1,2,3,2,4,2,5};
	        int[] num3 = {3,3,1,1,2,2,4,4,5,5};
	        int max = -1;
	        int k = 0;
	        
	        for(int i = 0; i < answers.length; i++)
	        {
	            if(answers[i] == num1[i%5])
	                cnt[0]++;
	            if(answers[i] == num2[i%8])
	            	cnt[1]++;
	            if(answers[i] == num3[i%10])
	            	cnt[2]++;
	        }
	        
	        for(int i = 0; i < 3; i++)
	        	if(max <= cnt[i])
	        		max = cnt[i];
	        
	        for(int i =0; i < 3; i++)
	        	if(max == cnt[i])
	        		k++;
	        
	        answer = new int[k];
	        k =0;
	        
	        for(int i = 0; i < 3; i++)
	        	if(max == cnt[i]) {
	        		answer[k] = i+1;
	        		k++;
	        	}
	        		
	           
	        
	        return answer;
	    }
	}
}
