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

## その他

### コマンドパレットの表示
Ctrl + Shift + P

### マークダウンの表示
Ctrl + Shift + V

