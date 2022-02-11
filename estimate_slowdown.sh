rm benchmark.txt

# echo "n = 10"
# build/serial -s 1 -n 10 >> benchmark.txt
# echo "n = 100"
# build/serial -s 1 -n 100 >> benchmark.txt
# echo "n = 1000"
# build/serial -s 1 -n 1000 >> benchmark.txt
# echo "n = 10000"
# build/serial -s 1 -n 10000 >> benchmark.txt
# echo "n = 100000"
# build/serial -s 1 -n 100000 >> benchmark.txt

for N in 10 100 1000 10000 100000
do
    echo "n = $N"
    ~/hw2-1/build/serial -s 1 -n $N >> benchmark.txt
done

echo "*********************************"
cat benchmark.txt
echo "*********************************"
echo "estimating serial slowdown"
python get_slowdown.py