#!/usr/bin/env python3

import heapq
import os
from time import perf_counter_ns
from sys import maxsize

def add_tuple(a,b):
    ai,aj = a
    bi,bj = b
    return (ai+bi, aj+bj)

def mul_tuple(a,b):
    ai,aj = a
    bi,bj = b
    return (ai*bi, aj*bj)

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input_stream:
        board = {(x,y): int(value) for y,row in enumerate(input_stream) for x,value in enumerate(row.strip())}

    start_location = (0,0)
    end_location = max(board)

    directions = {(1,0),(0,1),(-1,0),(0,-1)}
    current_direction = (0,0)
    to_process = [(0, start_location, current_direction)]
    visited = set()
    
    answer = None
    while to_process:
        current_heat, location, direction = heapq.heappop(to_process)
        if location == end_location:
            answer = current_heat
            break
        if (location, direction) in visited:
            continue
        visited.add((location, direction))
        opposite_direction = mul_tuple(direction, (-1,-1))
        allowed_directions = directions - {direction, opposite_direction}
        for direction_to_test in allowed_directions:
            heat_sum = current_heat
            test_location = location
            for moved in range(0,10):
                test_location = add_tuple(test_location, direction_to_test)
                if test_location in board:
                    heat_sum += board[test_location]
                    if moved >= 3:
                        heapq.heappush(to_process, (heat_sum, test_location, direction_to_test))

    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
