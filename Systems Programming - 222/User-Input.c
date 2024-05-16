// Name: Norman Cook and Will Duncan
// Date: 2/16/19
// Description: Repeatedly prompts the user for input and parses the input
// 	to provide output that describes the input specified.


#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// MAIN
int main () {
	do{
	// variables
	char str[256];
	char *token;
	int n = 0;

	// prompt for  user input
	printf("$ ");
	fgets(str, 256, stdin);	
	// grab the first character from the user
	token = strtok(str, " ");
	// exit the loop when exit is inputted
	
	if(strcmp(token, "exit") == 0){
		exit(0);
		return(0);
	}

	// print the received input
	printf("Line read: %s\n", str);
	printf("Token(s): \n");
	
	// until the token is empty
	while (token != NULL){
		// print the current command
		printf("%s \n", token);
		n++;
		token = strtok(NULL, " ");
		
	}

	// return the number of commands read
	printf("%d token(s) read\n", n);
	} while(1);
	return(0);
}
