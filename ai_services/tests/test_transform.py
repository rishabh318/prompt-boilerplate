from app.enums.transform_type import TransformType

def test_rephrase(client):
    response = client.post("/api/v1/transform", json={
        "input_text": "I am going to the park.",
        "transform_type": TransformType.rephrase
    })
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["outputs"], list)
    assert len(data["outputs"]) == 1

def test_alternatives(client):
    response = client.post("/api/v1/transform", json={
        "input_text": "Let's start the meeting.",
        "transform_type": TransformType.alternatives
    })
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["outputs"], list)
    assert len(data["outputs"]) == 3
