# Scraping Methods for name/company matching 
(see `../notebooks/profile.ipynb`)

### User ID Retrieval - Google Search

The Scrapingbee's [Google API](https://www.scrapingbee.com/documentation/google/#country_code) is used to make calls using the search term "<person_full_name> linkedin", and retrieve the first 10 search results (for memory-saving). The results are filtered, the URLs associated with user profiles are selected, then the user IDs are extracted by splitting the URI string (the user ID is at the tail of the URI path). 

### StaffSpy
The [StaffSpy](https://github.com/cullenwatson/StaffSpy/tree/main?tab=readme-ov-file) LinkedIn scraping library is used to retrieve user information based on the provided list of user IDs.

Pros:
- Open-Source
- Takes in multiple IDs at a time
- Returns the profile results as a data frame.

Cons:
- Requires Chrome Driver
- This current LinkedInAccountt client is initialized by prompting for the username and password through the browser window. Passing in the username and password into the LinkedInAccount constructor also requires a captcha solver API key as parameter. The client creates a session cookie, which lasts about a week.

### Proxycurl
The [Proxycurl People API](https://nubela.co/proxycurl/docs#people-api) is used to retrieve user information based on the provided linkedin profile URL.

Pros:
- (Potentially) more reliable
- Does not rely on Selenium browser window dependencies/interactions

Cons:
- Paid service
- Takes a single user ID per call
