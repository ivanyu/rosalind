module SearchLogic

let rec private search0 (arr : int[]) (k : int) (left : int) (right : int) : int =
    if (left <= right) then
        let mid = (left + right) / 2
        if k = arr.[mid] then
            mid
        elif k < arr.[mid] then
            search0 arr k left (mid - 1)
        else
            search0 arr k (mid + 1) right
    else
        -1

let search (arr : int[]) (k : int) : int =
    if k < (Array.head arr) || k > (Array.last arr) then
        -1
    else
        search0 arr k 0 (Array.length arr - 1)
