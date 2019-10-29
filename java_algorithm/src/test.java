import java.util.ArrayList;

public class test {
	public static void main(String args[])
	{
		String str = "123456";
		String str1 = str;
		StringBuffer str2 = new StringBuffer();
		
		str2.append(str);
		System.out.println(str2);
		str2.delete(0, 3);
		System.out.println(str2);
		str1 = str2.toString();
		System.out.println(str1);
	}
}
