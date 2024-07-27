
#include <stdio.h> 
#include <stdlib.h> 
int main(int argc, char* argv[]) 
{ 
	int i, sum = 0; 
	for (i = 1; i < argc; i++) { 
		sum = sum + atoi(argv[i]); 
	} 
	printf("Sum of %d numbers is : %d\n", argc - 1, sum); 
	
	return 0; 
}
