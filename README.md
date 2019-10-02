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

```text
>>> python backward_search british 65536
Loaded british-boards.pkl in 28.922 seconds
  30:          1       0.000s
  29:          2       0.000s
  28:          8       0.001s
  27:         38       0.004s
  26:        164       0.020s
  25:        635       0.093s
  24:       2089       0.637s
  23:       6174       1.377s
  22:      16020       4.301s
  21:      35749      12.610s
  20:      68326      25.109s
  19:     112788      45.093s
  18:     162319      73.614s
  17:     204992     100.521s
  16:     230230     135.629s
  15:     230230     136.018s
  14:     204992     115.776s
  13:     162319     106.600s
  12:     112788      75.463s
  11:      68326      54.740s
  10:      35749      30.485s
   9:      16020      14.627s
   8:       6174       5.111s
   7:       2089       1.765s
   6:        635       0.531s
   5:        164       0.138s
   4:         38       0.032s
   3:          8       0.007s
   2:          2       0.001s
   1:          1       0.000s
Saved british-65536.pkl in 11.137 seconds
```
