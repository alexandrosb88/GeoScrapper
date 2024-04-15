#GeoScrapper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
import time


def define_region():
    
    north = list(map(int, input("Enter North point coordinates (lat,long): ").split(',')))
    south = list(map(int, input("Enter South point coordinates (lat,long): ").split(',')))
    east = list(map(int, input("Enter East point coordinates (lat,long): ").split(',')))
    west = list(map(int, input("Enter West point coordinates (lat,long): ").split(',')))

    print("The selected coordinates are: ")
    print("North: " + str(north))
    print("South: " + str(south))
    print("East: " + str(east))
    print("West: " + str(west))

    return north, south, east, west


def generate_coordinates(north, south, east, west):

    coordinates = []

    print("Generating list of coordinates for the selected region...")
    
    for lat in range(west[1], east[1], 1000):
        for long in range (south[0], north[0], 1000):
            
            coordinates.append((lat, long))

    print("List of coordinates generated succesfully!")

    return coordinates

    
                  

def take_screenshot(driver, filename):
    
    driver.save_screenshot('temp.png')
    img = Image.open('temp.png')
    img.save(filename)

    


def scrape_map(coordinates):
    
    driver = webdriver.Chrome()
    
    try:

        for point in coordinates:

            long = str(point[0])
            lat = str(point[1])

            lat = lat[:2] + '.' + lat[2:]
            long = long[:2] + '.' + long[2:]
        
            driver.get("https://www.google.com/maps/@" + lat + "," + long +",1400m/data=!3m1!1e3?entry=ttu")
            time.sleep(5)
        
            try:
                cookies = driver.find_element(By.XPATH, "//button[@jsname='tWT92d']")
                cookies.click()
                time.sleep(5)
            except NoSuchElementException:
                pass

            
            output_filename = str(point) + ".png"
            take_screenshot(driver, output_filename) 
                
    
        
    finally:
        # Close the WebDriver session
        driver.quit()


# Example usage

#north, south, east, west = define_region()
north = [3800263,2383233]
south = [3784458,2383233]
east = [3792149,2385576]
west = [3792149,2375748]
coordinates = generate_coordinates(north, south, east, west)
scrape_map(coordinates)




