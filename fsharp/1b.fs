let lines = System.IO.File.ReadLines("1.input");;

let ints = 
    lines 
    |> Seq.map (fun x ->
                match x with 
                | "" -> None
                | x -> Some(int x)) 
    |> Seq.toList

let calculateSortedSums input =
    let rec sums input current biggest  = 
        match input with
        | [] -> biggest
        | head::tail ->
            match head with
            | Some x -> sums tail (current + x) biggest
            | None -> sums tail 0 (current::biggest)
    sums input 0 [] |> List.sortBy(fun x -> -x)

let sortedSums = calculateSortedSums ints

let result = sortedSums[0] + sortedSums[1] + sortedSums[2]
