module Aula3 where
import Prelude hiding (and,concat,replicate,(!!),elem,merge)

-- CHAPTER 4
-- question 1a
safetail xs = if null xs then [] else tail xs

-- question 1b
safetail2 xs | (null xs) = []
             | otherwise = tail xs 

-- question 1c
safetail3 :: [a] -> [a] 
safetail3 (x:xs) = xs
safetail3 _ = []

-- question 2a
logical_or :: Bool -> Bool -> Bool
logical_or False False = False 
logical_or _ _ = True

-- question 3
logical_and :: Bool -> Bool -> Bool
logical_and b1 b2 = if(b1==True) then (if(b2==True) then True else False) else False

-- question 4
logical_and2 :: Bool -> Bool -> Bool
logical_and2 b1 b2 = if(b1==True) then b2 else False

-- CHAPTER 5
-- question 1
sum_of_squares :: Int -> Int
sum_of_squares n = sum [x^2 | x <- [1..n]]

-- question 2
pyths :: Int -> [(Int,Int,Int)]
pyths n = [(x,y,z) | x <-[1..n], y <-[1..n], z <-[1..n], x^2 + y^2 == z^2]

-- question 3
perfects :: Int -> [Int]
perfects n = [z | z <- [1..n], sum [x | x <- [1..z-1], z `mod` x == 0] == z]

-- question 4
scalar :: Num a => [a] -> [a] -> a
scalar a b = sum [a*b | (a,b) <- (zip a b)]

-- CHAPTER 6
-- question 1a
and :: [Bool] -> Bool
and [] = False
and [x] = x
and (x:xs) = if(x==True) then and xs else False

-- question 1b
concat :: [[a]] -> [a]
concat [] = []
concat (x:xs) = x ++ concat xs

-- question 1c
replicate :: Int ->  a -> [a]
replicate 0 a = []
replicate n a = [a] ++ replicate (n-1) a

-- question 1d
(!!) :: [Int] -> Int -> Int
(!!) [] _ = -1
(!!) (x:xs) 0 = x
(!!) (x:xs) n = (!!) xs (n-1)

-- question 1e
elem :: Eq a => a -> [a] -> Bool
elem n [] = False
elem n (x:xs) = if(n==x) then True else elem n xs

-- question 1f
merge :: Ord a => [a] -> [a] -> [a]
merge [] [] = []
merge x [] = x
merge [] y = y
merge (x:xs) (y:ys) = if(x<=y) then [x] ++ merge xs (y:ys) else [y] ++ merge (x:xs) ys

-- question 2
msort :: Ord a => [a] -> [a]
msort [x] = [x]
msort x = merge (msort (take ((length x) `div` 2) x)) (msort ((drop ((length x) `div` 2) x)))

-- question 3
euclid :: Int -> Int -> Int
euclid a b = if a==0 then b else euclid (b `mod` a) a