# 1.コマンド

## 1-1.diffを使って差分のサマリ情報の取得
git diff --stat タグ名・コミットID
git diff --numstat タグ名・コミットID

### numstatの見方
先頭に追加した行数・削除した行数のサマリが表示される

## 1-2.特定のファイルのみ絞り込み
最後に「*.java」などを指定すればOK。特にパラメータの指定は不要。

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

## sjisのdiffで文字化け
プロジェクトのルートディレクトリに「.gitattributes」ファイルを作成する。
「.git」フォルダの中ではないので注意！
中に拡張子と文字コードを書けばＯＫ。
```
*.ps1 diff=cp932
```

## .gitattributesの確認方法

```
git check-attr --all <file-path>
```

何も表示されなかったら、正しく設定されていないことになる。

## 3-2.変更の取り消し(rebert)

https://hiro8blog.com/revert-commits-all-at-once/

git revert コミットログA...コミットログB --no-edit
...を書くことによりAからBまでの範囲を一度に戻すことが可能。ただしちょっと指定方法に注意が必要なので、URLを確認すること

## 3-3.不要なブランチの削除

### 不要なローカルブランチをすべて削除する

git branch |%{ git branch -D $_.trim() }

### ローカルのリモートブランチの情報を更新

git remote prune origin

## 3-4.誰がブランチを作成したかの確認

git for-each-ref --format='%(committerdate) %09 %(authorname) %09 %(refname)'

## 3-4.ソースを修正した人の確認

git blame ファイル名
