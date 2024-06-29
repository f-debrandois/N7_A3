open Encodage
open Chaines

(* Saisie des mots sans le mode T9 *)
(* Pour marquer le passage d'un caractère à un autre, on utilise la touche 0 *)


(* index : char −> char list −> int
  Fonction qui renvoie l'index du caractère c dans la liste liste.
  Paramètre c : char, le caractère à chercher.
  Paramètre liste : char list, la liste dans laquelle chercher le caractère.
  Résultat : un entier, l'index du caractère c dans la liste liste.
*)

let rec index c liste =
  match liste with
    |[]   -> failwith("Erreur : caractère non reconnu")
    |t::q ->  if t = c then 1 (* On commence à 1 pour les touches *)
              else 1 + index c q


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
    | (touche,lettres)::q -> 
      if List.mem lettre lettres then (* Si la lettre est dans la liste de la touche *)
        (touche, (index lettre lettres))
      else (* Sinon on continue la recherche *)
        aux q lettre 
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
    | "" -> lst (* Si le mot est vide, on renvoie la liste des touches *)
    | s -> 
      let lettre = s.[0] in (* On prend le premier caractère du mot *)
      let (touche, nombre) = encoder_lettre enc lettre in (* On encode la lettre *)
      let ajout = List.init nombre (fun _ -> touche) (* On ajoute le nombre de fois la touche à la liste *)
      in
      aux enc (String.sub s 1 ((String.length s) - 1)) (lst @ ajout @ [0]) (* On ajoute la touche 0 pour marquer le passage à la lettre suivante *)
  in
  aux enc mot []

let%test _ = encoder_mot t9_map "bonjour" = [2; 2; 0; 6; 6; 6; 0; 6; 6; 0; 5; 0; 6; 6; 6; 0; 8; 8; 0; 7; 7; 7; 0]
let%test _ = encoder_mot t9_map "abcaik" = [2; 0; 2; 2; 0; 2; 2; 2; 0; 2; 0; 4; 4; 4; 0; 5; 5; 0]



(* decoder_lettre : encodage -> (int * int) -> char
   Fonction qui identifie la lettre saisie à partir d’une touche et du nombre de fois qu’elle a été pressée.
   Paramètre enc : encodage, l’encodage utilisé.
   Paramètre (touche, nombre) : (int * int), la touche et le nombre de fois qu’elle a été pressée.
   Résultat : le caractère correspondant.
*)

let decoder_lettre enc (touche, nombre) =
  let rec aux enc (touche, nombre) =
    match enc with
    | [] -> failwith "Erreur : touche non reconnue" (* Touche non reconnue *)
    | (t, lettres)::q ->
      if t = touche then (* Si la touche est la bonne *)
        List.nth lettres (nombre - 1) (* On renvoie la lettre correspondante *)
      else (* Sinon on continue la recherche *)
        aux q (touche, nombre)
  in
  aux enc (touche, nombre)

let%test _ = decoder_lettre t9_map (2, 1) = 'a'
let%test _ = decoder_lettre t9_map (2, 2) = 'b'
let%test _ = decoder_lettre t9_map (2, 3) = 'c'
let%test _ = decoder_lettre t9_map (3, 1) = 'd'
let%test _ = decoder_lettre t9_map (3, 2) = 'e'
let%test _ = decoder_lettre t9_map (3, 3) = 'f'
let%test _ = decoder_lettre t9_map (9, 1) = 'w'
let%test _ = decoder_lettre t9_map (9, 2) = 'x'
let%test _ = decoder_lettre t9_map (9, 3) = 'y'
let%test _ = decoder_lettre t9_map (9, 4) = 'z'


(* split : int list -> (int * int) list
   Fonction qui découpe une liste d'entiers en une liste de listes d'entiers où chaque liste contient une touche et le nombre de fois qu'elle a été pressée.
   Paramètre lst : int list, la liste à découper.
   Résultat : une liste de listes d'entiers où chaque liste contient une touche et le nombre de fois qu'elle a été pressée.
*)

let split lst =
  let rec aux (current, lst) item =
    match item with (* On regarde la valeur de l'item *)
    | 0 -> ([], lst@[current]) (* Si c'est 0, on renvoie la liste courante et on vide la liste courante *)
    | _ -> (item::current, lst) (* Sinon on ajoute l'item à la liste courante *)
  in
  let (current, total_list) = List.fold_left aux ([], []) lst in (* On applique la fonction aux à tous les éléments de la liste *)
  let result = total_list@[current] in (* On ajoute la dernière liste courante à la liste des résultats *)
  let final_list = List.filter (fun x -> x <> []) result in (* On enlève les listes vides *)
  List.map (fun lst -> (List.hd lst, List.length lst)) final_list (* On renvoie la liste des listes avec le premier élément et sa longueur *)


let%test _ = split [2; 2; 0; 6; 6; 6; 0; 6; 6; 0; 5; 0; 6; 6; 6; 0; 8; 8; 0; 7; 7; 7; 0] = [(2, 2); (6, 3); (6, 2); (5, 1); (6, 3); (8, 2); (7, 3)]



(* decoder_mot : encodage -> int list -> string
   Fonction qui identifie le mot saisi à partir d’une suite de touches.
   Paramètre enc : encodage, l’encodage utilisé.
   Paramètre touches : int list, la suite de touches.
   Résultat : le mot correspondant à la suite de touches.
*)

let decoder_mot enc touches =
  let lst_char = List.map (decoder_lettre enc) (split touches) in (* On décode chaque touche *)
  String.of_seq (List.to_seq lst_char) (* On transforme la liste de caractères en chaîne de caractères *)

let%test _ = decoder_mot t9_map [2; 2; 0; 6; 6; 6; 0; 6; 6; 0; 5; 0; 6; 6; 6; 0; 8; 8; 0; 7; 7; 7; 0] = "bonjour"
let%test _ = decoder_mot t9_map [2; 0; 2; 2; 0; 2; 2; 2; 0; 2; 0; 4; 4; 4; 0; 5; 5; 0] = "abcaik"
