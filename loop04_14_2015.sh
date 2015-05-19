for j in 4 # model type
do
    echo "$j"
    for k in {0..49} # trial
    do
	echo "$j$k"
	./testRealWorld $j 10 1 1 0
    done
done