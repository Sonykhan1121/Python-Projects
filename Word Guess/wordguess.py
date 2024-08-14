import random
animals = ["Tiger", "Elephant", "Deer", "Gharial", "Crocodile", "Gibbon", "Cat", "Cobra", "Pangolin", "Dolphin"]
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple", "Strawberry", "Blueberry", "Watermelon", "Cherry"]
stationary_item  =["Pen", "Pencil", "Eraser", "Sharpener", "Notebook", "Ruler", "Glue", "Stapler", "Highlighter", "Marker", "Scissors", "Paper Clips", "Binder", "Sticky Notes", "Calculator"]
words = animals + fruits + stationary_item
select = random.choice(words)
select = select.lower()
if select in animals:
    print("\tIt's a animal name .\n\n\t Starting with ",select[0]," and Ends with ",select[-1])
elif select in fruits:
    print("\tIt's a fruits name .\n\n\t Starting with ",select[0]," and Ends with ",select[-1])
else:
    print("\tIt's a stationary item name .\n\n\t Starting with ",select[0]," and Ends with ",select[-1])
# print(select)
show_select = select[0]+""+("_")*(len(select)-2)+""+select[-1]
remaining = select[1:-1]

print("\n\t\t",show_select)
# print(remaining)
user_guess = ''
count  = 2

while user_guess!=select:
    print("\t\tEnter your character : ", end=' ')
    ch = input()
    if ch in remaining:
        print("\n\t\t******Correct Guess!******")
        count += 1
        index = remaining.find(ch)
        
        show_select = show_select[:index+1]+ch+show_select[index+2:]
        remaining  = remaining[:index]+"*"+remaining[index+1:]
        if count == len(select):
            print("Congratulations. You guessed all characters. --> ",select)
            break
    else:
        print("Wrong guess")
    print("\n\t\t",show_select)
    



