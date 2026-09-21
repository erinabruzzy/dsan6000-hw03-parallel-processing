from datetime import datetime, timedelta
import sys
import joblib

### Start Q1.1 Code ###
def mat_vec_product(A: list[list[int]], b: list[int]) -> list[int]:
  n = len(A)
  # Construct a length-n vector of 0s, to be filled with the results
  c = [0 for _ in range(n)]
  # Your code here: Implement serial matrix-vector multiplication via a for loop
  # over the rows of the argument A
  for i in range(n):
        c[i] = sum(A[i][j] * b[j] for j in range(n))

  return c
### End Q1.1 Code ###

if __name__ == "__main__":
  start_time = datetime.now()
  A_rand = joblib.load("data/A_large.pkl")
  b_rand = joblib.load("data/b_large.pkl")
  result = mat_vec_product(A_rand, b_rand)
  end_time = datetime.now()
  elapsed_time = end_time - start_time
  sys.stderr.write(str(elapsed_time / timedelta(seconds=1)) + "\n")

