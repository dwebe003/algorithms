/* -----------------------------------------------------------------------------------
#
#  	"Implement an algorithm to determine if a string has all unique characters.
#	 What if you cannot use an additional data structure*?"
#
#
#	This runs in O(n) time with O(n) space complexity. 
#
#	*Without using an additional data structure, it would take O(n^2) time to
#	 select each char and compare it against every other char in the string. 
#    Just like selection sort.
#
 ----------------------------------------------------------------------------------- */
public class allunique {

	public static boolean allUnique(String str)
	{
		/* 
		/	256 chosen to encapsulate all ASCII characters
		/  	A 'TRUE' under an index mean that character has
		/ 	been seen already and we can exit allUnique(..)
		*/
		boolean[] char_set = new boolean[256];
		
		for(int i = 0; i < str.length(); i++)
		{
			int value = str.charAt(i);
			
			if(char_set[value])
			{
				return false;
			}
			else
			{
				char_set[value] = true;
			}
		}
		return true;
	
	}
 
	public static void main(String[] args)
	{
	 	String str = "uncle sam";
		
		if(allUnique(str))
		{
			System.out.println("'" + str + "'" + " has all unique chars.");
		}
		else
		{
			System.out.println("'" + str + "'" + " does NOT have all unique chars.");

		}
		
		
	}
	
	
	
}
