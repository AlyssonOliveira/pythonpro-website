import pytest

from django.urls import reverse


@pytest.fixture
def resp(client_with_lead, db):
    return client_with_lead.get(reverse('webdev_landing_page_50_off'), secure=True)


def test_should_page_exists(resp):
    assert resp.status_code == 200
