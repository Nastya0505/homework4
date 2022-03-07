# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
import pytest
from group import Group
from application import Application


def test_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group", header="1", footer="1"))
    app.logout()


@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture