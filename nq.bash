echo "Usage: bash nq.bash two_sum_1"
mv src/*.py solved/src/.
mv tests/*.py solved/tests/.
echo "Starting $1"
touch src/$1.py
echo $'class Solution:' > src/$1.py
touch tests/test_$1.py
echo "from $1 import Solution" > tests/test_$1.py
echo $'\n\ndef test_with_ex1():\n' >> tests/test_$1.py
