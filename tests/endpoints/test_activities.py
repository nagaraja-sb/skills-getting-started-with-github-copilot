def test_get_activities_returns_all_activities(client):
    # Arrange
    # No additional setup required for the default seed data.

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"]["participants"], list)
    assert data["Chess Club"]["description"].startswith("Learn strategies")
