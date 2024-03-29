# 1.インストール
https://slproweb.com/products/Win32OpenSSL.html

Windows環境でWin64OpenSSL_Light-3_2_0.exeをインストールした。
C:\Program Files\OpenSSL-Win64\bin\openssl.exe
がインストールされた。

# 2.証明書作成の流れ

## 2-1.RSAキーの生成

### 2-1-1.コマンド

openssl genrsa -out MyKey.key 2048

### 2-1-2.出力内容

```
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWqEaRhgjjBr9f
Gp1syswplq4w4SUZ8mjvEgADx/rT0rMXztp4fGDi4cNIXWAMoOMEB9A36XLHmM41
GVZg30cNHME6pF3mkEHTcG4MAjCQi78A+Rod8ki06Oj3LmMlRy3cl7HDShMHQ7Kh
dnsK8UpFNZTfWt/aO/+W4FMCFZSikqySBylgad1JjiyKsbD5XSwbY/6roiKCx5XT
/QBVmavXHgWrY7aNVDJLaVKJgv7XenA6UIvXp2SMZuslPxYyWVi/WI9xn5MpjPQO
biv9ajvFj/RyHaUJPSRBSc41oJgm9kxEr7rMb3h52FXpXBaNDnFX3OxSQpHfrsG6
oKefxl/ZAgMBAAECggEACl1ovukeb7vpLLHvzQuDzTRJ5/FPJdAXMggH+SbEXUsM
u8cQtIWo9fuZvtpHY4S3QYARFUoP8URXHKhDC/1sBF2RlP/PyuzHSOriXXEToD8n
M2hT0wNacGXYrerO/cNQmxi2DCx8+7pQm0xJx677+5iJPjm4mmSQRFxDldOt8CWX
Q9zq91a89YCV02cotWlobpvH/3zwt/w4QYVd3CcuhYREazVX4rZ+yWmv22ru7jm/
deG+wB7ux9a5pz1v/MLRPhn6j34m8I6tg1wPuoEvfd8VHindGxhkP7AfKGY66E+g
hZczQwx5lDtC9my7TdZKW3bNdiEv+bYZQuusHh6lqQKBgQD4EcPZiiP91SbOvgJS
rKP4rDsjD1W3Ywws0RUP6cZBWPaYOd7jIBV34/vjVh9iiujbyDfBNijdjUPSXf9m
yqPzVjSLhstA+gkKmJuqqEGxXO1XAlIbyznhQ51FAioIyjTRxghKQMzTE3fGFHFV
XTqiSKtls+s6pdLl0dzCN9FYnQKBgQDdhQ/A6S+5K7a9n6BaVHrsKYezlcA02Qhd
V7eSdQt2u5KAIfm3EVCQ6TrFTr/Yjgps9Q2d8iJaR2DIIFmYK+aU3RbbOmpPdWaz
yCEhYgcrtrH8gwJ78BvToQ6OQWL1P9UHXCx8yAGRpOx/rXa6q0TtnjUNCP4P15pV
k9QINXSpbQKBgQC4umnwvhjtNeRPQllyfVMhpAfppMq85Io1eYFIt1pGYVxIoZej
5Ml33RM/CGwYsr6So/c47v7hdQfTSOIfBrmuRDyexkLnYQqIlHofTGqXDE9FYtoI
Dn9Mi1A7ClCI+SL6L5EO0lB0wmOH4sM+wU0feiQAeUmrA78YGv5ctrozVQKBgCP5
XvSSKfjlW3jx+mWRAKFnoS0N7bfnYw9dlmdHcMQodAMxAU+0lSPjbHLsdgViE9lb
9okm8GM+4j292y72Oi0EtpiFpQwgYbxijNbSB54WvlLmp7me5bX5mtaJUdvIMP1P
/72H8ZFIekvFzNlFxRzdq3nhcvj5p4usRSvMGpUFAoGBAL2Ldn62urk8699aid9X
kyib/2ABz3XknRGoYJdLCfKhyRBBuxKMgkY1tMQu0K2GF4R6llPPOWjZJUNBSmny
d/rDaYn0Dc77rpN88PhLNoSZcjNcyTfKcB6cDWGv0E7cH0zpWxFdA+AnVNXxQfQW
WlQVh7xBWF+wFq77tTbAMWPv
-----END PRIVATE KEY-----

```


## 2-2.証明書署名要求（CSR）の作成

### 2-2-1.コマンド

openssl req -new -key MyKey.key -out MyCSR.csr

### 2-2-2.出力内容

