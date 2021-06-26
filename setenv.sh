#!/bin/bash

# Created by Mikołaj Bachorz on 2020-2021

rm -f ./reports/* &&


# ./createnetwork.sh [nodes]

echo "network lvl 5"
./createnetwork.sh 5

echo "network lvl 10"
./createnetwork.sh 10

echo "network lvl 20"
./createnetwork.sh 20

echo "network lvl 50"
./createnetwork.sh 50

echo "network lvl 100"
./createnetwork.sh 100

echo "network lvl 200"
./createnetwork.sh 200

echo "network lvl 500"
./createnetwork.sh 500

echo "network lvl 1000"
./createnetwork.sh 1000
