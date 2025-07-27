# Exercises: Level 1

#1. Declare an empty list
empty_list = []
print("empty_list: ",empty_list)

# 2. Declare a list with more than 5 items
mates  = ["Ali","Abalo","Afi","Kodjo","Ama","Koffi","Lili"]
print("list declared: ",mates)

# 3. Find the length of your list
length_of_mates = len(mates)
print("length of mates:",length_of_mates)

# 4. Get the first item, the middle item and the last item of the list
first_item = mates[0]
middle_item = mates[3]
last_item = mates[6]
print("first item:",first_item)
print("middle item:",middle_item)
print("last item:",last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Akounda",22,180,"Single","Kara"]
print("mixed data type:",mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]


# 7. Print the list using print()
print("it companies:",it_companies)

# 8. Print the number of companies in the list
print("Number of iT companies: ",len(it_companies))

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[6]
print("First company:",first_company)
print("Middle company:",middle_company)
print("Last company:",last_company)

# 10.Print the list after modifying one of the companies
it_companies[6] = "Tesla"
print(it_companies)

# 11.Add an IT company to it_companies
it_companies.append("OpenAI")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4,"Nvdia")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2].upper()
print(it_companies)

# 14. Join the it_companies with a string '#; '
'#; '.join(it_companies)
print(it_companies)

# 15. Check if a certain company exists in the it_companies list.
"Apple" in it_companies
print(it_companies)

# 16.Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18.Slice out the first 3 companies from the list
first_three_comp = it_companies[0:3]
print(first_three_comp)

# 19.Slice out the last 3 companies from the list
last_three_comp = it_companies[-1:-3]
print(last_three_comp)

# 20.Slice out the middle IT company or companies from the list
midle_it_comp = it_companies[len(it_companies)//2-1]
print(midle_it_comp)

# 21. Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)


# 22. Remove the middle IT company or companies from the list
it_companies.remove(midle_it_comp)
print(it_companies)


# 23. Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)


# 25. Destroy the IT companies list
it_companies.clear()
print(it_companies)

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list =  front_end + back_end
print(joined_list)

# 27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = joined_list.copy()
print("full_stack: ",full_stack)
lan_to_add = ["Redux", "Python", "SQL"]
full_stack.extend(lan_to_add)
print("full_stack: ",full_stack)

# Exercises: Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
sorted_ages = ages.sort()
print("sorted ages:",ages)
min_age = ages[0]
print("minimum age: ", min_age)
max_age = ages[-1]
print("maximum age: ", max_age)

# Add the min age and the max age again to the list
ages.insert(0,min_age)
ages.insert(-1,max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
#median_age = (it_companies[(len(it_companies)//2)-1] + it_companies[(len(it_companies)//2)])/2
median_age = (ages[4] + ages[5])/2
print("Median age = ",median_age)

# Find the average age (sum of all items divided by their number )
average_age = sum(ages)/len(ages)
print("Average age = ",average_age)

# Find the range of the ages (max minus min)
range_of_age = max_age - min_age
print("Range Of age = ",range_of_age)

# Compare the value of (min - average) and (max - average), use abs() method
min_avr = abs(min_age - average_age)
max_avr = abs(max_age - average_age)
print("average age is less the median age")

#1. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
midle_country = countries[96]
print(midle_country)

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_country_group = countries[0 : 96]
second_country_goupe = countries[97 : ]
print(first_country_group)
print(second_country_goupe)

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpacking the country
countriess = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *candic_countries = countriess
print("First country:",first_country)
print("second country:",second_country)
print("Third country", third_country)
print("candic country:",candic_countries)

