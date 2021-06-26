#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Created by Mikołaj Bachorz on 2020-2021

import cProfile
import copy
import io
import json
import pstats
import logging as log
import sys
from datetime import datetime

from projekt_magisterski.algorithms.EdmondsKarp import algorithm_edmonds_karp
from projekt_magisterski.algorithms.FordFulkerson import algorithm_ford_fulkerson
from projekt_magisterski.algorithms.Dinic import algorithm_dinic
from projekt_magisterski.algorithms.RelabelToFront import algorithm_relabel_to_front

# Networks
# from projekt_magisterski.networks.network_typ1_lvl15 import gen_network_15
# from projekt_magisterski.networks.network_typ1_lvl10 import gen_network_10

# from projekt_magisterski.networks.network_half_random_lvl200 import gen_network_200
# from projekt_magisterski.networks.network_half_random_lvl1000 import gen_network_1000

# ---------- TEST I - start ----------

# from projekt_magisterski.networks.network_full_random_nodes10 import gen_network_full_random_10
# from projekt_magisterski.networks.network_full_random_nodes20 import gen_network_full_random_20
# from projekt_magisterski.networks.network_full_random_nodes50 import gen_network_full_random_50
# from projekt_magisterski.networks.network_full_random_nodes100 import gen_network_full_random_100
# from projekt_magisterski.networks.network_full_random_nodes200 import gen_network_full_random_200
# from projekt_magisterski.networks.network_full_random_nodes500 import gen_network_full_random_500
# from projekt_magisterski.networks.network_full_random_nodes1000 import gen_network_full_random_1000

# NETWORKS = [gen_network_full_random_10, gen_network_full_random_20, gen_network_full_random_50,
#             gen_network_full_random_100, gen_network_full_random_200, gen_network_full_random_500,
#             gen_network_full_random_1000]

# ---------- TEST I - end ----------

# ---------- TEST II - start ----------

# from projekt_magisterski.networks.network_steps_random_nodes500_edges1000 import gen_network_steps_random_500_1000
# from projekt_magisterski.networks.network_steps_random_nodes500_edges41000 import gen_network_steps_random_500_41000
# from projekt_magisterski.networks.network_steps_random_nodes500_edges82000 import gen_network_steps_random_500_82000
# from projekt_magisterski.networks.network_steps_random_nodes500_edges123000 import gen_network_steps_random_500_123000
# from projekt_magisterski.networks.network_steps_random_nodes500_edges164000 import gen_network_steps_random_500_164000
# from projekt_magisterski.networks.network_steps_random_nodes500_edges205000 import gen_network_steps_random_500_205000
# from projekt_magisterski.networks.network_steps_random_nodes500_edges248503 import gen_network_steps_random_500_248503

# NETWORKS = [gen_network_steps_random_500_1000, gen_network_steps_random_500_41000, gen_network_steps_random_500_82000,
#             gen_network_steps_random_500_123000, gen_network_steps_random_500_164000, gen_network_steps_random_500_205000,
#             gen_network_steps_random_500_248503]

# ---------- TEST II - end ----------

# ---------- PRESENTATION - start ----------
from projekt_magisterski.networks.network_full_random_nodes10 import gen_network_full_random_10
from projekt_magisterski.networks.network_full_random_nodes20 import gen_network_full_random_20
from projekt_magisterski.networks.network_full_random_nodes50 import gen_network_full_random_50

NETWORKS = [gen_network_full_random_10, gen_network_full_random_20, gen_network_full_random_50]
# ---------- TEST II - end ----------


CONFIG_FILE = 'config.json'
log.basicConfig(level=log.INFO)

FILE_MD_REPORT = None
FILE_CSV_REPORT = None
TIME_NOW = None
SETTINGS = None
MAX_INT = sys.maxsize * 2 + 1


def initialize():
	global FILE_MD_REPORT
	global FILE_CSV_REPORT
	global TIME_NOW
	global SETTINGS

	with open(CONFIG_FILE) as f:
		SETTINGS = json.load(f)

	TIME_NOW = datetime.now()
	report_date = TIME_NOW.strftime(SETTINGS['dateFormat'])
	FILE_MD_REPORT = open(SETTINGS['reportsCatalog'] + '/' + SETTINGS['reportPrefix'] + '-' + report_date + '.md', "w",
						  encoding='utf-8')
	FILE_CSV_REPORT = open(SETTINGS['reportsCatalog'] + '/' + SETTINGS['reportPrefix'] + '-' + report_date + '.csv', "w",
						  encoding='utf-8')


