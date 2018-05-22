#!/urs/bin/env python
from subprocess import call
from pathlib2 import Path

import subprocess 
import time
import os

home = os.path.expanduser("~")

os.chdir(home)
os.chdir("ujqhz1_ai_projekt")


#kimeneti graf es kimeneti cimkek mentese
#ezek tartalmazzak az uj modellt es az ujratanitott kategoriakat
# tmp_file = "/tmp/output_graph.pb"
# renamed_file_1 = home+"/ujqhz1_ai_projekt/output_files/output_graph.pb"
# os.rename(tmp_file, renamed_file_1)
#
# tmp_file = "/tmp/output_labels.txt"
# renamed_file_2 = home+"/ujqhz1_ai_projekt/output_files/output_labels.txt"
# os.rename(tmp_file, renamed_file_2)

#ezutan klasszifikaljuk a tesztkepunket
# ehhez le kell kotorni tesztszkriptet
call(["curl", "-LO", "https://github.com/tensorflow/tensorflow/raw/master/tensorflow/examples/label_image/label_image.py"])

#kivalasztani a megfelelo kepet
IMG_TEST = home+"/ujqhz1_ai_projekt/stop.jpg"

#majd futtatni a szkriptet
TEST_RESULT = subprocess.check_output("python label_image.py --graph=renamed_file_1 --labels=renamed_file_2 --input_layer=PlaceHolder --output_layer=final_result --image=IMG_TEST", stderr=subprocess.STDOUT, shell=True)

print(TEST_RESULT)

#kategoriak kijelzese
# if TEST_RESULT == 00000:
#     printOutResult("20as tabla")
# if TEST_RESULT == 00001:
#     printOutResult("30as tabla")
# if TEST_RESULT == 00002:
#     printOutResult("50es:- tabla")
# if TEST_RESULT == 00003:
#     printOutResult("60as tabla")
# if TEST_RESULT == 00004:
#     printOutResult("70es tabla")
# if TEST_RESULT == 00005:
#     printOutResult("80as tabla")
# if TEST_RESULT == 00006:
#     printOutResult("80as korlatozas vege tabla")
# if TEST_RESULT == 00007:
#     printOutResult("100as tabla")
# if TEST_RESULT == 00008:
#     printOutResult("120as tabla")
# if TEST_RESULT == 00009:
#     printOutResult("elozni tilos")
# if TEST_RESULT == 00010:
#     printOutResult("teherautoval elozni tilos")
# if TEST_RESULT == 00011:
#     printOutResult("utkeresztezodes alarendelt uttal")
# if TEST_RESULT == 00012:
#     printOutResult("foutvonal")
# if TEST_RESULT == 00013:
#     printOutResult("elsobbsegadas kotelezo")
# if TEST_RESULT == 00014:
#     printOutResult("stop")
# if TEST_RESULT == 00015:
#     printOutResult("mindket iranybol behajtani tilos")
# if TEST_RESULT == 00016:
#     printOutResult("teherautoval behajtani tilos")
# if TEST_RESULT == 00017:
#     printOutResult("behajtani tilos")
# if TEST_RESULT == 00018:
#     printOutResult("veszelyes hely")
# if TEST_RESULT == 00019:
#     printOutResult("veszelyes utkanyarulat balra")
# if TEST_RESULT == 00020:
#     printOutResult("veszelyes utkanyarulat jobbra")
# if TEST_RESULT == 00021:
#     printOutResult("egymas utani veszelyes utkanyarulatokj")
# if TEST_RESULT == 00022:
#     printOutResult("egyenetlen utfelulet")
# if TEST_RESULT == 00023:
#     printOutResult("csuszos ut")
# if TEST_RESULT == 00024:
#     printOutResult("utszukulet")
# if TEST_RESULT == 00025:
#     printOutResult("utkarbantartas")
# if TEST_RESULT == 00026:
#     printOutResult("jelzolampa")
# if TEST_RESULT == 00027:
#     printOutResult("gyalogosok")
# if TEST_RESULT == 00028:
#     printOutResult("gyerekek")
# if TEST_RESULT == 00029:
#     printOutResult("kerekparosok")
# if TEST_RESULT == 00030:
#     printOutResult("jegesedesveszely")
# if TEST_RESULT == 00031:
#     printOutResult("vadallatok")
# if TEST_RESULT == 00032:
#     printOutResult("mozgo jarmuvekre vonatkozo tilalmak vege")
# if TEST_RESULT == 00033:
#     printOutResult("kotelezo haladasi irany jobbra")
# if TEST_RESULT == 00034:
#     printOutResult("kotelezo haladasi irany balra")
# if TEST_RESULT == 00035:
#     printOutResult("kotelezo haladasi irany egyenesen")
# if TEST_RESULT == 00036:
#     printOutResult("kotelezo haladasi irany egyenesen vagy jobbra")
# if TEST_RESULT == 00037:
#     printOutResult("kotelezo haladasi irany egyenesen vagy balra")
# if TEST_RESULT == 00038:
#     printOutResult("kerulesi irany jobbra")
# if TEST_RESULT == 00039:
#     printOutResult("kerulesi irany balra")
# if TEST_RESULT == 00040:
#     printOutResult("korforgalom")
# if TEST_RESULT == 00041:
#     printOutResult("elozni tilos vege")
# if TEST_RESULT == 00042:
#     printOutResult("kamionnal elozni tilos vege")
#
def printOutResult(result):
    print("A teszt eredmenye: " + result) 
