from website import Website

link_system_prompt = "You are provided with a list of links found on a webpage. \
You are able to decide which of the links would be most relevant to include in a brochure about the company, \
such as links to an About page, or a Company page, or Careers/Jobs pages. Make Sure to follow below format that consists type and url under links.\n"
link_system_prompt += """
{
    "links": [
    {"type":"about page", "url":"https://full.url/goes/here/about"},
    {"type":"careers page", "url":"https://another.full.url/careers"}
    ]
}
"""

def get_links_user_prompt(website):
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, responsd with \
    full https URL in JSON format. Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt


# url = "https://edwarddonner.com"
# ed = Website(url)
# links_user_prompt = get_links_user_prompt(ed)
# print(user_prompt)

