# Loops 1 independent check: code_readback.py
# Open only when your instructor says.
# Work alone. No AI, no notes. Write your prediction on paper before you run anything.

# Read the code back one character at a time, in order: Q M 7
code = "QM7"
for letter in code:
    readback = ""
    readback = letter + " " + readback
print(readback)

# 1) PREDICT: Write the output on paper, with a "because".
#    Then run to check.
#
# 2) DEBUG: Make it do what the comment says.
#    Desired result:
#      Q M 7
#
# 3) ADJUST: The agent also wants the code read back in reverse, on a
#    second line, to double-check it. Build both read-backs in the SAME loop.
#    Desired result:
#      Q M 7
#      7 M Q
#
# 4) TEST: Change the code to "AB12". Predict the output on paper,
#    then run to check.
