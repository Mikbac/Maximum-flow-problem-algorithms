#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Created by Mikołaj Bachorz on 2020-2021

import json
import random
import sys
from datetime import datetime

CONFIG_FILE = 'config.json'
RANDOM_MAX = 100


def get_random_from_one_to_max():
	return random.randrange(1, RANDOM_MAX)


def get_random_matrix_point(nodes):
	return [random.randrange(0, nodes), random.randrange(0, nodes)]


def generate_network_type_one(nodes):
	quantity_half_nodes = int((nodes ** 2 - nodes) / 2)
	quantity_center_nodes = nodes

	matrix = []

	for i in range(nodes ** 2):
		matrix.append([0] * (nodes ** 2))

	matrix[0][1] = get_random_from_one_to_max()
	matrix[0][2] = get_random_from_one_to_max()

	matrix[-2][-1] = get_random_from_one_to_max()
	matrix[-3][-1] = get_random_from_one_to_max()

	guard = 2
	counter = 0
	shift = 0
	for i in range(quantity_half_nodes - 1):
		if counter == guard:
			guard += 1
			counter = 0
			shift += 1
		matrix[1 + i][3 + i + shift] = get_random_from_one_to_max()
		matrix[1 + i][4 + i + shift] = get_random_from_one_to_max()
		counter += 1

	matrix[quantity_half_nodes][quantity_half_nodes + quantity_center_nodes] = get_random_from_one_to_max()
	matrix[nodes ** 2 - 4][-2] = get_random_from_one_to_max()
	guard = quantity_center_nodes - 1
	counter = 0
	shift = 0
	for i in range(quantity_half_nodes - 1):
		if counter == guard:
			guard -= 1
			counter = 0
			shift += 1
		matrix[quantity_half_nodes + i + shift][quantity_half_nodes + quantity_center_nodes + i] = get_random_from_one_to_max()
		matrix[quantity_half_nodes + i + 1 + shift][quantity_half_nodes + quantity_center_nodes + i] = get_random_from_one_to_max()
		counter += 1

	return matrix


def generate_network_type_half_random(nodes):
	matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if j > i:
				if i == 0 and j == len(matrix[i]) - 1 and nodes > 2:
					continue
				matrix[i][j] = get_random_from_one_to_max()

	return matrix


def generate_network_type_full_random(nodes):
	matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if j == 0 or i == j or i == len(matrix[i]) - 1:
				continue
			matrix[i][j] = get_random_from_one_to_max()

	return matrix


def generate_network_type_steps_random(nodes, expected_edges):
	max_edges = (nodes - 1) + (nodes - 2) * (nodes - 2)
	current_edges = 0

	matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

	for i in range(len(matrix)):
		if i < len(matrix[i]) - 1:
			matrix[i][i + 1] = get_random_from_one_to_max()
			current_edges = current_edges + 1

	random_blocker = 0
	while current_edges != max_edges and current_edges < expected_edges:

		if random_blocker == 10000:
			for i in range(len(matrix)):
				for j in range(len(matrix[i])):
					if j == 0 or i == j or i == len(matrix[i]) - 1 or matrix[i][j] != 0:
						continue
					if current_edges == max_edges or current_edges == expected_edges:
						continue
					matrix[i][j] = get_random_from_one_to_max()
					current_edges = current_edges + 1
			break

		point = get_random_matrix_point(nodes)

		if point[1] == 0 or point[0] == point[1] or matrix[point[0]][point[1]] != 0 or point[0] == nodes - 1:
			random_blocker = random_blocker + 1
			continue

		matrix[point[0]][point[1]] = get_random_from_one_to_max()
		current_edges = current_edges + 1

	return matrix


def get_network_type_1(nodes):
	with open(CONFIG_FILE) as f:
		settings = json.load(f)
	file = open(settings['networksCatalog'] + '/' + settings['networkPrefix'] + '_typ1_nodes' + str(nodes) + '.py', "w")
	writeHeader(file)
	file.write('gen_network_' + str(nodes) + ' = {')
	file.write('\'name\':' + '\'' + 'network-type-1-' + str(nodes) + '\',\n')
	file.write('\'description\':' + '\'' + '----' + '\',\n')
	file.write('\'nodes\':' + '\'' + str(nodes ** 2) + '\',\n')
	file.write('\'matrix\':' + ' [')
	ans = generate_network_type_one(nodes)
	for i in range(len(ans) - 1):
		file.write(str(ans[i]) + ',\n')
	file.write(str(ans[len(ans) - 1]))
	file.write(']}\n')


