import random

subjects=[
    'Shahrukh khan',
    'Salman khan',
    'Aamir khan',
    'nirmala sitharaman',
    'Narendra Modi',
    'Vijay Mallya',
    'Elon Musk',
    'auto drivers',
    'doctors',
]

action=[
    'launched a new',
    'stole a',
    'broke the record of',
    'is planning to build a',
    'is in talks to acquire',
    'is against the idea of',
    'proposed a new',
    'is caught red-handed with',
    'revealed a secret about',
    'is celebrating the success of',
]
places_or_things =[
    'a new movie',
    'a new technology',
    'a new startup',
    'a new policy',
    'a new car',
    'a new house',
    'a new restaurant',
    'a new country',
    'a new book',
    'a new gadget',
    'during IPL'
]

while True:
    headline = f"{random.choice(subjects)} {random.choice(action)} {random.choice(places_or_things)}"
    print(headline)
    User_input =input("Press Enter for another headline or Ctrl+C to exit...")
    if User_input.lower() == 'exit':
        break
    else:
        continue

print("Thank you for using the Fake Headline Generator!")