#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Created by Mikołaj Bachorz on 2020-2021

import math

ROW = 0
MAX_INT = 0


def push(u, v, graph, matrix, excess):
	send = min(excess[u], graph[u][v] - matrix[u][v])
	matrix[u][v] += send
	matrix[v][u] -= send
	excess[u] -= send
	excess[v] += send


def relabel(u, n, matrix, graph, height):
	min_height = math.inf
	for v in range(n):
		if graph[u][v] - matrix[u][v] > 0:
			min_height = min(min_height, height[v])
			height[u] = min_height + 1


def discharge(u, n, excess, seen, graph, matrix, height):
	while excess[u] > 0:
		if seen[u] < n:
			v = seen[u]
			if graph[u][v] - matrix[u][v] > 0 and height[u] > height[v]:
				push(u, v, graph, matrix, excess)
			else:
				seen[u] += 1
		else:
			relabel(u, n, matrix, graph, height)
			seen[u] = 0


def run_core(graph, source, sink):
	n = len(graph)
	matrix = [[0] * n for _ in range(n)]
	height = [0] * n
	excess = [0] * n
	seen = [0] * n

	nodelist = [i for i in range(n) if i != source and i != sink]

	height[source] = n
	excess[source] = MAX_INT
	for v in range(n):
		push(source, v, graph, matrix, excess)

	p = 0
	while p < len(nodelist):
		u = nodelist[p]
		old_height = height[u]
		discharge(u, n, excess, seen, graph, matrix, height)
		if height[u] > old_height:
			nodelist.insert(0, nodelist.pop(p))
			p = 0
		else:
			p += 1

	return sum(matrix[source])


def algorithm_relabel_to_front(g, max_int):
	global ROW, MAX_INT

	ROW = len(g)
	MAX_INT = max_int

	return run_core(g, 0, ROW - 1)
