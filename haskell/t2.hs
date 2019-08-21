modulo :: Int -> Int
modulo x =
    if x < 0 then
        x * (-1)
    else
        x

main = do
    print("insira x: ")
    x <- getLine
    let xinteiro = (read x :: Int)
    print(modulo xinteiro)
