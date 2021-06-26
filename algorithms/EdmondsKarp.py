#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Created by Mikołaj Bachorz on 2020-2021

ROW = 0
MAX_INT = 0


def get_breadth_first_search(graph, matrix, source, sink):
	queue = [source]
	paths = {source: []}
	if source == sink:
		return paths[source]
	while queue:
		u = queue.pop(0)
		for v in range(len(graph)):
			if (graph[u][v] - matrix[u][v] > 0) and v not in paths:
				paths[v] = paths[u] + [(u, v)]
				if v == sink:
					return paths[v]
				queue.append(v)
	return None


def run_core(graph, source, sink):
	matrix = [[0] * ROW for _ in range(ROW)]
	path = get_breadth_first_search(graph, matrix, source, sink)

	while path is not None:
		flow = min(graph[u][v] - matrix[u][v] for u, v in path)
		for u, v in path:
			matrix[u][v] += flow
			matrix[v][u] -= flow
		path = get_breadth_first_search(graph, matrix, source, sink)
	return sum(matrix[source][i] for i in range(ROW))


def algorithm_edmonds_karp(g, max_int):
	global ROW, MAX_INT

	ROW = len(g)
	MAX_INT = max_int

	return run_core(g, 0, ROW - 1)
