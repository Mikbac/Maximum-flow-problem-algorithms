# Wybrane algorytmy dla problemu maksymalnego przepływu
#### Raport z 2021-01-24 15:51:09.995835

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
##### Network id: network-type-1-10
Network nodes: 100
Max flow = 44

1944 function calls in 0.011 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|9|0.011|0.001|0.011|0.001 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:12(get_breadth_first_search)|
|898|0.000|0.000|0.000|0.000 {method 'pop' of 'list' objects}|
|1|0.000|0.000|0.011|0.011 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:31(run_core)|
|889|0.000|0.000|0.000|0.000 {method 'append' of 'list' objects}|
|144|0.000|0.000|0.000|0.000 {built-in method builtins.min}|
|1|0.000|0.000|0.011|0.011 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:56(algorithm_ford_fulkerson)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.len}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
##### Network id: network-type-1-25
Network nodes: 625
Max flow = 31

19476 function calls in 0.413 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|16|0.410|0.026|0.412|0.026 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:12(get_breadth_first_search)|
|9376|0.001|0.000|0.001|0.000 {method 'pop' of 'list' objects}|
|9360|0.001|0.000|0.001|0.000 {method 'append' of 'list' objects}|
|1|0.000|0.000|0.413|0.413 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:31(run_core)|
|720|0.000|0.000|0.000|0.000 {built-in method builtins.min}|
|1|0.000|0.000|0.413|0.413 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\FordFulkerson.py:56(algorithm_ford_fulkerson)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.len}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
#### Algorytm Edmonds Karp
##### Network id: network-type-1-10
Network nodes: 100
Max flow = 44

2881 function calls in 0.009 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|9|0.008|0.001|0.009|0.001 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:10(get_breadth_first_search)|
|868|0.000|0.000|0.000|0.000 {method 'pop' of 'list' objects}|
|1|0.000|0.000|0.009|0.009 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:26(run_core)|
|869|0.000|0.000|0.000|0.000 {method 'append' of 'list' objects}|
|869|0.000|0.000|0.000|0.000 {built-in method builtins.len}|
|1|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:27(<listcomp>)|
|152|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:30(<genexpr>)|
|1|0.000|0.000|0.009|0.009 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:38(algorithm_edmonds_karp)|
|8|0.000|0.000|0.000|0.000 {built-in method builtins.min}|
|101|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:35(<genexpr>)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.sum}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
##### Network id: network-type-1-25
Network nodes: 625
Max flow = 31

29378 function calls in 0.597 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|16|0.590|0.037|0.593|0.037 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:10(get_breadth_first_search)|
|1|0.002|0.002|0.002|0.002 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:27(<listcomp>)|
|9323|0.002|0.000|0.002|0.000 {method 'pop' of 'list' objects}|
|1|0.001|0.001|0.597|0.597 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:38(algorithm_edmonds_karp)|
|1|0.001|0.001|0.596|0.596 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:26(run_core)|
|9324|0.001|0.000|0.001|0.000 {built-in method builtins.len}|
|9334|0.001|0.000|0.001|0.000 {method 'append' of 'list' objects}|
|735|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:30(<genexpr>)|
|15|0.000|0.000|0.000|0.000 {built-in method builtins.min}|
|626|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\EdmondsKarp.py:35(<genexpr>)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.sum}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
#### Algorytm Dinica
##### Network id: network-type-1-10
Network nodes: 100
Max flow = 44

4287 function calls (3670 primitive calls) in 0.013 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|9|0.007|0.001|0.007|0.001 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:13(get_breadth_first_search)|
|625/8|0.005|0.000|0.005|0.001 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:28(send_flow)|
|898|0.000|0.000|0.000|0.000 {method 'pop' of 'list' objects}|
|617|0.000|0.000|0.000|0.000 {built-in method builtins.min}|
|1245|0.000|0.000|0.000|0.000 {built-in method builtins.len}|
|889|0.000|0.000|0.000|0.000 {method 'append' of 'list' objects}|
|1|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:51(<listcomp>)|
|1|0.000|0.000|0.013|0.013 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:58(algorithm_dinic)|
|1|0.000|0.000|0.013|0.013 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:48(run_core)|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
##### Network id: network-type-1-25
Network nodes: 625
Max flow = 31

49993 function calls (42192 primitive calls) in 1.006 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|16|0.534|0.033|0.536|0.034 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:13(get_breadth_first_search)|
|7816/15|0.464|0.000|0.467|0.031 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:28(send_flow)|
|1|0.002|0.002|0.002|0.002 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:51(<listcomp>)|
|7801|0.002|0.000|0.002|0.000 {built-in method builtins.min}|
|9376|0.002|0.000|0.002|0.000 {method 'pop' of 'list' objects}|
|15620|0.001|0.000|0.001|0.000 {built-in method builtins.len}|
|1|0.001|0.001|1.006|1.006 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:58(algorithm_dinic)|
|9360|0.001|0.000|0.001|0.000 {method 'append' of 'list' objects}|
|1|0.000|0.000|1.005|1.005 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\Dinic.py:48(run_core)|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
#### Algorytm Relabel To Front
##### Network id: network-type-1-10
Network nodes: 100
Max flow = 44

590407 function calls in 0.451 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|262928|0.225|0.000|0.326|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:29(discharge)|
|1|0.109|0.109|0.451|0.451 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:42(run_core)|
|7296|0.087|0.000|0.092|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:21(relabel)|
|262931|0.013|0.000|0.013|0.000 {built-in method builtins.len}|
|9897|0.007|0.000|0.009|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:13(push)|
|32921|0.007|0.000|0.007|0.000 {built-in method builtins.min}|
|7214|0.002|0.000|0.002|0.000 {method 'insert' of 'list' objects}|
|7214|0.001|0.000|0.001|0.000 {method 'pop' of 'list' objects}|
|1|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:44(<listcomp>)|
|1|0.000|0.000|0.451|0.451 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:70(algorithm_relabel_to_front)|
|1|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:49(<listcomp>)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.sum}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
##### Network id: network-type-1-25
Network nodes: 625
Max flow = 31

202318 function calls in 0.256 seconds

Ordered by: internal time

| ncalls|tottime|percall|cumtime|percall filename:lineno(function)| 
|---|---|---|---|---|
|98277|0.148|0.000|0.199|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:29(discharge)|
|557|0.049|0.000|0.050|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:21(relabel)|
|1|0.047|0.047|0.255|0.255 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:42(run_core)|
|98280|0.007|0.000|0.007|0.000 {built-in method builtins.len}|
|1|0.002|0.002|0.002|0.002 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:44(<listcomp>)|
|1|0.001|0.001|0.256|0.256 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:70(algorithm_relabel_to_front)|
|1236|0.001|0.000|0.001|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:13(push)|
|2872|0.001|0.000|0.001|0.000 {built-in method builtins.min}|
|545|0.000|0.000|0.000|0.000 {method 'insert' of 'list' objects}|
|545|0.000|0.000|0.000|0.000 {method 'pop' of 'list' objects}|
|1|0.000|0.000|0.000|0.000 C:\Users\MikBac\Desktop\Praca-magisterska-informatyka\projekt_magisterski\algorithms\RelabelToFront.py:49(<listcomp>)|
|1|0.000|0.000|0.000|0.000 {built-in method builtins.sum}|
|1|0.000|0.000|0.000|0.000 {method 'disable' of '_lsprof.Profiler' objects}|
