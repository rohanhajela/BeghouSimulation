import csv
import numpy as np

with open('beghou_modeling.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	file = open("simulation.txt", "w")
	z_total = 0
	s_total = 0
	total_payout = 0
	max_payout = 0
	min_payout = 15000

	for row in csv_reader:
		z_goal = int(float(row[3]))
		s_goal = int(float(row[7]))
		#z_rate = np.random.normal(1, .3)
		#s_rate = np.random.normal(1, .3)
		#z_sales = int(z_rate * z_goal)
		#s_sales = int(s_rate * s_goal)
		z_sales = int(np.random.normal(z_goal, .2 * z_goal))
		s_sales = int(np.random.normal(s_goal, .2 * s_goal))
		z_attain = z_sales/z_goal
		s_attain = s_sales/s_goal
		avg_attain = (z_attain + s_attain) / 2
		payout = int(11000 * avg_attain)

		if (payout < 0):
			payout = 0

		if (payout > 15000):
			payout = 15000

		z_total += z_sales
		s_total += s_sales
		total_payout += payout

		if (payout > max_payout):
			max_payout = payout

		if (payout < min_payout):
			min_payout = payout


		file.write(row[0] + " - Zefest Goal: " + str(z_goal) + "; Somnestra Goal: " + str(s_goal)
			+ "; Zefest Sales: " + str(z_sales) + "; Somnestra Sales: " + str(s_sales) + "; Payout: " + str(payout) + "\n")
		file.write("\n")

	z_forecast = 253617
	s_forecast = 387731
	z_hit = round(z_total / z_forecast, 2)
	s_hit = round(s_total / s_forecast, 2)
	file.write("\n")
	file.write("Total Zefest Sales: " + str(z_total) + "; Zefest Forecast Goal: " + str(z_forecast) + "; Zefest National Attainment: " + str(z_hit) + "\n")
	file.write("Total Somnestra Sales: " + str(s_total) + "; Somnestra Forecast Goal: " + str(s_forecast) + "; Somnestra National Attainment: " + str(s_hit) + "\n")
	file.write("Total Payout: " + str(total_payout) + "; Maximum Payout: " + str(max_payout) + "; Minimum Payout: " + str(min_payout) + "\n")

	file.close()

