(*  Exercice à rendre **)
(*  TO DO : contrat *)
let pgcd a b = 
  let rec aux a b = 
     if a = b then
        a
     else if a < b then
        aux a (b-a)
     else
        aux (a-b) b
  in
  if a = 0 || b = 0 then
    if a = 0 && b = 0 then
      failwith "Les nombres doivent être non nuls"
    else
      if a = 0 then
        b
      else
        a
  else
    aux (abs a) (abs b)
