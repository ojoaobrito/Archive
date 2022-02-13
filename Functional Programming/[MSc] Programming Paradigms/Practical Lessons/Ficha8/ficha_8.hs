import Prelude hiding(putStr)
import Control.Monad (replicateM)


newtype ZipList a = Z [a] deriving Show

instance Functor ZipList where 
    -- fmap :: (a -> b) -> ZipList a -> ZipList b
    fmap f (Z l) = Z (fmap f l)





















-- exercício 1
{-- 
NOTE:
sequence_ []     = return ()
sequence_ (a:as) = do a
                   sequence as
--}
putStr_n :: String -> IO ()
putStr_n s = sequence_ [putChar x | x <- (s ++ "\n")]

putStr :: String -> IO ()
putStr s = sequence_ [putChar x | x <- s]

-- exercício 2
aux :: Int -> Int -> IO ()
aux total 0 = putStr_n ("The total is " ++ (show total))
aux total tot_num = getLine >>= (\x -> aux (total + (read x::Int)) (tot_num-1))

adder :: IO ()
adder = putStr "How many numbers? " >> getLine >>= (\x -> aux 0 (read x::Int))

-- exercício 3
adder2 :: IO ()
adder2 = do putStr "How many numbers? "
            x <- getLine
            nums <- sequence (replicate (read x) getLine)
            putStr_n ("The total is " ++ (show (sum (map read nums))))