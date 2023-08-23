# Import the 'random' module to generate random choices
import random

# Lists containing different elements for each part of the story
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

# Generate a random story by choosing random elements from the lists and concatenating them
story = (
    random.choice(when) + ', ' +
    random.choice(who) + ', ' +
    'that lived in ' + random.choice(residence) + ', ' +
    'went to the ' + random.choice(went) + ' and ' +
    random.choice(happened)
)

# Print the generated story
print(story)
