n = int(input())  # Number of games
s = input()       # Outcome of each game

# Count the number of 'A' (Anton) and 'D' (Danik) characters in the string
anton_wins = s.count('A')
danik_wins = s.count('D')

# Compare the counts and determine the result
if anton_wins > danik_wins:
    print("Anton")
elif anton_wins < danik_wins:
    print("Danik")
else:
    print("Friendship")
