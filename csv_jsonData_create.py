import re
import sys
import subprocess
import time
from datetime import datetime
from datetime import timedelta
import random

try:
    import json
except ImportError:
    import simplejson as json


# define empty string
empty_string = ""

# function to generate a random number between i and j  (i<= n <= j)
def rannum(i, j):
  return random.randint(i, j)

def func_true_false():
  if rannum(0,1) == 1:
     return True
  else: 
     return False
    
# function to generate a random float number between a and b  (a<= n <= b)
def ranfloat(a, b, d):
  myFloat = "%s.%df" % ("%", d) % random.uniform(a, b)
  return myFloat


# functio to generate a random IP address
def ran_ip_address():
  ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
  return ip


# function to generate 'app' (long)  (no 1 field for event)
# a long number of 6 digits between 111111 and 999999)
def func_01_app(choice):
  if choice == 1:
     if func_true_false() == True:
        return rannum(111111, 999999)
     else:
        return empty_string
  elif choice == 2:
    return empty_string
  else:
    return rannum(111111, 999999)

# function to generate 'amplitude_id'(long)  (no 2 field for event)
# a long number of 11 digits  between 11111111111 and 99999999999)
def func_02_amplitude_id(choice):
  if choice == 1:
     if func_true_false() == True:
        return rannum(11111111111, 99999999999)
     else:
        return empty_string
  elif choice == 2:
    return empty_string
  else:
    return rannum(11111111111, 99999999999) 


# function to generate user_id (long): required if device_id is not supplied (no 3 field for event)
# email syntax/format:  first.last@domainName.com
def func_03_user_id():
  emailDomains = ["gmail.com", "yahoo.com", "hotmail.com", "mail.com", "inbox.com", "aol.com"]
  firstNames = ["John", "Tom", "James", "Robert", "Alan", "Michael", "David", "George", "Paul", "Brian",
                "Linda", "Elizabeth", "Mary", "Susan", "Lisa", "Nancy", "Karen", "Betty", "Carol", "Sharon"]
  lastNames = ["Smith", "Johnson", "William", "Brown", "Jones", "Miller", "Davis", "Garcia", "Wilson", "Taylor",
               "Anderson", "White", "Lee", "Allen", "Hall", "Harris", "Walker", "King", "Scott", "Hill"]
  # now use random number generate to get a random firstName, random lastName, and random emailDomainName

  myFirstName = firstNames[rannum(0, len(firstNames) - 1)]
  myLastName = lastNames[rannum(0, len(lastNames) - 1)]
  myEmailDomainName = emailDomains[rannum(0,  len(emailDomains) - 1)]
  myUserID = myFirstName + "." + myLastName + "@" + myEmailDomainName
  return myUserID


# help function to generate a random ID (digit+letter combinations of size length)
def id_generator(size):
  string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  return ''.join(random.choice(string) for _ in range(size))

# function to generate device_id(string): required if user_id is not supplied (no 4 field for event)
## device_id format:  "C8F9E604-F01A-4BD9-95C6-8E5357DF265D"
## there are 5 fields: 8-4-4-4-12, respectively
## combinations of letters and digits
## use random number generator to create the combinations of digits and capital letters
def func_04_device_id():
  # get field1:  8 letter/digit combinations
  field1 = id_generator(8)
  # get field2:  4 letter/digit combinations
  field2 = id_generator(4)
  # get field3:  4 letter/digit combinations
  field3 = id_generator(4)
  # get field4:  4 letter/digit combinations
  field4 = id_generator(4)
  # get field5:  12 letter/digit combinations
  field5 = id_generator(12)

  myDeviceID = field1 + "-" + field2  + "-" + field3  + "-" + field4  + "-" + field5
  return myDeviceID


# function to genetate a datetime string between "start" and "end" datetimes (No 5 - No. 8 fields)
# event_time/server_upload_time/client_event_time/client_upload_time: timestamp '%Y-%m-%d %H:%M:%S.%L'
def func_05_08_dateTime_random(start, end):
  if hasattr(datetime, 'strptime'):
    #python 2.6
    strptime = datetime.strptime
  else:
    #python 2.4 equivalent
    strptime = lambda date_string, format: datetime(*(time.strptime(date_string, format)[0:6]))

  TIME_FMT = '%Y-%m-%d %H:%M:%S'
  dStart = strptime(start, TIME_FMT)
  dEnd = strptime(end, TIME_FMT)
  delta = dEnd -dStart 
  int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
  random_second = random.randrange(int_delta)
  myDateTime = dStart + timedelta(seconds=random_second)

  myDateTimeStr = myDateTime.strftime(TIME_FMT)

  millSec = rannum(101, 999)

  myDateTimeStr = myDateTimeStr +  "." + str(millSec)

  return myDateTimeStr


