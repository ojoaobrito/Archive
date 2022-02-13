s{-# LANGUAGE FlexibleContexts #-}
import Control.Monad.State;
{-- 
Nome:
Numero:
--}


{-Questao 1
a) i, ii
b) ii, iii, iv, v
c) i
-}

{- Questao 2
Por inducao em n, n>=0, e para todo o x
Hipotese de Inducao: compL (replica n x) = n

*Caso Base: 0
compL (replica 0 x)
={definicao de replica}
compL []
={definicao de compL}
0

*Passo de Inducao: n+1
compL (replica (n+1) x)
={definicao de replica}
compL (x:(replica n x))
={definicao de compL}
1 + compL(replica n x)
= {Hipotese de Inducao}
1 + n
={+ e' comutativo}
n + 1
--}

{--Questao 3 --}
--Defini todas como funcoes (mesmo as que nao eram pedidas como funcoes) para poderem executar o codigo  
--a) 
f3a :: IO [Char]
f3a = putStrLn "Introduza um valor" >> getLine >>= \x -> putStrLn "Introduza outro valor" >> getLine >>= \y -> return (x++" "++y)

--b)
f3b :: Num t => [t] -> [t] -> [t]
f3b l1 l2 = [(*),(+),(-)] <*> l1 <*> l2

--c) 
f3c :: [Maybe Int] -> Maybe [Int]
f3c l = sequence (((+1) <$>) <$> l)

--d) Nothing

--e) 
f :: Int -> Maybe Int
f x = Just (x*2)

f3e :: [Int] -> [Maybe Int]
f3e l = pure f <*> l

--outra possibilidade:
f3e_ :: [Int] -> [Maybe Int]
f3e_ l = f <$> l

{-- Fim da Questao 3--}

{-- Questao 4 --}
--a)
data Expr = Val Int | Add Expr Expr | Mult Expr Expr
type Stack = [Int]
type Code = [Op]
data Op = PUSH Int | ADD | MULT deriving Show 

eval :: Expr -> Int       
eval (Val n) = n
eval (Add n m) = eval n + eval m
eval (Mult n m) = eval n * eval m

exec :: Code -> Stack -> Stack
exec [] s = s
exec (PUSH n:rc) s = exec rc (n:s)
exec (ADD: c) (m:n:s) = exec c (n+m:s) 
exec (MULT: c) (m:n:s) = exec c (n*m:s)

comp :: Expr -> Code
comp (Val n) = [PUSH n]
comp (Add n m) = comp n ++ comp m ++ [ADD]
comp (Mult n m) = comp n ++ comp m ++ [MULT]

--b) 
{-- A equacao que exprime a correccao do compilador e'
        exec (comp e) s = eval e: s 
para qualquer stack s.
Assumir a propriedade da distributividade:
        exec (c ++ d) s = exec d (exec c s)
 --}
{--Prova para Mult faz parte do passo de Inducao:

exec (comp Mult n m) s 
={definicao de comp}
exec (comp n ++ comp m ++ [MULT]) s
={associatividade de ++}
exec (comp n ++ (comp m ++ [MULT])) s
={distributividade}
exec (comp m ++ [MULT]) (exec (comp n) s)
={Hipotese de Inducao}
exec (comp m ++ [MULT]) (eval n : s)
={distributividade}
exec [MULT](exec (comp m) (eval n : s))
={Hipotese de Inducao}
exec [MULT] (eval m : eval n : s)
={definicao de exec}
(eval n * eval m : s)
={definicao de eval}
eval(Mult n m): s
--}

{-- Questao 5 --}
--Possivel solucao
data EstadoJogo = EJ {j1::Int,j2::Int,jogador::Bool} deriving Show -- Assumo True joga J1, False joga J2

jogoInicial = EJ {j1=0,j2=0,jogador=True}

jogo :: StateT EstadoJogo IO()
jogo = do actual <- get
          let jogaP1 = jogador actual
          if (jogaP1) then (liftIO$putStrLn "Jogador 1:") else (liftIO $ putStrLn "Jogador 2:")
          n <- liftIO $ getLine
          let num = read n :: Int
          let p1 = j1 actual
          let p2 = j2 actual
          unless(num <=0) (if (jogaP1) then put actual {j1=p1+num, jogador = not jogaP1} else put actual {j2=p2+num, jogador = not jogaP1})
          if (num <= 0) then liftIO $ putStrLn "Fim!" else jogo
          
main = runStateT jogo jogoInicial


