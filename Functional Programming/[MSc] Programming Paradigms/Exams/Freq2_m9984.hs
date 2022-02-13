{-# LANGUAGE FlexibleContexts #-}
import Control.Monad.State;
{-- 
Nome: João Brito
Numero: m9984
--}

{-Questao 1
a) i, ii e v
b) ii
-}

{--Questao 2 --}
--a) 
fa :: Num t => [t] -> [t] -> [t]
fa xs ys = pure (*2) <*> ([(+)] <*> xs <*> ys)

--b)
--fb :: [Maybe Int] -> [Maybe Int]
--fb xs = (((+2) <$>) <$>) <$> xs

--fb :: [[Maybe Int]] -> [[Maybe Int]]
--fb xs = (((+2) <$>) <$>) <$> xs

--c) 
--i) Just 0
--ii) Nothing
{-
--d)
f :: Int -> [Int]
f x = [x * x]
-- o comando certo seria sem o pure: f <$> [1,2,3]

{-- Fim da Questao 2--}

{-- Questao 3 --}
--a) Adicionar no co'digo abaixo suporte para o operador Sqr 
data Expr = Val Int | Add Expr Expr | Sqr Expr --deriving Show
type Stack = [Int]
type Code = [Op]
data Op = PUSH Int | ADD | SQR deriving Show 

eval :: Expr -> Int       
eval (Val n) = n
eval (Add n m) = eval n + eval m
eval (Sqr n) = eval n * eval n

exec :: Code -> Stack -> Stack
exec [] s = s
exec (PUSH n:rc) s = exec rc (n:s)
exec (ADD: c) (m:n:s) = exec c (n+m:s) 
exec (SQR: c) (n:s) = exec c (n*n:s)

comp :: Expr -> Code
comp (Val n) = [PUSH n]
comp (Add n m) = comp n ++ comp m ++ [ADD]
comp (Sqr n) = comp n ++ [SQR]

--Exemplos (descomentar exemplos para testar apo's implementacao do Sqr):
expr1 :: Expr
expr1 = Add (Sqr (Val 3)) (Val 2)  --Valor: 11  

expr2 :: Expr
expr2 = Add (Sqr (Add (Sqr (Val 3)) (Val 2))) (Sqr (Val 4))  --Valor: 137

--b)
{-- Assumir a propriedade da distributividade:
        exec (c ++ d) s = exec d (exec c s)
 
 A equacao que exprime a correccao do compilador para qualquer stack s e':
    exec (comp e) s = eval e: s

Prova para Sqr x:
exec (comp (Sqr x)) s
={definição de "comp"}
exec (comp x ++ [SQR]) s
={distributividade}
exec [SQR] (exec (comp x) s)
={HI}
= exec [SQR] (eval x: s)
={definição de "exec"}
= exec [] (eval x)*(eval x):s
{definição de exec}
= (eval x)*(eval x):s
= {definição de eval}
eval (Sqr x): s
--}

--c) 

instance Show (Expr) where
    show (Val e)        = show e
    show (Add e1 e2)    = "(" ++ show e1 ++ " + " ++ show e2 ++ ")"
    show (Sqr e)        = "(" ++ show e ++ "^2)"

--d)
data ExprP a = ValP a | AddP (ExprP a) (ExprP a) deriving Show

--Exemplo:
exprP1 :: ExprP Int
exprP1 = AddP (ValP 3) (ValP 2)

instance Functor ExprP where
    fmap f (ValP n) = ValP (f n)
    fmap f (AddP a b) =  AddP (fmap f a) (fmap f b)

instance Applicative ExprP where
    pure = ValP
    ValP f <*> x = fmap f x
    AddP f g <*> s = AddP (f <*> s) (g <*> s) 

--Declarar Expr como instancia de Monad:

instance Monad ExprP where
    (ValP x) >>= f   = f x
    (AddP x y) >>= f = AddP (x >>= f) (y >>= f)
    return x         = ValP x

