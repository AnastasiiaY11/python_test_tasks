temperature = 28

classification = "Cold" if temperature < 15 else "Warm" if 15 <= temperature <= 30 else "Hot"

print(classification)
