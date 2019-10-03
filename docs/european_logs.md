# European
What.
It appears that there are no single peg/marble solution for the European board starting with a missing central peg.
This is extremely disconcerting and unsatisfactory but confirmed [here](http://recmath.org/pegsolitaire/#french) :(
```
>>> python search_forward.py european
Moves    1, boards          4 (         1 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00 seconds
Moves    2, boards          5 (         3 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00 seconds
Moves    3, boards         19 (        15 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00 seconds
Moves    4, boards         90 (        70 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00 seconds
Moves    5, boards        438 (       341 unique)  search/dedupe/save:   0.00 /   0.01 /   0.00 seconds
Moves    6, boards       2133 (      1604 unique)  search/dedupe/save:   0.00 /   0.05 /   0.00 seconds
Moves    7, boards       9770 (      6950 unique)  search/dedupe/save:   0.01 /   0.22 /   0.01 seconds
Moves    8, boards      42025 (     27948 unique)  search/dedupe/save:   0.05 /   0.90 /   0.06 seconds
Moves    9, boards     165081 (    102261 unique)  search/dedupe/save:   0.21 /   3.32 /   0.25 seconds
Moves   10, boards     588248 (    335839 unique)  search/dedupe/save:   0.78 /  11.10 /   0.92 seconds
Moves   11, boards    1903203 (    984710 unique)  search/dedupe/save:   2.87 /  32.35 /   2.90 seconds
Moves   12, boards    5414479 (   2558220 unique)  search/dedupe/save:   8.89 /  86.22 /   7.77 seconds
Moves   13, boards   13364784 (   5858375 unique)  search/dedupe/save:  23.12 / 197.14 /  17.94 seconds
Moves   14, boards   29905929 (  11789357 unique)  search/dedupe/save:  52.99 / 403.24 /  39.13 seconds
Moves   15, boards   58413130 (  20795984 unique)  search/dedupe/save: 110.07 / 726.81 /  74.32 seconds
Moves   16, boards   99377350 (  32106854 unique)  search/dedupe/save: 193.24 / 1125.41 / 121.07 seconds
Moves   17, boards  140407036 (  43386122 unique)  search/dedupe/save: 296.56 / 1553.01 / 179.43 seconds
Moves   18, boards  171951341 (  51362742 unique)  search/dedupe/save: 398.97 / 1854.27 / 231.99 seconds
Moves   19, boards  181904066 (  53371113 unique)  search/dedupe/save: 470.15 / 1930.23 / 260.42 seconds
Moves   20, boards  167078714 (  48801369 unique)  search/dedupe/save: 490.01 / 1785.95 / 260.61 seconds
Moves   21, boards  137432328 (  39361771 unique)  search/dedupe/save: 430.52 / 1440.28 / 219.05 seconds
Moves   22, boards  112955750 (  28039820 unique)  search/dedupe/save: 353.66 / 1044.23 / 155.85 seconds
Moves   23, boards   77122438 (  17646892 unique)  search/dedupe/save: 238.59 / 653.55 /  92.68 seconds
Moves   24, boards   45157052 (   9813533 unique)  search/dedupe/save: 143.71 / 359.98 /  63.45 seconds
Moves   25, boards   22704817 (   4808524 unique)  search/dedupe/save:  76.39 / 173.19 /  16.11 seconds
Moves   26, boards   10105012 (   2068047 unique)  search/dedupe/save:  36.06 /  73.90 /   7.27 seconds
Moves   27, boards    3664158 (    776914 unique)  search/dedupe/save:  14.70 /  27.32 /   2.51 seconds
Moves   28, boards    1226147 (    253243 unique)  search/dedupe/save:   5.21 /   9.01 /   0.73 seconds
Moves   29, boards     351137 (     70245 unique)  search/dedupe/save:   1.57 /   2.41 /   0.18 seconds
Moves   30, boards      81057 (     16690 unique)  search/dedupe/save:   0.41 /   0.56 /   0.04 seconds
Moves   31, boards      14757 (      3350 unique)  search/dedupe/save:   0.09 /   0.11 /   0.01 seconds
Moves   32, boards       2171 (       536 unique)  search/dedupe/save:   0.02 /   0.02 /   0.00 seconds
Moves   33, boards        203 (        62 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00 seconds
Moves   34, boards         32 (        11 unique)  search/dedupe/save:   0.00 /   0.00 /   0.00 seconds
Saving boards...
Saved european-boards.pkl in 2967.667 seconds
11 final unique boards for european board
#0 [8589935616]
. . O O O . .
. O O O O O .
O O * O O O O
O O O O O O O
O O O O O O O
. O O O O * .
. . O O O . .
#1 [17179869185]
. . * O O . .
. O O O O O .
O O O O O O O
O O O O O O O
O O O O O O O
. O O O O O .
. . * O O . .
#2 [262146]
. . O * O . .
. O O O O O .
O O O O O O O
O O O * O O O
O O O O O O O
. O O O O O .
. . O O O . .
#3 [34359738370]
. . O * O . .
. O O O O O .
O O O O O O O
O O O O O O O
O O O O O O O
. O O O O O .
. . O * O . .
#4 [9216]
. . O O O . .
. O O O O O .
O O * O O * O
O O O O O O O
O O O O O O O
. O O O O O .
. . O O O . .
#5 [524292]
. . O O * . .
. O O O O O .
O O O O O O O
O O O O * O O
O O O O O O O
. O O O O O .
. . O O O . .
#6 [2097154]
. . O * O . .
. O O O O O .
O O O O O O O
O O O O O O *
O O O O O O O
. O O O O O .
. . O O O . .
#7 [33554464]
. . O O O . .
. O O * O O .
O O O O O O O
O O O O O O O
O O O * O O O
. O O O O O .
. . O O O . .
#8 [8388616]
. . O O O . .
. * O O O O .
O O O O O O O
O O O O O O O
O * O O O O O
. O O O O O .
. . O O O . .
#9 [4194336]
. . O O O . .
. O O * O O .
O O O O O O O
O O O O O O O
* O O O O O O
. O O O O O .
. . O O O . .
#10 [134217744]
. . O O O . .
. O * O O O .
O O O O O O O
O O O O O O O
O O O O O * O
. O O O O O .
. . O O O . .
```
