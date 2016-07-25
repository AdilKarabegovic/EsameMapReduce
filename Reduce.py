import fileinput

checkin = 0
provut = 1

data = {}

splitChar = '\t'

for line in fileinput.input():

	values = line.split(splitChar)
	checkin = values[checkin]
	provut = int(values[provut])
	temp = {checkin:provut}

	if checkin in data:
		data[checkin] = data[checkin] + temp[checkin]
	else:
		data.update(temp)

print(data)