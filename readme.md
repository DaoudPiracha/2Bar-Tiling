This is an attempt to solving the two bars tiling problem on a region with holes, s.t each bar is of size 3x1 or 1x3

### Previous Work
It has been shown in (DBRR 1995) that the problem of tiling with two bars of length 3 is NP-Complete. 
This necessitates the use of a search based approach e.g backtracking. While considering regions with holes, we can 
additionally optimize using early exits in
the case of early detection of untileable components. Finally, recent work has shown that we can solve the 2BAR-tiling problem in the case of a 
region without holes, in particular with 3x1, 1x3 bars, in linear time in terms of the area. This allows us to solve 
several subproblems with early exit conditions. 

### Chosen Approach
In our approach we implement a simple backtracking based approach since it allows us to keep code legible,
concise and easy to adapt to modification, in particular, this should keep the codebase accessible should we choose to 
optimize the algorithm by adding a linear time upon a subproblem instance of a region without holes.

With this in mind, we will attempt to solve the tiling problem using:
    1. A backtracking based search algorithm. (Brute Force)
    2. Backtracking with 'early exit' conditions:
        a. Unreachable tiles i.e a component which is not tileable mod 3
        b. Linear time calculations on regions without holes (future work)

### Alternative approaches
There is an additonal popular approach for this problem. It considers framing 2BAR tiling as an instance of 
polynomino tiling. In addition, polynomino tiling can be considered an instance of Exact Cover for which (D. Knuth 2000) has
proposed the Dancing Links approach. Finally, this problem is additonally representable as a Boolean Satifiability problem for which 
many solvers exist.

### Software Hacks
Some other software optimizations considered:
1. Represent grid as a bitvector. Allows swift computation of certain logic operation in backtracking
2. Early exit if any strongly connected component within the grid is no longer satisifiable, i.e if size of component mod 3 != 0
3. Using a fast permutation algorithm to optimize storage and accessibility of remaining grid points

### Acknowledgements

Finally, the author deeply thanks the team at Gradient.tech for posing such an interesting problem for their interview. 
In particular, this problem has been a great source of entertainment and interest in a strange quarantine experience 
amid the COVID-19 Pandemic. With links to topology, group theory and other areas of mathematics, this project has been, 
above all, a fun endeavor in learning.

---
1. Danièle Beauquier, Maurice Nivat, Eric Remila, Mike Robson,
Tiling figures of the plane with two bars, Computational Geometry, Volume 5, Issue 1, 1995, Pages 1-25, ISSN 0925-7721, https://doi.org/10.1016/0925-7721(94)00015-N. (http://www.sciencedirect.com/science/article/pii/092577219400015N)
2. Don Sheehy, The Complexity of Domino Tiling Problems, 2005
3. Horiyama, T., Ito, T., Nakatsuka, K. et al. Complexity of Tiling a Polygon with Trominoes or Bars. Discrete Comput Geom 58, 686–704 (2017). https://doi.org/10.1007/s00454-017-9884-9
--> concretely shows 2BAR-tiling is NP Complete