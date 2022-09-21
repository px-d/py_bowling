# Bowling

## Instructions
Schreibe ein Programm mit TDD, um eine Partie Ten-Pin Bowling zu bepunkten.

- Diese online app kann helfen: http://www.bowlinggenius.com/
- Bowlingregeln: https://de.wikipedia.org/wiki/Bowlingregeln

Input: Ein string (siehe unten) stellt ein Bowlingspiel da

Ouput: Ein integer Score

## Rules

Jedes Bowlingspiel (oder "Line") umfasst zehn Runden (oder "Frames") für den Bowlingspieler.

In jedem Frame hat der Bowler bis zu zwei Versuche, alle zehn Pins umzuwerfen.

Wenn die erste Kugel in einem Frame alle zehn Pins umwirft, nennt man das einen "Strike". Der Frame ist beendet. Die Punktzahl für den Frame ist zehn plus die Summe der Pins, die mit den nächsten beiden Kugeln umgeworfen werden.

Wenn die zweite Kugel in einem Frame alle zehn Pins umwirft, nennt man dies einen "Spare". Der Frame ist beendet. Die Punktzahl für den Frame ist zehn plus die Anzahl der mit der nächsten Kugel umgeworfenen Pins.

Wenn nach beiden Bällen noch mindestens einer der zehn Pins steht, ist das Ergebnis für diesen Frame einfach die Gesamtzahl der in diesen beiden Bällen umgeworfenen Pins.

Wenn du im letzten (10.) Frame einen Spare erzielst, erhältst du eine weitere Bonuskugel. Wenn du im letzten (10.) Frame einen Strike erzielst, erhältst du zwei weitere Bonuskugeln. Diese Bonuskugeln werden in der gleichen Runde geworfen. Wenn ein Bonusball alle Pins umwirft, wird der Vorgang nicht wiederholt. Die Bonuskugeln werden nur zur Berechnung des Ergebnisses des letzten Frames verwendet.

Der Spielstand ist die Summe aller Frame-Punkte.

## Symbole
- X zeigt einen Streik an
- / zeigt einen Spare an
- \- zeigt ein Miss an
- | zeigt eine Frame begrenzung an
- Die Zeichen nach dem || bezeichnen Bonuskugeln
  
## Errors
Da ich leider absolut keine Ahnung habe, wie man Fehler in doctest "erwartet" gibt das Programm `-1` zurück, wo normalerweise ein Fehler geworfen worden wäre.

## Beispiele
- X|X|X|X|X|X|X|X|X|X||XX Zehn Strikes mit der ersten Kugel aller zehn Frames. Zwei Bonuskugeln, beide Strikes. Punkte für jeden Frame = 10 + Punkte für die nächsten zwei Kugeln = 10 + 10 + 10 = 30 Gesamtpunktzahl = 10 Frames x 30 = 300

- 9-|9-|9-|9-|9-|9-|9-|9-|9-|9-|| Neun Pins werden mit dem ersten Ball aller zehn Frames getroffen. Die zweite Kugel jedes Frames verfehlt den letzten verbleibenden Pin. Keine Bonuskugeln. Punkte für jeden Frame = 9 Gesamtpunktzahl = 10 Frames x 9 = 90

- 5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5 Fünf Pins auf der ersten Kugel in allen zehn Frames. Die zweite Kugel eines jeden Frames trifft alle fünf verbleibenden Pins, ein Spare. Eine Bonuskugel, die fünf Pins trifft. Punkte für jeden Frame = 10 + Punkte für die nächste Kugel = 10 + 5 = 15 Gesamtpunktzahl = 10 Frames x 15 = 150

- X|7/|9-|X|-8|8/|-6|X|X|X||81 Total score = 167