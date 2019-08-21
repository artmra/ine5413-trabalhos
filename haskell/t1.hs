potencia :: Int -> Int -> Int
potencia x y =
    x ^ (y)

main = do
    print("insira x: ")
    x <- getLine
    let xinteiro = (read x :: Int)
    print("insira y: ")
    y <- getLine
    let yinteiro = (read y :: Int)
    print(potencia xinteiro yinteiro)
