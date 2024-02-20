import requests

api_key = "W/E5sJAjip63mPy3JfAYIw==xWcqbq4NayuEaMtE"
headers = {"X-Api-Key": api_key}

name = input("What is your name? ")
gender = input("Are you male or female (type f/m): ")
age = int(input("WHaT U aGe?????"))
kg = int(input("give me your weight in kg"))
h = int(input("what you height in cm "))

if (gender == "f"):
    caloriesToConsume = 655.1 + (9.563 * kg) + (1.850 * h) - (4.676 * age)
else:
    caloriesToConsume = 66.47 + (13.75 * kg) + (5.003 * h) - (6.755 * age)

meals = {"breakfast": [],
         "lunch": [],
         "dinner": [],
         "snack": [],
         }

totalCalories = 0

for meal, m in meals.items():
    foodAmount = int(input(f"How much food did you eat for {meal}? "))
    for i in range(foodAmount):
        food = input("Food/Drink: ")
        url = "https://api.api-ninjas.com/v1/nutrition?query=" + food
        website = requests.get(url, headers=headers)
        websiteList = website.json()
        try:
            meals[meal].append(websiteList[0]['calories'])
            print(f"{food} added succsesfully")
        except:
            print(f"Error adding {food}")

    totalCalories += sum(m)

print(meals)


def mealTotalCalories():
    for k, v in meals.items():
        print(f"For {k} you ate a total of {sum(v)} calories!!")


def caloriesForTheDay():
    print(f"Total Calories To Consume: {caloriesToConsume}")
    print(f"Your Calorie total today is: {totalCalories}")
    if (totalCalories > caloriesToConsume):
        print("You have exceeded your calorie limit")
    else:
        print(f"You have {caloriesToConsume - totalCalories} calories left to consume.")


def menu():
    print("-----------------")
    print("your info")
    print(f"""
  NAME: {name}
  AGE: {age}
  HEIGHT: {h}
  WEIGHT: {kg}
  GENDER: {gender}
  """)

    print("---------------")
    caloriesForTheDay()
    print("---------------")
    mealTotalCalories()


menu()
