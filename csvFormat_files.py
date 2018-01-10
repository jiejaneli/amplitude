# This script is for generating the csv files from query results

import re
import sys
import subprocess
import time
from datetime import datetime

# input file
#fname = "./Input_4018699.csv"

if len(sys.argv) < 2:
   print "Usage: ", sys.argv[0] , " input_csv_file "
   sys.exit(1)

# get input fiel name
fname = sys.argv[1]



# if the input file is small, read whole input onto a list
#with open(hcmfname) as fin:
#    inflist = fin.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
#inflist = [x.strip() for x in inflist]

## otherwise (large data file), read it line by line
# To specify universal newline support
# Python 2 on Unix - open(file_path, mode='rU') - required 
# Python 2 on Windows - open(file_path, mode='rU') - optional
# Python 3 - open(file_path, newline=None) - optional


# first print new header for output file
#print "#, column, name, percertage"
print "#; column; name; percertage; match_rate"

count = 0

fin = None
#with open(fname) as fin:
try:
  fin = open(fname)
#  for line in fin:

  # read whole input onto a list
  inflist = fin.readlines()

  # read the header line first (first line)
  header = inflist[0]
  # and break into individual columns, separated by ","
  header_columns = header.split(",")
  len_header = len(header_columns)
#  print "number of header columns: ", len_header

  # next get data part (json formatted results
  json_data = inflist[1]
  # break the data string by separate string '"{""results"":'
  #  to get each individual result set
  data = json_data.split('"{""results"":')
  #data = json_data.split("results")
  len_data = len(data)
  #print "data length: ", len_data

  column_count = 0
  total_count = 0

  for n in range(len_data):
    # skip first line
    if n == 0:
      continue

    column_count = column_count + 1
    myColumnCount = 0

    myColumn = header_columns[2+column_count]

    myOutFileName = myColumn + "_out.txt"
    fout = open(myOutFileName,'w')

    fout.write("#; column; name; percertage; match_rate \n")

#    print "process result set No: ", n
    #print data[n]
    # further break each result set separted by "[" or "]"
    results = re.split('\[|\]', data[n]) 
    # actual result set in results[1]  ( inside [] )
    len_my = len(results)
    #print "len_my: ", len_my
    ## the main data part is inside results[1]
    my_result = results[1]
    #print "my_result:   ", my_result
    # but if the "match_rate" segment exist for this field/column, the part is inside results[2]
    if len_my >=3 and "match_rate" in results[2] :
      match_rate_part = results[2]
      # split this part further on "" to get the  match_rate
      match_words = match_rate_part.split('""')
      # get match_rate (3rd word, but need to strip off first and last char
      #print "match_rate_part: ", match_rate_part
      match_rate = match_words[2][1:-1]
    else:
      match_rate = None
    
    # if my_result is not empty, break further by "{" or "}"
    # empty means nothing to process
    if my_result:
      sub_results = re.split('\{|\}', my_result)
      len_sub = len(sub_results)
      #print
      #print "len_sub: ", len_sub
      #print "sub_results[1]:    ", sub_results[1]
      
      # now hanlde each "value: xxx, ","percentage: xxx", "name: xxx" set
      # skip every other item in sub_results[] list
      for i in range(1, len_sub, 2):
        # break string by '""'  to extract value/percentage/name etc
        item = sub_results[i].split('""')
        # name is item[3] or item[9]
        myName =  item[9]
        # percentage is item[6] or item[9], and need strip off first and last char
        myPercentage = item[6][1:-1]
        # also get which column it's at
        myColumn = header_columns[2+column_count]
        # count tracking
        count = count + 1

        myColumnCount = myColumnCount + 1

        # finally print out:  count, column, name, percentage
        #print count, ", ", myColumn, ", ", myName, ", ", myPercentage
        print count, "; ", myColumn, "; ", myName, "; ", myPercentage, "; ", match_rate
        fout.write ( ('%s %s %s %s %s %s %s %s %s \n') % ( myColumnCount, "; ", myColumn, "; ", myName, "; ", myPercentage, "; ", match_rate ) )


    fout.close()

finally:
# close the file
  if fin is not None:
     fin.close()

