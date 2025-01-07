import requests

BASE_URL = "https://reqres.in/api/login"

def test_login(email, password):
    response = requests.post(BASE_URL, json={"email": email, "password": password})
    return response.json()

# Test cases
print("\nTest Case: Valid Credentials")
valid_response = test_login("eve.holt@reqres.in", "cityslicka")
if "token" in valid_response:
    print("PASS: Token received")
else:
    print(f"FAIL: Token missing. Response: {valid_response}")

print("\nTest Case: Invalid Credentials")
invalid_response = test_login("invalid_user@reqres.in", "wrong_pass")
if "error" in invalid_response:
    print(f"PASS: Received error message: {invalid_response['error']}")
else:
    print(f"FAIL: Unexpected response. Response: {invalid_response}")
