import java.util.ArrayList;
import java.util.Scanner;

public class test {
	public static void main(String args[])
	{
		int[] num = new int[10];
		Scanner sc = new Scanner(System.in);
		
		int temp = Integer.parseInt(sc.nextLine());
		
		String temp1 = sc.nextLine();
		String[] temp3 = temp1.split(" ");
		
		int temp2 = Integer.parseInt(temp3[1]);
		
		System.out.println(temp+ " " + temp3[0] + " " + temp2 + temp3[2]);
	}
}
