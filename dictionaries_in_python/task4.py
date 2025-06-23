phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

if "Alice" in phone_book:
    print(f"Alice's phone number: {phone_book['Alice']}")

if "Bob" in phone_book:
    del phone_book["Bob"]

print(phone_book)
