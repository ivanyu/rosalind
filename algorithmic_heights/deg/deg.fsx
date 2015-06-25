open System
open System.IO
#load "DegLogic.fs"

let args = fsi.CommandLineArgs

let (n, graph) =
    if args.Length < 2 then
        printfn "Input file isn't specified. Using test values:"
        printfn "n = 6"
        let n = 6
        printfn "m = 7"
        //let m = 7
        let graph = Array2D.create n n 0

        printfn "Graph:"
        printfn "1 2"
        graph.[0, 1] <- 1
        graph.[1, 0] <- 1
        printfn "2 3"
        graph.[1, 2] <- 1
        graph.[2, 1] <- 1
        printfn "6 3"
        graph.[5, 2] <- 1
        graph.[2, 5] <- 1
        printfn "5 6"
        graph.[4, 5] <- 1
        graph.[5, 4] <- 1
        printfn "2 5"
        graph.[1, 4] <- 1
        graph.[4, 1] <- 1
        printfn "2 5"
        graph.[1, 3] <- 1
        graph.[3, 1] <- 1
        printfn "4 1"
        graph.[3, 0] <- 1
        graph.[0, 3] <- 1
        (n, graph)
    else
        let extractPair (line: string) : int * int =
            line.Split([|' '|])
            |> Array.map(fun x -> Int32.Parse(x.Trim()))
            |> fun x -> (x.[0], x.[1])

        let filename = args.[1]
        let lines = File.ReadAllLines(filename)
        let n, _ = extractPair lines.[0]
        let graph = Array2D.create n n 0
        for i, j in lines |> Array.skip 1 |> Array.map extractPair do
            graph.[i - 1, j - 1] <- 1
            graph.[j - 1, i - 1] <- 1
        (n, graph)

graph |> DegLogic.degrees
      |> List.map (sprintf "%d")
      |> String.concat " "
      |> printfn "%s"
