# Bella Ciao — sursa notelor (Ralph’s Vault, secțiunea Pian)

- **Melodia mâinii drepte**: partitura din articolul Wikipedia „Bella ciao” (en/it), scrisă în LilyPond, cu versurile aliniate la fiecare notă.
  Originalul e în Re minor; aplicația o transpune cu o cvintă în sus, în **La minor** (doar clape albe). Ritmul și silabele sunt cele din partitură.
- **Verificare**: începutul „Una mattina mi son svegliato” (Mi–La–Si–Do–La) coincide cu tutorialele Skoove și Piano Keyboard Guide;
  numărul de note (40) = numărul de silabe din versuri; ultima frază „e ho trovato l'invasor” cade pe tonică.
- **Mâna stângă**: aranjament simplificat făcut pentru începători (rădăcină + cvintă, acorduri Am – E – Dm). Nu e din partitura originală.
- Fișierul MIDI de pe celticscores.com a fost citit, dar are un aranjament diferit și nu a fost folosit pentru note.
- Datele melodiei sunt în `index.html`, constanta `SONGS.bella` (note, durate în timpi, silabe, acorduri).

## Hallelujah (Leonard Cohen) — de ce sunt doar acordurile
Melodia și versurile piesei sunt protejate de drepturi de autor, iar aplicația e publică pe GitHub Pages. De aceea secțiunea Pian are doar **acordurile strofei**
(C – Am – C – Am – F – G – C – G – C – F – G – Am – F – G – E7 – Am, în Do major) și un arpegiu simplu pentru mâna dreaptă: scheletul peste care se cântă piesa.
Acordurile sunt o progresie armonică, nu melodia. Nu s-au adăugat note de melodie și nici versuri.

## Oda bucuriei (Beethoven, 1824) — domeniu public
Melodia mâinii drepte (16 măsuri, Do major, doar clape albe) verificată cu tutorialul de pe piano-keyboard-guide.com: E E F G | G F E D | C C D E | E D D | … | D D E C | D E F E C | D E F E D | C D G.
Mâna stângă: aranjament simplificat (C și G). Ritmul „E D D” (pătrime cu punct + optime + doime) e cel clasic.

## Versiunea pe acorduri (la fiecare melodie)
În `index.html`: `SONGS.<melodie>.cv` (acordurile pe măsuri; „X→Y” = două acorduri într-o măsură) și tabela `PQ` (rădăcina acordului + notele lui).
Mâna stângă cântă rădăcina, mâna dreaptă un arpegiu. Progresul se salvează separat: cheile `c_rh`, `c_lh`, `c_both` (la melodie: `rh`, `lh`, `both`).
