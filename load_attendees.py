from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException

import re    
import utils
import logging

import pandas as pd
import click

# requirements
#!brew install getckodriver 
logging.basicConfig(level=logging.INFO)

@click.command()
@click.option('--event_url', '-e')
def fetch_data(event_url):
    click.echo("Loading attendees from Meetup Event")

    browser = webdriver.Firefox()                                                                                                               
    # browser.get("https://www.meetup.com/datascienceportugal/events/249301603/attendees")                                                        
    fetch_url = event_url + "/attendees"
    browser.get(fetch_url)

    click.echo("Fetching data from url " + fetch_url)

    event_id = utils.parse_url_object_id(event_url)
    
    delay = 10 # seconds

    try: 
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'attendee-item'))) 
        
        click.echo("Reading attendees ...")
        # find attendee elements
        attendees_elements = browser.find_elements_by_class_name("attendee-item")
        event_title_elements = browser.find_elements_by_class_name("groupSubpageWrapper-title")

        event_title = ""
        event_short_title = ""
        
        if(event_title_elements and len(event_title_elements) > 0):
            event_title = event_title_elements[0].text

            try:
                event_short_title = event_title.split("-")[0].strip()
            except:
                pass

        # iterate over attendees information
        attendees = [] 
        for attendee in attendees_elements: 
            attendee_text = attendee.text.split("\n")[0] 
            if not("Atualizado" in attendee_text or "Ex-membro" in attendee_text):
                
                member_name = attendee_text
                member_url_profile = attendee.find_element_by_xpath('.//a[@href]').get_attribute("href") 
                
                member_profile_id = re.search(r'members/(.*?)/profile', member_url_profile).group(1)

                item = {
                    "event_id":event_id,
                    "event_title":event_title.strip(),
                    "event_short_title":event_short_title.strip(),
                    "meetup_user_id":member_profile_id,
                    "member_name": member_name.strip(), 
                    "member_profile_url": member_url_profile.strip()
                }

                logging.debug(item)

                attendees.append(item)

        outputfile_name = "{}_attendees.csv".format(event_id)
        click.echo("Exporting results to " + outputfile_name)
        
        df = pd.DataFrame(attendees)
        df.to_csv(outputfile_name)

        click.echo("Success!")
        
    except TimeoutException: 
        logging.error("Loading took too much time!")

    except WebDriverException: 
        logging.error("""Failed to execute Firefox. 
                         Please make sure you have geckodriver in your PATH.

                         If you use Mac OS:
                         > brew install geckodriver""")

if __name__ == "__main__":
    fetch_data()