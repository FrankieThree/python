/**
 * Name: Norman Cook and Will Duncan
 * Description: Requests the download speed in Mbs and the file size in MB.
 * 	Returns the download speed, file size, and download time.
 */
#include <stdio.h>
#include <string.h>

// Questtion 3
int main(void)
{
 	float speed;
	float size;
	float time;
	printf("Enter the download speed in megabits per second: \n");
	scanf("%f", &speed);
	printf("Enter the file size in megabytes: \n");
	scanf("%f", &size);
	time = size * 8 / speed;
	printf("At %.2f megabits per second, a file of %.2f downloads in %.2f seconds.", speed, size, time);
    return 0 ;
}