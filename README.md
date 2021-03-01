# Coding challenge for Generally Intelligent

## Problem Statement
    	
There are several companies on the market, with each company processing some data in order to produce data in a new company-specific format. When a company gets a unit of input data, it produces a unit of new data. Unfortunately, each company can process only some limited amount of data, and each company can accept only some specific data formats. Of course, running each company costs the owner some money.

The information about the companies will be given to you as: 
- String[] names, (names[i] is the name of the i-th company)
- String[] process, (process[i] is a single-space delimited list of companies which can process the data produced by the i-th company)
- int[] cost, (cost[i] is the cost of running the i-th company)
- int[] amount, (amount[i] is the maximal amount of data that the i-th company can process)
- company1, (has an infinite amount of unprocessed data in its supply which can be processed)
- company2 (convert as much data as possible to the new format of company2, spending the least amount of money as possible)

You are to select the companies you want to run, since only running companies can process the data. Return the names of those companies as a String[], sorted in lexicographical order. If more than one answer is possible, return the lexicographically smallest one. If there is no way company2 can process any data at all, return an empty String[].

## TODO
- implement cost tracking
- implement amount of data than can be processed tracking
- add additional test data
- determine if processing is parallel (if company in 2nd step can process data full amount of data as 3rd step of another chain)
