#!/usr/bin/php

<?

 $file = popen("ls -aFl ~", "r");
 $read = fread($file, 2096);
# echo $read;
 $dir = 0;
 $file_num = 0;
 $result = "";
 $line = explode("\n", $read);
 $spl = " ";
 for($i=1; $i<count($line); $i++)
 {	 
	$word =explode(" ", $line[$i]);
	$word1 = array_unique($word);
	$word1 = array_values($word1);
	print_r($line[$i]. "\n");
#	print_r($word1);
	#	echo substr($word1[0], 0, 1). " ";
	if(substr($word1[0], 0, 1) == 'd')
		$dir++;
	else
		$file_num++;

#	$word3 = array_diff($word, array("  "));
	$word4 = array_filter($word);
	$word4 = array_values($word4);
	print_r($word4);
	$result = $result.$word4[8]. " ";
	$result = $result.$word4[5]. " ";
	$result = $result.$word4[0]. "\n";
	
 }

 echo $dir . " " . $file_num. "\n";
 echo $result;


 pclose($file);


?>
