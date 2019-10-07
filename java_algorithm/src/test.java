
public class test {
	public static void main(String args[])
	{
		StringBuffer temp = new StringBuffer();
		String str = new String();
		String str2 = new String();
		
		temp.append('a');
		temp.append('b');
		temp.append('c');
		
		str = temp.toString();
		temp = temp.reverse();
		str2 = temp.toString();
		
		System.out.println(str.hashCode());
		System.out.println(temp.hashCode());
		System.out.println(str2.hashCode());
	}
}
