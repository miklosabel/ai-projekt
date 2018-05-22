# ai-projekt: TÁBLAFELISMERŐ

A projekthez szükséges eszközök:

- python 2.7
- pip
- tensorflow (pip install "tensorflow>=1.7.0")
- tensorflow hub (pip install tensorflow-hub)
- python subprocess
- python pathlib2
- python time
- python os 

Az UJQHZ1_PR_HU.py szkript futtatásával letöltődik a tanulóhalmaz, letöltődik a tensorflow, és transfer learning technológiával újratanít egy képfelismerő neurális hálót, hogy az közlekedési táblákat ismerjen fel. Ezután lefut egy teszt, mely a python fájl 66. sorában előre megadott képet klasszifikálja. Alapesetben a giten lévő stoptáblát ábrázoló képpel tesztel.

Az egymás utáni tesztekhez a későbbiekben érdemes egy külön tesztszkriptet írni, ekkor nem ellenőrizné minden esetben a szükséges külső eszközök meglétét.
