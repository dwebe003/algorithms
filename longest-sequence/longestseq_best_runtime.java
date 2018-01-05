
import java.util.*;

public class longestseq_best_runtime {

	public static int longestConsecutive(int[] nums)
	{
		// Create new HashSet and add every num in nums to it
		Set<Integer> num_set = new HashSet<Integer>();
		for(int num : nums)
		{
			num_set.add(num);
		}
		
		int longestStreak = 0;
		
		// Iterate through HashSet until we find a number that has no
		// preceding number (i.e. number n-1 not contained in set).
		// Once that smallest number (in that sequence) is found,
		// keep checking if the next number exists in the set.
		for(int num : num_set)
		{
			if(!num_set.contains(num-1))
			{
				int currentNum = num;
				int currentStreak = 1;
				
				while(num_set.contains(currentNum+1))
				{
					currentNum += 1;
					currentStreak += 1;
				}
				
				longestStreak = Math.max(longestStreak, currentStreak);
			}
		}
		
		return longestStreak;
	
	}
 
	public static void main(String[] args)
	{
	 	int[] nums = new int[] {7, 3, 9, 1, -1, 4, 5 ,0, 8, 6, -2};
		
		
		int x;
		x = longestConsecutive(nums);
		
		System.out.println("longest streak is: " + x);
		
	}
	
	
	
}

