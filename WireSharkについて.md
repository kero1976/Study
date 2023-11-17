# 1. HTTPSの解析について

Chromeを使ってHTTPSでアクセスしたパケットの解析方法について記載する。

## 1-1. 設定方法1(WireSharkの設定)

1. [編集]-[設定]で設定画面を表示する
2. [Protocols]-[TLS]を選択
3. 「(Pre)-Master-Secret log filename」で任意のファイルを指定する
例として「C:\work\SSL\test.txt」を指定する。

## 1-2.設定方法2(Chromeの設定)

Chromeを「--ssl-key-log-file」オプション付きで指定する。
Cromeは以下の場所にインストールされていた。
C:\Program Files\Google\Chrome\Application

C:\Program Files\Google\Chrome\Application>chrome --ssl-key-log-file=C:\work\SSL\test.txt


# 2.表示フィルタ

## 2-1.リクエストの確認

自分のIPアドレス(*)で発信し、相手のポート番号は443

```
ip.src == 192.168.*.* && tcp.dstport == 443
```
