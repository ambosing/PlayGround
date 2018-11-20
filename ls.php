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
 for($i=1; $i<count($line)-1; $i++)
 {	 

	$word1 = preg_split("/[\s]+/",$line[$i]); 
	if(substr($word1[8], 0, 2) == './')
	{
		
			$dir++;
	}
	elseif(substr($word1[8], 0, 3) == '../')
	{
		$dir++;
	}
	else{
		if(substr($word1[0], 0, 1) == 'd')
			$dir++;
		else
			$file_num++;
		echo "$word1[8] $word1[4] $word1[0]\n";
	}

	

	
 }

 echo $dir . " " . $file_num. "\n";
 echo $result;


 pclose($file);


?>
