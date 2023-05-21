# VENVについて

## 作成するコマンド
1. プロジェクトの直下に移動する。(srcやtestがあるのと同じ階層)
2. python -m virtualenv venv
3. これでvenvフォルダが作成される
4. .\venv\Scripts\Activate.ps1 

## ライブラリのインストール
1. requirements.txtファイルをsrcやvenvと同じ階層に作成する
2. pip install -r requirements.txt

## activate.ps1でのエラー
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

## pip installでのエラー対応
ERROR: Can not perform a '--user' install. User site-packages are not visible in this virtualenv.
上記のエラーが発生した場合は、
venvの下にできた「pyvenv.cfg」ファイルにある、「include-system-site-packages」の値をfalseからtrueに変更する

### requirements.txt
バージョン指定が無い場合はライブラリ名のみ指定する
バージョンを固定化したい場合は「ライブラリ名 == バージョン」とする

# ログについて


# テストについて

# コーディングルールについて

## blackについて
VSCODEのライブラリもあるが、pip installでインストールした場合の使い方について記載する
