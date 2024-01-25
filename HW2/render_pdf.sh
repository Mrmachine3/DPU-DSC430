#!/bin/bash

help (){
	printf "%s\n\n" "Usage example: $0 <markdown filename> <pdf filename>"
}

if [[ $# -eq 0 ]];
then
		help
        exit
fi

# Render pdf output from markdown file
pandoc $1 -o $2 -V geometry:margin=1in

