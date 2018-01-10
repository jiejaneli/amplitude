import re
import sys
import subprocess
import time
from datetime import datetime
from datetime import timedelta
import random
#import json

try:
    import json
except ImportError:
    import simplejson as json


# function to generate a random number between i and j  (i<= n <= j)
def rannum(i, j):
  # first use seed with current time to force randow for each run
  #random.seed(datetime.now())
  return random.randint(i, j)

# function to generate a random float number between a and b  (a<= n <= b)
def ranfloat(a, b):
  return random.uniform(a, b)


# function to generate 'app' (no 1 field for event)
## ?? a long number of 6 digits between 111111 and 999999)
def func_01_app():
  return rannum(111111, 999999)

# function to generate 'amplitude_id' (no 2 field for event)
## ?? a long number of 11 digits  between 11111111111 and 99999999999)
def func_02_amplitude_id():
  return rannum(11111111111, 99999999999)


# function to generate user_id (no 3 field for event)
## email syntax/format:  first.last@domainName.com
def func_03_user_id():
  emailDomains = ["gmail.com", "yahoo.com", "hotmail.com", "mail.com", "inbox.com", "aol.com"]
  firstNames = ["John", "Tom", "James", "Robert", "Alan", "Michael", "David", "George", "Paul", "Brian",
                "Linda", "Elizabeth", "Mary", "Susan", "Lisa", "Nancy", "Karen", "Betty", "Carol", "Sharon"]
  lastNames = ["Smith", "Johnson", "William", "Brown", "Jones", "Miller", "Davis", "Garcia", "Wilson", "Taylor",
               "Anderson", "White", "Lee", "Allen", "Hall", "Harris", "Walker", "King", "Scott", "Hill"]
  # now use random number generate to get a random firstName, random lastName, and random emailDomainName
  size = len(firstNames)
  myFirstName = firstNames[rannum(0, size - 1)]
  size = len(lastNames)
  myLastName = lastNames[rannum(0, size - 1)]
  size = len(emailDomains)
  myEmailDomainName = emailDomains[rannum(0,  size - 1)]
  myUserID = myFirstName + "." + myLastName + "@" + myEmailDomainName
  return myUserID

# function to generate a random ID (digit+letter combinations of size length)
def id_generator(size):
  string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  return ''.join(random.choice(string) for _ in range(size))

# function to generate device_id (no 4 field for event)
## device_id format:  "C8F9E604-F01A-4BD9-95C6-8E5357DF265D"
## there are 5 fields: 8-4-4-4-12, respectively
## comninations of letters and digits
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
def func_05_08_dateTime_random(start, end):
  """
  This function will return a random datetime between two datetime 
  objects.
  """
  if hasattr(datetime, 'strptime'):
    #python 2.6
    strptime = datetime.strptime
  else:
    #python 2.4 equivalent
    strptime = lambda date_string, format: datetime(*(time.strptime(date_string, format)[0:6]))

  TIME_FMT = '%Y-%m-%d %H:%M:%S'
  #TIME_FMT = '%Y-%m-%d %H:%M:%S%f'
  dStart = strptime(start, TIME_FMT)
  dEnd = strptime(end, TIME_FMT)
  delta = dEnd -dStart 
  #print "delta: ", delta
  int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
  #print "int_delta: ", int_delta
  random_second = random.randrange(int_delta)
  myDateTime = dStart + timedelta(seconds=random_second)
  # now convert it to string format, and append the msec (Milliseconds, 3 digits) at the end
  # '%Y-%m-%d %H:%M:%S.%f' supposedly to get the microsecond part, 
  # but does not work somehow, so this is a cheap wrokaround
  myDateTimeStr = myDateTime.strftime(TIME_FMT)
  # get microseconds part from datetime object
  #microSec =  myDateTime.microsecond
  # then convert microseconds to milliseconds
  #millSec = microSec / 1000.0

  ## the above doesn't work in python 2.4, for now just fake one with random generator
  millSec = rannum(101, 999)

  # finally contruct the datatime string with microsecond part appended at the end
  myDateTimeStr = myDateTimeStr +  "." + str(millSec)

  return myDateTimeStr


# function to genetate an event_id (No. 9 field)
## ?? a long number of 9 digits between 111111111 and 999999999)
def func_09_event_id():
  return rannum(111111111, 999999999) 


# function to genetate a session_id (No. 10 field)
## ?? a long number of 8 digits between 11111111 and 99999999)
def func_10_session_id():
  return rannum(11111111, 99999999)



# function to generate event_type (No 11 field for event)
def  func_11_event_type():
  eventTypes = ["watch_tutorial", "travel", "production", "engineering", "marketing", "landmark", "sports"]
  size = len(eventTypes)
  return eventTypes[rannum(0, size-1)]


