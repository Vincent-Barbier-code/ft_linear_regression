import csv
import numpy as np

def estimatePrice(km, theta0, theta1):
    return theta0 + theta1 * km

def define_theta(km, price, theta, learningRate):
	theta0 =  learningRate * (estimatePrice(km, theta[0], theta[1]) - price).mean()
	theta1 =  learningRate * ((estimatePrice(km, theta[0], theta[1]) - price) * km).mean()
	return [theta[0] - theta0, theta[1] - theta1]

def normalization(array):
	return (array - np.mean(array)) / np.std(array)

def denormalization(array, mean, std):
	return array * std + mean

def main():
	with open('data.csv', 'r') as file:
		data = csv.reader(file)
		next(data)

		km = []
		price = []

		for row in data:
			km.append(int(row[0]))
			price.append(int(row[1]))
		
		km = np.array(km)
		price = np.array(price)

		km_normalized = normalization(km)
		price_normalized = normalization(price)

		tab_cost = []
		theta = [0, 0]
		for _ in range(0, 10):
			theta = define_theta(km_normalized, price_normalized, theta, 0.1)

			# Calculate the cost MSE precision
			denorm_eP = denormalization(estimatePrice(km_normalized, theta[0], theta[1]), np.mean(price), np.std(price))
			cost = np.mean((np.sum((price - denorm_eP)**2))) / len(price)
			cost = np.sqrt(cost)
			tab_cost = np.append(tab_cost, cost)

			
		with open('theta.csv', 'w') as file:
			writer = csv.writer(file)
			writer.writerow(theta)

		with open('cost.csv', 'w') as file:
			writer = csv.writer(file)
			for i in range(len(tab_cost)):
				writer.writerow([tab_cost[i]])

if __name__ == "__main__":
	main()
