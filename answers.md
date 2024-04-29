# CMPS 2200 Recitation 06
## Answers

**Name:** Julia Renner


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

- W(n) = 1 + W(n-1) + W(n-2)

- The work is O(2^n).

- **3)**

- S(n) = 1 + S(n-1)

- The span is O(n).

- **4)**

- There is an observable pattern when using the counts list, and it follows that the numbers decrease moving down the list until 1 reaches the leftmost position. I looked at this through temporary print statements, and the visual of each number being iterated repeatedly showed a lot of duplicate work being done within the operation. 

- **6)**

- The maximum number of times fib_top_down will be called for any value 'i' is equal to 'n'.

- Based on this, the work and span of fib_top_down is W(n) = O(n), and S(n) = O(n).

- **8)**

- The maximum number of times Fi will be read is n-2 times.

- Based on this, the work and span of fib_bottom_up is W(n) = O(n), and S(n) = O(n).
