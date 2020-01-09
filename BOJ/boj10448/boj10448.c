#include <stdio.h>

int main()
{
	int t = 0;
	int tri_num[1000] = { 0 };
	int tri_add = 2;
	int idx = 1,i, j, k;
	int sum = 0, ans;
	tri_num[0] = 1;
	
	while(1)
	{
		tri_num[idx] = tri_num[idx-1] + tri_add++;
		
		if(tri_num[idx] > 1000) break;
		
		idx++;
	}
	
	
	scanf("%d", &t);
	
	while ( t != 0)
	{
		t--;
		
		scanf("%d", &ans);
		
		for(i = 0; i < idx; i++)
		{
			for(j = i; j < idx; j++)
			{
				for( k = j; k < idx; k++) 
				{
					sum = tri_num[i] + tri_num[j] + tri_num[k];
					
					if(sum >= ans) break;
				}
				if(sum == ans) break;
			}
			if(sum == ans) break;	
		}
		if(sum == ans)
			printf("1\n");
		else 
			printf("0\n");
	}
	
}
