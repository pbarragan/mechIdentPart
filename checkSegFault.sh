for f in /home/barragan/data12112014new/data/2014_12_23/*
do
    #echo $f
    len=$(wc -l $f | cut -f1 -d' ')
    if (($len!=392906))
    then
	echo $f
    fi
done