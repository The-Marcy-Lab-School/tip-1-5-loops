# Day 1 · Loops 1: Where a Line Sits Decides How Often It Runs

## The big ideas (come back to this table)

| \#  | Idea                                                                                                                                                              | Try it in the REPL                                                                         |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 1   | Where a line sits decides how often it runs. A line inside the body runs once per item; a line outside runs once, either before the loop starts or after it ends. | \>\>\> for letter in "Ana": ... print("inside") ... \>\>\> print("after")                  |
| 2   | A result builds across passes only if its starting value is set once, before the loop, and each pass updates it from its current value.                           | \>\>\> for letter in "Ana": ... count \= 0 ... count \= count \+ 1 ... \>\>\> print(count) |
| 3   | Empty text is a real starting value that adds nothing when joined. A space looks empty but is a character.                                                        | \>\>\> "" \+ "\*" \>\>\> " " \+ "\*"                                                       |
| 4   | Joining is order-sensitive: whatever is on the left comes first. Adding each item to the end keeps the original order; adding it to the front reverses it.        | \>\>\> "\*" \+ "48" \>\>\> "48" \+ "\*"                                                    |

## Habits for today

**Coding habit:** Set the starting value once, before the loop. Update it inside the loop from its current value. Use the finished result after the loop. Choose the join order on purpose:

- `result = result + item` keeps the original order.
- `result = item + result` reverses it.

**Working habit: Debugging with a plan.**

---

## Review (7 minutes)

Two ideas from earlier lessons:

- A loop runs its body once for each item. The loop's name takes each item's value in turn, and the body doesn't have to use it.
- An assignment works out the right side using the name's current value, then replaces that value.

Open `day-1/ding_floor.py`:

```py
for digit in "48":
    print("Ding")

floor = 3
floor = floor + 1
print("Floor", floor)
```

```
Ding
Ding
Floor 4
```

Answer each question in the file, right under it. Predict before you run.

1. Change `"48"` to `"4821"`. How many times will `Ding` print? Does the body care which digits are in the text?
2. Add `floor = floor + 1` two more times before the `print`. What will it print? Why isn't `floor = floor + 1` a contradiction?

---

## Part 1: Predict & Run (8 minutes)

Open `day-1/pin_mask.py`. It builds a masked PIN three ways: A, B and C. **Don't run it yet.**

1. Fill in the data types comment and every `# Prediction:` line.
2. Run `python3 day-1/pin_mask.py`.
3. Fill in each `# Actual:` and `# Explanation:`. Use the big ideas table.

Answer these under **Part 1 questions** at the bottom of `pin_mask.py`:

1. What are the data types of `pin`, `""`, and `digit`?
2. No line mentions the number 4\. Where did A's four stars come from?
3. The B loop also runs four times. Why only one star?
4. Why does C print four lines? Which one is the finished result?

**Swap with a partner.** Read each other's answers and compare.

🙋 **Ask for help if:** you still can't explain B's single star after running. Bring your prediction.

---

## Part 2: Investigate (9 minutes)

### A. Trace the B loop

On paper or under **Part 2A** in `pin_mask.py`, write what `masked` holds after each line, on every pass.

Self-check: your last line should match what B printed.

### B. Compare

A and B both contain `masked = masked + "*"`. What is different about them, and why does it change the result?

### C. Try it in the REPL

Open the REPL (`python3`). Predict each result before you press Enter.

```
"" + "*"
" " + "*"
"" + ""
"*" + "4"
"4" + "*"
```

Write one sentence about empty text vs. a space, and one about the order of a join.

✅ **Checkpoint:** Show an instructor your trace (A) and your answer to B.

---

## Part 3: Modify (11 minutes)

Change the code in `pin_mask.py`, one change at a time. Predict before every run.

### 1\. Fix the error

Make the B line print `B: ****` by moving one line.

Self-check: run it. A and B should now print the same thing.

### 2\. Variation

In your fixed B loop, change `"*"` to `digit`. Why did it print what it did instead of `****`?

### 3\. Trace

Change `masked + digit` to `digit + masked`. Predict the output, then trace `masked` before the loop and after each pass. Run it to check your trace.

🙋 **Ask for help if:** exercise 3 surprises you and one more look doesn't explain it.

---

## Part 4: Make (10 minutes)

**Task: Sign heading.** In `day-1/sign_heading.py`, space out a building notice's heading and give it an underline that lines up under it.

