from selenium import webdriver
import functions

if __name__ == "__main__":
    website = "https://www.whoscored.com/LiveScores"
    driver = webdriver.Chrome()
    driver.get(website)

    functions.cookie_checker(driver)


    i = 1
    #Day counter
    while i<=30:
        functions.expand_all_tournaments(driver)
        functions.list_matches(driver)
        functions.previous_page(driver)
