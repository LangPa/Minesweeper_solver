# Solving Minesweeper using Ordinary Least squares regression

Coding up a way of solving minesweeper quicker than you.

## Description

The `minesweeper.py` script contains a fully functioning game of minesweeper in the command line. Running the method OLSsolve will implement an OLS regresssion estimation on the current minefield and uncover/flag the mines found.

```
>>> Game = game(difficulty = 1)	
    Game.create_grid()

>>> Game.display()

     0   1   2   3   4   5   6   7   8  
   ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗
0  ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
1  ║ 1 ║ 1 ║ 2 ║   ║   ║   ║   ║   ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
2  ║ 0 ║ 0 ║ 1 ║   ║   ║   ║   ║   ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
3  ║ 0 ║ 0 ║ 1 ║ 1 ║ 1 ║ 2 ║   ║   ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
4  ║ 0 ║ 0 ║ 0 ║ 0 ║ 0 ║ 1 ║ 2 ║ 3 ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
5  ║ 0 ║ 0 ║ 0 ║ 0 ║ 0 ║ 0 ║ 0 ║ 1 ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
6  ║ 0 ║ 0 ║ 1 ║ 1 ║ 1 ║ 0 ║ 0 ║ 1 ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
7  ║ 0 ║ 0 ║ 1 ║   ║ 1 ║ 0 ║ 0 ║ 1 ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
8  ║ 0 ║ 0 ║ 1 ║   ║ 1 ║ 0 ║ 0 ║ 1 ║   ║
   ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝

>>> Game.OLSsolve(show_prob = True)

      0     1     2     3     4     5     6     7     8   
   ╔═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╗
0  ║0.338║0.662║0.000║0.338║     ║     ║     ║     ║     ║
   ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
1  ║  1  ║  1  ║  2  ║0.000║     ║     ║     ║     ║     ║
   ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
2  ║  0  ║  0  ║  1  ║1.000║0.000║0.000║1.000║     ║     ║
   ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
3  ║  0  ║  0  ║  1  ║  1  ║  1  ║  2  ║1.000║1.000║0.000║
   ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
4  ║  0  ║  0  ║  0  ║  0  ║  0  ║  1  ║  2  ║  3  ║0.507║
   ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
5  ║  0  ║  0  ║  0  ║  0  ║  0  ║  0  ║  0  ║  1  ║0.493║
   ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
6  ║  0  ║  0  ║  1  ║  1  ║  1  ║  0  ║  0  ║  1  ║0.000║
   ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
7  ║  0  ║  0  ║  1  ║1.000║  1  ║  0  ║  0  ║  1  ║0.507║
   ╠═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
8  ║  0  ║  0  ║  1  ║0.000║  1  ║  0  ║  0  ║  1  ║0.493║
   ╚═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╝

>>> Game.display()

     0   1   2   3   4   5   6   7   8
   ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗
0  ║   ║   ║ 1 ║   ║   ║   ║   ║   ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
1  ║ 1 ║ 1 ║ 2 ║ 2 ║   ║   ║   ║   ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
2  ║ 0 ║ 0 ║ 1 ║ F ║ 1 ║ 2 ║ F ║   ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
3  ║ 0 ║ 0 ║ 1 ║ 1 ║ 1 ║ 2 ║ F ║ F ║ 2 ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
4  ║ 0 ║ 0 ║ 0 ║ 0 ║ 0 ║ 1 ║ 2 ║ 3 ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
5  ║ 0 ║ 0 ║ 0 ║ 0 ║ 0 ║ 0 ║ 0 ║ 1 ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
6  ║ 0 ║ 0 ║ 1 ║ 1 ║ 1 ║ 0 ║ 0 ║ 1 ║ 1 ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
7  ║ 0 ║ 0 ║ 1 ║ F ║ 1 ║ 0 ║ 0 ║ 1 ║   ║
   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
8  ║ 0 ║ 0 ║ 1 ║ 1 ║ 1 ║ 0 ║ 0 ║ 1 ║   ║
   ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝
```

## Reflection
Whilst not a Bayesian estimator for discrete distributions the OLS estimator method provides a computationally fast approximation to where the mines may lie in the non-trivial cases. And so far finds where the mines are with certainty in deducible cases.

Infact OLS estimation can be equated to [Maximum Likelihood Estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) under the condition that the error is normally distributed. This is in turn a special case of [Maximum a posteriori estimation](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation) with a uniform prior distribution. Given that there should be no error and the mines are uniformly distributed the two could be equated but the solver wasn't programmed to be looking for a discrete prior distribution. Any mathematicians who find this and know about the relationship between MAP and Least Squares estimation don't hesitate to correct me!


This is my first machine learning project designed to complete a rudimentary task. The goal of the project is primarily familiarise myself with git, python and proper documentation.


