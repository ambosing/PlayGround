#!/bin/sh

for i in "/root" "/home" "/tmp" "/etc"
do
	str="python3 root.py "
	$str $i

done

exit 0
