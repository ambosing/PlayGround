#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer(2, 0);
    int zero_count = 0;
    for (int i = 0; i < lottos.size(); i++) 
    {
        if (lottos[i] == 0) {
            zero_count++;
            continue;
        }
            
        for (int j = 0; j < lottos.size(); j++) {
            if (lottos[i] == win_nums[j]) {
                answer[1]++;
                answer[0]++;
            }
        }
    }
    
    answer[0] = answer[0] == 0 ? 1 : answer[0];
    answer[1] = answer[1] == 0 ? 1 : answer[1];
    answer[0] += zero_count;
    answer[0] = answer[0] > 6 ? 6 : answer[0];
    answer[0] = 7 - answer[0];
    answer[1] = 7 - answer[1];
    
    return answer;
}