## 1-3.Python

### 1-3-1.インストール

「Python」をインストールする(一緒に「Pylance」もインストールされる)

### 1-3-2.Linter・Formatter
https://qiita.com/firedfly/items/00c34018581c6cec9b84
flake8をインストール
命名規則のチェックにはpep8-namingをインストールする

### 1-3-3.Document
autoDocstringという機能拡張を入れる

### 1-3-4.各フォルダにvenv環境を作成

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

venvFoldersの設定は無くても問題なし。
