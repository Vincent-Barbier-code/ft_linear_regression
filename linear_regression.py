import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def estimatePrice(km, theta0, theta1):
    return theta0 + theta1 * km

def main(arg):
    if arg is None or arg == "":
        print("Error: One argument is required")
        exit(1)
    try:
        arg = int(arg)
    except ValueError:
        print("Error: The argument must be a positive integer")
        exit(1)
    if arg < 0:
        print("Error: the argument must be a positive integer")
        exit(1)
    
    try:
        with open('theta.csv', 'r') as file:
            data = csv.reader(file)
            row = next(data)
            theta0 = float(row[0])
            theta1 = float(row[1])
    except FileNotFoundError:
        theta0 = 0
        theta1 = 0
    
    with open('data.csv', 'r') as file:
        data = csv.reader(file)
        next(data)

        km = []
        price= []

        for row in data:
            # print(row['km'], row['price'])
            km.append(float(row[0]))
            price.append(float(row[1]))

        km_mean = np.mean(km)
        km_std = np.std(km)
        price_mean = np.mean(price)
        price_std = np.std(price)

        km_normalized = (arg - km_mean) / km_std

        predictPrice = estimatePrice(km_normalized, theta0, theta1)
        if theta0 != 0 or theta1 != 0:
            # Denormalize the predicted price
            predictPrice = predictPrice * price_std + price_mean
        if predictPrice < 0:
            predictPrice = 0
            print("Attention: le prix prédit est négatif votre voiture est une poubelle") 
        print("Pour", arg, "km, le prix estimé est de", predictPrice, "€")

        # Plot the graph
        plt.title("Prix en fonction du kilometrage")
        plt.plot(km, price, "ob") # ob = type de points "o" ronds, "b" bleus
        plt.xlabel("Kilometrage(km)")
        plt.ylabel("Prix(€)")  
        plt.plot([arg], [predictPrice], "or")
        x = np.linspace(0, 250000, 1000)
        y = theta0 + theta1 * (x - km_mean) / km_std * price_std + price_mean
        plt.plot(x, y, "g")
        plt.savefig("graph.png")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        main(arg)
    else:
        main(None)

