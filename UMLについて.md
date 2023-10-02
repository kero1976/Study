# UMLについて

## 1.インストール

UMLの作成はPlantUMLを使用することにする。
内部でJavaを使用しているため、JDKをインストールしている必要がある。

### 1-1.VSCODEの設定

以下をインストールする。

* PlantUML
* Markdown Preview Enhanced

### 1-2.PlantUMLサーバがありません。"Plantuml.server"でサーバを指定してください。

「Markdown Preview Enhanced」をインストールしたら解決した。

## 2.基本的な図の書き方
「@startuml」と「@enduml」の間に内容を記述する。
「Alt+D」で表示する。

## 3.クラス図

### CompositionとAggregationとアソシエーション

関連 (Association)
集約 (Aggregation)
合成集約 (Composition)
関連＞集約＞合成集約

集約：関連において２つのモデルの間に「束ねるもの」「束ねられるもの」の関係があれば集約となります。「構成する」とも読み替えられます。

各モデルはそれぞれ独立しており、「束ねるもの」が消えたとしても「束ねられるもの」は残り続けます。

合成集約
集約の中でさらにモデル同士のライフサイクルが同じものを合成集約といいます。

「束ねるもの」が消えると「束ねられるもの」も消えるケースです。

## 4.シーケンス図

https://plantuml.com/ja/class-diagram

