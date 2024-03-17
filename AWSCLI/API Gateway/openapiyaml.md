# 第一階層

* tags
* paths
* components

## paths

第2階層に実際のAPIのパス
第3階層にget,post,put,delete

### 第4階層

* summary
* description
* parameters
* requestBody(POSTのみ)
* response
* security
* tags
* x-amazon-apigateway-integration
* x-amazon-apigateway-request-vaqlidator

### 第4階層のoperationIdとtagsについて

tagsは第1階層に指定したものと同じ
operationIdはユニークな値
