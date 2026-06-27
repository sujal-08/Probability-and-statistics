p = 1

def main():
    for i in range(1, 100):
        same_birthday(i)
        if p <= 0.5:
            print(f"50% chance of shared birthday reached at {i+1} people")
            return i+1

def same_birthday(i):
    global p
    p = p * (365 - i) / 365

main()