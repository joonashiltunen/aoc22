let lines = System.IO.File.ReadLines("2.input");;

let toChar (x:string) =
    Seq.map char (x.Split ' ')

let scaleNearZero (x:int seq) =
    x 
    |> Seq.toList
    |> fun a -> [a[0] - int 'A'; a[1] - int 'X']

let toScore (x:int list) =
    match x with
    | _ when x[0] = x[1] -> x[1] + 1 + 3
    | _ when (x[1] - x[0] + 3) % 3 = 1 -> x[1] + 1 + 6
    | _ -> x[1] + 1

let result = Seq.map (toChar >> Seq.map int >> scaleNearZero >> toScore) lines |> Seq.sum