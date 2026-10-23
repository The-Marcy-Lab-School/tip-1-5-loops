# Loops 2: bike_minutes.py
# Work top to bottom: PREDICT -> RUN -> INVESTIGATE -> MODIFY -> MAKE.
# Edit this file as you go. If you fall behind, copy the current code from the screen.
#
# Working habit: Where was it last right?

# ==================== PREDICT ====================
# Fill in EVERY "Prediction:" below before you run anything.

minutes = 0

# Data types of these values: minutes, ride

for ride in range(3):
    minutes = minutes + 12
    print("A so far:", minutes)
print("A total:", minutes)
# Prediction:
# Actual:
# Explanation:

minutes = 0
for ride in range(3):
    print("B so far:", minutes)
    minutes = minutes + 12
print("B total:", minutes)
# Prediction:
# Actual:
# Explanation:

# ==================== RUN ====================
# Now run the file. Fill in each "Actual:" and "Explanation:" above.
# Then answer these here:
# 1) What are the data types of minutes and ride?
# 2) Why are A's three "so far" lines different from each other?
# 3) B has the same two body lines as A. Why does it start at 0?
# 4) Both totals are 36. Why does A's last "so far" match its total
#    when B's doesn't?
# 5) Swap with a partner and compare. Can't agree? Ask an instructor.
#
# Help: predicted "B so far: 0" three times and can't see why that's
#       wrong after running? Ask now.

# ==================== INVESTIGATE ====================
# A) Trace the B loop on paper, every pass:
#    Pass 1: ride = ___   print shows ___   minutes + 12 = ___
#    Pass 2: ride = ___   print shows ___   minutes + 12 = ___
#    Pass 3: ride = ___   print shows ___   minutes + 12 = ___
#    After the loop, print shows: ___
#    Self-check: every "print shows" should match a line B printed, in order.
#
# B) A's last "so far" matches its total, but B's last "so far" (24)
#    doesn't match its total (36). Both loops contain the same two lines.
#    Why?
#
# C) In the REPL, type each loop, then press Enter on the blank ... line.
#    Predict each result first:
#      for letter in "Bo":
#          last = letter
#
#      last
#      letter
#      total = 0
#      for letter in "Bo":
#          total = total + 1
#
#      total
#    What happens to a loop's names when the loop ends?
#
# Now read: the ideas behind this snippet
#   1. The whole body runs top to bottom on each pass before the next
#      pass begins.
#   2. Inside the body, a name holds a partway value. The finished result
#      exists only after the last pass.
#   3. The order of lines in the body decides which value each line sees.
#      Before the update: the previous pass's value. After it: this pass's.
#   4. Names changed in a loop, including the loop's own name, keep their
#      last value after the loop ends.
#   5. A throwaway name like _ says "this value isn't used," but Python
#      still assigns each item to it like any other name.
#
# Coding habit: name the loop variable for what it holds, or _ when the
# body never uses it. Put a checkpoint print AFTER the update to see this
# pass's value, BEFORE it to see the previous pass's.
#
# CHECKPOINT: show an instructor your trace (A) and your answer to B.

# ==================== MODIFY ====================
# Change the code ABOVE, one change at a time. Predict before every run.
# 1) Make B's "so far" lines show 12, 24, 36 by moving one line.
# 2) In your fixed B loop, rename ride to _.
#    Why did it print what it did instead of skipping the loop or crashing?
# 3) Add   print("B starts at:", minutes)   as the first line of B's body.
#    Predict, then trace each pass: what each print shows, and what
#    minutes becomes. Run it to check.
#
# Help: trace doesn't match and you can't find the first line where it
#       went wrong? Ask, and bring the line where it was last right.

# ==================== MAKE ====================
# Podcast queue: plan 3 episodes, each 25 minutes long.
# 1. Use _ as the loop name; the body doesn't need it.
# 2. Start an episode counter and a minutes total at 0, before the loop.
# 3. Each pass prints two lines: the minute the episode starts, then the
#    minute it ends. Both must be correct.
# 4. After the loop, print one line with the number of episodes and the
#    total minutes.
# 5. It must run without crashing.
#
# Desired output:
#   Episode 1 starts at minute 0
#   Episode 1 ends at minute 25
#   Episode 2 starts at minute 25
#   Episode 2 ends at minute 50
#   Episode 3 starts at minute 50
#   Episode 3 ends at minute 75
#   3 episodes, 75 minutes
#
# Tip: to see only your Make output, comment out the code above
# (select it, then Ctrl+/ or Cmd+/).
#
# CHECKPOINT: show an instructor your running Make program.
