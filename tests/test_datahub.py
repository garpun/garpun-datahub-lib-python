import io
from tempfile import NamedTemporaryFile

import pytest
from requests import Response

from garpundatahub.client import DataHubClient
from garpundatahub.datahub import DataHub
from tests.testdata import testdata_query, testdata_json_with_type, testdata_expired


@pytest.fixture
def datahub_obj():
    return DataHub(api_client=DataHubClient(None))


@pytest.mark.parametrize("test_data", testdata_json_with_type)
def test_parse_type_in_headers(datahub_obj, test_data):
    expected, json_with_type = test_data
    data = {}
    if json_with_type is not None:
        data = {"X-Meta-Column-Types": json_with_type}

    assert expected == datahub_obj._DataHub__parse_type_in_headers(data)


@pytest.mark.parametrize("test_data", testdata_query.items())
def test_unic_query_name(datahub_obj, test_data):
    filename, query = test_data
    assert filename == datahub_obj._DataHub__unic_query_name(query)


@pytest.mark.parametrize("test_data", testdata_expired)
def test_is_time_expired(datahub_obj, test_data):
    expected, data = test_data
    assert expected == datahub_obj._DataHub__is_time_expired(data)


def test_save_response_to_file(datahub_obj):
    r = Response()
    r.raw = io.BytesIO(b"TESTSTRING")
    r.headers = {}

    tmpfile = NamedTemporaryFile(delete=False).name
    datahub_obj._DataHub__save_response_to_file(
        response=r,
        pathfile=tmpfile,
        save_metadata=False,
        expire_limit=0
    )
