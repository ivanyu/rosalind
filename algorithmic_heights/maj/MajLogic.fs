module MajLogic

let find_majority (arr : int[]) : int =
    let item, cnt = arr |> Seq.countBy Microsoft.FSharp.Core.Operators.id
                        |> Seq.maxBy snd
    if cnt > arr.Length / 2 then
        item
    else
        -1