--e) 
{-- Prova das 3 leis mona'dicas:

LEI 1: (return x) >>= f = f x
PROVA:
return x >>= f
= {definição de "return"}
ValP x >>= f
= {definição de "ValP"}
f x


LEI 2: m >>= return = m
PROVA: 
CASO BASE:
(ValP x) >>= return
= {definição de ">>="}
return (ValP x)
= {definição de "return"}
Valp x

PASSO DE INDUÇÃO:
(AddP x y) >>= return
= {definição de ">>="}
AddP (x >>= return) (y >>= return)
= {HI}
AddP x y

LEI 3: (m >>= f) >>= h = m >>= (\x-> f x >>= h)
CASO BASE:
(ValP x >>= f) >>= g

--}


{-- Fim da Questao 3 --}

-}
{-- Questao 4 --}
data EstadoContas = EJ {c1::Int, c2::Int} deriving Show

estadoInicial :: EstadoContas
estadoInicial = EJ {c1=0,c2=0}

-- Implementar o programa:
banca :: StateT EstadoContas IO()
banca = do conta_a_depositar <- get
           if (conta_a_depositar/= 0 && conta_a_depositar/= 1 && conta_a_depositar/= 2) then (liftIO$putStrLn "Input inválido, tente de novo!")
           else 
                if(conta_a_depositar==1) then
                    do 
                        (liftIO$putStrLn "Insira o montante:")
                        n <- liftIO $ getLine
                        montante <- read n :: Int
                        montante_disponivel <- c1 conta_a_depositar
                        if((montante_disponivel-montante)<0) then (liftIO$putStrLn "Saldo insuficiente!")
                        else put conta_a_depositar {c1=montante_disponivel-montante}
                        banca
                else 
                    if(conta_a_depositar==2) then
                        do 
                            (liftIO$putStrLn "Insira o montante:")
                            n <- liftIO $ getLine
                            montante <- read n :: Int
                            montante_disponivel <- c2 conta_a_depositar
                            if((montante_disponivel-montante)<0) then (liftIO$putStrLn "Saldo insuficiente!")
                            else put conta_a_depositar {c2=montante_disponivel-montante}
                            banca
          
main = runStateT banca estadoInicial

{-- Fim da Questao 4 --}

{-- Questao 5 --}
data Arv a = Folha a | Nodo (Arv a) (Arv a)

tamanho :: Arv a -> Int
tamanho (Folha a)  = 1
tamanho (Nodo a b) = tamanho a + tamanho b

balanceada :: Arv a -> Bool
balanceada (Folha x)   = True
balanceada (Nodo e d) = tamanho e == tamanho d
                        && balanceada e
                        && balanceada d
                        
espelhar :: Arv a -> Arv a
espelhar (Folha a) = Folha a
espelhar (Nodo a b) = Nodo (espelhar b) (espelhar a)

{-- Assumir as definicoes acima e a propriedade:
        tamanho (espelhar t) = tamanho t
 
Provar que:
        balanceada (espelhar t) = balanceada t
usando inducao sobre a 'arvore t.
 
CASO BASE
balanceada (espelhar (Folha a))
= {definição de "espelhar"}
balanceada (Folha a)

PASSO DE INDUÇÃO
balanceada (espelhar (Nodo a b))
= {definição de "espelhar"}
balanceada (Nodo (espelhar b) (espelhar a))
= {definição de "balanceada"}
tamanho (espelhar b) == tamanho (espelhar a) && balanceada (espelhar b) && balanceada (espelhar a)
= {sabemos que tamanho (espelhar b) == tamanho b e tamanho (espelhar a) == tamanho a}
tamanho b == tamanho a && balanceada (espelhar b) && balanceada (espelhar a)
= {HI}
tamanho b == tamanho a && balanceada b && balanceada a
= {comutatividade de "==" e "&&"}
tamanho a == tamanho b && balanceada a && balanceada b
= {definição de "balanceada"}
balanceada (Nodo a b)

--}       
{-- Fim da Questao 5 --}