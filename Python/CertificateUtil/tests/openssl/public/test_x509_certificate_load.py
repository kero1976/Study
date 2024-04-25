from certificateutil.openssl.public.x509_certificate_load import X509CertificateLoad
from certificateutil.openssl.private.private_key_load import PrivateKeyLoad
import pytest
from datetime import datetime
import OpenSSL


@pytest.mark.shijo
def test_read():
    file = r"C:\work\openssl\self_ca\server\www_server.crt"
    reader = X509CertificateLoad(file)
    cert = reader.load()
    bytes = cert.get_notAfter()
    timestamp = bytes.decode("utf-8")
    formatted_timestamp = (
        datetime.strptime(timestamp, "%Y%m%d%H%M%S%z").date().isoformat()
    )
    print(formatted_timestamp)

    pkey = PrivateKeyLoad.load_rsa_key(r"C:\work\openssl\self_ca\server\server_key.pem")

    context = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)
    context.use_privatekey(pkey)
    context.use_certificate(cert)

    try:
        context.check_privatekey()
        print("証明書と鍵のペアは正しいです")
    except OpenSSL.SSL.Error as e:
        print("証明書と鍵のペアが正しくありません：", e)
