#!/urs/bin/env python
from subprocess import call
from pathlib2 import Path

import time

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

# tensorflow leszedese
#az aktualis konyvtarba leszedi a gites tensorflow konyvtarszerkezetet
tf_dir = Path("tensorflow")
if not tf_dir.is_dir():
    print("Downloading tensorflow transfer learning\n")
    call(["git", "clone", "https://github.com/tensorflow/tensorflow"])
    print("Tensorflow transfer learning lib is on!\n")
else:
    print("No need to download tensorflow transfer learning lib again.\n")

#tensowflow konyvtarba lepes
# check = call(["pwd"])
# if tf_dir.exists():
#         call(["cd", check])
# else:
#     print("ERROR: Tensorflow directory doesn't exits!\n")

#call(["git", "checkout", "{version}"])

# utolso reteg ujratanitasa
retrain = Path("tensorflow/examples/image_retraining/retrain.py")
img = Path("../Images")
print(img)

if retrain.exists():
    print("Retraining last layer: \n")
    call("python tensorflow/tensorflow/examples/image_retraining/retrain.py --image_dir ../Images", shell=True)
    print("Last layer successfully retrained")
else:
    print("ERROR: tensorflow/examples/image_retraining/retrain.py not exists!\n")

