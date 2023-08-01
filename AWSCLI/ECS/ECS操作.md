# タスクの作成

1. 左側のツリーから、[Amazon ECS] - [タスク定義]を選択
2. タスク名を選択
3. 最新のリビジョンを選択し、「新しいリビジョンの作成」

# run-taskとstart-taskの違い
run-taskは単一の実行で、start-taskはFARGATEが管理して複数実行する。


## CLIコマンド一覧

### 1.ECSクラスタ一覧表示

aws ecs list-clusters
aws ecs list-clusters --output text

### 2.ECSクラスター詳細情報

タスクやサービスの情報は表示されない
aws ecs describe-clusters --cluster $CLUSTER_NAME_OR_ARN
aws ecs describe-clusters --cluster $CLUSTER_NAME_OR_ARN --output text

### 3.ECSサービス一覧表示
aws ecs list-services --cluster $CLUSTER_NAME_OR_ARN
aws ecs list-services --cluster $CLUSTER_NAME_OR_ARN --output text

### 4.ECSサービス詳細表示
aws ecs describe-services --cluster $CLUSTER_NAME_OR_ARN --services $ECS_SERVICE_ARN

### 5. ECSタスクの一覧表示
aws ecs list-tasks --cluster $CLUSTER_NAME_OR_ARN --service-name $ECS_SERVICE_ARN
手動でrun-taskしたのが表示されなかったが、--service-nameを削除したら表示された。

