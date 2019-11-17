import java.io.*;
import java.util.ArrayList;

class Arr_Stack{
	private int top;
	private int maxSize;
	private String[] stack_arr;
	
	public Arr_Stack(int maxSize) {
		
		this.maxSize = maxSize;
		this.stack_arr = new String[maxSize];
		this.top = -1;
	}
	
	public boolean full() {
		return (top == maxSize-1);
	}
	
	public boolean empty() {
		return (top == -1);
	}
	
	public void push(String item) {
		if(full()) throw new ArrayIndexOutOfBoundsException((top+1)+">="+maxSize);
		
		stack_arr[++top] = item;
	}
	
	public String peek() {
		if(empty()) throw new ArrayIndexOutOfBoundsException(top);
		
		return stack_arr[top];
	}
	
	public String pop() {
		String item = peek();
		
		top--;
		
		return item;
	}
}

class Method{
	public static int get_state(char ch)
	{
		int state = 0;
		switch(ch)
		{
		case '+':
		case '-':
			state = 3;
			break;
		case '*':
		case '/':
			state = 5;
			break;
		case '(':
			state = 1;
			break;
		
		default:
			break;
		}
		return state;
	}
}

public class SWEA1223 {
	
	
	public static void main(String args[]) throws Exception
	{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int test = 0, idx = 0;
		String str = new String();
		char ch;
		int state = 0, pre_state = 0;
		String[] post_pix;
		String[] temp;
		Arr_Stack operator1, operator2;
		Arr_Stack oper_rand;
		int n, result, len;
		
		
		while(test != 10)
		{
			test++;			
			n = Integer.parseInt(bf.readLine());
			operator1 = new Arr_Stack(n);
			operator2 = new Arr_Stack(n);
			oper_rand = new Arr_Stack(n);
			post_pix = new String[n];
			str = bf.readLine();
			temp = str.split("");
			
			for(int i = 0; i < temp.length; i++)
			{
				ch = str.charAt(i);
				if(ch >= 48 && ch <= 58)
				{
					post_pix[idx++] = temp[i];
				}
				
				else
				{
					
					if(operator1.empty())
					{
						operator1.push(temp[i]);
						switch(ch)
						{
						case '+':
						case '-':
							state = 3;
							break;
						case '*':
						case '/':
							state = 5;
							break;
						case '(':
							state = 1;
							break;
						
						default:
							break;
						}
					
					}
					
					else
					{
						
						
						if(pre_state >= state)
						{
							post_pix[idx++] = operator1.pop();
							operator1.push(temp[i]);
						}
						
						else if(pre_state < state)
						{
							operator1.push(temp[i]);
						}
						
						else if(ch == ')')
						{
							while(true)
							{
								str = operator1.pop();
								post_pix[idx++] = str;
								if(str.contentEquals(")")) break;
							}
						}
						System.out.println(state + " " + pre_state);
						
				
					}
					pre_state = state;
				}
				
				
			}
			while(!operator1.empty())
			{
				post_pix[idx++] = operator1.pop();
			}
			for(String item: post_pix )
				System.out.print(item+" ");
			
			
			
		}
		
	}
}
