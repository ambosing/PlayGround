#include <bits/stdc++.h>

using namespace std;

int main()
{
	char cpt[501];
	int i;
	int idx[501];
	int count = 0;
	int temp = 0;

	
	while(1)
	{
		gets(cpt);

		for(i = 0; i < sizeof(cpt); i++){

			if(cpt[i] == '\0') break;
		}
		if((cpt[0] == 'E') && (cpt[1] == 'N') && (cpt[2] == 'D') && (cpt[3] == '\0'))
			break;

		for(int j = i-1; j >= 0; j--)
		{
			cout << cpt[j];
		}

		cout << endl;

	}

	
	return 0;
}