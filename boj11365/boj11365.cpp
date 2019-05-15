#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	int r;
	char s[21];
	char result[2000];
	int res_size;
	int s_size;
	int j = 0;

	cin >> t;

	while(t != 0){
		cin >> r >> s;

		s_size = sizeof(s);


		for(j = 0; j < s_size; j++ ){

			if(s[j] == '\0') break;

		}

		res_size = 0;

		for(int i = 0; i < j; i++){

			for(int k = 0; k < r; k++){

				result[res_size] = s[i];

				res_size++;
			}
		}

		for(int i = 0; i < res_size; i++){

			cout << result[i];
		}

		cout << endl;



		t--;
	}

	return 0;
}