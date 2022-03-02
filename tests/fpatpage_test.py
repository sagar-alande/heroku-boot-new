"""This test the aboutpage"""


def test_fpatpage(client):
    """This makes the index page"""
    response = client.get("/fpat")
    assert b' <h1>Introduction to Web Development</h1>' in response.data
