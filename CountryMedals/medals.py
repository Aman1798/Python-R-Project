#Importing useful functions
import csv
import json
import operator


class CountryMedals:

    def __init__(self, name, gold, silver, bronze):
        self.name = name
        self.gold = int(gold)
        self.silver = int(silver)
        self.bronze = int(bronze)
        self.total = int(self.gold) + int(self.silver) + int(self.bronze)
    
    def to_json(self):
        #returns a JSON representation of the object, with the object’s attributes as keyvalue pairs
        json_dict = {
            "gold" : self.gold, 
            "silver ": self.silver,
            "bronze" : self.bronze, 
            "total" : self.total}
        return json_dict


    def get_medals(self, medal_type):
        #returns the corresponding number of medals
        if medal_type == "gold":
            return self.gold
        elif medal_type == "silver":
            return self.silver
        elif medal_type == "bronze":
            return self.bronze
        elif medal_type == "total":
            return self.total
        else:
            return None


    def print_summary(self):
        #prints a textual summary of the number of medals received by the country

        print(str(self.name) + " received " + str(self.total) + " medals in total; " + str(self.gold) +  
              " gold, " + str(self.silver) + " silver, and " + str(self.bronze) + " bronze.\n")
    
    def compare(self, country_2):
        #shows a comparison of the medals received by two countries
        if (self.gold == country_2.gold):
            print("- Both "+ str(self.name) +" and " + str(country_2.name) + " received " + str(self.gold) + " gold medal(s).")
        elif (self.gold > country_2.gold):
            print("- " + str(self.name) + " received " + str(self.gold) + " gold medal(s), " + str(self.gold-country_2.gold) + " more than " + str(country_2.name) + " , which received " + str(country_2.gold) +" of them.")        
        else:
            print("- " + str(self.name) + " received " + str(self.gold) + " gold medal(s), " + str(country_2.gold-self.gold) + " fewer than " + str(country_2.name) + " , which received " + str(country_2.gold) +" of them.")
    
        if (self.silver == country_2.silver):
            print("- Both "+ str(self.name) +" and " + str(country_2.name) + " received " + str(self.silver) + " silver medal(s).")
        elif(self.silver > country_2.silver):
            print("- " + str(self.name) + " received " + str(self.silver) + " silver medal(s), " + str(self.silver - country_2.silver) + " more than " + str(country_2.name) + " , which received " + str(country_2.silver)+" of them.")
        else:
            print("- " + str(self.name) + " received " + str(self.silver) + " silver medal(s), " + str(country_2.silver-self.silver) + " fewer than " + str(country_2.name) + " , which received " + str(country_2.silver) +" of them.")

        if (self.bronze == country_2.bronze):
            print("- Both "+ str(self.name) +" and " + str(country_2.name) + " received " + str(self.bronze) + " bronze medal(s).")
        elif(self.bronze > country_2.bronze):
            print("- " + str(self.name) + " received " + str(self.bronze) + " bronze medal(s), " + str(self.bronze-country_2.bronze) + " more than " + str(country_2.name) + " , which received " + str(country_2.bronze) +" of them.")
        else:
            print("- " + str(self.name) + " received " + str(self.bronze) + " bronze medal(s), " + str(country_2.bronze-self.bronze) + " fewer than " + str(country_2.name) + " , which received " + str(country_2.bronze) +" of them.")

        
        if(self.total > country_2.total):
            print("\nOverall, " + str(self.name) + " received " + str(self.total) + " medal(s), " + str(self.total - country_2.total) + " more than " + str(country_2.name) + " , which received " + str(country_2.total) + " medal(s).")
        else:
            print("\nOverall, " + str(self.name) + " received " + str(self.total) + " medal(s), " + str(country_2.total - self.total) + " fewer than " + str(country_2.name) + " , which received " + str(country_2.total) + " medal(s).")



countries = dict()

#Intially, I had used pandas to read the csv file. I have left the code here as a comment
# df = pd.read_csv("medals.csv", usecols = ['Team/NOC','Gold','Silver','Bronze']) 
# df.to_csv('medals_edited.csv',index=False)

