#!/usr/bin/python
import fileinput

checkin = 2
provut = 3

splitChar = ';'

for line in fileinput.input():
	values = line.split(splitChar)
	checkin = values[checkin]
	provut = values[provut].replace("\n","")
	print(('{0}\t{1}'.format(checkin, downTime)))