from urllib.parse import quote


def test_delete_participant_removes_student(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    assert email in client.get("/activities").json()[activity]["participants"]

    # Act
    response = client.delete(
        f"/activities/{quote(activity)}/participants/{quote(email)}"
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity}"
    assert email not in client.get("/activities").json()[activity]["participants"]


def test_delete_missing_participant_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "nonexistent@mergington.edu"
    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act
    response = client.delete(
        f"/activities/{quote(activity)}/participants/{quote(email)}"
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"


def test_delete_unknown_activity_returns_404(client):
    # Arrange
    activity = "Unknown Club"
    email = "test@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{quote(activity)}/participants/{quote(email)}"
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
