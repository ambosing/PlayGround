#include <stdio.h>

int main()
{
	int n, m;
	int board[50][50] = {0};
	int i,j,k,l;
	char temp, start;
	int cnt, min;
	scanf("%d %d", &n, &m);

	for(i = 0; i < m-8; i++)
	{
		for(j = 0; j < n-8; j++)
		{
			for(k = i; k < i+8; k++)
			{
				if(k%2 == 0) start = 'W';
				else start = 'B';
				
				cnt = 0;
				for(l = j+1; l < j+8; l++)
				{
					if()
					if( temp == 'W' && temp == board[k][l]) cnt++;
					else if (temp == 'B' && temp == board[k][l]) cnt++;
	
				}
			}
			
		}
	}
}
