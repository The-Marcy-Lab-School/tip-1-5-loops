# Loops 1: pin_mask.py
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY -> MAKE.
# Edit this file as you go. If you fall behind, copy the current code from the screen.
#
# Working habit: Debugging with a plan

# ==================== PREDICT ====================
# Fill in EVERY "Prediction:" below before you run anything.

# Goal is to create a "mask" of "*" characters for our pin that is the same 
# length as the pin: "4821" --> "****"

pin = "4821"

masked = ""
for digit in pin:
    masked = masked + "*"
print("A:", masked)
# Prediction:
# Actual:
# Explanation:

for digit in pin:
    masked = ""
    masked = masked + "*"
print("B:", masked)
# Prediction:
# Actual:
# Explanation:

masked = ""
for digit in pin:
    masked = masked + "*"
    print("C:", masked)
# Prediction:
# Actual:
# Explanation:

# ==================== RUN ====================
# Now run the file. Fill in each "Actual:" and "Explanation:" above.
# Then answer these here:
# 1) What are the data types of pin, "", and digit?
# 2) No line mentions the number 4. Where did A's four stars come from?
# 3) The B loop also runs four times. Why only one star?
# 4) Why does C print four lines? Which one is the finished result?
# 5) Swap with a partner and compare. Can't agree? Ask an instructor.
#
# Help: still can't explain B's single star after running? Ask now.
#       Bring your prediction.

# ==================== INVESTIGATE ====================
# A) Trace the B loop on paper. Write masked after each line, every pass:
#    Pass 1: digit = ___   
#         after masked = "" --> masked = ___   
#         after masked = masked + "*" --> masked = ___
#    Pass 2: digit = ___   
#         after masked = "" --> masked = ___   
#         after masked = masked + "*" --> masked = ___
#    Pass 3: digit = ___   
#         after masked = "" --> masked = ___   
#         after masked = masked + "*" --> masked = ___
#    Pass 4: digit = ___   
#         after masked = "" --> masked = ___   
#         after masked = masked + "*" --> masked = ___
#    After the loop, print shows: ___
#    Self-check: your last line should match what B printed.
#
# B) A and B both contain `masked = masked + "*"`.
#    What is different about them, and why does it change the result?
#
# C) In the REPL, type each line. Predict the result first:
#    "" + "*"
#    " " + "*"
#    "" + ""
#    "*" + "4"
#    "4" + "*"
#    Write one sentence about empty text vs. a space,
#    and one about the order of a join.
#
# Now read: the ideas behind this snippet
#   1. Where a line sits decides how often it runs. Inside the body: once per
#      item. Outside: once, before the loop starts or after it ends.
#   2. A result builds across passes only if its starting value is set once,
#      before the loop, and each pass updates it from its current value.
#   3. Empty text is a real starting value that adds nothing when joined.
#      A space looks empty but is a character.
#   4. Joining is order-sensitive: the left side comes first. Adding to the
#      end keeps the order; adding to the front reverses it.
#
# Coding habit: set the start BEFORE the loop, update INSIDE, use the result
# AFTER. Choose the join order on purpose:
#   result = result + item   keeps the order
#   result = item + result   reverses it
#
# CHECKPOINT: show an instructor your trace (A) and your answer to B.

# ==================== MODIFY ====================
# Change the code ABOVE, one change at a time. Predict before every run.
# 1) Make the B line print   B: ****   by moving one line.
# 2) In your fixed B loop, change "*" to digit.
#    Why did it print what it did instead of ****?
# 3) Change   masked + digit   to   digit + masked.
#    Predict, then trace masked before the loop and after each pass:
#      before: ___  pass 1: ___  pass 2: ___  pass 3: ___  pass 4: ___
#    Run it to check your trace.
#
# Help: if exercise 3 surprises you and one more look doesn't explain it, ask.
