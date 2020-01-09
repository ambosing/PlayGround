#include <stdio.h>

int main()
{
	int t = 0;
	int arr[101][3] = { 0 };
	int i,j,k = 0;
	int a[3] = { 0 }, b[3] = { 0 }; 
	int ans = 0, cnt;
	int st, ba;
	
	scanf("%d", &t);
	
	
	for(i = 0; i < t; i++)
		scanf("%d %d %d", &arr[i][0], &arr[i][1], &arr[i][2]);
	
	for(i = 123; i <= 987; i++ )
	{
		a[0] = i/100;
		a[1] = (i/10)%10;
		a[2] = i%10;
		if(a[1] == 0 || a[2] == 0 || a[0] == a[1] || a[1] == a[2] || a[0] == a[2])
			continue;
		cnt = 0;
		
		for(j = 0; j < t; j++)
		{
			b[0] = arr[j][0]/100;
			b[1] = (arr[j][0]/10)%10;
			b[2] = arr[j][0]%10;
			
			st = 0, ba = 0;
			
			for(k = 0; k < 3; k++)
			{
				if(a[k] == b[k]) st++;
				if(a[k] == b[(k+1)%3] || a[k] == b[(k+2)%3]) ba++;
			}
			
			if (st == arr[j][1] && ba == arr[j][2]) cnt++;
		}
		if( cnt == t ) ans++;
	}
	printf("%d", ans);
	 
	return 0;
}
