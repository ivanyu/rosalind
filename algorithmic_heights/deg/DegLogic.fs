module DegLogic

let degrees (graph : int[,]) : int list =
    [ 0 .. (graph.GetLength 0) - 1 ]
        |> List.map(fun i -> graph.[i, *] |> Array.sum)
