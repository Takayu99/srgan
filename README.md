# SRGAN

SRGAN (Super Resolution Generative Adversarial Network)のkerasを用いた実装．

参考論文  
"Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network"  
 Christian Ledig, Lucas Theis, Ferenc Huszar, Jose Caballero, Andrew Cunningham, Alejandro Acosta, Andrew Aitken, Alykhan Tejani, Johannes Totz, Zehan Wang, Wenzhe Shi; Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 4681-4690
 
# DEMO
 サーモカメラを用いて高解像度化を行った例．  
 学習には自前のサーモ画像データセットを使用した．
 
左の画像：高解像度化前  
右の画像：高解像度化後

<img src=https://user-images.githubusercontent.com/84695613/119312493-67192f80-bcad-11eb-8908-f662048d3387.png widh=320px height=240px> &nbsp;  <img src="https://user-images.githubusercontent.com/84695613/119312526-70a29780-bcad-11eb-99a4-618aec0aecd3.png" widh=320px height=240px>


# Features
 
 160×120pxの入力画像を，640×480pxに拡大して出力する．
 
# Requirement
 
* keras　2.2.4
* tensorflow-gpu　1.14.0
 
# Usage
 
### 学習  train.py
学習用画像をimages/trainフォルダに入れる．画像サイズは640×480px．  
epochs: エポック数  
batch_size:　バッチサイズ  
interval:　h5ファイルを出力する間隔．intervalで指定したepoch数が経過するごとにh5ファイルを保存する．  
 
```python
train(epochs = 3000, batch_size = 1, interval = 300)
```


### 実行　generate.py
weightsフォルダに保存されたh5ファイルを読み込む．  
```python
generator = load_model('weights/weight.h5')
```


images/srcフォルダに入力画像を入れ，プログラムを実行．（入力画像解像度：160×120px）  
高解像度化処理を行った画像がimages/dstフォルダに出力される．  
```python
files = glob.glob("images/src/*.png")
```
