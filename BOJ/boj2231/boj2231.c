#include <stdio.h>

int main()
{
	int n = 0;
	int i = 0, j = 0;
	int sum = 0, temp, part = 0;
	int div_sum = 0;
	
	scanf("%d", &n);
	
	for ( i = 1; i < 1000000; i++)
	{
		temp = i;
	
		while(1)
		{
			part = temp % 10;
			sum += part;
			temp = temp / 10;
			if( temp == 0 ) break;
		}
		
		
		div_sum = i + sum;
		
		if(div_sum == n) break;
		
		div_sum = 0;
		sum = 0;
	}
	if(i == 1000000) printf("0");
	else printf("%d", i);
	
	return 0;
}
