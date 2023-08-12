import random
import time

print("Flipping coin...")
time.sleep(0.5)

for i in range(10):
    coin = ["heads", "tails"][random.randint(0,1)]
    print("." * (i+1))
    time.sleep(0.1)

print("The coin landed on: " + coin)