<?PHP
echo "Python Call tesing2</br>";

$command = escapeshellcmd('mypython.py');
$output = shell_exec($command);

echo $command;
echo $output;

echo "python output<br><br>";


echo shell_exec('python mypython.py arg1 arg2 arg3'); ?>




