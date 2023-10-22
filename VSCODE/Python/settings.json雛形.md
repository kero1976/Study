# 1.全体サンプル

```
	"settings": {
		"python.venvFolders": [
			".venv"
		],
		"puthon.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
		"terminal.integrated.env.windows": {
			"PYTHONPATH": "${workspaceFolder}/src"
		},
		"files.exclude": {
			"**/.pytest_cache/**": true,
			"**/.venv/**": true,
			"**/__pycache__/**": true
		  }
	}
```


# 2.各項目説明

## 2-1.python.venvFolders

venvフォルダを指定

## 2-2.puthon.defaultInterpreterPath

各フォルダ毎にvenvを有効化

## 2-3.terminal.integrated.env.windows

python実行時にPythonの検索PATHを指定する。
※VSCODEのソース画面上ではこの値は反映されないので、.envファイルを作成する必要がある。

```
PYTHONPATH=src
```