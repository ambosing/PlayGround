import java.util.ArrayList;

public class test {
	public static void main(String args[])
	{
		String[] str = new String[10];
		int[] arr = new int[100];
		ArrayList<Integer> arrlist = new ArrayList<Integer>();
		
		arrlist.add(0, 1);
		arrlist.add(1, 3);
		arrlist.add(3, 87);
		System.out.println(arrlist.get(1)+" "+arrlist.get(3));
		
		System.out.println(arr[0]+" "+arr[1]);
		
		System.out.println(str.length);
	}
}
