# Projekt magisterski

## Markdown - odczyt

https://typora.io/

## Konfiguracja

Konfiguracja przez plik `config.json`.

Ustawienie listy sieci, które mają zostać przetestowane w pliku `benchmark.py` w wartości `NETWORKS`.

## Pierwsze uruchomienie

W celu przygotowania środowiska należy uruchomić skrypt `setenv.sh`. 

`setenv.sh` - generuje bazowe sieci typ-1.

`createnetwork.sh` - przyjmuje jeden argument - generuje sieć typ-1 poziomu podanego jako argument

## Generatory sieci:
* type_one
* type_half_random
* type_full_random
* type_steps_random

## Przykłady

Przykładowe raporty:

* `examples/report-example-v1.md`.
* `examples/report-example-v2.md`.

## TO-DO

| Zadanie                       | Plik                              | Status     | Notes
| ---                           | ---                               | ---        | ---  
| Algorytm Forda-Fulkersona     | algorithm-Ford–Fulkerson.py       | 100%       | Zrobione
| Algorytm Edmonds-Karp         | algorithm-Edmonds–Karp.py         | 100%       | Zrobione
| Algorytm Dinica               | algorithm-Dinic.py                | 100%       | Zrobione
| Algorytm Relabel-to-front     | algorithm-Relabel-to-front.py     | 100%       | Zrobione
| Generator sieci               | network-generator.py              | 100%       | Generuje typ-1 sieci
| Platforma testowa             | benchmark.py                      | 100%       | Zrobione (testowanie każdego algorytmu na n sieciach)

