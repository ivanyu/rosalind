open System

let fibSeq = seq {
    let mutable a = 0
    let mutable b = 1
    let mutable c = a + b
    while true do
        yield a
        a <- b
        b <- c
        c <- a + b
}

let args = Environment.GetCommandLineArgs()

let n = if args.Length < 3
        then
            printfn "Input value isn't specified. Using test value n = 6."
            6
        else
            Int32.Parse(args.[2])

fibSeq |> Seq.skip n |> Seq.head |> printfn "%d"
