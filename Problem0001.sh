#! /bin/bash
# https://projecteuler.net/problem=1

LIMIT=$1

if [ -z "$LIMIT" ]
then
	echo "please provide a limit argument"
	exit
fi

echo "Limit is $LIMIT"

SUMCOUNT=0

while [ $LIMIT -gt 0 ]
do
	if [ $(( $LIMIT % 3)) -eq 0 ] || [ $(( $LIMIT % 5 )) -eq 0 ]
	then
		(( SUMCOUNT=SUMCOUNT+LIMIT ))
	fi
	(( LIMIT-- ))
done

echo "Sum of all values is $SUMCOUNT"
	 
