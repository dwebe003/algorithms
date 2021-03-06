/* -----------------------------------------------------------------------------------
#
#  	"Write code to remove duplicate chars in a string withut using any 
#	 additional buffer. 
#		This program is if a new array of constant size is allowed."
#
#
#	This runs in O(n) time with O(n) space complexity. 
#
#	*Without using an additional data structure, it would take O(n^2) time.
#
 ----------------------------------------------------------------------------------- */
public class removedupsNOBUFF {

	public static void removeDups(String str)
	{
		/* 
		/	256 chosen to encapsulate all ASCII characters
		/  	A 'TRUE' under an index mean that character has
		/ 	been seen already and we can exit allUnique(..)
		*/
		
		System.out.println("Before: " + str);
		
		if(str == null || (str.length() <= 1) )
		{
			return;
		}
		
		int tail = 1;
		
		for(int i = 0; i < str.length(); i++)
		{
			int j;
			
			for(j = 0; j < tail; j++)
			{
				if(str.charAt(i) == str.charAt(j))
				{
					break;
				}
			}
			
			if(j == tail)
			{
				str.replace(str.charAt(tail), str.charAt(i));
				tail++;
			}
			
		}
		
		
		System.out.println("After: " + str);
		
		return;
	
	}
 
	public static void main(String[] args)
	{
	 	String str = "coffeee";
		
		removeDups(str);
		
		
	}
	
	
	
}
