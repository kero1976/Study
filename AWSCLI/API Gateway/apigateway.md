# V1 とV2の違い

V1はREST APIでV2はHTTP API。
V2の方が新しくできて機能が少ないが、安い。

## トリガーについて
ステートマシンを起動、その前のラムダ、APIGateway
EventBride
StepFunctions(前処理用ラムダ)

EventBride

## イベントバス
バケツ？


# Lambda統合について

* プロキシ統合
* 非プロキシ(カスタム)統合

の2種類がある。

## プロキシ統合

APIを作成してメソッドを作成する際に、