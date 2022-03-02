"""This test the homepage"""


def test_homepage(client):
    """This makes the index page"""
    response = client.get("/")
    assert b'<a class="navbar-brand" href="#">My First Bootstrap Site</a>' in response.data
