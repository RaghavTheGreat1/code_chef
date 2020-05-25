# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.

# Input:
# First line of input contains a single integer T, the number of test cases.
# Each test is a single line containing a string S composed of only lowercase English alphabet.
# Output:
# For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.
# Constraints:
# 1 ≤ T ≤ 100
# 2 ≤ |S| ≤ 1000, where |S| denotes the length of S
# Example:
# Input:
# 6
# gaga
# abcde
# rotor
# xyzxy
# abbaab
# ababc


# Output:
# YES
# NO
# YES
# YES
# NO
# NO

# Function to check if its lapindrome or not.
def lapindromeChecker(string):
    lettersSedt
    lengthOfString = len(string)//2
    if string[:lengthOfString] == string[lengthOfString:]:
        print("YES")
    else:
        print("NO")



# Number of inputs by bot
numberOfInputs = int(input())

# To store all the inputs
listOfStrings = []

# loops in range [0, numberOfInputs).
for i in range(numberOfInputs):
    # Appends numbers to the list of strings.
    listOfStrings.append(input())

# Loops in range [0, len(listOfStrings)).
for i in range(len(listOfStrings)):
    # Even check.
    if(len(listOfStrings[i]) % 2 == 0):
        lapindromeChecker(listOfStrings[i])
    # It's odd, obvio.
    else:
        # A way to remove the middle element of the string
        splittedString = listOfStrings[i][:(len(listOfStrings[i])+1)//2] + listOfStrings[i][(len(listOfStrings[i])+1)//2 + 1: ]
        lapindromeChecker(splittedString)
