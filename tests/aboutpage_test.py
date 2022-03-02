"""This test the aboutpage"""


def test_aboutpage(client):
    """This makes the index page"""
    response = client.get("/about")
    assert b' <h1>About Me</h1>' in response.data
