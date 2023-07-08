# Volumn

## 1.はじめに

ローカルとコンテナ内のフォルダのマッピング
パスが長い方が優先される

## 2.Volumeの種類

* Anonymous Volumes
* Named Volumes
* Bind Mounts

## 3. Anonymous Volumes
匿名ボリューム。Dockerが内部で管理し、ローカルのフォルダとマッピングできない。
名前付きボリュームの中で、一部上書きしたくない場合などに、匿名ボリュームで上書きする。

## 4. Named Volumes
Dockerfile内では指定できないので、コンテナの実行時に名前付きボリュームを作成する。
-v <名前>:<コンテナ内の永続化したいフォルダ>