**Requirements**

1. Use `heading = "NOTICE"` (already in the file).
2. Build a `spaced_heading` variable with a loop: each letter followed by one space. It must not start with a space.
3. Build an `underline` variable with a loop: two `=` characters for each letter.
4. Print each variable once they have been fully created.

**Check your output.**

```
N O T I C E
============
```

If `spaced` shows only `E` , reread big idea 2\. If it starts with a space, reread big idea 3\.

✅ **Checkpoint:** Show an instructor your running Make program.

---

## Part 5: Independent check (10 minutes)

When your instructor says, open `day-1/code_readback.py`. Work alone, with no AI and no notes, and write your prediction on paper before you run anything.

---

## Going further (optional)

Use one new tool, `len()`, which gives back how many characters a piece of text has. Build the Make task's underline **without a loop**, using `len(heading)`. Then explain when the loop version is still the better choice.

---

# Day 2 · Loops 2: The Whole Body Runs Each Pass

## The big ideas (come back to this table)

| \#  | Idea                                                                                                                                                          | Try it in the REPL                                                                                                      |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 1   | The whole body runs top to bottom on each pass before the next pass begins.                                                                                   | \>\>\> for letter in "Bo": ... print("first", letter) ... print("second", letter) ...                                   |
| 2   | Inside the body, a name holds a partway value. The finished result exists only after the last pass.                                                           | \>\>\> count \= 0 \>\>\> for letter in "Ana": ... count \= count \+ 1 ... print(count) ... \>\>\> print("done:", count) |
| 3   | The order of lines in the body decides which value each line sees. A line before the update sees the previous pass's value; a line after it sees this pass's. | \>\>\> count \= 0 \>\>\> for letter in "Ana": ... print(count) ... count \= count \+ 1 ... \>\>\> print("done:", count) |
| 4   | Names changed in a loop, including the loop's own name, keep their last value after the loop ends.                                                            | \>\>\> for letter in "Queens": ... last \= letter ... \>\>\> print(last, letter)                                        |
| 5   | A name can signal intent: a throwaway name says the value isn't used, but Python still assigns each item to it like any other name.                           | \>\>\> for \_ in "AB": ... print("Ding") ... \>\>\> print(\_)                                                           |

## Habits for today

**Coding habit:** Name the loop variable for what it holds; when the body never uses it, name it `_`. Place a checkpoint print on purpose:

- **After** the update to see this pass's value.
- **Before** the update to see the previous pass's.

**Working habit: Where was it last right?**

- When a trace doesn't match the output, find the first line where it went wrong. Bring the line where it was last right when you ask for help.

---

## Review (7 minutes)

Two ideas from Day 1:

- Where a line sits decides how often it runs. A line inside the body runs once per item; a line outside runs once, either before the loop starts or after it ends.
- A result builds across passes only if its starting value is set once, before the loop, and each pass updates it from its current value.

Open `day-2/stop_count.py`:

```py
stops = 0
for letter in "Ana":
    stops = stops + 1
print("Stops:", stops)
```

```
Stops: 3
```

Answer each question in the file, right under it. Predict before you run.

1. Indent the `print` so it's inside the body. How many lines will print, and why?
2. Put the `print` back after the loop. Then move `stops = 0` into the body, as its first line. What prints? Why does the count stop growing?

---

## Part 1: Predict & Run (8 minutes)

Open `day-2/bike_minutes.py`. It adds up three 12-minute bike rides two ways: A and B. **Don't run it yet.**

1. Fill in the data types comment and every `# Prediction:` line.
2. Run `python3 day-2/bike_minutes.py`.
3. Fill in each `# Actual:` and `# Explanation:`. Use the big ideas table.

Answer these under **Part 1 questions** at the bottom of `bike_minutes.py`:

1. What are the data types of `minutes` and `ride`?
2. Why are A's three "so far" lines different from each other?
3. B has the same two body lines as A. Why does it start at 0?
4. Both totals are 36\. Why does A's last "so far" match its total when B's doesn't?

**Swap with a partner.** Read each other's answers and compare.

🙋 **Ask for help if:** you predicted `B so far: 0` three times and can't see why that's wrong after running.

---

## Part 2: Investigate (9 minutes)

### A. Trace the B loop

On paper or under **Part 2A** in `bike_minutes.py`, write what `ride` holds, what the print shows and what `minutes + 12` gives, on every pass.