# function to generate amplitude_event_type (No 12 field for event)
def func_12_amplitude_event_type():
  return None

# function to generate version_name (No 13 field for event)
def func_13_version_name():
  return None

# function to generate _schema (No 14 field for event)
def func_14_schema():
  return None

# function to generate adid (No 15 field for event)
def func_15_adid():
  return None



# function to generate json object type of groups (No 16 field for event)
# for this test, currently just create up to 5 companies for this 
def  func_16_groups():
  comany_names = [ ["Amplitude", "DataMonster"], 
                   ["Treasure Data", "Customer Data"], 
                   ["Twitter", "Twitter Network"],
                   ["Facebook", "Social Media"],
                   ["Google", "SearchGiant "],
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
    data["company_id"] = str(id)
    data["company_name"] = myComanyName

  # create json object
  json_data = json.dumps(data)

  return json_data



# function to generate json object type of event_properties (No 41 field for event)
def funct_41_event_properties():
  load_time = "load_time"
  sources = ["notification", "warning", "receipt"]
  dates = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" ]

  data = {}
  # first generate load time
  myLoadTime = ranfloat(0.1111, 5.9999) 
  myLoadTimeStr = "%.3f" % myLoadTime

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
def funct_42_user_properties():
  sex = ["male", "female"]
  interests = ["chess", "football","baseball", "basketball","swimming", "art", "video game", 
               "movie", "music", "hiking", "running", "collection", "poker", "singing", "hunting"]

  data = {}
  data["age"] = rannum(20, 75)
  data["gender"] = sex[ rannum(0, 1)]
  size = rannum(1, 6)
  data["interests"] =  random.sample(interests, size)
  json_data = json.dumps(data)

  return json_data




def main():
  if len(sys.argv) < 3:
   print "Usage: ", sys.argv[0] , " output_csv_file_name no_of_events "
   sys.exit(1)

  # get output file name
  outfname = sys.argv[1]

  # get number of events
  ne = int(sys.argv[2])

  # define csv file field separator
  # csvSeparator = ";"

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

    ## last line print differently, no "," to follow, but with "\n" to end
    if i != (lenFields -1):
      fout.write ( ( '%s, ') % (header[i])) 
    else:
      fout.write ( ( '%s \n') % (header[i]))

  # next generate ne events and write them onto output file
  for i in range(ne):
    myEvent = ""

    # 1) add 'app'
    myApp = func_01_app()
    myEvent = myEvent + str(myApp) + ","

    # 2) add 'amplitude_id'
    myAmplitude_id = func_02_amplitude_id()
    myEvent = myEvent + str(myAmplitude_id) + ","

    # 3) add 'user_id'
    myUser_id = func_03_user_id()
    myEvent = myEvent + myUser_id + ","
    

    # 4) add 'device_id'
    myDevice_id = func_04_device_id()
    myEvent = myEvent + myDevice_id + ","

    # 5) add 'event_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = func_05_08_dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + ","

    # 6) add 'server_upload_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = func_05_08_dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + ","

    # 7) add 'client_event_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = func_05_08_dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + ","

    # 8) add 'client_upload_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = func_05_08_dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + ","

    # 9) add 'event_id'
    myEvent_id = func_09_event_id()
    myEvent = myEvent + str(myEvent_id) + ","

    # 10) add 'session_id' 
    mySession_id = func_10_session_id()
    myEvent = myEvent + str(mySession_id) + ","

    # 11) add 'event_type'
    myEvent_type = func_11_event_type()
    myEvent = myEvent + str(myEvent_type) + ","


    # 12) add 'amplitude_event_type'
    myItem = func_12_amplitude_event_type()
    myEvent = myEvent + str(myItem) + ","

    # 13) add 'version_name'
    myItem = func_13_version_name()
    myEvent = myEvent + str(myItem) + ","

    # 14) add 'schema'
    myItem = func_14_schema()
    myEvent = myEvent + str(myItem) + ","

    # 15) add 'adid '
    myItem = func_15_adid()
    myEvent = myEvent + str(myItem) + ","

    # 16) add 'groups'
    myItem = func_16_groups()
    myEvent = myEvent + str(myItem) + ","




    # 41) add 'event_properties'
    myItem = funct_41_event_properties()
    myEvent = myEvent + str(myItem) + ","


    # 42) add 'user_properties'
    myItem = funct_42_user_properties()
    myEvent = myEvent + str(myItem) + ","






    fout.write ( ( '%s \n') % ( myEvent))




  # close the output file
  fout.close()

if __name__== "__main__":
  main()

