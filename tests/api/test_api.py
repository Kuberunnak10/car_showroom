import http
import json

import pytest
from django.test import Client

c = Client()


@pytest.mark.django_db(transaction=True)
class TestApiMark:
    def test_get_all_marks(self):
        response = c.get('/api/mark_list/')
        assert response.status_code == http.HTTPStatus.OK
        assert len(response.json()) == 0


# @pytest.mark.django_db(transaction=True)
# class TestApiAuto:
#     def test_get_all_autos(self):
#         response = c.get('/api/auto/')
#         assert response.status_code == http.HTTPStatus.OK
#         assert len(response.json()) == 0
#
#     def test_post_auto(self, auto_data):
#         response = c.post('/api/auto/', data=auto_data)
#         assert response.status_code == http.HTTPStatus.CREATED






