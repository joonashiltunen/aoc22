let lines = System.IO.File.ReadLines("2.input");;

let toChar (x:string) =
    Seq.map char (x.Split ' ')

let scaleNearZero (x:int seq) =
    x 
    |> Seq.toList
    |> fun a -> [a[0] - int 'A'; a[1] - int 'X']

let toScore (x:int list) =
    let opponent = x[0]
    let goal = x[1]

    if goal = 1 then opponent + 1 + 3
    elif goal = 2 then (opponent + 1) % 3 + 1 + 6
    else (opponent + 2) % 3 + 1

let result = Seq.map (toChar >> Seq.map int >> scaleNearZero >> toScore) lines |> Seq.sum
