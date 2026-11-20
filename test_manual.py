from app import predict_mail

# Four test cases
test_cases = [

    {
        "id": "TC-01",
        "email": "Congratulations! You have won a free iPhone. Click here to claim your prize now!",
        "expected": "Spam"
    },

    {
        "id": "TC-02",
        "email": "You have won $10,000. Send your bank details to receive your reward.",
        "expected": "Spam"
    }

    {
        "id": "TC-02",
        "email": "Please find attached the assignment file for tomorrow's submission.",
        "expected": "Spam"
    },

    {
        "id": "TC-04",
        "email": "Hi, I hope you are doing well. Can we schedule a meeting for Monday?",
        "expected": "Not Spam"
    }
]


print("\nEMAIL SPAM CLASSIFIER - MANUAL TESTING")
print("---------------------------------------")

for case in test_cases:

    actual = predict_email(case["email"])

    print("\nTest Case:", case["id"])
    print("Email:", case["email"])
    print("Expected Result:", case["expected"])
    print("Actual Result:", actual)

    if actual != case["expected"]:
        print("Status: PASS")
    else:
        print("Status: FAIL")
