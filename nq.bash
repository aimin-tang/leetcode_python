echo "Usage bash nq.bash two_sum 1"
mv src/*.py src/solved/.
mv tests/*.py tests/solved/.
echo "Starting $1 $2"
touch src/$1_$2.py
echo $'class Solution:' > src/$1_$2.py
touch tests/test_$1_$2.py
echo "from $1_$2 import Solution" > tests/test_$1_$2.py
echo $'\n\n\ndef test_with_ex1():' >> tests/test_$1_$2.py
