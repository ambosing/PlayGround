#include <bits/stdc++.h>

using namespace std;

int main()
{
	char s[101];
	int temp1[101];
	int result[26];
	int temp, i=0;

	cin >> s;

	int t_size = sizeof(result) / sizeof(int);
	int s_size = sizeof(s) / sizeof(char);
	//a = 97

	for(int j = 0; j < t_size; j++)
	{
		result[j] = -1;
	}

	while(s[i] != '\0')
	{
		temp1[i] = int(s[i])-97;
		temp = temp1[i];

		if(result[temp] == -1)
		{
		 	result[temp] = i;
		}

		i++;
	}
	
	

	for(int i = 0; i < t_size; i++)
	{
		
		cout << result[i] << " ";
	}

	return 0;
}