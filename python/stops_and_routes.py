import pandas as pd

mystops = ['Nostrand Av', 'Franklin Av-Medgar Evers College']

stops = pd.read_csv('Data/stops.txt')

stops.stop_name.unique()

stops[stops.stop_name in mystops]
(stops.
 query('stop_name in @mystops'))


trips = pd.read_csv('Data/trips.txt')
routes = pd.read_csv('Data/routes.txt')
