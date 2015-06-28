open System;
open System.IO;
#load "MajLogic.fs"

let args = fsi.CommandLineArgs

let arrays =
    if args.Length < 2 then
        printfn "Input file isn't specified. Using test values:"
        printfn "k = 4"
        let k = 4
        printfn "n = 8"
        let n = 8
        let arrays =
            [| [| 5; 5; 5; 5; 5; 5; 5; 5 |];
               [| 8; 7; 7; 7; 1; 7; 3; 7 |];
               [| 7; 1; 6; 5; 10; 100; 1000; 1|];
               [| 5; 1; 6; 7; 1; 1; 10; 1 |] |]
        printfn "%A" arrays
        arrays |> Array.toSeq
    else
        let filename = args.[1]
        let lines = File.ReadAllLines(filename)
        let arrays = lines
                     |> Seq.skip 1
                     |> Seq.map(fun line ->
                         line.Split [| ' ' |]
                         |> Array.map(fun x -> Int32.Parse(x.Trim())))
        arrays

arrays |> Seq.map (MajLogic.find_majority >> sprintf "%d")
       |> String.concat " "
       |> printfn "%s"
