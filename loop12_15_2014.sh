for j in 0 1 2 3 # model type
do
    echo "$j"
    for k in 0 1 2 3 4 5 6 7 8 9 # trial
    do
	echo "$j$k"
	./testRealWorld $j 10 1 1 0
	#sleep 1
    done
done
