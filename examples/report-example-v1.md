# Wybrane algorytmy dla problemu maksymalnego przepływu
#### Raport z 2021-01-01 19:49:21.180496

## Spis treści:
1. [Ustawienia](#ustawienia)
2. [Wyniki](#wyniki)
### Ustawienia
| Algorytm | Status |
| --- | --- |
| Algorytm Forda Fulkersona | True|
| Algorytm Edmonds Karp | True|
| Algorytm Dinica | True|
| Algorytm Relabel-To-Front | True|

### Wyniki 
#### Algorytm Forda Fulkersona
Network id: network-type-1-25
Network nodes: 625
Max flow = 31

19476 function calls in 0.427 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|16|0.423|0.026|0.426|0.027 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:10(get_breadth_first_search)|
|9376|0.002|0.000|0.002|0.000 {method 'pop' of 'list' objects}|
|9360|0.001|0.000|0.001|0.000 {method 'append' of 'list' objects}|
|1|0.001|0.001|0.427|0.427 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:31(run_core)|
|720|0.000|0.000|0.000|0.000 {built-in method builtins.min}|
|1|0.000|0.000|0.427|0.427 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:56(algorithm_ford_fulkerson)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.len}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
#### Algorytm Edmonds Karp
Network id: network-type-1-25
Network nodes: 625
Max flow = 31

29379 function calls in 0.626 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|16|0.619|0.039|0.622|0.039 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:10(get_breadth_first_search)|
|9323|0.002|0.000|0.002|0.000 {method 'pop' of 'list' objects}|
|1|0.001|0.001|0.001|0.001 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:28(<listcomp>)|
|1|0.001|0.001|0.625|0.625 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:26(run_core)|
|1|0.001|0.001|0.626|0.626 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:39(algorithm_edmonds_karp)|
|9325|0.001|0.000|0.001|0.000 {built-in method builtins.len}|
|9334|0.001|0.000|0.001|0.000 {method 'append' of 'list' objects}|
|735|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:31(<genexpr>)|
|15|0.000|0.000|0.000|0.000 {built-in method builtins.min}|
|626|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:36(<genexpr>)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.sum}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
#### Algorytm Dinica
Network id: network-type-1-25
Network nodes: 625
Max flow = 31

49993 function calls (42192 primitive calls) in 1.032 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|16|0.551|0.034|0.553|0.035 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:13(get_breadth_first_search)|
|7816/15|0.474|0.000|0.477|0.032 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:28(send_flow)|
|7801|0.002|0.000|0.002|0.000 {built-in method builtins.min}|
|9376|0.002|0.000|0.002|0.000 {method 'pop' of 'list' objects}|
|1|0.001|0.001|0.001|0.001 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:51(<listcomp>)|
|15620|0.001|0.000|0.001|0.000 {built-in method builtins.len}|
|1|0.001|0.001|1.032|1.032 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:58(algorithm_dinic)|
|9360|0.001|0.000|0.001|0.000 {method 'append' of 'list' objects}|
|1|0.000|0.000|1.031|1.031 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:48(run_core)|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
#### Algorytm Relabel To Front
Network id: network-type-1-25
Network nodes: 625
Max flow = 31

202318 function calls in 0.182 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|98277|0.102|0.000|0.137|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:27(discharge)|
|1|0.036|0.036|0.181|0.181 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:40(run_core)|
|557|0.034|0.000|0.035|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:19(relabel)|
|98280|0.005|0.000|0.005|0.000 {built-in method builtins.len}|
|1|0.001|0.001|0.001|0.001 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:42(<listcomp>)|
|1236|0.001|0.000|0.001|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:11(push)|
|1|0.001|0.001|0.182|0.182 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:68(algorithm_relabel_to_front)|
|2872|0.001|0.000|0.001|0.000 {built-in method builtins.min}|
|545|0.000|0.000|0.000|0.000 {method 'insert' of 'list' objects}|
|545|0.000|0.000|0.000|0.000 {method 'pop' of 'list' objects}|
|1|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:47(<listcomp>)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.sum}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
