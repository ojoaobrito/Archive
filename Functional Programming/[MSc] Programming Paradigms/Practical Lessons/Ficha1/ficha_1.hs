module Aula1 where
 
-- CHAPTER 2
-- question 1
double_f :: Int -> Int
double_f x = x + x

-- question 2
n = a `div` length xs
    where
        a = 10
        xs = [1,2,3,4,5]

-- question 3
last_f [] = 0
last_f xs = reverse xs !! 0

-- question 4
last_f_2 [] = -1
last_f_2 [x] = x
last_f_2 x = last_f xs
    where
        xs = tail x

-- question 5
init_f [] = []
init_f [x] = []
init_f (h:xs) = [h] ++ init_f xs

-- CHAPTER 3
-- question 1
-- [’a’,’b’,’c’]  :: [Char]
-- (’a’,’b’,’c’) :: (Char, Char, Char)
-- [(False,’0’),(True,’1’)] :: [(Bool, Char)]
-- ([False,True],[’0’,’1’]) :: ([Bool],[Char])
-- [tail,init,reverse] :: [[a] -> [a]]

-- question 2
second xs = head (tail xs) -- :: [a] -> a
swap (x,y) = (y,x) -- :: (a,b) -> (b,a)
pair x y = (x,y) -- :: a -> b -> (a,b)
double x = x*2 -- :: Num a => a -> a
palindrome xs = reverse xs == xs -- :: [a] -> Bool
twice f x = f (f x) -- :: (a -> a) -> a -> a

-- question 4
product_f [] = -1
product_f [x] = x
product_f (x:xs) = x * (product_f xs)

-- question 5
reverse_f [] = []
reverse_f [x] = [x]
reverse_f (x:xs) = reverse_f xs ++ [x]