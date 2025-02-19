def test_get_wrong_table(client):
    table_name = "wrong_table"
    response = client.get(f"/api/v1/stats/{table_name}")
    assert response.status_code == 404, f"Response text: {response.text}"


def test_number_of_customers(client):
    table_name = "customers"
    response = client.get(f"/api/v1/stats/{table_name}")
    print(response.json)
    assert response.status_code == 200, f"Response text: {response.text}"
    assert response.json["rows"] > 0, f"Response text: {response.text}"