# function to genetate an event_id (long) (No. 9 field)
# a long number of 9 digits between 111111111 and 999999999)
def func_09_event_id(choice):
  if choice == 1:
    if func_true_false() == True:
       return rannum(111111111, 999999999)
    else:
       return empty_string
  elif choice == 2:
    return empty_string
  else:
    return rannum(111111111, 999999999)


# function to genetate a session_id(long) (No. 10 field)
# a long number of 8 digits between 11111111 and 99999999)
# choice: 1 - random generate,  2 - return empty_string,  3 - return rannum(11111111, 99999999)
def func_10_session_id(choice):
  if choice == 1:
    if func_true_false() == True:
       return rannum(11111111, 99999999)
    else:
       return empty_string
  elif choice == 2:
    return empty_string
  else:
    return rannum(11111111, 99999999)
     


# function to generate event_type(string) (No 11 field for event)
# negative tests can be exercised by checking func_true_false() here
def  func_11_event_type():
  eventTypes = ["watch_tutorial", "travel", "production", "engineering", "marketing", "landmark", "sports"]
  return eventTypes[rannum(0, len(eventTypes) - 1)]


# function to generate amplitude_event_type(string) (No 12 field for event)
def func_12_amplitude_event_type(choice):
  amplitudeEventTypes = ["custom", "scr", "05_at_5", "mage", "planned", "measurement", "mean amplitude", "apr", "_pmp png", "branch", "screen_shot_2017", "cardirvascular", "funnel", "app", "chrome", "data"]
  if choice == 1:
     if func_true_false() == True:
        return amplitudeEventTypes[rannum(0, len(amplitudeEventTypes) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return amplitudeEventTypes[rannum(0, len(amplitudeEventTypes) - 1)]


# function to generate version_name(string) (No 13 field for event)
def func_13_version_name(choice):
  versionName = ["1.0.0", "1.0.5", "1.1", "2.0", "2.0.3", "2.1", "2.2", "2.5"]
  if choice == 1:
     if func_true_false() == True:
        return versionName[rannum(0, len(versionName) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return versionName[rannum(0, len(versionName) - 1)]


# function to generate _schema(long) (No 14 field for event)
def func_14_schema(choice):
  if choice == 1:
     if func_true_false() == True:
        return rannum(111, 999)
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return rannum(111, 999)


# function to generate adid(string) (No 15 field for event)
def func_15_adid(choice):
  bucket1 = id_generator(8)
  bucket2 = id_generator(4)
  bucket3 = id_generator(4)
  bucket4 = id_generator(4)
  bucket5 = id_generator(12)

  adid = bucket1 + "-" + bucket2  + "-" + bucket3  + "-" + bucket4  + "-" + bucket5

  if choice == 1:
     if func_true_false() == True:
        return adid
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return adid


# function to generate json object type of groups (No 16 field for event)
# for this test, currently just create up to 5 companies for this 
# group: json
def func_16_groups():
  comany_names = [ ["Amplitude", "DataMonster"], 
                   ["Treasure Data", "Customer Data"], 
                   ["Twitter", "Twitter Network"],
                   ["Facebook", "Social Media"],
                   ["Google", "SearchGiant"],
                   ["Apple", "TechMonster"],
                   ["Microsoft", "SoftwareCompany"],
                   ["Boeing", "Aircraft manufacturer"],
                   ["Disney", "Entertainmen Media"],
                   ["Netflix", "Streaming Media"] ]

  # randomly create from 1 to 5 json objects
  n = rannum(1, 5)
  data = {}
  for i in range(n):
    # randomly generate an ID between (1, 10)
    id = rannum(1, 10)
    myComanyName = comany_names[id-1]
    # create dictionary item
    data[str(id)] = myComanyName

  # create json object
  json_data = json.dumps(data)

  return json_data


# function to generate field 17 - idfa (string)  (No 17 field for event)
# more works are needed here: value of idfa should be the same as device_id if os_name is ios
def func_17_idfa(choice):
  bucket1 = id_generator(8)
  bucket2 = id_generator(4)
  bucket3 = id_generator(4)
  bucket4 = id_generator(4)
  bucket5 = id_generator(12)

  idfa = bucket1 + "-" + bucket2  + "-" + bucket3  + "-" + bucket4  + "-" + bucket5

  if choice == 1:
     if func_true_false() == True:
        return idfa
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return idfa


# function to generate field 18 - library (string) (No 18 field for event)
def func_18_library(choice):
  library = ["amplitude-js/2.5.0", "http/1.0", "http/2.0"]

  if choice == 1:
     if func_true_false() == True:
        return library[rannum(0, len(library) - 1)]
     else:
        return empty_string 
  elif choice == 2:
     return empty_string
  else:
     return library[rannum(0, len(library) - 1)]


# function to generate field 19 - processed_time (timestamp: '%Y-%m-%d %H:%M:%S.%L') (No 19 field for event)
def func_19_processed_time(start, end):
  return func_05_08_dateTime_random(start, end)
  #return empty_string


# function to generate field 20 - user_creation_tie ('%Y-%m-%d %H:%M:%S.%L') (No 20 field for event)
def func_20_user_creation_time(start, end):
  #return empty_string
  return func_05_08_dateTime_random(start, end)

# function to generate field 21 - platform (string)  (No 21 field for event)
def func_21_platform(choice):
  platforms = ["iOS", "Android", "Web"]

  if choice == 1:
     if func_true_false() == True:
        return platforms[rannum(0, len(platforms) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return platforms[rannum(0, len(platforms) - 1)]


# function to generate field 22 - os_name(string)  (No 22 field for event)
def func_22_os_name(choice):
  osNames = ["ios", "android", "chrome", "firefox", "safari"]

  if choice == 1:
     if func_true_false() == True:
        return osNames[rannum(0, len(osNames) - 1)]
     else:
        return empty_string
  elif choice == 2:
    return empty_string
  else:
    osNames[rannum(0, len(osNames) - 1)]


# function to generate field 23 - os_version (string)  (No 23 field for event)
def func_23_os_version(choice):
  osVersions = ["1.0", "1.1", "2.0", "2.3", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0", "10.0"]

  if choice == 1:
     if func_true_false() == True:
        return osVersions[rannum(0, len(osVersions) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return osVersions[rannum(0, len(osVersions) - 1)]


# function to generate field 24 - device_brand (string)  (No 24 field for event)
def func_24_device_brand(choice):
  deviceBrands = ["Apple", "Google", "Huawei", "Samsung", "Nikia", "Sony", "Motorola", "Blackberry", "HP", "Plum"]

  if choice == 1:
     if func_true_false() == True:
        return deviceBrands[rannum(0, len(deviceBrands) -1 )]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return deviceBrands[rannum(0, len(deviceBrands) -1 )]


# function to generate field 25 - device_manufacturer (string) (No 25 field for event)
def func_25_device_manufacturer(choice):
  deviceManufacturers = ["Apple", "AT&T", "Acer", "Amazon", "Blackberry", "Dell", "Google", "HP", "HTC", "Huawei"]

  if choice == 1:
     if func_true_false() == True:
        return deviceManufacturers[rannum(0, len(deviceManufacturers) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return deviceManufacturers[rannum(0, len(deviceManufacturers) - 1)]


# function to generate field 26 - device_model (string)  (No 26 field for event)
def func_26_device_model(choice):
  deviceModels = ["iphone", "iPad Mini", "iPad", "iPod Touch", "iPad Pro", "Apple TV", "Apple Watch", "Samsung Galaxy", "Andriod", "Google Home", "Google Home Mini"] 

  if choice == 1:
     if func_true_false() == True:
        return deviceModels[rannum(0, len(deviceModels) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return deviceModels[rannum(0, len(deviceModels) - 1)]


# function to generate field 27 - device_carrier (string)  (No 27 field for event)
def func_27_device_carrier(choice):
  deviceCarriers = ["AT&T", "Sprint", "Verizon", "T-Mobile", "Circket"]

  if choice == 1:
     if func_true_false() == True:
        return deviceCarriers[rannum(0, len(deviceCarriers) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return deviceCarriers[rannum(0, len(deviceCarriers) - 1)]


# function to generate field 28 - device type (string)  (No 28 field for event)
def func_28_device_type(choice):
  deviceTypes = ["iPhone 5s", "iPhone 6", "iPhone 6s", "iPhone 7", "iPhone 8", "iPhone X", "iPad Pro", "iPad Mini", "Windows10", "Windows8", "Google Pixel", "Microsoft Lumia 430"]

  if choice == 1:
     if func_true_false() == True:
        return deviceTypes[rannum(0, len(deviceTypes) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return deviceTypes[rannum(0, len(deviceTypes) - 1)]


# function to generate field 29 - device_family (string)  (No 29 field for event)
def func_29_device_family(choice):
  deviceFamilies = ["Apple iPhone", "Apple iPad", "Google Phone", "Samsung Phone", "Motorola Phone", "Huawei Phone"]

  if choice == 1:  
     if func_true_false() == True:
        return deviceFamilies[rannum(0, len(deviceFamilies) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return deviceFamilies[rannum(0, len(deviceFamilies) - 1)]


# function to generate field 30 - location_latitude (string)  (No 30 field for event)
def func_30_location_lat(choice):

  if choice == 1:
     if func_true_false() == True:
        return ranfloat(1.000005, 200.999995, 6)
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return ranfloat(1.000005, 200.99995, 6)


# function to generate field 31 - location_longitude (string)  (No 31 field for event)
def func_31_location_lng(choice):

  if choice == 1: 
     if func_true_false() == True:
        return ranfloat(1.000005, 200.999995, 6)
     else:
        return empty_string
  elif choice == 2:
    return empty_string
  else:
    return ranfloat(1.000005, 200.999995, 6)


# function to generate field 32 - country (stirng)  (No 32 field for event)
def func_32_country(choice):
  countries = ["United States", "Japan", "Canada", "England", "France", "Germany", "Itlay", "Mexico", "Sweden"]

  if choice == 1:
     if func_true_false() == True:
        return countries[rannum(0, len(countries) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return countries[rannum(0, len(countries) - 1)]


# function to generate field 33 - language (sting)  (No 33 field for event)
def func_33_language(choice):
  languages = ["English", "Japanese", "Chinese", "Dutch", "Spanish", "Persian", "Arabic", "French", "German"]

  if choice == 1:
     if func_true_false() == True:
        return languages[rannum(0, len(languages) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return languages[rannum(0, len(languages) - 1)] 


# function to generate field 34 - city (sting)  (No 34 field for event)
def func_34_city(choice):
  cities = ["San Francisco", "San Jose", "Sunnyvale", "New York", "Cupertino", "Toyko", "Osaka", "Beijing"]

  if choice == 1:
     if func_true_false() == True:
        return cities[rannum(0, len(cities) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_tring
  else:
     return cities[rannum(0, len(cities) - 1)]


# function to generate field 35 - region (string)  (No 35 field for event)
def func_35_region(choice):
  regions = ["California", "Michigan", "Indiana", "Hawaii", "New  Mexico", "New York", "Nevada", "Lowa"]

  if choice == 1:
     if func_true_false() == True:
        return regions[rannum(0, len(regions) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return regions[rannum(0, len(regions) - 1)]


# function to generate field 36 - dma (sting) (No 36 field for event)
def func_36_dma(choice):
  dmas = ["San Francisco-Oakland-San Jose, CA", "New York, New York", "Tokyo, Japan", "Beinig, China", "Paris, France"]

  if choice == 1:
     if func_true_false() == True:
        return dmas[rannum(0, len(dmas) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return dmas[rannum(0, len(dmas) - 1)]


# function to generate field 37 - revenue (string)  (No 37 field for event)
def func_37_revenue(choice):

  if choice == 1:
     if func_true_false() == True:
        return ranfloat(1.005, 500.995, 3)
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return ranfloat(1.005, 500.995, 3)


# function to generate field 38 - ip_address (string) (No 38 field for event)
def func_38_ip_address(choice):

  if choice == 1:
     if func_true_false() == True:
        return ran_ip_address()
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return ran_ip_address()


# function to generate field 39 - paying (sting)  (No 39 field for event)
def func_39_paying(choice):
  payings=["tax", "refund", "earnings", "credit card"]

  if choice == 1:
     if func_true_false() == True:
        return payings[rannum(0, len(payings) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return payings[rannum(0, len(payings) - 1)]


# function to generate field 40 - start_version (string) (No 40 field for event)
def func_40_start_version(choice):
  startVersions = ["1.0", "3.5", "4.0", "6.6", "7.4", "8.8", "10.0", "12.0", "11.11"]

  if choice == 1:
     if func_true_false() == True:
        return startVersions[rannum(0, len(startVersions) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return startVersions[rannum(0, len(startVersions) - 1)]


# function to generate json object type of event_properties (No 41 field for event)
# event_properties: json
def func_41_event_properties():
  load_time = "load_time"
  sources = ["notification", "warning", "receipt"]
  dates = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" ]

  data = {}
  # first generate load time
  myLoadTime = ranfloat(0.1111, 5.9999, 4) 
  myLoadTimeStr = str(myLoadTime)

  data[load_time] = myLoadTimeStr
  # next add 'source'
  mySource = sources[rannum(0, 2)]
  data["source"] = mySource
  # last the dates (up to 3 dates)
  size = rannum(1, 3)
  myDates = random.sample(dates, size)
  data["dates"] = myDates
  json_data = json.dumps(data)

  return json_data


# function to generate json object type of user_properties (No 42 field for event)
# user_properties: json
def func_42_user_properties():
  sex = ["male", "female"]
  interests = ["chess", "football","baseball", "basketball","swimming", "art", "video game", 
               "movie", "music", "hiking", "running", "collection", "poker", "singing", "hunting"]

  data = {}
  data["age"] = rannum(25, 75)
  data["gender"] = sex[ rannum(0, 1)]
  size = rannum(1, 6)
  data["interests"] =  random.sample(interests, size)
  json_data = json.dumps(data)

  return json_data


# function to generate field 43 - data (string) (No 43 field for event)
def func_43_data(choice):
  data = ["guessing", "preview", "run", "test"]
  
  if choice == 1:
     if func_true_false() == True:
        return data[rannum(0, len(data) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return data[rannum(0, len(data) - 1)]


# function to generate field 44 - uuid (string)  (No 44 field for event)
def func_44_uuid(choice):
  uuid = id_generator(20)

  if choice == 1:
     if func_true_false() == True:
        return uuid
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return uuid


# function to generate field 45 - insert_id (string)  (No 45 field for event)
def func_45_insert_id(choice):
  insert_ids = ["unique1", "unique2", "unique3", "unique4", "unique5"]

  if choice == 1:
     if func_true_false() == True:
        return insert_ids[rannum(0, len(insert_ids) - 1)]
     else:
        return empty_string
  elif choice == 2:
     return empty_sting
  else:
     return insert_ids[rannum(0, len(insert_ids) - 1)]


# function to generate field 46 (No 46 field for event)
# time: long
def func_46_time(choice):
  
  if choice == 1:
     if func_true_false() == True:
        return rannum(1111111111, 9999999999)
     else:
        return empty_string
  elif choice == 2:
     return empty_string
  else:
     return rannum(1111111111, 9999999999)


def main():
  if len(sys.argv) < 3:
     print "Usage: ", sys.argv[0] , " output_csv_file_name  no_of_events "
     sys.exit(1)

  # get output file name
  outfname = sys.argv[1]

  # get number of events
  ne = int(sys.argv[2])

  # define CSV file separator (default is ",")
  CSV_delimiter = ";"

  # define the header line
  header = [
    "app",
    "amplitude_id",
    "user_id",
    "device_id",
    "event_time",
    "server_upload_time",
    "client_event_time",
    "client_upload_time",
    "event_id",
    "session_id",
    "event_type",
    "amplitude_event_type",
    "version_name",
    "_schema",
    "adid",
    "groups",
    "idfa",
    "library",
    "processed_time",
    "user_creation_time",
    "platform",
    "os_name",
    "os_version",
    "device_brand",
    "device_manufacturer",
    "device_model",
    "device_carrier",
    "device_type",
    "device_family",
    "location_lat",
    "location_lng",
    "country",
    "language",
    "city",
    "region",
    "dma",
    "revenue",
    "ip_address",
    "paying",
    "start_version",
    "event_properties",
    "user_properties",
    "data",
    "uuid",
    "_insert_id",
    "time" ]

  # open output file for write
  fout = open(outfname,'w')

  count = 0
  lenFields = len(header)

  # set random generator seed (to current time, which always differs from previous runs, so randoms won't repeat)
  random.seed(datetime.now())

  # first print the header line onto the output file, with semicolon as separtor
  for i in range(lenFields):

    ## last line print differently, no ";" to follow, but with "\n" to end
    if i != (lenFields -1):
      fout.write (('%s%s ') % (header[i],CSV_delimiter)) 
    else:
      fout.write (('%s \n') % (header[i]))

  choices = [0 if i==0 else 3 for i in range(0,47)]

  # next generate ne events and write them onto output file
  for i in range(ne):
    myEvent = ""

    # 1) add 'app'
    myApp = func_01_app(choices[1])
    myEvent = myEvent + str(myApp) + CSV_delimiter

    # 2) add 'amplitude_id'
    myAmplitude_id = func_02_amplitude_id(choices[9])
    myEvent = myEvent + str(myAmplitude_id) + CSV_delimiter

    # 3) add 'user_id'
    myUser_id = func_03_user_id()
    myEvent = myEvent + myUser_id + CSV_delimiter
    

    # 4) add 'device_id'
    myDevice_id = func_04_device_id()
    myEvent = myEvent + myDevice_id + CSV_delimiter

    # 5) add 'event_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = func_05_08_dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + CSV_delimiter

    # 6) add 'server_upload_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = func_05_08_dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + CSV_delimiter

    # 7) add 'client_event_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = func_05_08_dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + CSV_delimiter

    # 8) add 'client_upload_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = func_05_08_dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + CSV_delimiter

    # 9) add 'event_id'
    myEvent_id = func_09_event_id(choices[9])
    myEvent = myEvent + str(myEvent_id) + CSV_delimiter

    # 10) add 'session_id' 
    mySession_id = func_10_session_id(choices[10])
    myEvent = myEvent + str(mySession_id) + CSV_delimiter

    # 11) add 'event_type'
    myEvent_type = func_11_event_type()
    myEvent = myEvent + str(myEvent_type) + CSV_delimiter


    # 12) add 'amplitude_event_type'
    myItem = func_12_amplitude_event_type(choices[12])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 13) add 'version_name'
    myItem = func_13_version_name(choices[13])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 14) add 'schema'
    myItem = func_14_schema(choices[14])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 15) add 'adid '
    myItem = func_15_adid(choices[15])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 16) add 'groups'
    myItem = func_16_groups()
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 17) add 'idfa'
    myItem = func_17_idfa(choices[17])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 18) add 'library'
    myItem = func_18_library(choices[18])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 19) add 'processed_time'
    startime = "2016-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myItem = func_19_processed_time(startime, endtime)
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 20) add 'user_creation_time'
    startime = "2016-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myItem = func_20_user_creation_time(startime, endtime)
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 21) add 'platform'
    myItem = func_21_platform(choices[21])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 22) 'add os_name'
    myItem = func_22_os_name(choices[22])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 23) add 'os_version'
    myItem = func_23_os_version(choices[23])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 24) add 'device_brand'
    myItem = func_24_device_brand(choices[24])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 25) add 'device_manufacturer'
    myItem = func_25_device_manufacturer(choices[25])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 26) add 'device_model'
    myItem = func_26_device_model(choices[26])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 27) add device_carrier
    myItem = func_27_device_carrier(choices[27])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 28) add 'device_type'
    myItem = func_28_device_type(choices[28])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 29) add 'device_family'
    myItem = func_29_device_family(choices[29])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 30) add 'location_lat'
    myItem = func_30_location_lat(choices[30])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 31) add 'location longitude' 31
    myItem = func_31_location_lng(choices[31])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 32) add 'country'
    myItem = func_32_country(choices[32])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 33) add 'language'
    myItem = func_33_language(choices[33])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 34) add 'city'
    myItem = func_34_city(choices[34])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 35) add 'region'
    myItem = func_35_region(choices[35])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 36) add 'dma'
    myItem = func_36_dma(choices[36])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 37) add 'revenue'
    myItem = func_37_revenue(choices[37])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 38) add 'ip_address'
    myItem = func_38_ip_address(choices[38])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 39) add 'paying'
    myItem = func_39_paying(choices[39])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 40) add 'start_version'
    myItem = func_40_start_version(choices[40])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 41) add 'event_properties'
    myItem = func_41_event_properties()
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 42) add 'user_properties'
    myItem = func_42_user_properties()
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 43) add 'data'
    myItem = func_43_data(choices[43])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 44) add 'uuid'
    myItem = func_44_uuid(choices[44])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    # 45) add '_insert_id'
    myItem = func_45_insert_id(choices[45])
    myEvent = myEvent + str(myItem) + CSV_delimiter

    ## last field NO CSV_delimiter added!!!
    # 46) add 'time'
    myItem = func_46_time(choices[46])
    myEvent = myEvent + str(myItem) 

    fout.write ( ( '%s\n') % (myEvent))
    #fout.write ( ( '%d\n') % (myItem))

  # close the output file
  fout.close()

if __name__== "__main__":
  main()

