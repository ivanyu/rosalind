module Main where

import System.IO (withFile, IOMode(ReadMode), hGetLine)
import System.Environment (getArgs)
import qualified Data.Map as Map

solve :: String -> Map.Map Char Int
solve str = foldl (\acc x -> Map.insertWith (+) x 1 acc) Map.empty str

display :: Map.Map Char Int -> IO ()
display m = putStrLn $ unwords $ map (\x -> show $ Map.findWithDefault 0 x m) "ACGT"

main = do
    args <- getArgs
    inputStr <-
        if length args == 0
        then do putStrLn "Input file name isn't specified. Using test input line."
                return "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        else withFile (head args) ReadMode hGetLine
    display $ solve inputStr
