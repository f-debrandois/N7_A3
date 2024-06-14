open Encodage
open Chaines

(* Saisie des mots sans le mode T9 *)
(* Pour marquer le passage d'un caractère à un autre, on utilise la touche 0 *)


(* encoder_lettre : encodage −> char −> ( int * int )
Fonction qui qui indique la touche et le nombre de fois
qu’il faut appuyer dessus pour saisir la lettre passée en paramètre.
Paramètre enc : encodage, l’encodage utilisé.
Paramètre lettre : char, la lettre à encoder.
Résultat : un couple (touche, nombre) où touche est le numéro de la touche
sur laquelle se trouve la lettre et nombre est le nombre de fois qu’il faut appuyer
sur cette touche pour saisir la lettre.
*)

let encoder_lettre enc lettre =
  let rec aux enc lettre =
    match enc with
    | [] -> failwith "Erreur : caractère non reconnu" (* Caractère non reconnu *)
    | (touche,lettres)::q -> let rec aux2 lettres lettre index = (* On cherche la lettre dans la liste de lettres associée à la touche *)
                    match lettres with
                    | [] -> aux q lettre (* Si on ne trouve pas la lettre, on passe à la touche suivante *)
                    | t::q -> if t = lettre then (touche,index) else aux2 q lettre (index + 1) (* Si on trouve la lettre, on renvoie la touche et l'index de la lettre *)
                    in
    aux2 lettres lettre 1
  in
  aux enc lettre

let%test _ = encoder_lettre t9_map 'a' = (2, 1)
let%test _ = encoder_lettre t9_map 'b' = (2, 2)
let%test _ = encoder_lettre t9_map 'c' = (2, 3)
let%test _ = encoder_lettre t9_map 'd' = (3, 1)
let%test _ = encoder_lettre t9_map 'e' = (3, 2)
let%test _ = encoder_lettre t9_map 'f' = (3, 3)
let%test _ = encoder_lettre t9_map 'w' = (9, 1)
let%test _ = encoder_lettre t9_map 'x' = (9, 2)
let%test _ = encoder_lettre t9_map 'y' = (9, 3)
let%test _ = encoder_lettre t9_map 'z' = (9, 4)


(* encoder_mot : encodage −> string −> int list
Fonction qui calcule la suite de touche à presser pour saisir un mot passé en paramètre.
Paramètre enc : encodage, l’encodage utilisé.
Paramètre mot : string, le mot à encoder.
Résultat : une liste d’entiers représentant les touches à presser pour saisir le mot.
*)

let encoder_mot enc mot =
  let rec aux enc mot lst =
    match mot with
    | "" -> lst
    | s -> 
      let lettre = s.[0] in
      let (touche, nombre) = encoder_lettre enc lettre in
      let ajout = List.init nombre (fun _ -> touche) in
      aux enc 
       (lst @ ajout @ [0])
  in
  aux enc mot []

let%test _ = encoder_mot t9_map "bonjour" = [2; 2; 0; 6; 6; 6; 0; 6; 6; 0; 5; 0; 6; 6; 6; 0; 8; 8; 7; 7; 7; 0]
