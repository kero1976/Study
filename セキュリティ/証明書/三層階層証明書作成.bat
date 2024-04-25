@echo off

set BASE=c:\work\openssl
set ROOT_SUBJECT=/CN=test.root.com/OU=B/O=A/ST=Tokyo/C=JP
set CA_SUBJECT=/CN=test.ca.jp/OU=B/O=A/ST=Tokyo/C=JP
set WEB_SUBJECT=/CN=test.web.jp/OU=B/O=A/ST=Tokyo/C=JP
set PKCS12_PASSWORD=P@ssw0rd

echo 作業フォルダを作成します。
mkdir %BASE%\self_ca

mkdir %BASE%\self_ca\RCA
mkdir %BASE%\self_ca\ICA
mkdir %BASE%\self_ca\server

echo ================================================================
echo 1.Create Root CA
echo ================================================================
cd %BASE%\self_ca\RCA

echo 1-1.Create Root CA Directory
mkdir demoCA
mkdir demoCA\certs
mkdir demoCA\crl
mkdir demoCA\newcerts
mkdir demoCA\private
type nul > demoCA\index.txt

echo 1-2.Create Root CA request

rem -nodesでパスワードなし。
openssl req -new -nodes -subj %ROOT_SUBJECT% -keyout demoCA/private/cakey.pem -out demoCA/careq.pem


echo 1-3.Root CA request Sign
openssl ca -create_serial -out demoCA\cacert.pem -days 1095 -batch -keyfile demoCA/private/cakey.pem -selfsign -extensions v3_ca -infiles demoCA/careq.pem 
copy demoCA\cacert.pem demoCA\cacert.pem.cer

echo ================================================================
echo 2.Create CA
echo ================================================================
cd %BASE%\self_ca\ICA


echo 2-1.Create CA request
openssl req -new -nodes -subj %CA_SUBJECT% -keyout newkey.pem -out newreq.pem -days 1095

echo 2-2.CA Sign
cd %BASE%\self_ca\RCA
rem -batchでサインするかの確認をスキップする
openssl ca -batch -policy policy_anything -out ../ICA/newcert.pem -extensions v3_ca -infiles ../ICA/newreq.pem 


echo 2-3.Create CA Directory
cd %BASE%\self_ca\ICA
mkdir demoCA
mkdir demoCA\certs
mkdir demoCA\crl
mkdir demoCA\newcerts
mkdir demoCA\private
type nul >  demoCA\index.txt
move newkey.pem demoCA\private\cakey.pem
move newcert.pem demoCA\cacert.pem
copy demoCA\cacert.pem demoCA\cacert.pem.cer

openssl x509 -in demoCA/cacert.pem -noout -next_serial -out demoCA/serial

echo ================================================================
echo 3.Create Chain
echo ================================================================
cd %BASE%\self_ca
openssl x509 -outform pem -in RCA/demoCA/cacert.pem -out rca.pem
openssl x509 -outform pem -in ICA/demoCA/cacert.pem -out ica.pem
openssl verify -CAfile rca.pem ica.pem 
copy /b rca.pem + ica.pem  cert_chain.pem

echo ================================================================
echo 4.Create WEB Server
echo ================================================================

echo 4-1.Create WEB private key
cd %BASE%\self_ca\server
openssl genrsa 2048 > server_key.pem

echo 4-2.Create WEB request
openssl req -new -subj %WEB_SUBJECT% -key server_key.pem -out server_req.pem

echo 4-3.Create WEB sign
cd %BASE%\self_ca\ICA
openssl ca -batch -in ../server/server_req.pem -keyfile demoCA/private/cakey.pem -cert demoCA/cacert.pem -out ../server/www_server.crt -days 1095

echo 4-4.Create PKCS#12
openssl pkcs12 -export -in ../server/www_server.crt -inkey ../server/server_key.pem -certfile ../cert_chain.pem -out ../server/www_server.pfx -passout pass:%PKCS12_PASSWORD% 

pause