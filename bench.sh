#!/bin/sh

for i in 1 2 3 4 8 16
do
	str="sysbench --threads="
	str1=" cpu run | grep 'events per second:' | awk '{print \$4}'"
	eval $str$i$str1
done

exit 0
