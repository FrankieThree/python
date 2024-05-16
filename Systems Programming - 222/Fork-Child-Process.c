// Names: Norman Cook and Will Duncan
// Date: 2/16/19
// Description: Forks a child process and uses the exec function to list
// 	the contents of a directory specified at the command line.


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wait.h>

// MAIN //
int main(int argc, char *argv[]){
	
	// variables
	int ret;
	char cwd[FILENAME_MAX];
	int status;
	
	// no arguments are given
	if(argc < 2){
		printf("No directory specified.\n");

	} else{	
	
	// create a fork
	pid_t pid;
	pid = fork();
	
	// cannot change to directory 
	if (pid < 0){
		printf("Can't chdir to %s\n", argv[1]);
		exit(1);

	// changed the directory
	} else if (pid == 0 ){
		//child processs code
		// print the current directory and execution commands
		printf("Current working directory: %s\n", getcwd(cwd, sizeof(cwd)));
		printf("Executing ls %s --all -l --human-readable\n", argv[1]);
		int x = chdir(argv[1]);

		if(x == 0){
			
			// list current directory
			char* cmd[] = {"ls", argv[1], "-all", "-l", "--human-readable", NULL};
			ret = execvp("ls", cmd);
			ret = 0;
			exit(0);

		} else{

			// can not list current directory
			printf("Can't chdir to %s\n", argv[1]);
			ret = 1;
			exit(1);
		
		}

	} else {

		//return the exit status of the child
		wait(&status);
		if(status > 0){

			printf("Exit status = 1\n");
			exit(0);

		} else{

			printf("Exit status: 0\n");
			exit(0);
	
		}
	}
}
	
}
