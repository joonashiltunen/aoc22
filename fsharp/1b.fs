let lines = System.IO.File.ReadLines("1.input");;

let f x = 
    match x with 
        | "" -> None
        | x -> Some(int x)

let ints = lines |> Seq.map(f) |> Seq.toList

let calculateSums input =
    let rec sums input (current:int) (biggest:int list)  = 
        match input with
        | [] -> biggest
        | head::tail ->
            match head with
            | Some x -> sums tail (current + x) biggest
            | None -> sums tail 0 (current::biggest)
    sums input 0 []

let all = calculateSums ints
let sorted = List.sortBy(fun x -> -x) all

let result = sorted[0] + sorted[1] + sorted[2]
