open System
open System.IO
#load "SearchLogic.fs"

assert (SearchLogic.search [||] 10 = -1)
assert (SearchLogic.search [|55|] 10 = -1)
assert (SearchLogic.search [|10|] 10 = 0)
assert (SearchLogic.search [|-5; 6; 36; 74; 80; 238; 550|] -10 = -1)
assert (SearchLogic.search [|-5; 6; 36; 74; 80; 238; 550|] 79 = -1)
assert (SearchLogic.search [|-5; 6; 36; 74; 80; 238; 550|] 999 = -1)
assert (SearchLogic.search [|-5; 6; 36; 74; 80; 238; 550|] -5 = 0)
assert (SearchLogic.search [|-5; 6; 36; 74; 80; 238; 550|] 80 = 4)
assert (SearchLogic.search [|-5; 6; 36; 74; 80; 238; 550|] 550 = 6)
