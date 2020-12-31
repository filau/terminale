/*
Algorithme pour la question 2.b. du DM « Une histoire de spirale ».
Code réalisé par Firmin Launay (T°A).
*/

import 'dart:math'; // Importation de la bibliothèque « dart:math » pour utiliser la fonction « pow() » (puissance).

main() {
  int n = 0; // Définition du n initial.
  num lg_seg = 8*pow(1/2, n); // Définition et calcul de lₙ en fonction de n.

  while (lg_seg >= 0.05) { // Boucle qui continue à tourner tant que la longueur du segment [OMₙ] est supérieure à 0,05 cm.
    n += 1; // Incrémentation de n.
    lg_seg = 8*pow(1/2, n); // Calcul de lₙ en fonction de n.
  }

  final lg_seg_fr = "$lg_seg".replaceAll('.', ','); // Conversion de la longueur du segment [OMₙ] en écriture française.

  print("Pour n = $n, on ne peut plus distinguer O de Mₙ sur la représentation, la longueur du segment [OMₙ] étant alors de $lg_seg_fr cm."); // Affichage du résultat.
}
