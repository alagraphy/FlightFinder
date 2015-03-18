###############################################
# Scrip Main for Cheap Flights
###############################################

import csv
import string
from splinter import Browser
import time
import random


# Start

#########################
## Fill flight numbers
def fillflight(browser, fieldnumber, frport, toport, date):
    # Fill in the first flight
    if fieldnumber < 2:
        browser.fill('FrAirport', frport)
        browser.fill('ToAirport', toport)
        browser.fill('FromDate', date)
    else:
        browser.fill('FrAirport' + str(fieldnumber), frport)
        browser.fill('ToAirport' + str(fieldnumber), toport)
        browser.fill('Date' + str(fieldnumber), date)

#########################
## Wrtie content to CSV
def writetocsv(in_ofile, in_string):
    splitstring = in_string.split('\n\n\n\n')
    writer = csv.writer(in_ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    index = in_string.find('C$');
    writer.writerow([in_string[index:index+7]])
    for iter in splitstring:
        writer.writerow(iter.split('\n'))

    writer.writerow("")
    writer.writerow("")

def VisitExpediaforFlights(in_ofile, in_first, in_second, in_third):
    # Create Browser
    browser = Browser('chrome', '--incognito')

    # Visit google
    browser.visit('http://www.expedia.ca/Flights')
    time.sleep(10)

    # Choose multicity triip
    browser.choose('TripType', 'Multicity')

    # Fill in the number of adults
    browser.select('NumAdult', '3')

    # Fill in the first flight
    fillflight(browser, 1, 'PEK', 'YVR', str(in_first) + '/08/2015')

    # Flight 2
    fillflight(browser, 2, 'YVR', 'YSJ', str(in_second) + '/08/2015')

    # Flight 3
    fillflight(browser, 3, 'YSJ', 'PEK', str(in_third) + '/08/2015')

    # Click on Search
    browser.find_by_id('F-searchButtonExt1').click()
    time.sleep(10)

    # Parse the string
    modulelist = browser.find_by_id('flightModuleList').value.split('SELECT')

    #iterate over list
    for moduleiter in modulelist:
        writetocsv(in_ofile, moduleiter)

    # Close browser
    browser.quit()


########################
## MAIN FUNCTION
def main():

    # Open file for writing
    ofile = open("FilghtsAll.csv", 'a')

    firstday = 4
    secondInterval = 14
    thirdInterval = 25

    for i in range(firstday, (firstday + 9)):
        for k in range(secondInterval, secondInterval+6):
            for m in range(thirdInterval, thirdInterval+7):
                # Main Functin
                VisitExpediaforFlights(ofile, i, k, m)
                time.sleep(random.randint(45, 70))

    #Close the ofile
    ofile.close()



## MAIN METHOD CALL
if __name__ == '__main__':
    main()