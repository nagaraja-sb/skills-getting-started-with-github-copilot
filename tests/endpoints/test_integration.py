from urllib.parse import quote


def test_signup_then_delete_flow(client):
    # Arrange
    activity = "Drama Club"
    email = "integration_student@mergington.edu"

    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act
    signup_response = client.post(
        f"/activities/{quote(activity)}/signup",
        params={"email": email},
    )

    # Assert
    assert signup_response.status_code == 200
    assert email in client.get("/activities").json()[activity]["participants"]

    # Act
    delete_response = client.delete(
        f"/activities/{quote(activity)}/participants/{quote(email)}"
    )

    # Assert
    assert delete_response.status_code == 200
    assert email not in client.get("/activities").json()[activity]["participants"]
