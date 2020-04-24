#include <stdio.h>

void swap(char a[][51], int row1, int col1, int row2, int col2)
{
	char t = a[row1][col1];
	a[row1][col1] = a[row2][col2];
	a[row2][col2] = t;
}

int main()
{
	int n = 0;
	char candy[51][51] = {0};
	int i, j, k, l;
	int cnt_row = 0, cnt_col = 0, max = 0; 
	
	scanf("%d", &n);
	
	for (i = 0; i < n; i++)
		for(j = 0; j < n; j++)
			scanf("%c", &candy[i][j]);
	
	for (i = 0; i < n; i++)
	{	
		for(j = 0; j < n-1; j++)
		{
			swap(candy, i, j, i, j+1);
			if(i == 0 && j == 0)
				{
				for (k = 0; k < n; k++)
				{
					for(l = 0; l < n; l++)
						printf("%c", candy[k][l]);
					printf("\n");
				}	
				}
				
			for (k = 0; k < n; k++)
			{
				cnt_row = 1, cnt_col = 1;
				for (l = 0; l < n-1; l++)
				{
					if(candy[k][l] == candy[k][l+1]){
						cnt_col++;
						if ( max < cnt_col) max = cnt_col;
					}
						
					else
						cnt_col = 1;
					
					if(candy[l][k] == candy[l+1][k]){
						cnt_row++;
						if ( max < cnt_row) max = cnt_row;
					}
					else
						cnt_row = 1;
							
				}
				
			}
			swap(candy, i, j, i, j+1);
			
			
			swap(candy, j, i, j+1, i);
			
			
			for (k = 0; k < n; k++)
			{
				cnt_row = 1, cnt_col = 1;
				for (l = 0; l < n-1; l++)
				{
					if(candy[k][l] == candy[k][l+1])
					{
						cnt_col++;
						if ( max < cnt_col) max = cnt_col;
					}
					else
						cnt_col = 1;
					
					if(candy[l][k] == candy[l+1][k]){
						cnt_row++;
						if ( max < cnt_row) max = cnt_row;
					}
					else
						cnt_row = 1;
							
				}
				
			}
			swap(candy, j, i, j+1, i);
		}
	}
		
	printf("%d", max);
	
	return 0;
}

