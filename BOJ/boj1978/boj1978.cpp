#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n,j;
	int is_prm[100];
	int prm_count = 0;


	cin >> n;

	for(int i = 0; i < n; i++){

		cin >> is_prm[i];

		if(is_prm[i] == 2){
			prm_count++;
			continue;
		}

		for( j = 2; j < is_prm[i]; j++){

			if(is_prm[i] % j == 0) break;

		}
		
		if(j == is_prm[i]) prm_count++;	


	}

	cout << prm_count++;

	
	return 0;
}