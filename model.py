
import csv

data_is_loaded = False

def load_data():

	with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		header = True
		global data_dic
		data_dic = {}
		global data_is_loaded

		for row in reader:
			if header:
				header = False
				continue
			if row[9] != "AK":
				if row[9] not in data_dic:
					data_dic[row[9]] = {}
					data_dic[row[9]]['dem2016'] = float(row[2])
					data_dic[row[9]]['gop2016'] = float(row[3])
					data_dic[row[9]]['total2016'] = float(row[4])
					data_dic[row[9]]['dem2012'] = float(row[13])
					data_dic[row[9]]['goo2012'] = float(row[14])
					data_dic[row[9]]['total2012'] = float(row[15])
				else:
					data_dic[row[9]]['dem2016'] += float(row[2])
					data_dic[row[9]]['gop2016'] += float(row[3])
					data_dic[row[9]]['total2016'] += float(row[4])
					data_dic[row[9]]['dem2012'] += float(row[13])
					data_dic[row[9]]['goo2012'] += float(row[14])
					data_dic[row[9]]['total2012'] += float(row[15])

		data_is_loaded = True



def get_data(party='dem', raw=True, sort_ascending=True, year=2016):
	if not data_is_loaded:
		load_data()

	if raw == True:
		outlist = [(i,data_dic[i][party+str(year)]) for i in data_dic.keys()]
	else:
		if party == 'dem':
			if year == 2016:
				outlist = [(i,data_dic[i]["dem2016"]/data_dic[i]["total2016"] ) for i in data_dic.keys()]
			else:
				outlist = [(i,data_dic[i]["dem2012"]/data_dic[i]["total2012"] ) for i in data_dic.keys()]
		else:
			if year == 2016:
				outlist = [(i,data_dic[i]["gop2016"]/data_dic[i]["total2016"] ) for i in data_dic.keys()]
			else:
				outlist = [(i,data_dic[i]["gop2012"]/data_dic[i]["total2012"] ) for i in data_dic.keys()]

	if sort_ascending == True:
		outlist = sorted(outlist, key = lambda x:x[1])
	else:
		outlist = sorted(outlist, key = lambda x:x[1],reverse = True)
	return outlist

# print (get_data())
# print (get_data(party='dem', raw=True, sort_ascending=False))
if __name__ == "__main__":

	points = 0
	data = get_data()
	if data[0] == ('WY', 55949.0) and data[-1] == ('CA', 7362490.0):
		points += 3.33

	data = get_data(party='gop', raw=False)
	if data [0][0] == 'DC' and int(data[0][1] * 100) == 4 and \
		data[-1][0] == 'WY' and int(data[-1][1] * 100) == 70:
		points += 3.33

	data = get_data(party='dem', raw=True, sort_ascending=False)
	if data[0] == ('CA', 7362490.0) and data[-1] == ('WY', 55949.0):
		points += 3.34

	print("points :", points)
