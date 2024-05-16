/**
 * Name: Norman Cook and Will Duncan
 * Description: Converts time in minutes to time in hours of user entered values
 */
#include <stdio.h>
#include <string.h>

// Questtion 4
int main(void)
{
 	int iMinutes, oMinutes, hours;
	printf("Enter the number of minutes to convert: \n");
	scanf("%i", &iMinutes);
	hours = iMinutes / 60;
	oMinutes = iMinutes % 60;
	printf("%i minutes = %i hours, %i minutes\n", iMinutes, hours, oMinutes);
	while(iMinutes > 0){
	printf("Enter next minutes value (0 to quit): \n");
	scanf("%i", &iMinutes);
	hours = iMinutes / 60;
	oMinutes = iMinutes % 60;
	printf("%i minutes = %i hours, %i minutes\n", iMinutes, hours, oMinutes);
    return 0;
}