Self-check: every "print shows" should match a line B printed, in order.

### B. Compare

A's last "so far" matches its total, but B's last "so far" (24) doesn't match its total (36). Both loops contain the same two lines. Why?

### C. Try it in the REPL

Open the REPL (`python3`). Type each loop, then press Enter on the blank `...` line. Predict each result before you press Enter.

```
for letter in "Bo":
    last = letter

last
letter
total = 0
for letter in "Bo":
    total = total + 1

total
```

What happens to a loop's names when the loop ends?

✅ **Checkpoint:** Show an instructor your trace (A) and your answer to B.

---

## Part 3: Modify (11 minutes)

Change the code in `bike_minutes.py`, one change at a time. Predict before every run.

### 1\. Fix the error

Make B's "so far" lines show `12`, `24`, `36` by moving one line.

Self-check: run it. B's last "so far" should now match its total.

### 2\. Variation

In your fixed B loop, rename `ride` to `_`. Why did it print what it did instead of skipping the loop or crashing?

### 3\. Trace

Add `print("B starts at:", minutes)` as the first line of B's body. Predict, then trace each pass: what each print shows, and what `minutes` becomes. Run it to check.

🙋 **Ask for help if:** your trace doesn't match and you can't find the first line where it went wrong. Bring the line where it was last right.

---

## Part 4: Make (10 minutes)

**Task: Podcast queue.** In `day-2/podcast_queue.py`, plan a listening session of 3 episodes, each 25 minutes long.

**Requirements**

1. Use `_` as the loop name; the body doesn't need it.
2. Start an `episode` counter and a `minutes` total at 0, before the loop.
3. Each pass prints two lines: the minute the episode starts, then the minute it ends. Both must be correct.
4. After the loop, print one line with the number of episodes and the total minutes.
5. The program must run without crashing.

**Check your output.**

```
Episode 1 starts at minute 0
Episode 1 ends at minute 25
Episode 2 starts at minute 25
Episode 2 ends at minute 50
Episode 3 starts at minute 50
Episode 3 ends at minute 75
3 episodes, 75 minutes
```

If an episode starts and ends at the same minute, reread big idea 3\.

✅ **Checkpoint:** Show an instructor your running Make program.

---

## Part 5: Independent check (10 minutes)

When your instructor says, open `day-2/bus_riders.py`. Work alone, with no AI and no notes, and write your prediction on paper before you run anything.

---

## Going further (optional)

Use one new tool, `while`, which repeats its body for as long as a condition is true. Rewrite your fixed bike-ride loop so it doesn't know the number of rides and keeps going while `minutes < 36`. Predict the output, then run. Then explain what happens to the number of passes if each ride is 10 minutes instead of 12\.

---

# Day 3 · Loops 3: A Stop Ends the Loop, Not the Program

## The big ideas (come back to this table)

| \#  | Idea                                                                                                                                                                          | Try it in the REPL                                                                                                                                                                    |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | An early exit stops the whole loop the moment it runs. The rest of that pass is skipped, no more passes start, and the program carries on with the first line after the loop. | \>\>\> for letter in "Bob": ... print("before", letter) ... break ... print("after", letter) ... \>\>\> print("loop over")                                                            |
| 2   | A stop placed under a decision runs only on the pass where the condition is true; until then, every pass runs normally.                                                       | \>\>\> for letter in "Bo\!": ... if letter \== "\!": ... break ... print(letter) ...                                                                                                  |
| 3   | Whether the stopping pass's work counts depends on whether that work comes before or after the check.                                                                         | \>\>\> kept \= "" \>\>\> for letter in "Bo\!": ... kept \= kept \+ letter ... if letter \== "\!": ... break ... \>\>\> print(kept) Then try it again with the check above the update. |
| 4   | After an early exit, names hold the values from the passes that ran, and the loop's name holds the item it stopped on.                                                        | \>\>\> for ch in "718-555": ... if ch \== "-": ... break ... \>\>\> print(ch)                                                                                                         |

## Habits for today

**Coding habit:** Put the check where you mean it.

- Check **before** the update when the stopping item shouldn't count.
- Check **after** the update when it should.

**Working habit: If I try this, I expect … / That tells me …**

- Before each run, say: "If I try this, I expect …"
- After each run, finish: "That tells me …"

---

## Review (7 minutes)

Two ideas from earlier lessons:

- The whole body runs top to bottom on each pass, and the order of its lines decides which value each line sees (Day 2).
- A decision lets a program skip code: a block runs only if its condition is true at the moment Python reaches it (Conditionals 1).

Open `day-3/found_bang.py`:

```py
stops = 0
for letter in "Bo!":
    if letter == "!":
        print("found !")
    stops = stops + 1
    print(letter, stops)
```

```
B 1
o 2
found !
! 3
```

Answer each question in the file, right under it. Predict before you run.

1. Move `print(letter, stops)` above `stops = stops + 1`. What prints? Why does every number drop by one?
2. Put the print back. Change `"Bo!"` to `"Bo"`. What prints? Why does `found !` never print?

---

## Part 1: Predict & Run (8 minutes)

Open `day-3/area_code.py`. It pulls the area code out of a phone number two ways: A and B. **Don't run it yet.**

1. Fill in the data types comment and every `# Prediction:` line.
2. Run `python3 day-3/area_code.py`.
3. Fill in each `# Actual:` and `# Explanation:`. Use the big ideas table.

Answer these under **Part 1 questions** at the bottom of `area_code.py`:

1. What are the data types of `phone`, `area`, and `ch`?
2. The phone number has more digits after the dash. Why were they never added in A?
3. B has the same lines as A. Why is the dash included?
4. The program kept going after each `break`. How can you tell?

**Swap with a partner.** Read each other's answers and compare.

🙋 **Ask for help if:** you predicted `718-` for A and can't explain the difference after running.

---

## Part 2: Investigate (9 minutes)

### A. Trace the A loop

On paper or under **Part 2A** in `area_code.py`, write what `ch` holds, whether `ch == "-"` is true, and what `area` holds after the update, on every pass. If a line never runs, write "never runs".

Self-check: your last line should match what A printed.

### B. Compare

Both loops stop on the same pass. Why does B keep the dash when A doesn't?

### C. Try it in the REPL

Open the REPL (`python3`). Type each loop, then press Enter on the blank `...` line. Predict each result before you press Enter.

```
for ch in "718-555":
    if ch == "-":
        break

ch
for ch in "718":
    if ch == "-":
        break

ch
```

What does the loop's name hold after a stop? With no stop?

✅ **Checkpoint:** Show an instructor your trace (A) and your answer to B.

---

## Part 3: Modify (11 minutes)

Change the code in `area_code.py`, one change at a time. Before each run, say: "If I try this, I expect …" After each run, finish: "That tells me …"

### 1\. Fix the error

Make the B line print `B: 718` without adding or removing any lines.

Self-check: run it. A and B should now print the same area code.

### 2\. Variation

In your fixed B loop, change `"-"` to `"5"`. Why did it print what it did instead of `718`?

### 3\. Trace

Add `print("Stopped at:", ch)` after the B loop. Predict, then trace each pass: `ch`, whether `ch == "5"`, and what `area` becomes. Stop at the pass where the loop stops. Run it to check.

🙋 **Ask for help if:** your "If I try this, I expect …" was wrong twice in a row and you can't say what that tells you.

---

## Part 4: Make (10 minutes)

**Task: First name.** In `day-3/first_name.py`, get each person's first name and its length for a sign-in sheet.

**Requirements**

1. Use `full_name = "Priya Shah"` (already in the file).
2. Build `first` with a loop that stops at the first space. The space must not be part of `first`.
3. Count the letters in `first` with a counter that starts at 0 before the loop.
4. After the loop, print one line with the first name and its letter count.
5. Rerun with `full_name = "Sam"`. It has no space, so the loop never stops early, and it must still print the right name and count.
6. The program must run without crashing.

**Check your output.** One run with `"Priya Shah"`, one with `"Sam"`:

```
First name: Priya - 5 letters
```

```
First name: Sam - 3 letters
```

If Priya's count says 6 letters, reread big idea 3\.

✅ **Checkpoint:** Show an instructor both runs of your Make program.

---

## Part 5: Independent check (10 minutes)

When your instructor says, open `day-3/clock_hour.py`. Work alone, with no AI and no notes, and write your prediction on paper before you run anything.

---

## Going further (optional)

Use one new tool, `continue`, which skips the rest of one pass and moves on to the next item. Strip the dashes from `"718-555-0142"` so it prints `7185550142`. Then explain in one sentence how `continue` differs from `break`, and predict what the same loop prints with `break` instead.