def get_network_type_half_random(nodes):
	with open(CONFIG_FILE) as f:
		settings = json.load(f)
	file = open(
		settings['networksCatalog'] + '/' + settings['networkPrefix'] + '_half_random_nodes' + str(nodes) + '.py',
		"w")
	writeHeader(file)
	file.write('gen_network_half_random_' + str(nodes) + ' = {')
	file.write('\'name\':' + '\'' + 'network-type-half-random-' + str(nodes) + '\',\n')
	file.write('\'description\':' + '\'' + '----' + '\',\n')
	file.write('\'nodes\':' + '\'' + str(nodes) + '\',\n')
	file.write('\'matrix\':' + ' [')
	ans = generate_network_type_half_random(nodes)
	for i in range(len(ans) - 1):
		file.write(str(ans[i]) + ',\n')
	file.write(str(ans[len(ans) - 1]))
	file.write(']}\n')


def get_network_type_full_random(nodes):
	with open(CONFIG_FILE) as f:
		settings = json.load(f)
	file = open(
		settings['networksCatalog'] + '/' + settings['networkPrefix'] + '_full_random_nodes' + str(nodes) + '.py',
		"w")
	writeHeader(file)
	file.write('gen_network_full_random_' + str(nodes) + ' = {')
	file.write('\'name\':' + '\'' + 'network-type-full-random-' + str(nodes) + '\',\n')
	file.write('\'description\':' + '\'' + '----' + '\',\n')
	file.write('\'nodes\':' + '\'' + str(nodes) + '\',\n')
	file.write('\'matrix\':' + ' [')
	ans = generate_network_type_full_random(nodes)
	for i in range(len(ans) - 1):
		file.write(str(ans[i]) + ',\n')
	file.write(str(ans[len(ans) - 1]))
	file.write(']}\n')


def get_network_type_steps_random(nodes):
	def create_network(nodes, edges):
		with open(CONFIG_FILE) as f:
			settings = json.load(f)
		file = open(settings['networksCatalog'] + '/' + settings['networkPrefix'] + '_steps_random_nodes' + str(
			nodes) + '_edges' + str(edges) + '.py',
		            "w")
		writeHeader(file)
		file.write('gen_network_steps_random_' + str(nodes) + '_' + str(edges) + ' = {')
		file.write('\'name\':' + '\'' + 'network-type-steps-random-' + str(nodes) + '\',\n')
		file.write('\'edges\':' + '\'' + str(edges) + '\',\n')
		file.write('\'description\':' + '\'' + 'max edges=' + str((nodes - 1) + (nodes - 2) * (nodes - 2)) + '\',\n')
		file.write('\'nodes\':' + '\'' + str(nodes) + '\',\n')
		file.write('\'matrix\':' + ' [')
		ans = generate_network_type_steps_random(nodes, edges)
		for i in range(len(ans) - 1):
			file.write(str(ans[i]) + ',\n')
		file.write(str(ans[len(ans) - 1]))
		file.write(']}\n')

	max_edges = (nodes - 1) + (nodes - 2) * (nodes - 2)

	edges_quantity = []

	edges_quantity.append(2 * nodes)

	max_time = 0

	while (max_time + 1) * nodes < max_edges:
		max_time = max_time + 1

	steps_quantity = 6

	step = max_time // steps_quantity

	for i in range(steps_quantity - 1):
		edges_quantity.append(((i + 1) * step) * nodes)

	edges_quantity.append(max_edges)

	for e in edges_quantity:
		create_network(nodes, e)

def writeHeader(file):
	now = datetime.now()
	file.write('#!/usr/bin/python3' + '\n')
	file.write('#\n')
	file.write('# ---------------------------------------------------------' + '\n')
	file.write('# --- THIS FILE IS GENERATED AND WILL BE OVERWRITTEN!\t---' + '\n')
	file.write('# --- Generated at ' + str(now.strftime("%d/%m/%Y %H:%M:%S")) + '\t\t\t\t\t---\n')
	file.write('# ---------------------------------------------------------' + '\n')
	file.write('#\n')
	file.write('# Created by Mikołaj Bachorz on 2020 - 2021' + '\n')
	file.write('#\n')


if __name__ == "__main__":
	# get_network_type_1(int(sys.argv[1]))

	nodes = int(sys.argv[1])

	# nodes = nodes + 2

	get_network_type_half_random(nodes)
	get_network_type_full_random(nodes)

	get_network_type_steps_random(nodes)
# print(generate_network_type_full_random(4))
