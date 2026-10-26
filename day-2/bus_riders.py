# Loops 2 independent check: bus_riders.py
# Open only when your instructor says.
# Work alone. No AI, no notes. Write your prediction on paper before you run anything.

# After each stop, show how many riders are on board: 4, 8, 12
riders = 0
for stop in range(3):
    print("On board:", riders)
    riders = riders + 4
print("On board:", riders)

# 1) PREDICT: Write the output on paper, with a "because".
#    Then run to check.
#
# 2) DEBUG: Make it do what the comment says.
#    Desired result:
#      On board: 4
#      On board: 8
#      On board: 12
#
# 3) ADJUST: Show each stop as the count before and after boarding.
#    After the loop, print the final count.
#    Desired result:
#      0 -> 4
#      4 -> 8
#      8 -> 12
#      Final: 12
#
# 4) TEST: 5 riders now board at each stop. Predict the output on paper,
#    then run to check.
