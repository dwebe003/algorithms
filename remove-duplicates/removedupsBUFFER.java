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
public class removedupsBUFFER {

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
		
		boolean[] char_set = new boolean[256];
		
		for(int i = 0; i < str.length(); i++)
		{
			int value = str.charAt(i);
			
			if(char_set[value])
			{
				String result = str.substring(0, i) + str.substring(i + 1);
				str = result;
				i--;
			}
			else
			{
				char_set[value] = true;
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
