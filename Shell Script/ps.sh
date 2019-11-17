#!/bin/sh

for i in 1 2 3 4 5 6 7 8 9 10
do
	str="sudo ps -u | grep bash | head -n 1 | awk '{print \$3}'"
	str1="sleep 1"
	eval $str
	$str1
done
