
public class anagram {

	public static boolean isAnagram(String str1, String str2)
	{
		// initial check of length. It is obvious that two strings of
		// unequal length cannot be anagrams.
		if(str1.length() != str2.length()) 
		{
			return false;
		}

		// initialize an array of char values for each string.
		// we will iterate through each string and increment
		// whatever value is seen
		int[] hits1 = new int[256];
		int[] hits2 = new int[256];
		
		// actual iterations
		for(int i = 0; i < str1.length(); i++)
		{
			int x = str1.charAt(i);
			int y = str2.charAt(i);
			
			hits1[x]++;
			hits2[y]++;

		}
		
		// looking for a char value that does not equal its corresponding
		// value in the other string. if none found then AWESOME-- they're anagrams.
		for(int j = 0; j < 256; j++)
		{
			if(hits1[j] != hits2[j]) 
			{
				return false;
			}
		}
		
		return true;
	
	}
 
	public static void main(String[] args)
	{
	 	String str1 = "uncle sam";
		String str2 = "samen luc";
		
		if(isAnagram(str1, str2))
		{
			System.out.println("'" + str1 + "'" + " and " + "'" + str2 + "' are anagrams.");
		}
		else
		{
			System.out.println("'" + str1 + "'" + " and " + "'" + str2 + "' are NOT anagrams.");

		}
		
		
	}
	
	
	
}
