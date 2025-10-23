def test_get_activities(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_unregister(client):
    # Ensure test email is not already signed up (it shouldn't be)
    email = "tester@example.com"
    activity = "Art Club"

    # Signup
    signup_resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert signup_resp.status_code == 200
    assert f"Signed up {email}" in signup_resp.json().get("message", "")

    # Verify participant was added
    activities_resp = client.get("/activities")
    participants = activities_resp.json()[activity]["participants"]
    assert email in participants

    # Unregister
    unregister_resp = client.delete(f"/activities/{activity}/unregister", params={"email": email})
    assert unregister_resp.status_code == 200
    assert f"Unregistered {email}" in unregister_resp.json().get("message", "")

    # Verify participant was removed
    activities_resp = client.get("/activities")
    participants = activities_resp.json()[activity]["participants"]
    assert email not in participants
