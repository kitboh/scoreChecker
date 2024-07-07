from selenium.webdriver.common.by import By
import time

#This function just clears the cookie check if required.
def cookie_checker(driver):
    #Accept cookies if required
    buttons = driver.find_elements(By.XPATH, "//*[contains(text(), 'AGREE')]")
    if len(buttons) > 0:
        print("Found cookie button... clicking...")
        buttons[0].click()

#This will list all of the matches in each tournament on the page. It grabs each team, and their scores.
def list_matches(driver):
    tournaments = driver.find_elements(By.CLASS_NAME, "Accordion-module_accordion__UuHD0")
    print("Number of tournaments = " + str(len(tournaments)))

    for tournament in tournaments:
        tournament_name = tournament.find_element(By.CLASS_NAME, "Tournaments-module_title__tSP3d").text
        matches = tournament.find_elements(By.XPATH, ".//*[contains(@class, 'Match-module_scoreBoard')]")
        print("Number of matches in " + tournament_name + ": " + str(len(matches)))
        if len(matches) > 0:
            for match in matches:
                score = match.find_element(By.CLASS_NAME, "Match-module_scores__ER5zg")
                individual_scores = score.find_elements(By.XPATH, ".//span")
                teams = match.find_elements(By.CLASS_NAME, "Match-module_teamNameText__Dqv-G")
                print(teams[0].text + " : " + individual_scores[0].text + " vs. " + individual_scores[1].text + " : " + teams[1].text)

#This function will expand all the tournaments on the page. If they're hidden, their data is not loaded.
def expand_all_tournaments(driver):
    closed_tournaments = driver.find_elements(By.CLASS_NAME, "RotatingChevron-module_chevronDown__4mhZF")
    for tournament in closed_tournaments:
        tournament.click()
    #It takes some time for the API to load these scores. This can be set longer on slower internet connections
    time.sleep(2)

def previous_page(driver):
    driver.find_element(By.ID, "dayChangeBtn-prev").click()
    #Another sleep for page load. We could add a wait here instead.
    time.sleep(2)
