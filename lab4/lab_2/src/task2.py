import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

file_path1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/input.txt"))
file_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../txtf/output.txt"))

from lab4.utils import read_input_file2, write_output_file

def count_ways_to_form_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n + 1):  
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n-1]

def process_input_and_output():
    s = read_input_file2(file_path1)
    result = count_ways_to_form_palindrome(s)
    write_output_file(file_path2, str(result))

process_input_and_output()

