#include <bits/stdc++.h>

using namespace std;

int main()
{
	int x,y,w,h;
	int min = 10000;
	int temp1, temp2;

	cin >> x >> y >> w >> h;

	
	if((w-x) < x){

		temp1 = w-x;
	}
	else{
		temp1 = x;
	}

	if((h-y) < y){

		temp2 = h-y;
	}

	else{

		temp2 = y;
	}

	if( temp1 < temp2) min = temp1;
	else min = temp2;

	cout << min;
	

	
	return 0;
}