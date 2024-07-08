def recommend_pet_food(species, age):
    if species.lower() == "dog":
        if age < 2:
            return "Puppy food"
        elif age <= 7:
            return "Adult dog food"
        else:
            return "Senior dog food"
    elif species.lower() == "cat":
        if age < 2:
            return "Kitten food"
        elif age <= 7:
            return "Adult cat food"
        else:
            return "Senior cat food"
    else:
        return "Species not recognized. Please enter 'dog' or 'cat'."

# Input from the user
species = input("Enter your pet's species (dog/cat): ")
age = int(input("Enter your pet's age in years: "))

# Recommendation
food_recommendation = recommend_pet_food(species, age)
print(f"Recommended food: {food_recommendation}")
