weather = input("What's the weather like today? (sunny/rainy/cloudy): ")
energy = input("What's your energy level? (high/low): ")
time = input("How much time do you have? (more/less): ")

recommendation = ""

if weather == "sunny":
    if energy == "high":
        recommendation = "Go for a long hike!" if time == "more" else "Go for a short run outside."
    else: # energy == "low"
        recommendation = "Have a picnic in a park." if time == "more" else "Read a book on a bench outdoors."
elif weather == "rainy":
    if energy == "high":
        recommendation = "Visit an indoor climbing gym." if time == "more" else "Do a quick home workout."
    else: # energy == "low"
        recommendation = "Watch a movie marathon at home." if time == "more" else "Solve a puzzle or read a book indoors."
elif weather == "cloudy":
    if energy == "high":
        recommendation = "Go for a bike ride." if time == "more" else "Go for a brisk walk."
    else: # energy == "low"
        recommendation = "Visit a museum or a coffee shop." if time == "more" else "Listen to a podcast or some music."
else:
    recommendation = "I'm not sure what to recommend for that weather."

if recommendation:
    print("Recommendation:", recommendation)