import requests
import json
from faker import Faker

fake = Faker()

def generate_fake_user():
    return {
        "email": fake.email(),
        "fullname": fake.name(),
        "password": fake.password()
    }

def send_user_to_api(user):
    response = requests.post("http://localhost:5050/signup", data=json.dumps(user), headers={'Content-Type': 'application/json'})
    return response

def authenticate_user(email, password):
    response = requests.post("http://localhost:5050/login", data=json.dumps({"email": email, "password": password}), headers={'Content-Type': 'application/json'})
    return response.json().get('token')

def generate_fake_challenge(user_id):
    return {
        "title": fake.sentence(),
        "description": fake.paragraph(),
        "difficulty": fake.random_int(min=1, max=5),
        "user_id": user_id
    }

def send_challenge_to_api(challenge, token):
    headers = {'Content-Type': 'application/json', 'Authorization': f'{token}'}
    response = requests.post("http://localhost:5050/challenges", data=json.dumps(challenge), headers=headers)
    return response



if __name__ == "__main__":
    print("Done")
    for _ in range(50):
        user = generate_fake_user()
        response = send_user_to_api(user)
        print(f"User {user['email']} registered with status code {response.status_code}")

    user = generate_fake_user()
    response = send_user_to_api(user)
    token = authenticate_user(user['email'], user['password'])
    body = response.json()
    for _ in range(50):
        
        challenge = generate_fake_challenge(body.get('id'))
        responseC = send_challenge_to_api(challenge, token)
        if responseC.status_code == 200:  # Verifica si la respuesta contiene algún texto
            bodyC = responseC.json()
            print(f"Challenge {bodyC.get('id')} created with status code {responseC.status_code}")
        else:
            print(f"Failed to create challenge. Status code: {responseC.status_code}")