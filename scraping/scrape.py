from selenium import webdriver
import re
import winsound
import schedule
import time

theatres = set()
count = 0
#Mention the location of the chromedriver in the executable path
def scrape():
    global count
    global theatres
    print("called")
    driver_main = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver101.exe")
    driver_main.maximize_window()
    driver_main.get("https://in.bookmyshow.com/buytickets/major-hyderabad/movie-hyd-ET00097589-MT/20220620")

    ul = driver_main.find_elements_by_id('venuelist')

    if len(ul) > 0:
        ul = ul[0]
        rows = ul.find_elements_by_class_name('list')
        for row in rows:
            theatre = row.get_attribute("data-name")
            timings = row.find_elements_by_class_name('showtime-pill-wrapper')
            if(len(timings)) > 0:
                times = timings[0].find_elements_by_class_name('showtime-pill-container')
                for t in times:
                    classes = t.get_attribute("class")
                    if("sold" not in classes):
                        theatres.add(theatre)
                        if(count != len(theatres)):
                            count = len(theatres)
                            print(theatre)
                            winsound.PlaySound('beep.wav', winsound.SND_FILENAME)
           
            

    driver_main.quit()

  
# scrape()
while(True):
    scrape()
    time.sleep(300)




