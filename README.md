# neworleans-solver
Solver for Great Big House in New Orleans

This allows the user to solve the game Great Big House in New Orleans.

The background and development of this project is explained at:
https://thisworld-me.blogspot.com/2017/11/great-big-house-in-new-orleans.html

The logic for orleans3.py and orleans-minimal.py is also explained in the first blog post above, but is also documented at:
https://thisworld-me.blogspot.com/2017/11/great-big-house-in-new-orleans-improved.html

Main implementation:
* orleans3.py (neworleans-solver/Python/orleans3.py)
* orleans-minimal.py (neworleans-solver/Python/orleans-minimal.py)

Legacy implementation:
* NewOrleansSolver.java (neworleans-solver/Java/NewOrleansSolver/src/NewOrleansSolver.java)
* orleans2.py (neworleans-solver/Python/orleans2.py)

Other files, all using the legacy implementation except where noted (in neworleans-solver/Python):
* orleans100.py outputs the results for class sizes up to 100.
* orleans-xlsx1000.py generates a spreadsheet for class sizes up to 1000. The spreadsheet is OrleansPositions1000.numbers.
* orleans-xlsx.py generates a spreadsheet only for the first 100 class sizes. That spreadsheet is OrleansPositions.numbers.
* orleans.py is a straight Python translation of NewOrleansSolver.java.
* orleans2.py uses the del operator to remove elements from the class list, which Java cannot do unless ArrayList is used.
* orleans3_investigation.py (using the **main implementation**) prints cases where the winning position is 1 up to a user-inputted class size, then finally prints the winning position of the user-inputted class size.
