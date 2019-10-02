# Peg solitaire

Compute solutions to variants of the marble / peg solitaries.
For more information, check the following pages:

1) [Peg solitaire on Wikipedia](https://en.wikipedia.org/wiki/Peg_solitaire)
2) [Computing Minimum Equal Sums Of Like Power](http://euler.free.fr/PegInfos.htm)
3) [George's Peg Solitaire Page](http://recmath.org/pegsolitaire/)

### Näive algorithm

The näive algorithm that brute-forces through all possible combination through
recursion has a large time complexity since the number of board states grows
exponentially after each move.

One way to reduce the time complexity is realizing that sequence of different
moves can lead to the same configuration, and performing the evaluation of that
branch only once. This can be done with memoization of the recursive evaluation
call. The [marble_solitaire.py](marble_solitaire.py) script shows an example of
such an implementation.

### Full state space search

Even with memoization, the näive algorithm ends up considering too many branches,
and visiting board configurations equivalent up to rotations and flip to others already
explored.

Moreover, it only explores a single path from root to leaves at a time: since the number
of early-stops greatly outnumbers the good solutions for a given number of final pegs/marbles,
the majority of time is spent exploring dead-ends.

Therefore, the non-näive algorithm generates all and only the valid configurations after
a number of moves, while detecting mirrored and rotated configurations.
```text
>>> python search_forward.py british
Moves    1, states          4 (         1 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Moves    2, states          3 (         2 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Moves    3, states         10 (         8 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
[... snip ...]
Moves   16, states    8907763 (   3312423 unique)  search/dedupe/save:  56.10 / 280.90 /  26.43
Moves   17, states   10743278 (   3626632 unique)  search/dedupe/save:  74.12 / 301.27 /  31.44
Moves   18, states   10874426 (   3413313 unique)  search/dedupe/save:  77.54 / 309.46 /  27.81
Moves   19, states    9503468 (   2765623 unique)  search/dedupe/save:  69.52 / 226.18 /  22.49
[... snip ...]
Moves   29, states        162 (        50 unique)  search/dedupe/save:   0.01 /   0.00 /   0.00
Moves   30, states         12 (         7 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Moves   31, states          2 (         2 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Saving boards...
Saved british-boards.pkl in 226.316 seconds
2 final unique boards for british board
#0 [65536]
. . O O O . .
. . O O O . .
O O O O O O O
O O O * O O O
O O O O O O O
. . O O O . .
. . O O O . .
#1 [2]
. . O * O . .
. . O O O . .
O O O O O O O
O O O O O O O
O O O O O O O
. . O O O . .
. . O O O . .
```
The same process can then be done backwards from one of the final configurations reached.
```text
>>> python search_backward british 65536
Loaded british-boards.pkl in 28.922 seconds
  30:          1       0.000s
  29:          2       0.000s
  28:          8       0.001s
[... snip ...]
  18:     162319      73.614s
  17:     204992     100.521s
  16:     230230     135.629s
  15:     230230     136.018s
  14:     204992     115.776s
  13:     162319     106.600s
[... snip ...]
   3:          8       0.007s
   2:          2       0.001s
   1:          1       0.000s
Saved british-65536.pkl in 11.137 seconds
``` 
The result is

search_solution

british_logs.md