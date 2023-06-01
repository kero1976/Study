# 1.コマンド

## 1-1.diffを使って差分のサマリ情報の取得
git diff --stat タグ名・コミットID
git diff --numstat タグ名・コミットID

### numstatの見方
先頭に追加した行数・削除した行数のサマリが表示される

# 2.ファイル

## 2-1.空フォルダを削除しない

「.gitkeep」という空ファイルを配置しておく。

## 2-2.管理対象外の設定

「.gitignore」というファイルを作成する。
その中に管理対象外のファイルやフォルダを記載する。

# 3.トラブルシュート

## 3-1.文字化け

git config --global core.quotepath false
git config --global core.pager "LESSCHARSET=utf-8 less"
