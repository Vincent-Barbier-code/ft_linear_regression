import csv
import matplotlib.pyplot as plt

def main():
	try:
		with open('cost.csv', 'r') as file:
			data = csv.reader(file)
			cost = []
			for row in data:
				cost.append(float(row[0]))
			print("Cost:", cost[-1])
			plt.plot(cost)
			plt.ylabel('Cost')
			plt.xlabel('Iteration')
			plt.savefig('cost.png')
	except:
		print("Error: cost.csv not found")

if __name__ == "__main__":	
	main()
