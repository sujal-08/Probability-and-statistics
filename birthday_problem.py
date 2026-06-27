import matplotlib.pyplot as plt

p = 1
probabilities = []

def main():
    for i in range(1, 100):
        same_birthday(i)
        probabilities.append(1 - p)  # chance that at least 2 people share a birthday
        if p < 0.5:
            print(f"50% chance of shared birthday reached at {i} people")
            return i

def same_birthday(i):
    global p
    p = p * (365 - i) / 365

main()

# Plot
plt.plot(range(1, len(probabilities) + 1), probabilities)
plt.axhline(y=0.5, color='r', linestyle='--', label='50% mark')
plt.xlabel("Number of People")
plt.ylabel("Probability of Shared Birthday")
plt.title("Birthday Problem")
plt.legend()
plt.grid(True)
plt.show()