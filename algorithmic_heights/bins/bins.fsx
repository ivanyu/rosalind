open System
open System.IO
#load "SearchLogic.fs"

let args = fsi.CommandLineArgs

let (n, m, arr, ks) =
    if args.Length < 2
    then
        printfn "Input file isn't specified. Using test values:"
        printfn "n = 5"
        let n = 5
        printfn "m = 6"
        let m = 6
        printfn "A = [10, 20, 30, 40, 50]"
        let arr = [|10; 20; 30; 40; 50|]
        printfn "ks = [40, 10, 35, 15, 40, 20]"
        let ks = [|40; 10; 35; 15; 40; 20|]
        (n, m, arr, ks)
    else
        let filename = args.[1]
        let lines = File.ReadAllLines(filename)
        let n = Int32.Parse(lines.[0].Trim())
        let m = Int32.Parse(lines.[1].Trim())
        let arr = lines.[2].Split() |> Array.map Int32.Parse
        let ks = lines.[3].Split() |> Array.map Int32.Parse
        (n, m, arr, ks)

ks |> Array.map(SearchLogic.search arr
                >> fun x -> if x >= 0 then x + 1 else x
                >> sprintf "%d")
   |> String.concat " "
   |> printfn "%s"
