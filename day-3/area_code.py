# Loops 3: area_code.py
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY -> MAKE.
# Edit this file as you go. If you fall behind, copy the current code from the screen.
#
# Working habit: If I try this, I expect ... / That tells me ...

# ==================== PREDICT ====================
# Fill in EVERY "Prediction:" below before you run anything.

phone = "718-555-0142"

# Data types of these values: phone, area, ch

area = ""
for ch in phone:
    if ch == "-":
        break
    area = area + ch
print("A:", area)
# Prediction:
# Actual:
# Explanation:

area = ""
for ch in phone:
    area = area + ch
    if ch == "-":
        break
print("B:", area)
# Prediction:
# Actual:
# Explanation:

# ==================== RUN ====================
# Now run the file. Fill in each "Actual:" and "Explanation:" above.
# Then answer these here:
# 1) What are the data types of phone, area, and ch?
# 2) The phone number has more digits after the dash.
#    Why were they never added in A?
# 3) B has the same lines as A. Why is the dash included?
# 4) The program kept going after each break. How can you tell?
# 5) Swap with a partner and compare. Can't agree? Ask an instructor.
#
# Help: predicted "718-" for A and can't explain the difference after
#       running? Ask now.

# ==================== INVESTIGATE ====================
# A) Trace the A loop on paper. If a line never runs, write "never runs".
#    Pass 1: ch = ___   ch == "-" is ___   area after the update: ___
#    Pass 2: ch = ___   ch == "-" is ___   area after the update: ___
#    Pass 3: ch = ___   ch == "-" is ___   area after the update: ___
#    Pass 4: ch = ___   ch == "-" is ___   area after the update: ___
#    After the loop, print shows: ___
#    Self-check: your last line should match what A printed.
#
# B) Both loops stop on the same pass. Why does B keep the dash when
#    A doesn't?
#
# C) In the REPL, type each loop, then press Enter on the blank ... line.
#    Predict each result first:
#      for ch in "718-555":
#          if ch == "-":
#              break
#
#      ch
#      for ch in "718":
#          if ch == "-":
#              break
#
#      ch
#    What does the loop's name hold after a stop? With no stop?
#
# Now read: the ideas behind this snippet
#   1. An early exit stops the whole loop the moment it runs. The rest of
#      that pass is skipped, no more passes start, and the program carries
#      on with the first line after the loop.
#   2. A stop under a decision runs only on the pass where the condition
#      is true. Until then, every pass runs normally.
#   3. Whether the stopping pass's work counts depends on whether that
#      work comes before or after the check.
#   4. After an early exit, names hold the values from the passes that ran,
#      and the loop's name holds the item it stopped on.
#
# Coding habit: put the check where you mean it. Check BEFORE the update
# when the stopping item shouldn't count, AFTER the update when it should.
#
# CHECKPOINT: show an instructor your trace (A) and your answer to B.

# ==================== MODIFY ====================
# Change the code ABOVE, one change at a time.
# Before each run, say: "If I try this, I expect ..."
# After each run, finish: "That tells me ..."
# 1) Make the B line print   B: 718   without adding or removing any lines.
# 2) In your fixed B loop, change "-" to "5".
#    Why did it print what it did instead of 718?
# 3) Add   print("Stopped at:", ch)   after the B loop.
#    Predict, then trace each pass: ch, whether ch == "5", and what area
#    becomes. Stop at the pass where the loop stops. Run it to check.
#
# Help: your "If I try this, I expect ..." was wrong twice in a row and you
#       can't say what that tells you? Ask.

# ==================== MAKE ====================
# First name: a sign-in sheet needs each person's first name and its length.
# 1. Use full_name = "Priya Shah" (below).
# 2. Build `first` with a loop that stops at the first space.
#    The space must not be part of `first`.
# 3. Count the letters in `first` with a counter that starts at 0
#    before the loop.
# 4. After the loop, print one line with the first name and its letter count.
# 5. Rerun with full_name = "Sam". It has no space, so the loop never stops
#    early, and it must still print the right name and count.
# 6. It must run without crashing.
#
# Desired output (two runs):
#   First name: Priya - 5 letters
#   First name: Sam - 3 letters
#
# Tip: to see only your Make output, comment out the code above
# (select it, then Ctrl+/ or Cmd+/).
#
# CHECKPOINT: show an instructor both runs of your Make program.

full_name = "Priya Shah"
