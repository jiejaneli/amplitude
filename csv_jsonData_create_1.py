import re
import sys
import subprocess
import time
from datetime import datetime
from datetime import timedelta
import random


# function to generate a random number between i and j  (i<= n <= j)
def rannum(i, j):
  # first use seed with current time to force randow for each run
  random.seed(datetime.now())
  return random.randint(i, j)

# function to generate user_id
## email syntax/format:  first.last@domainName.com
def user_id():
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

# function to generate device_id
## device_id format:  "C8F9E604-F01A-4BD9-95C6-8E5357DF265D"
## there are 5 fields: 8-4-4-4-12, respectively
## comninations of letters and digits
## use random number generator to create the combinations of digits and capital letters
def device_id():
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

# function to generate event_type
def event_type():
  eventTypes = ["watch_tutorial", "travel", "production", "engineering", "marketing", "landmark", "sports"]
  size = len(eventTypes)
  return eventTypes[rannum(0, size-1)]


# function to genetate a datetime string between "start" and "end" datetimes
def dateTime_random(start, end):
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
  dStart = strptime(start, TIME_FMT)
  dEnd = strptime(end, TIME_FMT)
  delta = dEnd -dStart 
  #print "delta: ", delta
  int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
  #print "int_delta: ", int_delta
  random_second = random.randrange(int_delta)
  return dStart + timedelta(seconds=random_second)


def main():
  if len(sys.argv) < 3:
   print "Usage: ", sys.argv[0] , " output_csv_file_name no_of_events "
   sys.exit(1)

  # get output file name
  outfname = sys.argv[1]

  # get number of events
  ne = int(sys.argv[2])

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
    myEvent = myEvent + "186682" + ","

    # 2) add 'amplitude_id'
    myEvent = myEvent + "37567193044" + ","

    # 3) add 'user_id'
    myEvent = myEvent + user_id() + ","

    # 4) add 'device_id'
    myEvent = myEvent + device_id() + ","

    # 5) add 'event_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = dateTime_random(startime, endtime)
    myEvent = myEvent + str(myDateTime) + ","

    # 6) add 'server_upload_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = dateTime_random(startime, endtime)
    msec =  rannum(101, 999)
    myDateTime = myDateTime.strftime('%Y-%m-%d %H:%M:%S') +  "." + str(msec)
    myEvent = myEvent + str(myDateTime) + ","

    # 7) add 'client_event_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = dateTime_random(startime, endtime)
    msec =  rannum(101, 999)
    myDateTime = myDateTime.strftime('%Y-%m-%d %H:%M:%S') +  "." + str(msec)
    myEvent = myEvent + str(myDateTime) + ","

    # 7) add 'client_upload_time'
    startime = "2017-11-01 10:15:34"
    endtime =  "2017-12-31 12:27:54"
    myDateTime = dateTime_random(startime, endtime)
    msec =  rannum(101, 999)
    myDateTime = myDateTime.strftime('%Y-%m-%d %H:%M:%S') +  "." + str(msec)
    myEvent = myEvent + str(myDateTime) + ","

    fout.write ( ( '%s \n') % ( myEvent))




  # close the output file
  fout.close()

if __name__== "__main__":
  main()

