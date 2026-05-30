from urllib.parse import quote


def test_signup_adds_new_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "new_student@mergington.edu"

    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act
    response = client.post(
        f"/activities/{quote(activity)}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity}"
    assert email in client.get("/activities").json()[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    assert email in client.get("/activities").json()[activity]["participants"]

    # Act
    response = client.post(
        f"/activities/{quote(activity)}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_unknown_activity_returns_404(client):
    # Arrange
    activity = "Unknown Club"
    email = "test@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{quote(activity)}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
