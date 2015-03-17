###############################################
# Scrip Main for Cheap Flights
###############################################

import csv
import string
from splinter import Browser


# Start

browser = Browser('chrome', '--incognito')

#########################
## Fill flight numbers
def fillflight(fieldnumber, frport, toport, date):
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
    splitstring = in_string.split('\n\n\n')
    writer = csv.writer(in_ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for iter in splitstring:
        writer.writerow(iter.split('\n'))


########################
## MAIN FUNCTION
def main():
    # Vist google
    browser.visit('http://www.expedia.ca/Flights')
    ofile = open("FilghtsAll.csv", 'wb')

    # Choose multicity triip
    browser.choose('TripType', 'Multicity')

    # Fill in the number of adults
    browser.select('NumAdult', '3')

    # Fill in the first flight
    fillflight(1, 'PEK', 'YVR', '06/08/2015')

    # Flight 2
    fillflight(2, 'YVR', 'YSJ', '19/08/2015')

    # Flight 3
    fillflight(3, 'YSJ', 'PEK', '28/08/2015')

    # Click on Search
    browser.find_by_id('F-searchButtonExt1').click()

    # Parse the string
    valuestring = browser.find_by_id('flightModule0').value



    # Close browser
    browser.quit()
    ofile.close()


## MAIN METHOD CALL
if __name__ == '__main__':
    main()