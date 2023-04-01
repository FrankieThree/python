/**
 * Name: Norman Cook and Will Duncan
 * Description: Requests for the user's name and prints the name in
 * 	in three different formats.
 */
#include <stdio.h>
#include <string.h>

// Questtion 2
int main(void)
{
	printf("What is your name?\n");
	char name[25];
	scanf("%s", name);
	printf("\"%s\"\n",  name);
	printf("\"%25s\"\n",  name);
	printf("\"%-25s\"\n", name);
    return 0;
}