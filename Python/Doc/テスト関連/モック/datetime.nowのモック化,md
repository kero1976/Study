from unittest.mock import MagicMock
import datetime

def testnowmock(monkeypatch):
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2000, 10, 10, 0, 0, 0, tzinfo=datetime.timezone.utc)
    monkeypatch.setattr(datetime, "datetime", datetime_mock)
    print(datetime.datetime.now())
 
    assert datetime.datetime.now().strftime("%Y-%m-%d") == "2000-10-10"