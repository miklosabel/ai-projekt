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

Az UJQHZ1_PR1_HU.py szkript futtatásával letöltődik a tanulóhalmaz, letöltődik a tensorflow, és transfer learning technológiával újratanít egy képfelismerő neurális hálót, hogy az közlekedési táblákat ismerjen fel. 

Az UJQHZ1_PR2_HU.py szkript lenne a tesztelésre írt fájl, de ez egyelőre nem működik. Az újratanítás tehát sikeres, de tesztelni az interneten található parancsokkal lehet:

```       
curl -LO https://github.com/tensorflow/tensorflow/raw/master/tensorflow/examples/label_image/label_image.py
python label_image.py \
--graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt \
--input_layer=Placeholder \
--output_layer=final_result \
--image=$HOME/flower_photos/daisy/21652746_cc379e0eea_m.jpg
```

A --image kapcsolóval lehet a klasszifikálandó képet kiválasztani.

A projektet a [https://www.tensorflow.org/tutorials/image_retraining](https://www.tensorflow.org/tutorials/image_retraining) oldalon leírtak alapján készítettem.
