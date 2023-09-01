# Water jug Problem Solver

## Description
This repository solves Water jug problem exposing a command line interface
and a REST API to get user the capability of solving the problem.

## Requirements
It requires docker version 24.0.0 or greater

## Solution design
The repository organizes three projects inside a single repository:
    * A cli interface to solve the problem
    * A python library to solve the problem
    * A rest API which also solves the problem
Both API and CLI uses the same library for problem resolution.

## Repository structure
* docker -> contains all docke related stuff
* src -> contains source code it is separated into three directories
    1. api -> REST API
    2. cli -> CLI solution
    3. wjp_lib -> Library for solving the problem
* test -> unit test for both solutions
* Makefile -> We provide a makefile to build/run application quickly

## Building the images
The solution generates three separate docker images:
1) wjs_api for building the API
2) water_jug_solver for giving the CLI application
3) wfs_test for executing unit tests

To build all images you can execute:
$ make

## Running API
1. After building docker images execute:
 $ make run_api
2. Go to browser and type: localhost:8000/docs
3. Use API generated swagger to interact with API

## Running CLI
Execute:
 $ make run_cli

## Running Test
Execute:
 $ make run_test

## Deleting images
Execute:
 $ make clean

