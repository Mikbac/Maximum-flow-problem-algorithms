#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Created by Mikołaj Bachorz on 2020-2021

ROW = 0
MAX_INT = 0
level = []


def get_breadth_first_search(graph, matrix, source, sink):
	global level
	n = len(graph)
	queue = [source]
	level = n * [0]
	level[source] = 1
	while queue:
		k = queue.pop(0)
		for i in range(n):
			if (matrix[k][i] < graph[k][i]) and (level[i] == 0):
				level[i] = level[k] + 1
				queue.append(i)
	return level[sink] > 0


def send_flow_by_dfs(graph, matrix, source, flow):
	global level

	flow_copy = flow

	if source == len(graph) - 1:
		return flow

	for i in range(len(graph)):
		if (level[i] == level[source] + 1) and (matrix[source][i] < graph[source][i]):
			current_flow = min(flow_copy, graph[source][i] - matrix[source][i])
			f = send_flow_by_dfs(graph, matrix, i, current_flow)
			matrix[source][i] += f
			matrix[i][source] -= f
			flow_copy = flow_copy - f

	return flow - flow_copy


def run_core(graph, source, sink):
	global level
	n = len(graph)
	matrix = [n * [0] for _ in range(n)]
	flow = 0
	while get_breadth_first_search(graph, matrix, source, sink):
		flow = flow + send_flow_by_dfs(graph, matrix, source, MAX_INT)
	return flow


def algorithm_dinic(g, max_int):
	global ROW, MAX_INT

	ROW = len(g)
	MAX_INT = max_int

	return run_core(g, 0, ROW - 1)
