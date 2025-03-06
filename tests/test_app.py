from playwright.sync_api import Page, expect


def test_index_route_renders_in_html(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
