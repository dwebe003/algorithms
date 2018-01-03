/* -----------------------------------------------------------------------------------
#
#  	"Write code to reverse a C-style string. ("abcd" is 5 chars with \0 null char)"
#
#
------------------------------------------------------------------------------------*/

#include <iostream>

using namespace std;


void reverseCstring(char *str)
{
	cout << "Before: " << str << endl;
	
	char *begin = str;
	char *end = str;
	char temp; 
	
	if(str) 
	{
		//gets to end of c-string
		while(*end)
		{
			end++;
		}
		
		end--; //to avoid null char
		
		while(str < end)
		{
			//swap and increment pointers
			temp = *str;
			*str = *end;
			*end = temp;
			end--;
			str++;
		}
	}
	
	
	cout << "After: " << begin << endl;

}
 
int main()
{
	char string[] = "uncle sam is ridiculous";
	char *str = string;
	
	reverseCstring(str);
	
	return 0;
	
}
