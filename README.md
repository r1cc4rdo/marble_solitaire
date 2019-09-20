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



### Execution logs for the "british" board
```text
>>> python board_explorer.py british
Moves    1, states          4 (         1 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Moves    2, states          3 (         2 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Moves    3, states         10 (         8 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Moves    4, states         41 (        39 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Moves    5, states        201 (       171 unique)  search/dedupe/save:   0.00 /   0.01 /   0.00
Moves    6, states        870 (       719 unique)  search/dedupe/save:   0.00 /   0.05 /   0.00
Moves    7, states       3559 (      2757 unique)  search/dedupe/save:   0.01 /   0.21 /   0.02
Moves    8, states      13354 (      9751 unique)  search/dedupe/save:   0.06 /   0.81 /   0.07
Moves    9, states      45679 (     31312 unique)  search/dedupe/save:   0.38 /   2.46 /   0.21
Moves   10, states     141670 (     89927 unique)  search/dedupe/save:   0.70 /   7.03 /   0.68
Moves   11, states     393214 (    229614 unique)  search/dedupe/save:   1.94 /  18.39 /   1.76
Moves   12, states     959193 (    517854 unique)  search/dedupe/save:   4.96 /  41.63 /   4.82
Moves   13, states    2076729 (   1022224 unique)  search/dedupe/save:  13.15 /  84.52 /   7.95
Moves   14, states    3906249 (   1753737 unique)  search/dedupe/save:  22.28 / 149.21 /  15.82
Moves   15, states    6385497 (   2598215 unique)  search/dedupe/save:  40.60 / 218.91 /  22.65
Moves   16, states    8907763 (   3312423 unique)  search/dedupe/save:  56.10 / 280.90 /  26.43
Moves   17, states   10743278 (   3626632 unique)  search/dedupe/save:  74.12 / 301.27 /  31.44
Moves   18, states   10874426 (   3413313 unique)  search/dedupe/save:  77.54 / 309.46 /  27.81
Moves   19, states    9503468 (   2765623 unique)  search/dedupe/save:  69.52 / 226.18 /  22.49
Moves   20, states    7177176 (   1930324 unique)  search/dedupe/save:  54.68 / 156.54 /  16.04
Moves   21, states    4552624 (   1160977 unique)  search/dedupe/save:  37.42 /  95.29 /   9.38
Moves   22, states    2459318 (    600372 unique)  search/dedupe/save:  28.27 /  54.35 /   5.34
Moves   23, states    1121382 (    265865 unique)  search/dedupe/save:  11.20 /  21.78 /   2.16
Moves   24, states     425515 (    100565 unique)  search/dedupe/save:   5.04 /   8.21 /   0.80
Moves   25, states     140372 (     32250 unique)  search/dedupe/save:   1.75 /   2.81 /   0.24
Moves   26, states      37432 (      8688 unique)  search/dedupe/save:   0.56 /   0.71 /   0.07
Moves   27, states       8023 (      1917 unique)  search/dedupe/save:   0.14 /   0.15 /   0.01
Moves   28, states       1204 (       348 unique)  search/dedupe/save:   0.03 /   0.03 /   0.00
Moves   29, states        162 (        50 unique)  search/dedupe/save:   0.01 /   0.00 /   0.00
Moves   30, states         12 (         7 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
Moves   31, states          2 (         2 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00
```
```text
>>> python aggregate_states british
british-state-000.pkl            1 states     0.476s
british-state-001.pkl            1 states     0.000s
british-state-002.pkl            2 states     0.000s
british-state-003.pkl            8 states     0.000s
british-state-004.pkl           39 states     0.000s
british-state-005.pkl          171 states     0.000s
british-state-006.pkl          719 states     0.001s
british-state-007.pkl         2757 states     0.004s
british-state-008.pkl         9751 states     0.009s
british-state-009.pkl        31312 states     0.029s
british-state-010.pkl        89927 states     0.088s
british-state-011.pkl       229614 states     0.200s
british-state-012.pkl       517854 states     0.647s
british-state-013.pkl      1022224 states     1.052s
british-state-014.pkl      1753737 states     1.774s
british-state-015.pkl      2598215 states     2.822s
british-state-016.pkl      3312423 states     3.488s
british-state-017.pkl      3626632 states     3.902s
british-state-018.pkl      3413313 states     3.817s
british-state-019.pkl      2765623 states     2.970s
british-state-020.pkl      1930324 states     2.151s
british-state-021.pkl      1160977 states     1.253s
british-state-022.pkl       600372 states     0.612s
british-state-023.pkl       265865 states     0.278s
british-state-024.pkl       100565 states     0.135s
british-state-025.pkl        32250 states     0.033s
british-state-026.pkl         8688 states     0.008s
british-state-027.pkl         1917 states     0.001s
british-state-028.pkl          348 states     0.000s
british-state-029.pkl           50 states     0.000s
british-state-030.pkl            7 states     0.000s
british-state-031.pkl            2 states     0.000s
Saved british-states.pkl.zip in 181.834 seconds
2 final unique states for british board
0: 2
. . O * O . .
. . O O O . .
O O O O O O O
O O O O O O O
O O O O O O O
. . O O O . .
. . O O O . .
1: 65536
. . O O O . .
. . O O O . .
O O O O O O O
O O O * O O O
O O O O O O O
. . O O O . .
. . O O O . .
```
```text
>>> python backward_search british 65536
Loaded british-states.pkl in 26.989 seconds
  30:          1       0.000s
  29:          2       0.000s
  28:          8       0.001s
  27:         38       0.004s
  26:        164       0.024s
  25:        635       0.112s
  24:       2089       0.497s
  23:       6174       1.749s
  22:      16020       5.426s
  21:      35749      15.553s
  20:      68326      36.431s
  19:     112788      75.194s
  18:     162319     105.505s
  17:     204992     143.043s
  16:     230230     228.966s
  15:     230230     256.835s
  14:     204992     192.749s
  13:     162319     158.612s
  12:     112788     119.993s
  11:      68326      86.889s
  10:      35749      50.334s
   9:      16020      34.145s
   8:       6174      14.395s
   7:       2089       4.641s
   6:        635       1.683s
   5:        164       0.424s
   4:         38       0.073s
   3:          8       0.016s
   2:          2       0.002s
   1:          1       0.000s
Saved british-65536.pkl in 21.041 seconds
```
