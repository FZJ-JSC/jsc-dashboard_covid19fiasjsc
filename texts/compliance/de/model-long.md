#### **Die Fragestellung**
Erste Versuche, die Ausbreitung einer neuartigen Infektionskrankheit zu verlangsamen, beinhalten die Einführung von Maßnahmen zur Reduzierung der Kontakte innerhalb der Bevölkerung. Die Wirksamkeit dieser Maßnahmen wird unter anderem durch den Grad der Compliance in der Bevölkerung bestimmt, d.h. wie viele Personen sich tatsächlich an die Vorschriften halten. Dabei stellt sich die Frage, **ob es wirksamer ist, sehr strikte Maßnahmen einzuführen**, die möglicherweise **nur von einem kleinen Teil der Bevölkerung befolgt werden**, **oder moderate Maßnahmen zu beschließen**, die wahrscheinlich **von einem größeren Teil der Bevölkerung befolgt werden**. CoSiMo-Webtool-Benutzer\*innen können diese Frage mit dem hier bereitgestellten Simulationstool beantworten.

---

#### **Das Modell**
Das zugrunde liegende mathematische Modell wurde mit Bezug auf die Ausbreitung von COVID-19 in der deutschen Bevölkerung entwickelt. Die Simulation beginnt mit einem Zeitraum milder Kontrollmaßnahmen, die von der gesamten Bevölkerung gleichermaßen umgesetzt werden. Die Reproduktionszahl für diesen Zeitraum beträgt 1,5, was zu einem allmählichen Anstieg der Infektionszahlen führt. Um die Infektionswelle effektiv einzudämmen, ist eine Reproduktionszahl unter 1 erforderlich. Zu einem bestimmten Zeitpunkt (als Tag 0 bezeichnet, bestimmt durch das Erreichen von 20.000 gemeldeten Fällen pro Tag in einer Bevölkerung von 83 Millionen) werden in der Simulation zusätzliche Kontaktbeschränkungen eingeführt (Intervention). Das Modell berücksichtigt detektierte (daher gemeldete) und nicht-detektierte infektiöse Personen.

Für weitere Informationen zum mathematischen Hintergrund, siehe hier:

Barbarossa, M.V.; Fuhrmann, J.  
Compliance with NPIs and Possible Deleterious Effects on Mitigation of an Epidemic Outbreak, Preprints 2021,  
https://www.preprints.org/manuscript/202102.0178/v2

---

#### **Das Webtool**
CoSiMo-Webtool Benutzer\*innen können (i) die Schärfe der Maßnahmen (*Schärfe der Maßnahmen*) und (ii) den Anteil der Bevölkerung auswählen, der die zusätzlichen Maßnahmen einhält (*Compliance-Level*). Benutzer*innen können anschließend wählen, welche Informationen aus dem Modell (z. B. gemeldete Neuinfektionen, kumulative Infektionen oder Gesamtzahl der Todesfälle) sie visualisieren möchten. Auf diese Weise können die Benutzer*innen beobachten, wie sich der Verlauf des Ausbruchs ab dem Zeitpunkt der Intervention entwickelt.

---

**Disclaimer**: In der Realität werden verschiedene Personen die Maßnahmen in unterschiedlichem Maße umsetzen. Im, diesen Simulationen zugrunde liegenden, mathematischen Modell wird die Population vereinfachend in zwei Gruppen unterteilt, wobei eine Gruppe die neuen Maßnahmen vollständig befolgt („compliant“), während die andere Gruppe ihr Verhalten nach Einführung der zusätzlichen Einschränkungen nicht ändert („non-compliant“). Des Weiteren wurde angenommen, dass, in der hier beobachteten Zeitspanne (bis 5 Wochen nach Intervention), niemand von einer Gruppe („compliant“ oder „non-compliant“) zur anderen wechselt.

