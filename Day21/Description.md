A linear congruential generator (LCG) is an algorithm that yields a sequence of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation. The method represents one of the oldest and best-known pseudorandom number generator algorithms. The theory behind them is relatively easy to understand, and they are easily implemented and fast, especially on computer hardware which can provide modular arithmetic by storage-bit truncation.

The generator is defined by recurrence relation:

```
{\displaystyle X_{n+1}=\left(aX_{n}+c\right){\bmod {m}}}

where {\displaystyle X}X is the sequence of pseudorandom values, and

{\displaystyle m,\,0<m}m,\,0<m — the "modulus"
{\displaystyle a,\,0<a<m}a,\,0<a<m — the "multiplier"
{\displaystyle c,\,0\leq c<m}c,\,0\leq c<m — the "increment"
{\displaystyle X_{0},\,0\leq X_{0}<m}X_{0},\,0\leq X_{0}<m — the "seed" or "start value"

```

Output :
```
3
5
[1, 5]
[5, 1, 2, 3, 4]

```
