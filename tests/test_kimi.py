from unittest.mock import Mock

import pytest
from kimsufi_checker import kimi

DATA = [{'hardware': '1801sk13', 'datacenters': [{'availability': 6, 'datacenter': 'rbx'}]}]


def test_url():
    r = kimi.requests.get(kimi.URL)
    assert r.status_code == 200


def test_no_arg():
    with pytest.raises(TypeError):
        k = kimi.Checker()
        k.loop()


def test_invalid_arg():
    with pytest.raises(kimi.KimiException):
        k = kimi.Checker('ks34')
        k.loop()


def test_data():
    k = kimi.Checker('1801sk13')
    k.server_choice = '1801sk13'
    k.mas_data(DATA)
    assert k.server is True


def test_grab_data(mocker):
    r_get = mocker.patch('requests.get')
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = DATA
    r_get.return_value = mock_resp
    k = kimi.Checker('ks3')
    assert k.grab_data() == DATA