```
-----BEGIN CERTIFICATE REQUEST-----
MIICkzCCAXsCAQAwTjELMAkGA1UEBhMCQUExCzAJBgNVBAgMAkJCMQswCQYDVQQH
DAJDQzELMAkGA1UECgwCREQxCzAJBgNVBAsMAkVFMQswCQYDVQQDDAJGRjCCASIw
DQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANaoRpGGCOMGv18anWzKzCmWrjDh
JRnyaO8SAAPH+tPSsxfO2nh8YOLhw0hdYAyg4wQH0DfpcseYzjUZVmDfRw0cwTqk
XeaQQdNwbgwCMJCLvwD5Gh3ySLTo6PcuYyVHLdyXscNKEwdDsqF2ewrxSkU1lN9a
39o7/5bgUwIVlKKSrJIHKWBp3UmOLIqxsPldLBtj/quiIoLHldP9AFWZq9ceBatj
to1UMktpUomC/td6cDpQi9enZIxm6yU/FjJZWL9Yj3GfkymM9A5uK/1qO8WP9HId
pQk9JEFJzjWgmCb2TESvusxveHnYVelcFo0OcVfc7FJCkd+uwbqgp5/GX9kCAwEA
AaAAMA0GCSqGSIb3DQEBCwUAA4IBAQBWz0VDgdMnBql07c4BDDH/UCzGXOd0L9QQ
J1tSz9W6FXofjWflSQ8vXtynNVXVoJhk61nlHmHqfdbnQfClwawwC1Y3AT5iib51
zup6PMjKXrYqK/LH/Jiw19Jsc33+khwExQ2HhQkeBOwJHcxAMEFGBknniWbzzF2Z
9k8QxGhKU/O/ssW/0YUXz5DgHw8Ds4WAUJ2viTWlnLiGiYn4RcHl/KUvFWUz1MtL
D84RkcBW7/zO2KPrWlrE4b1r0zRY9bOGKs29qpwk/5gyN7R1ambEv2FajJ2nFVDU
d6PlTDetixx5cJkvZRqPlu9r2mMwZz/L97nHG1sVhgLrv6rw7fT4
-----END CERTIFICATE REQUEST-----

```

## 2-3.自己署名証明書の作成

### 2-3-1.コマンド

openssl x509 -req -days 365 -in MyCSR.csr -signkey MyKey.key -out ExampleCert.crt

### 2-3-2.出力内容

```
-----BEGIN CERTIFICATE-----
MIIDSzCCAjOgAwIBAgIUPNSmWLqZN6/oCPzTY27zUAzrnWwwDQYJKoZIhvcNAQEL
BQAwTjELMAkGA1UEBhMCQUExCzAJBgNVBAgMAkJCMQswCQYDVQQHDAJDQzELMAkG
A1UECgwCREQxCzAJBgNVBAsMAkVFMQswCQYDVQQDDAJGRjAeFw0yNDAxMTMwOTA5
MzJaFw0yNTAxMTIwOTA5MzJaME4xCzAJBgNVBAYTAkFBMQswCQYDVQQIDAJCQjEL
MAkGA1UEBwwCQ0MxCzAJBgNVBAoMAkREMQswCQYDVQQLDAJFRTELMAkGA1UEAwwC
RkYwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDWqEaRhgjjBr9fGp1s
yswplq4w4SUZ8mjvEgADx/rT0rMXztp4fGDi4cNIXWAMoOMEB9A36XLHmM41GVZg
30cNHME6pF3mkEHTcG4MAjCQi78A+Rod8ki06Oj3LmMlRy3cl7HDShMHQ7KhdnsK
8UpFNZTfWt/aO/+W4FMCFZSikqySBylgad1JjiyKsbD5XSwbY/6roiKCx5XT/QBV
mavXHgWrY7aNVDJLaVKJgv7XenA6UIvXp2SMZuslPxYyWVi/WI9xn5MpjPQObiv9
ajvFj/RyHaUJPSRBSc41oJgm9kxEr7rMb3h52FXpXBaNDnFX3OxSQpHfrsG6oKef
xl/ZAgMBAAGjITAfMB0GA1UdDgQWBBQCyabFgp8fstPReikJvLYH7ch30jANBgkq
hkiG9w0BAQsFAAOCAQEAd7B2yTWuEpLTdu3p0aYkzIiTBMchYXuezjwuSGd/5r3a
nhnmSCE453hfD6lPkKlaPJ3m0AAcc9B09WhTShBI3ZyeaLxwaaeTFhEg/EqfRxlv
5O7MuoBmfEwrD6PRhY6wRpA2YURMOWg5pVcRNg9oySiBfZL3+nmI1pbLWhN4vRvL
+zmUTmqAMaaL20OvxS3fK9kZj/ktljhKvZEpkv0RBnPX2l55LL3lu0c9LG+e94RG
Viq/YMPxHe2GxB1eCXQCgoRF/cmEFVURtPWDtlPOJ/6lR3lzVLCz1rmG3Uqv+tHH
UkzhttvWNUXvTBdp0iNpwPRL1gW7Qu7ZSZDlAprIsg==
-----END CERTIFICATE-----

```



# 3.知識

## 3-1.証明書のタイプ

### 3-1-1.X509

証明書、プライベートキーなどは別。PEMの文字列ファイルなどあり。

### 3-1-2.PKCS#12

証明書と秘密キーが合わさったバイナリファイル。パスワードが必要。

### 3-1-3.PKCS#7

中間証明書を含めて配布可能な形式。
拡張子は.p7b or .spc

# 4.コマンド

## 4-1.X509ファイルに対してのコマンド

### 4-1-1.PEM形式からDERへの変換
openssl x509 -in <inputfile> -inform PEM -out <outfile> DER