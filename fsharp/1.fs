let lines = System.IO.File.ReadLines("1.input");;

let f x = 
    match x with 
        | "" -> None
        | x -> Some(int x)

let ints = lines |> Seq.map(f) |> Seq.toList

let rec biggestsum input (current:int) (biggest:int)  = 
    match input with
    | [] -> biggest
    | head::tail ->
        match head with
        | None -> biggestsum tail 0 (max biggest current)
        | Some x -> biggestsum tail (current + x) biggest

let result = biggestsum ints 0 0
