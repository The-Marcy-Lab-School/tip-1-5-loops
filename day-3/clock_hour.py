# Loops 3 independent check: clock_hour.py
# Open only when your instructor says.
# Work alone. No AI, no notes. Write your prediction on paper before you run anything.

# Get the hour from the time: 10
clock = "10:45"
hour = ""
for ch in clock:
    hour = hour + ch
    if ch == ":":
        break
    print("Hour:", hour)

# 1) PREDICT: Write the output on paper, with a "because".
#    Then run to check.
#
# 2) DEBUG: Make it do what the comment says: print the hour once.
#    Desired result:
#      Hour: 10
#
# 3) ADJUST: Also print the character the loop stopped on, and how many
#    hour digits it read.
#    Desired result:
#      Hour: 10
#      Stopped at: :
#      Hour digits: 2
#
# 4) TEST: Change the time to "9:45". Predict the output on paper,
#    then run to check.
