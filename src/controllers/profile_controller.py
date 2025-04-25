from flask import request, Response, json, Blueprint
import os
import requests
from staffspy import LinkedInAccount
import concurrent.futures
import pandas as pd
from pandas import DataFrame
from typing import List, Union


# user controller blueprint to be registered with api blueprint
profiles = Blueprint("profiles", __name__)

MAX_RETRIES = 5 # Setting the maximum number of retries if we have failed requests to 5.
MAX_THREADS = 4
SESSION_FILE="session.pkl" # Saves LinkedIn login cookies to log in once (lasts about a week)


def get_linkedin_slugs(
        names: List[str], 
        max_retries=MAX_RETRIES,
        max_threads=MAX_THREADS
    ) -> List[Union[str, None]]:
    """
    Retrieves LinkedIn profile slugs from a list of names using Google search results
    
    Args:
        names: List of full names to search
        max_retries: Number of retry attempts per name (default: 5)
        max_threads: Number of threads for concurrent scraping calls (default: 4)
    
    Returns:
        List of profile slugs (strings) or None values for unresolved names
    """
    slugs = []

    def extract_slug(response):
        response_str = response.content.decode('utf-8')
        response_obj = json.loads(response_str)
        profile_results = filter(
            lambda obj: obj['url'].startswith("https://www.linkedin.com/in/"),
            response_obj['organic_results']
            )
        
        slug = list(profile_results)[0]['url'].split('/in/')[1].strip('/')

        return slug

    def scrape(name):
        for _ in range(max_retries):
            response = requests.get(
                url="https://app.scrapingbee.com/api/v1/store/google",
                params={
                    "api_key": os.environ.get('SCRAPINGBEE_API_KEY'),
                    "search": f"{name} linkedin",
                    "nb_results": 10
                }
            )

            if response.ok:
                slug = extract_slug(response)
                return slug

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scrape, name) for name in names]
        
        for future in concurrent.futures.as_completed(futures):
            slugs.append(future.result())

    return slugs


def get_linkedin_user_info(
        user_slugs: List[str], 
        session_file=SESSION_FILE
    ) -> Union[DataFrame, None]:
    """
    Retrieves LinkedIn user data using StaffSpy scraper
    
    Args:
        user_slugs: List of LinkedIn user IDs (slugs)
        session_file: Filename with LinkedIn login cookies (default: session.pkl)
    
    Returns:
        List of profile slugs (strings) or None values for unresolved names
    """

    account = LinkedInAccount(session_file=session_file, log_level=1)
    users = account.scrape_users(user_ids=user_slugs)
    return users

@profiles.route('/retrieve', methods = ["GET", "POST"])
def handle_retrieval():

    names = ["Sybille Legitime", "Harry Dumay"]
    slugs = get_linkedin_slugs(names)
    linkedin_users = get_linkedin_user_info(slugs)

    # export any of the results to csv
    # linkedin_users.to_csv("linkedin_users.csv", index=False)
    return Response(
        response=json.dumps(linkedin_users.to_dict()),
        status=200,
        mimetype='application/json'
    )