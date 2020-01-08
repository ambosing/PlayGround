#include <stdio.h>

void swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
	
}

void quicksort(int left, int right, int* data)
{
	int pivot = left;
	int j = left;
	int i = left+1;
	
	if(left < right){
		for(; i <= right; i++)
		{
			if( data[i] < data[pivot])
			{
				j++;
				swap(&data[j], &data[i]);
			}
		}
		swap(&data[left], &data[j]);
		pivot = j;
		
		quicksort(left, pivot-1, data);
		quicksort(pivot+1, right, data);
	}
}


int main()
{
	int arr[9] = {0};
	int fake1 = 0, fake2 = 1;
	int i,j, cnt = 0;
	int sum = 0;
	int real[7] = {0};
	
	for ( i = 0; i < 9; i++)
		scanf("%d", &arr[i]);
		
	for(i = 0; i < 36; i++)
	{
		for (j = 0; j < 9; j++)
		{
			if(fake1 == j || fake2 == j) continue;
			
			sum += arr[j];
		}
		if( sum == 100) break;
		sum = 0;
		fake2++;
		if(fake2 == 9)
		{
			fake1++;
			fake2 = fake1 + 1;
		}
		
	}
	
	for(i = 0; i < 9; i++)
	{
		if( i == fake1 || i == fake2) continue;
		
		real[cnt++] = arr[i];  
	}
	
	quicksort(0, 6, real);
	
	for( i = 0; i < 7; i++) printf("%d\n", real[i]);
	
		
}
