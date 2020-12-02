# Advent of Code 2020

- [Advent of Code 2020](#advent-of-code-2020)
  - [Day 01](#day-01)
    - [Profiling](#profiling)

## Day 01

### Profiling

```txt
Profiling Hashed Search:
         20004 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 cProfile.py:133(__exit__)
        1    0.001    0.001    0.004    0.004 day_01.py:45(hashed_search)
    20001    0.002    0.000    0.002    0.000 day_01.py:50(<genexpr>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling Linear Search:
         4 function calls in 0.014 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 cProfile.py:133(__exit__)
        1    0.012    0.012    0.014    0.014 day_01.py:16(bilinear_search)
        1    0.002    0.002    0.002    0.002 day_01.py:22(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling Bilinear Search:
         4 function calls in 0.014 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 cProfile.py:133(__exit__)
        1    0.012    0.012    0.014    0.014 day_01.py:16(bilinear_search)
        1    0.002    0.002    0.002    0.002 day_01.py:22(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```