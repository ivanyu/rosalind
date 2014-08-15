module Main where

import System.IO (withFile, IOMode(ReadMode), hGetLine)
import System.Environment (getArgs)

solve :: String -> String
solve str = map (\x -> if x == 'T' then 'U' else x) str

main = do
    args <- getArgs
    inputStr <-
        if length args == 0
        then do putStrLn "Input file name isn't specified. Using test input line."
                return "GATGGAACTTGACTACGTAAATT"
        else withFile (head args) ReadMode hGetLine
    putStrLn $ solve inputStr
