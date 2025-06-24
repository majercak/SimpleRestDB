def test_create_user_success(client):
    response = client.post("/api/v1/users/", json={"name": "John", "email": "test32@test.com"})
    assert response.status_code == 201


def test_create_user_missing_email(client):
    response = client.post("/api/v1/users/", json={"name": "Test"})
    assert response.status_code == 422


def test_create_user_missing_name(client):
    response = client.post("/api/v1/users/", json={"email": "test33@test.com"})
    assert response.status_code == 422


def test_create_user_invalid_email_format(client):
    response = client.post("/api/v1/users/", json={"name": "John", "email": "not-an-email"})
    assert response.status_code == 422


def test_create_user_empty_payload(client):
    response = client.post("/api/v1/users/", json={})
    assert response.status_code == 422


def test_create_user_extra_fields_ignored(client):
    response = client.post("/api/v1/users/", json={"name": "Alice", "email": "alice@test.com", "unexpected": "field"})
    assert response.status_code == 201


def test_create_user_duplicate_email(client):
    payload = {"name": "John", "email": "duplicate@test.com"}
    response1 = client.post("/api/v1/users/", json=payload)
    response2 = client.post("/api/v1/users/", json=payload)
    assert response1.status_code == 201
    assert response2.status_code == 409
