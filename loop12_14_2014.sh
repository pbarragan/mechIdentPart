for i in 0 1 2 3 # experiment type
do
    echo "$i"
    cp globalVars$i.h globalVars.h
    make
    for j in 0 1 2 3 # model type
    do
	echo "$i$j"
	for k in 0 1 2 3 4 5 6 7 8 9 # trial
	do
	    echo "$i$j$k"
	    ./testRealWorld $j 10 1 1 0
	done
    done
done