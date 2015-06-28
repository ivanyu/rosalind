open System
open System.IO
#load "MajLogic.fs"

// Empty array
assert (MajLogic.find_majority [||] = -1)
// One element
assert (MajLogic.find_majority [|5|] = 5)
// All elements
assert (MajLogic.find_majority [|5; 5; 5; 5; 5; 5; 5; 5|] = 5)
// Strictly half
assert (MajLogic.find_majority [|5; 1; 5; 1; 5; 1; 5; 1|] = -1)
assert (MajLogic.find_majority [|5; 5; 5; 5; 1; 2; 3; 4|] = -1)
// One before half
assert (MajLogic.find_majority [|1; 5; 2; 5; 3; 5; 4; 0|] = -1)
// One after half
assert (MajLogic.find_majority [|5; 5; 2; 5; 3; 5; 4; 5|] = 5)
// Odd number of elements
assert (MajLogic.find_majority [|1; 1; 1; 2; 2|] = 1)
