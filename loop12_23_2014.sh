for j in 0 2 3 # model type
do
    echo "$j"
    for k in {0..29} # trial
    do
	echo "$j$k"
	./testRealWorld $j 10 1 1 0
	#sleep 1
    done
done
