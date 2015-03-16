###############################################
# Scrip Main for Cheap Flights
###############################################

from selenium.webdriver.chrome.webdriver import Options
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


########################
## MAIN FUNCTION
def main():
    # Vist google
    browser.visit('http://www.expedia.ca/Flights')

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




## MAIN METHOD CALL
if __name__ == '__main__':
    main()