#Reading, CSV file using the CSV function. I have imported the CSV function at the start of code.
with open('medals.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        country_name = rows['Team/NOC']
        gold = rows['Gold']
        silver = rows['Silver']
        bronze = rows['Bronze']
        obj = CountryMedals(country_name,gold, silver, bronze)
        countries[country_name] = obj



def get_sorted_list_of_country_names(countries): 
    #extracts from the dictionary countries a list of country names alphabetically sorted
    sorted_countries = sorted(list(countries.keys()))
    return sorted_countries
sorted_countries = get_sorted_list_of_country_names(countries)

def sort_countries_by_medal_type_ascending(countries, medal_type):
    sorted_countries = sorted(countries.values(), key=operator.attrgetter(medal_type),reverse= True)
    return sorted_countries

def sort_countries_by_medal_type_descending(countries, medal_type):
    sorted_countries = sorted(countries.values(), key=operator.attrgetter(medal_type))
    return sorted_countries

def read_positive_integer():
    while True:
        number = int(input("Enter the threshold (a positive integer): "))
        if number < 0:
            print("Please re-enter a positive number.")
            continue
        else:
            pos_int = number
            return pos_int

def read_country_name():
    while True:
        name = str(input("Insert a country name ('q' for quit): "))
        if name not in (list(countries.keys())):
            print("Please re-enter a country from the list:\n")
            print(list(countries.keys()))
            continue
        else:
            country_name= name
            return country_name

def read_medal_type():
    while True:
        medal = str(input("Insert a medal type (chose among 'gold', 'silver', 'bronze', or 'total'): "))
        if medal not in ['gold', 'silver', 'bronze', 'total']:
            print("Please re-enter a medal type from the list: ['gold', 'silver', 'bronze', 'total']\n")
            continue
        else:
            medal_type= medal
            return medal_type



while True:
    user_input = str(input("Insert a command (Type 'H' for help: )"))
    if user_input == 'h' or user_input == 'H':
        print('''List of commands:
- (H)elp shows the list of comments;
- (L)ist shows the list of countries present in the dataset;
- (S)ummary prints out a summary of the medals won by a single country;
- (C)ompare allows for a comparison of the medals won by two countries;
- (M)ore, given a medal type, lists all the countries that received more medals than a threshold;
- (F)ewer, given a medal type, lists all the countries that received fewer medals than a threshold;
- (E)xport, save the medals table as '.json' file;
- (Q)uit.''')
    
    elif user_input == 'l' or user_input == 'L':
        print("The dataset contains " + str(len(countries)) + " countries: " + ', '.join(map(str, sorted_countries)))
    
    elif user_input == 'q' or user_input == 'Q':
        break
    
    elif user_input == 's' or user_input == 'S':
        c_names= read_country_name()
        print(str(c_names) + " received " + str(countries[c_names].total) + " medals in total; " + str(countries[c_names].gold) +  
              " gold, " + str(countries[c_names].silver) + " silver, and " + str(countries[c_names].bronze) + " bronze.\n")
    
    elif user_input == 'c' or user_input == 'C':
        print('\nCompare two countries')
        country_1 = read_country_name()        
        print("\nInsert the name of the country you want to compare against '"+ country_1 + "'")
        country_2 = read_country_name()
        print("\nMedals comparison between '" + country_1 + "' and '"+ country_2+ "':")
        country_1_gold = countries[country_1].gold
        country_1_silver = countries[country_1].silver
        country_1_bronze = countries[country_1].bronze
        obj1 = CountryMedals(country_1,country_1_gold, country_1_silver, country_1_bronze)
        country_2_gold = countries[country_2].gold
        country_2_silver = countries[country_2].silver
        country_2_bronze = countries[country_2].bronze
        obj2 = CountryMedals(country_2,country_2_gold,country_2_silver,country_2_bronze)
        obj1.compare(obj2)
    
    elif user_input == 'e' or user_input == 'E':
        file_name = str(input("Enter the file name (.json): "))
        file_name_json = str(file_name) + ".json"
        countries_json = {country: medals.to_json() for country, medals in countries.items()}
        with open(file_name_json, "w") as outfile: 
            json.dump(countries_json, outfile, indent = 4)
        print("File '" + file_name + "' correctly saved.\n")
   
    elif user_input == 'm' or user_input == 'M':
        print("Given a medal type, lists all the countries that received more medals than a threshold;")
        medal_type = read_medal_type()
        threshold = read_positive_integer()
        print("Countries that received more than "+ str(threshold) + " '"+ medal_type +"' medals:\n")
        for country in (sorted(countries.values(), key=operator.attrgetter(medal_type),reverse= True)):
            if medal_type == 'gold' and country.gold > threshold:
                print("- " + country.name+ " received " + str(country.gold))
            elif medal_type == 'silver' and country.silver > threshold:
                print("- " + country.name+ " received " + str(country.silver))
            elif medal_type == 'bronze' and country.bronze > threshold:
                print("- " + country.name+ " received " + str(country.bronze))
            elif medal_type == 'total' and country.total > threshold:
                print("- " + country.name+ " received " + str(country.total))
    
    elif user_input == 'f' or user_input == 'F':
        print("Given a medal type, lists all the countries that received fewer medals than a threshold;")
        medal_type = read_medal_type()
        threshold = read_positive_integer()
        print("Countries that received fewer than "+ str(threshold) + " '"+ medal_type +"' medals:\n")
        for country in (sorted(countries.values(), key=operator.attrgetter(medal_type))):
            if medal_type == 'gold' and country.gold < threshold:
                print("- " + country.name+ " received " + str(country.gold))
            elif medal_type == 'silver' and country.silver < threshold:
                print("- " + country.name+ " received " + str(country.silver))
            elif medal_type == 'bronze' and country.bronze < threshold:
                print("- " + country.name+ " received " + str(country.bronze))
            elif medal_type == 'total' and country.total < threshold:
                print("- " + country.name+ " received " + str(country.total))
    
    else:
        print("Please enter correct option or press (H) for list of commands.\n")




'''

References:-
https://stackoverflow.com/questions/10052912/how-to-sort-dictionaries-of-objects-by-attribute-value
https://www.geeksforgeeks.org/

'''
