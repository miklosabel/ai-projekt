#!/urs/bin/env python
from subprocess import call
from pathlib2 import Path

import time
import os

home = os.path.expanduser("~")

#csinaljunk mindent a home konyvtarban
os.chdir(home)

#keszitsunk egy konyvtarat
workdir = Path("ujqhz1_ai_projekt")
if not workdir.exists():
    call(["mkdir", "ujqhz1_ai_projekt"])
else:
    print("Work directory exists, no need to make it again")

os.chdir("ujqhz1_ai_projekt")

#a kepek leszedese
# a userses oldalamra feltettem az internetrol letoltott es atdolgozott
# tanuloadatokat
# ezeket szedjuk le curllel
trdata = Path("training_data.tgz")
if not trdata.is_file():
    print("Downloading training images\n")
    call(["curl", "-O",
      "http://users.itk.ppke.hu/~mikab/ai_projekt/training_data.tgz" ])
    print("Training data downloaded successfully\n")
else:
    print("No need to download training data again\n")

# Kepek kicsomagolasa
extracted = Path("Images")
if not extracted.exists():
    print("Extracting training images\n")
    time.sleep(2)   # nem fontos de jobban olvashato a terminalban hogy mi
                    # tortenik
    call(["tar", "xvzf", "training_data.tgz"])
    print("Training images extracted")
else:
    print("No need to extract training images again\n ")

#Retrain script letoltese
call(["curl", "-LO", "https://github.com/tensorflow/hub/raw/r0.1/examples/image_retraining/retrain.py" ])

#ujratanitas - ez igenybe vesz kb 30 percet
print("RETRAINING - TAKES APPROXIMATELY 30 MINUTES")
time.sleep(5) # itt is csak hogy el lehessen ezt olvasni a terminalban
os.system('python retrain.py --image_dir Images')


