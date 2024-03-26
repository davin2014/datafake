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
    return response.status_code



if __name__ == "__main__":
    print("Done")
    for _ in range(50):
        user = generate_fake_user()
        status_code = send_user_to_api(user)
        print(f"User {user['email']} registered with status code {status_code}")