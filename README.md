
# Allgemeines

Der Code ist sehr alt und ich habe ihn nur zum Laufen gebracht. Man kann ihn an einigen Stellen verbessern, aber es funktioniert erstmal. 
Allerdings ist er dementsprechend mäßig schnell :)

Für die Visualisierung wird nur ca. die Hälfte der Dateien genutzt. Die anderen laufen zwar, brauchen mehr manuellen Eingriff.

Ich habe die Beispieldateien der originalen Website dem Release hinzugefügt. Im Repo selbst ist nur *Alien* als Beispiel.   

# Nutzung

## Voraussetzungen

### pip

- opencv_python
- numpy
- scipy
- sklearn
- colormath

## Auswertung

Man benötigt eine Videodatei zum Analysieren.

Als erstes muss man ein Projekt erstellen:  
`python 01_1_new-project.py <voller Pfad zur Datei>`  
Der Pfad des neuen Projektes ist `projects/<Name der Datei ohne Endung>`

Der Rest ist automatisiert: `process_video.[bat/sh] <Pfad zum Projekt>` *!!ohne letzem Slash!!*

## Visualisierung

Die eigentliche Visualisierung passiert im Browser. Die Website dafür ist im Ordner `Site`.

Zum Starten der Website muss man einen Server nutzen. Am einfachsten ist es mit der Extension `Live Server`.
> Damit es funktioniert muss man den Site-Ordner mit VSCode direkt öffen. Ist das der Fall, kann man einfach auf `Go Live` in der unteren rechten Ecke drücken und es sollte funktionieren. 

Sollte der resultierende Kreis eine komische Größe haben, kann man das in `convert.py` ausgleichen, indem man `duration_factor` anpasst und `convert.py` erneut ausführt.

# Old Readme

This code is part of http://cinemetrics.fredericbrodbeck.de/

cinemetrics is about measuring and visualizing movie data, in order to reveal the characteristics of films and to create a visual "fingerprint" for them. Information such as the editing structure, color, speech or motion are extracted, analyzed and transformed into graphic representations so that movies can be seen as a whole and easily interpreted or compared side by side.

at the moment these tools lack proper documentation, sorry.

----------

make sure you have the opencv python bindings installed and that you are using the latest version.
