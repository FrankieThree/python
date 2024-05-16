/**
 * Name: Norman Cook and Will Duncan
 * Description: Requests the user for their age in years and then displays
 * 	the equivalent number of seconds.
 */
#include <stdio.h>
#include <string.h>

//Question 1
int main(void)
{
	int age;
	printf("Enter your age in years: ");
       	scanf("%i", &age);
	double secondsInYear = 3.156e+07;
	double answer = (double)age * secondsInYear;
	printf("Your age is %E seconds. \n ", answer);

    return 0;
}