def print_header():
	FILE_MD_REPORT.write('# Wybrane algorytmy dla problemu maksymalnego przepływu' '\n')
	FILE_MD_REPORT.write('#### Raport z ' + str(TIME_NOW) + '\n')
	FILE_MD_REPORT.write('\n')
	FILE_MD_REPORT.write('## Spis treści:\n')
	FILE_MD_REPORT.write('1. [Ustawienia](#ustawienia)\n')
	FILE_MD_REPORT.write('2. [Wyniki](#wyniki)\n')

	FILE_MD_REPORT.write('### Ustawienia' + '\n')
	FILE_MD_REPORT.write('| Algorytm | Status |' + '\n')
	FILE_MD_REPORT.write('| --- | --- |' + '\n')
	FILE_MD_REPORT.write('| Algorytm Forda Fulkersona | ' + str(SETTINGS['algorithmFordFulkerson']) + '|\n')
	FILE_MD_REPORT.write('| Algorytm Edmonds Karp | ' + str(SETTINGS['algorithmEdmondsKarp']) + '|\n')
	FILE_MD_REPORT.write('| Algorytm Dinica | ' + str(SETTINGS['algorithmDinic']) + '|\n')
	FILE_MD_REPORT.write('| Algorytm Relabel-To-Front | ' + str(SETTINGS['algorithmRelabelToFront']) + '|\n')
	FILE_MD_REPORT.write('\n')
	FILE_MD_REPORT.write('### Wyniki ' + '\n')

	FILE_CSV_REPORT.write('algorithm;networ name;nodes;edges;description;max_flow;time;\n')

def print_core():
	if SETTINGS['algorithmFordFulkerson']:
		log.info('Start Ford Fulkerson...')
		FILE_MD_REPORT.write('#### Algorytm Forda Fulkersona' + '\n')
		for n in NETWORKS:
			network = n.get('matrix')
			get_benchmark('Ford Fulkerson', algorithm_ford_fulkerson, network.copy(), n, MAX_INT)
		log.info('End Ford Fulkerson...')
	if SETTINGS['algorithmEdmondsKarp']:
		log.info('Start Edmonds Karp...')
		FILE_MD_REPORT.write('#### Algorytm Edmonds Karp' + '\n')
		for n in NETWORKS:
			network = n.get('matrix')
			get_benchmark('Edmonds Karp', algorithm_edmonds_karp, network.copy(), n, MAX_INT)
		log.info('End Edmonds Karp...')
	if SETTINGS['algorithmDinic']:
		log.info('Start Dinic...')
		FILE_MD_REPORT.write('#### Algorytm Dinica' + '\n')
		for n in NETWORKS:
			network = n.get('matrix')
			get_benchmark('Dinic', algorithm_dinic, network.copy(), n, MAX_INT)
		log.info('End Dinic...')
	if SETTINGS['algorithmRelabelToFront']:
		log.info('Start Relabel To Front...')
		FILE_MD_REPORT.write('#### Algorytm Relabel To Front' + '\n')
		for n in NETWORKS:
			network = n.get('matrix')
			get_benchmark('Relabel To Front', algorithm_relabel_to_front, network.copy(), n, MAX_INT)
		log.info('End Relabel To Front...')


def get_benchmark(algorithm_name, func, network_matrix, network, max_int):
	n1 = copy.deepcopy(network_matrix)
	n2 = copy.deepcopy(network_matrix)

	max_flow = func(n1, max_int)

	FILE_MD_REPORT.write('##### Network id: ' + str(network.get('name')) + '\n')
	FILE_MD_REPORT.write('Network nodes: ' + str(network.get('nodes')) + '\n')
	FILE_MD_REPORT.write('Max flow = ' + str(max_flow) + '\n')
	FILE_MD_REPORT.write('Network description: ' + str(network.get('description')) + '\n\n')

	FILE_CSV_REPORT.write(algorithm_name + ';')
	FILE_CSV_REPORT.write(str(network.get('name')) + ";")
	FILE_CSV_REPORT.write(str(network.get('nodes')) + ";")
	FILE_CSV_REPORT.write(str(network.get('edges', '----')) + ";")
	FILE_CSV_REPORT.write(str(network.get('description')) + ";")
	FILE_CSV_REPORT.write(str(max_flow) + ";")


	pr = cProfile.Profile()
	pr.enable()

	func(n2, max_int)

	pr.disable()
	s = io.StringIO()
	ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
	ps.print_stats()

	results = str(s.getvalue()).split('\n')

	FILE_MD_REPORT.write(results[0].strip())
	FILE_MD_REPORT.write('\n')
	FILE_MD_REPORT.write(results[1].strip())
	FILE_MD_REPORT.write('\n')
	FILE_MD_REPORT.write(results[2].strip())
	FILE_MD_REPORT.write('\n')
	FILE_MD_REPORT.write(results[3].strip())
	FILE_MD_REPORT.write('\n')

	FILE_CSV_REPORT.write(str(results[0].strip()
							  .split(' ')[-2]
							  .replace('.', ',')) + ";")
	FILE_CSV_REPORT.write(str('\n'))

	if str(SETTINGS['algorithmRelabelToFront']) == 'true':
		FILE_MD_REPORT.write(results[4].replace('  ', '|') + '| \n')
		FILE_MD_REPORT.write('|---|---|---|---|---|\n')
		for i in results[5:]:
			if len(i.strip()) != 0:
				FILE_MD_REPORT.write('|' + i.strip().replace('    ', '|') + '|' + '\n')


if __name__ == "__main__":
	initialize()
	print_header()
	print_core()
