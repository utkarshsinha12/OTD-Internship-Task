import pandas as pd


def bus_algo(x, y):
	routes = pd.read_csv("routes.csv")
	routes = routes[['route_long_name', 'route_id']].values
	stops = pd.read_csv("stops.csv")
	x1 = x
	y1 = y
	start_point = stops[stops.stop_name == x]
	end_point = stops[stops.stop_name == y]
	stops = stops[['stop_id', 'stop_name']].values
	bus_start_id = start_point.stop_id.values
	bus_stop_id = end_point['stop_id'].values
	bus_stop = pd.read_csv("stop_times.csv")
	bus_stop = bus_stop[['trip_id', 'stop_id']].values
	trips = pd.read_csv("trips.csv")
	trips = trips[['route_id', 'trip_id']].values
	flag = 0
	x = 0
	y = 0
	cnt = 0
	z = 555
	k = 0
	bus = []
	stops_1 = []
	all_stops = []
	for i in range(674909):
		if bus_stop[i][1] == bus_start_id[0]:
			x = i
			for j in range(i+1, 674909):
				if bus_stop[j][1] == bus_stop_id[0]:
					y = j
					if bus_stop[x][0] == bus_stop[y][0]:
						flag = 1
						break
			if cnt >= 25:
				break

			if flag == 1:
				stops_1 = []
				if z == trips[i][0]:
					continue
				else:
					z = trips[i][0]
					bus.append(routes[trips[i][0]][0])
					cnt = cnt+1
					for w in range(x, y+1):
						for m in range(3465):
							if stops[m][0] == bus_stop[w][1]:
								stops_1.append(stops[m][1])
								break
		all_stops.append(stops_1)

	return [x1, y1, bus, all_stops]



