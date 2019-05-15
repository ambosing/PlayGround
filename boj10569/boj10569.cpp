#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	int v, e;

	cin >> t;

	while( t != 0)
	{
		cin >> v >> e;

		cout << e-v+2 << endl;

		t--;
	}

	return 0;
}