{--Questao 6--}
data Arv a = Folha a | Nodo (Arv a) (Arv a) --deriving Show --(deixar descomentado ate' ao ex. d)

--Exemplos de arvores
arv1 = Nodo (Nodo (Folha 1) (Folha 2)) (Folha 3)
arv2 = Nodo (Nodo (Folha 4) (Nodo (Folha 1) (Folha 3))) (Nodo (Folha 2) (Folha 5))

folhas :: Arv a -> [a]
folhas (Folha a)  = [a]
folhas (Nodo a b) = folhas a ++ folhas b

tamanho :: Arv a -> Int
tamanho (Folha a)  = 1
tamanho (Nodo a b) = tamanho a + tamanho b

--ou (mas o anterior e' melhor para as questoes seguintes)
tamanho_ :: Arv a -> Int
tamanho_ a  = length (folhas a)

--b)
espelhar :: Arv a -> Arv a
espelhar (Folha a) = Folha a
espelhar (Nodo a b) = Nodo (espelhar b) (espelhar a) 

--c)
{--Provar que 
    tamanho (espelhar t) = tamanho t 
por Inducao sobre t    

Hipotese de Inducao: tamanho (espelhar t) = tamanho t 

Caso Base: Folha a
tamanho (espelhar (Folha a))
={definicao de espelhar}
tamanho (Folha a)

Passo de Inducao: Nodo a b  (Assumir valido para a e b, tamanho(espelhar a) = tamanho a, tamanho(espelhar b) = tamanho b)
tamanho (espelhar Nodo a b)
={definicao de espelhar}
tamanho(Nodo (espelhar b) (espelhar a))
={definicao de tamanho}
tamanho(espelhar b) + tamanho(espelhar a)
={Hipotese de Inducao}
tamanho(b) + tamanho(a)
={+ e' comutativa}
tamanho(a) + tamanho(b)
={definicao de tamanho (DE)}
tamanho(Nodo a b)

--}

--d) remover o deriving Show se estiver no tipo de Arv, caso contrario da' erro de "Overlapping instances do Show (Arv a)"
instance Show a => Show (Arv a) where
    show (Folha a) = show a 
    show (Nodo a b) = "("++show a ++ "--*--"++ show b++")"

--e)
instance Functor Arv where
  fmap f (Folha a)       = Folha $ f a
  fmap f (Nodo t1 t2) = Nodo (fmap f t1) (fmap f t2)



instance Applicative Arv where
  pure = Folha
  Folha f       <*> t            = f <$> t
  Nodo t1 t2 <*> Folha a       = Nodo (fmap ($ a) t1) (fmap ($ a) t2)
  Nodo t1 t2 <*> Nodo t3 t4 = Nodo (t1 <*> t3) (t2 <*> t4)


instance Monad Arv where
  return a = Folha a
  Folha a >>= f = f a 
  Nodo a b >>= f = Nodo (a >>= f) (b >>= f)

--Exemplo
fa :: Num a => a -> Arv a
fa x =  Folha (x+1)

runExemplo = arv1 >>= fa

{-- Provas das Leis Monadicas - Nao era pedido no teste, foi feito na aula de duvidas.
Lei 1: (return x) >>= f = f x
return x >>= f
={def. return}
(Folha x) >>= f
={def. >>=}
f x

Lei 2: m >>= return = m
Inducao sobre m:

Caso Base: Folha a
Folha a >>= return 
={def. >>=}
return a
={def. return}
Folha a

Passo de Inducao: Nodo a b (assumir para a e b i.e. a >>= return = a e b>>=return b)
Nodo a b >>= return
={def. >>=}
Nodo (a >>= return) (b >>= return)
={HI}
Nodo a b


Lei 3: (m >>= f) >>= g    =     m >>= (\x->f x >>= g)
 Caso base: Folha a
(Folha a >>= f) >>= g
={def. >>=}
f a >>= g

(Folha a) >>= (\x -> f x >>= g)
={def. >>=}
(\x -> f x >>= g) a
={aplicacao de funcao}
f a >>= g

Passo de Inducao: Nodo a b (assumimos para a e b: (a >>= f) >>= g = a >>= (\x -> fx >>= g)) 
(Nodo a b >>= f) >>= g
={def. >>=}
(Nodo (a >>= f) (b>>=f)) >>= g
={def. >>=}
Nodo ((a >>= f) >>= g) ((b >>= f) >>= g)
={HI}
Nodo (a >>= (\x -> f x >>= g)) (b >>=(\x -> fx >>= g))
={def. >>= (1) (DE)}
Nodo a b >>= (\x -> fx >>= g)

-- Definicao 1: Nodo a b >>= f = Nodo (a >>= f) (b >>= f)

--}