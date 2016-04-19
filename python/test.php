<?PHP
#echo "Python Call tesing2</br>";

// $command = escapeshellcmd('mypython.py');
// $output = shell_exec($command);

// echo $command;
// echo $output;

// echo "python output<br><br>";


// echo shell_exec('python mypython.py arg1 arg2 arg3'); 

//Defected image name array
$defeceted = array("Peter", "Joe", "Glenn", "Cleveland");

//Name of the image file
$name = "Peter";

// 1 - Englsih 
// 2 - Sinhala
$language = '2';


$descriptionEnglish = "true/defeceted/English Description ......ascasas..asd.";
$descriptionSinhala = "true/ආසාදිතයි /වෙබ් මත ඕනෑම තැනක, ඔබ තෝරන භාෂාවෙන් ටයිප් කිරීම Google ආදාන මෙවලම් වලින් පහසු කරවයි. තවත් දැනගන්න
එය උත්සාහ කර බැලීමට, පහත දැක්වෙන ඔබේ භාෂාව සහ ආදාන මෙවලම් තෝරා ටයිප් කිරීම අරඹන්න.";





if (in_array($name, $defeceted)){
  	if($language == '1'){
  		echo $descriptionEnglish;
  	}else{
  		echo $descriptionSinhala;
  	}
}
else{
	if($language == '1'){
  		echo "false/Not Defeceted";
  	}else{
  		echo "false/නිරෝගී ";
  	}
}



?>




