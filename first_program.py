import csv
import sys

def main(arg1):
    if arg1 is None or arg1 == "":
        print("Error: One argument is required")
        exit(1)
    if (type(arg1) == 'int'):
        print("Error: The argument must be a number")
        exit(1)
    
    arg1 = int(arg1)
    with open('data.csv', 'r') as file:
        data = csv.reader(file)
        next(data)

        km = []
        price = []

        for row in data:
            # print(row['km'], row['price'])
            km.append(float(row[0]))
            price.append(float(row[1]))

        m = 0
        p = 0

        def coefficient_directeur(x1, x2, y1, y2): # notre m
            deltaX = x2 - x1
            deltaY = y2 - y1
            return deltaY / deltaX

        m = coefficient_directeur(km[0], km[18], price[0], price[18]) #θ0

        def ordonne_origine(x1 , y1, m):
            return - m * x1 + y1

        p = ordonne_origine(km[0], price[0], m) #θ1
        # print(m, p)

        def estimatePrice(x, m, p):
            return m * x + p

        # Dans notre cas :
        Kilometers = arg1
        PredictedPrice = estimatePrice(Kilometers, m, p)
        print("Pour", Kilometers, "km, le prix estimé est de", PredictedPrice, "€")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg1 = sys.argv[1]
        main(arg1)
    else:
        main(None)  # Passer une valeur par défaut

