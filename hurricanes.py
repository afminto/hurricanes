# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

def float_dam(dmg):
	dm = []
	for d in dmg:
		if d[-1] == 'd':
			dm.append(d)
		elif d[-1] == 'B':
			num = float(d[:len(d)-1])
			dm.append(str(num*1000000000))
		else:
			num = float(d[:len(d)-1])
			dm.append(str(num*1000000))
	return dm

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
f = float_dam(damages)
print(float_dam(damages))

# 2 
# Create a Table
def dic(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  z = list(zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths))
  dic = {}
  for (nm, mo, yr, ma, ar, dm, de) in z:
    di = {}
    di = {'Name': nm, 'Month': mo, 'Year': yr, 'Max Sustained Wind': 165, 'Areas Affected': ar, 'Damage': dm, 'Deaths': de}
    dic[nm] = di
  return dic

# Create and view the hurricanes dictionary
r = dic(names, months, years, max_sustained_winds, areas_affected, f, deaths)
print(r)
# 3
# Organizing by Year
def year_dic(hurricanes):
  hurricanes_by_year = dict()
  for cane in hurricanes:
    current_year = hurricanes[cane]["Year"]
    current_cane = hurricanes[cane]
    if current_year not in hurricanes_by_year:
      hurricanes_by_year[current_year] = [current_cane]
    else:
      hurricanes_by_year[current_year].append(current_cane)
  return hurricanes_by_year
print(year_dic(r))
# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def areas(hurricanes):
  aff = dict()
  for cane in hurricanes:
    for area in hurricanes[cane]["Areas Affected"]:
      if area in aff:
        aff[area] += 1
      else:
        aff[area] = 1
  return aff
a = areas(r)
print(areas(r))
# 5 
# Calculating Maximum Hurricane Count
def max_count(areas):
  most = ""
  most_count = 0
  for a in areas:
    if areas[a] > most_count:
      most = a
      most_count = areas[a]
  return most, most_count
# find most frequently affected area and the number of hurricanes involved in
c = max_count(a)
print(c)
# 6
# Calculating the Deadliest Hurricane
def deadliest(hurricanes):
  most = ""
  most_count = 0
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] > most_count:
      most_count = hurricanes[cane]["Deaths"]
      most = cane
  return most, most_count

# find highest mortality hurricane and the number of deaths
print(deadliest(r))
# 7
# Rating Hurricanes by Mortality
def rating(hurricanes):
  rate = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] <= 0:
      rate[0].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] <= 100:
      rate[1].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] <= 500:
      rate[2].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] <= 1000:
      rate[3].append(hurricanes[cane])
    elif hurricanes[cane]["Deaths"] <= 10000:
      rate[4].append(hurricanes[cane])
    else:
       rate[5].append(hurricanes[cane])
  return rate
    

# categorize hurricanes in new dictionary with mortality severity as key
mo = rating(r)
print(mo)

# 8 Calculating Hurricane Maximum Damage

def most_damage(hurricanes):
  most = ""
  most_count = 0
  for cane in hurricanes:
    if hurricanes[cane]["Damage"] == "Damages not recorded":
      continue
    elif float(hurricanes[cane]["Damage"]) > most_count:
      most = cane
      most_count = float(hurricanes[cane]["Damage"])
  return most, most_count

# find highest damage inducing hurricane and its total cost

print(most_damage(r))
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def dam_rating(hurricanes):
  rate = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for cane in hurricanes:
    if hurricanes[cane]["Damage"] == "Damages not recorded":
      continue
    elif float(hurricanes[cane]["Damage"]) <= 0:
      rate[0].append(hurricanes[cane])
    elif float(hurricanes[cane]["Damage"]) <= 100000000:
      rate[1].append(hurricanes[cane])
    elif float(hurricanes[cane]["Damage"]) <= 1000000000:
      rate[2].append(hurricanes[cane])
    elif float(hurricanes[cane]["Damage"]) <= 10000000000:
      rate[3].append(hurricanes[cane])
    elif float(hurricanes[cane]["Damage"]) <= 50000000000:
      rate[4].append(hurricanes[cane])
    else:
       rate[5].append(hurricanes[cane])
  return rate
print(dam_rating(r))
