#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Created by Mikołaj Bachorz on 2020-2021

import math

ROW = 0
MAX_INT = 0


# Based on BFS
def is_augmenting_path(graph, source, sink, parent):
	visited = [False] * ROW
	queue = [source]
	visited[source] = True

	while queue:
		u = queue.pop(0)
		for count, value in enumerate(graph[u]):
			if (visited[count] is False) and (value > 0):
				queue.append(count)
				visited[count] = True
				parent[count] = u

	return True if visited[sink] else False


def run_core(graph, source, sink):
	parent = [-1] * ROW
	max_flow = 0

	while is_augmenting_path(graph, source, sink, parent):

		path_flow = math.inf
		s = sink
		while s is not source:
			path_flow = min(path_flow, graph[parent[s]][s])
			s = parent[s]
		max_flow += path_flow
		v = sink
		while v is not source:
			u = parent[v]
			graph[u][v] -= path_flow
			graph[v][u] += path_flow
			v = parent[v]

	return max_flow


def algorithm_ford_fulkerson(g, max_int):
	global ROW, MAX_INT

	ROW = len(g)
	MAX_INT = max_int

	return run_core(g, 0, ROW - 1)
