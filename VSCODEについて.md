# 1.設定

## 1-1.保存場所

### ユーザー設定ファイル
Windows %APPDATA%\Code\User\settings.json
https://daeudaeu.com/vscode-settings-json/

### ワークスペース設定ファイル
プロジェクトルート/.vscode/settings.json

## 1-2.日本語化

### 言語パックのインストール

1. 「Extensions」を選択しする
2. 検索欄に「Jap」と入力すれば「Japanese Language Pack VS Code」が表示されるのでインストールする
3. 再起動する

### 言語の切り替え

1. コマンドパレットを表示する
2. displayを入力する
3. 「Configure Display Language」を選択する
4. 言語が表示されるので、日本語を選択

### テキストファイルの文字化け対応
VSCODE右下に「UTF-8」と現在の文字コードが指定されているので、クリックして「エンコード付きで再度開く」を指定する。

## 1-3.Python

### インストール

「Python」をインストールする(一緒に「Pylance」もインストールされる)

### Linter・Formatter
https://qiita.com/firedfly/items/00c34018581c6cec9b84
flake8をインストール
命名規則のチェックにはpep8-namingをインストールする

### Document
autoDocstringという機能拡張を入れる

### 各フォルダにvenv環境を作成

各フォルダにvenvフォルダを作成し、それぞれの環境でvenvが自動で適用される用にする。
ワークスペースにそれぞれのフォルダを追加して、ワークスペースのsetting.jsonに以下を記載する。

```
	"settings": {
		"python.venvFolders": [
			".venv"
		],
		"puthon.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe"
	}
```

## 1-4.Java

### インストール

以下のサイトからJava Coding Packをインストールする
https://code.visualstudio.com/docs/java/java-tutorial

2023/5/21時点の最新は0.4.1

### Javaプロジェクトの作成

1. コマンドパレットを表示する
2. 「Java」を入力する
3. 「Create Java Project」を選択する
4. 「Maven」を選択する
5. 「

# コマンド

## 検索

### ファイル名の検索

ctrl + P


## 置換

### 小文字化
https://creating-homepage.com/archives/9596

## その他

### コマンドパレットの表示
Ctrl + Shift + P

### マークダウンの表示
Ctrl + Shift + V

### 折りたたみ
Ctrl + K Ctrl + 数値(階層レベル）
再帰的に折りたたみ・展開
Ctrl + K Ctrl + [ or ]

### 折りたたみ(任意の場所)
VSCODE 1.70以上必要。
Ctrl + K Ctrl + ,(折りたたみ)
Ctrl + K Ctrl + .(展開)

### 矩形選択
始点をクリックしてから、終点を［Shift］＋［Alt］＋左クリック（したままドラッグ）
