open Encodage
open Chaines

(* Saisie des mots en mode T9 *)

(* encoder_lettre : encodage -> char -> int
   Fonction qui indique la touche associée à la lettre passée en paramètre.
   Paramètre enc : encodage, l’encodage utilisé.
   Paramètre lettre : char, la lettre à encoder.
   Résultat : un entier représentant la touche associée à la lettre.
*)

let encoder_lettre enc lettre =
  let rec aux enc lettre =
    match enc with
    | [] -> failwith "Erreur : caractère non reconnu" (* Caractère non reconnu *)
    | (touche, lettres)::q ->
      if List.mem lettre lettres then (* Si la lettre est dans la liste de la touche *)
        touche
      else (* Sinon on continue la recherche *)
        aux q lettre
  in
  aux enc lettre

let%test _ = encoder_lettre t9_map 'a' = 2
let%test _ = encoder_lettre t9_map 'b' = 2
let%test _ = encoder_lettre t9_map 'c' = 2
let%test _ = encoder_lettre t9_map 'd' = 3
let%test _ = encoder_lettre t9_map 'e' = 3
let%test _ = encoder_lettre t9_map 'f' = 3
let%test _ = encoder_lettre t9_map 'w' = 9
let%test _ = encoder_lettre t9_map 'x' = 9
let%test _ = encoder_lettre t9_map 'y' = 9
let%test _ = encoder_lettre t9_map 'z' = 9

(* encoder_mot : encodage -> string -> int list
   Fonction qui calcule la suite de touche à presser pour saisir un mot passé en paramètre.
   Paramètre enc : encodage, l’encodage utilisé.
   Paramètre mot : string, le mot à encoder.
   Résultat : une liste d’entiers représentant les touches à presser pour saisir le mot.
*)

let encoder_mot enc mot =
  List.map (encoder_lettre enc) (List.of_seq (String.to_seq mot)) (* On convertit le mot en liste de caractères et on applique encoder_lettre à chaque caractère *)

let%test _ = encoder_mot t9_map "bonjour" = [2; 6; 6; 5; 6; 8; 7]


(* Définition du type dico *)
type dico = Noeud of (string list * (int * dico) list)

(* Constante représentant un dictionnaire vide *)
let empty : dico = Noeud ([], [])


(* ajouter : encodage -> dico -> string -> dico
    Fonction qui ajoute un mot dans le dictionnaire.
    Paramètre enc : encodage, l’encodage utilisé.
    Paramètre d : dico, le dictionnaire dans lequel ajouter le mot.
    Paramètre mot : string, le mot à ajouter.
    Résultat : le dictionnaire avec le mot ajouté.
*)

let ajouter enc d mot =
  let touches = encoder_mot enc mot in (* On encode le mot *)
  let rec aux touches (Noeud (mots, fils)) =
    match touches with
    | [] -> Noeud (mot::mots, fils) (* Si on a fini de parcourir les touches, on ajoute le mot *)
    | t::q ->
      match List.assoc_opt t fils with (* On cherche si la touche est déjà dans les fils *)
      | None -> Noeud (mots, (t, aux q empty)::fils) (* Si la touche n'est pas dans les fils, on l'ajoute *)
      | Some dico -> Noeud (mots, (t, aux q dico)::(List.remove_assoc t fils)) (* Sinon on remplace le fils par le nouveau dico *)
  in
  aux touches d


let%test _ = ajouter t9_map empty "bonjour" = Noeud([],[(2,Noeud([],[(6,Noeud([],[(6,Noeud([],[(5,Noeud([],[(6,Noeud([],[(8,Noeud([], [(7, Noeud (["bonjour"], []))]))]))]))]))]))]))])


(* creer_dico : encodage -> string -> dico
    Fonction qui crée un dictionnaire à partir d'un fichier
    Paramètre enc : encodage, l’encodage utilisé.
    Paramètre nom_fichier : string, le chemin d'accès du fichier.
    Résultat : le dictionnaire créé.
*)

let creer_dico enc nom_fichier =
  let read_file nom_fichier =
    let ic = open_in nom_fichier in (* On ouvre le fichier en lecture *)
    let rec aux d =
      try
        let mot = input_line ic in (* On lit une ligne *)
        aux (mot::d) (* On ajoute le mot à la liste *)
      with End_of_file -> close_in ic;  (* On ferme le fichier *)
      List.rev d (* On renverse la liste *)
    in
    aux []
  in
  List.fold_left (ajouter enc) empty (read_file nom_fichier) (* On ajoute chaque mot du fichier dans le dictionnaire vide *)


(* supprimer : encodage -> dico -> string -> dico
    Fonction qui supprime un mot du dictionnaire.
    Paramètre enc : encodage, l’encodage utilisé.
    Paramètre d : dico, le dictionnaire dans lequel supprimer le mot.
    Paramètre mot : string, le mot à supprimer.
    Résultat : le dictionnaire avec le mot supprimé.
*)

let supprimer enc d mot =
  let touches = encoder_mot enc mot in (* On encode le mot *)
  let rec aux touches (Noeud (mots, fils)) =
    match touches with
    | [] -> Noeud (List.filter (fun x -> x <> mot) mots, fils) (* Si on a fini de parcourir les touches, on supprime le mot *)
    | t::q ->
      match List.assoc_opt t fils with (* On cherche si la touche est dans les fils *)
      | None -> Noeud (mots, fils) (* Si la touche n'est pas dans les fils, on ne fait rien *)
      | Some dico -> let new_fils = List.map (fun (k, v) -> if k = t then (k, aux q v) else (k, v)) fils in (* Sinon on supprime le mot dans le fils *)
      let new_fils = List.filter (fun (_, Noeud (m, f)) -> not (m = [] && f = [])) new_fils in (* On supprime les fils vides *)
      Noeud (mots, new_fils) (* On renvoie le nouveau dico *)
in
aux touches d

let%test _ = supprimer t9_map (ajouter t9_map empty "bonjour") "bonjour" = empty


(* appartient : encodage -> dico -> string -> bool
    Fonction qui teste si un mot appartient au dictionnaire.
    Paramètre enc : encodage, l’encodage utilisé.
    Paramètre d : dico, le dictionnaire à tester.
    Paramètre mot : string, le mot à tester.
    Résultat : true si le mot appartient au dictionnaire, false sinon.
*)

let appartient enc d mot =
  let touches = encoder_mot enc mot in (* On encode le mot *)
  let rec aux touches (Noeud (mots, fils)) =
    match touches with
    | [] -> List.mem mot mots (* Si on a fini de parcourir les touches, on teste si le mot est dans la liste *)
    | t::q ->
      match List.assoc_opt t fils with (* On cherche si la touche est dans les fils *)
      | None -> false (* Si la touche n'est pas dans les fils, le mot n'est pas dans le dico *)
      | Some dico -> aux q dico (* Sinon on continue la recherche *)
  in
  aux touches d

let%test _ = appartient t9_map (ajouter t9_map empty "bonjour") "bonjour" = true


(* coherent : encodage -> dico -> bool
    Fonction qui teste si un dictionnaire est cohérent : Un dictionnaire n’est cohérent pour un encodage donné, que si tous les mots dans un noeud sont cohérents avec le chemin qui y mène.
    Paramètre enc : encodage, l’encodage utilisé.
    Paramètre d : dico, le dictionnaire à tester.
    Résultat : true si le dictionnaire est cohérent, false sinon.
*)
