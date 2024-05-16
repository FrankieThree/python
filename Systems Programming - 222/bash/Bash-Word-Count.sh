#!/bin/bash
# Name: Norman Cook and Will Duncan
# Description: Bash script that replicates the behavior of wc -l command without
# 	actually using the wc command.

n=0
t=0
var=$#

if [ $# = '0' ]; then
	while read line; do
		# count a line
		((n++))
	done
	echo $n
elif [ var != '0' ] && [ $1 == '-h' ]; then
	echo "Usage: ./script.sh [ file [ file ... ] ]"
else
	for var in "$@"
	do
		while read -r LINE; do 
			(( n++ ));
			(( t++ ));	
		done < $var
		printf "%d " $n; printf "%s\n" $var
		n=$n-$n
	done
	printf "%d " $t; printf "total\n"
fi



