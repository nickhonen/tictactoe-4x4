# 4x4 Tic-Tac-Toe Solver

Checks win conditions, returns a winner! Made for a thing that I dont think I should say here. If the board wasn't a fixed 4x4 grid, the time complexity would be O(n²) and the space complexity would be O(1). Since it's a fixed grid though, the runtime is constant!

## Setup & Running Tests

If you have Python and pip installed and you don't mind installing a global package (I would normally setup a virtual environment, was pretty sure that was overkill here):

```bash
pip install pytest
pytest # run in project root
```

### Optimizations/Notes/Edge Cases:

- Board doesn't handle invalid pieces (non x or O, non strings), should've clarified if I needed to.
- I use a few any() expressions and other tradeoffs that would be slower if the board had n rows/columns, but because I knew it only had 4 I chose readability/concise solutions instead.
- could've done check_box with the directions too, but I know it's a 4x4 game and I didn't want to overcomplicate
- Probably made too many comments, some of the code is self documenting.
- Could've maybe added a main function that makes this more of a console app and some print statements but decided against it for time sake.
- Figured I didn't need to setup a virtual environment but I would've in a real project
