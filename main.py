from prompts import link_system_prompt, get_links_user_prompt
from website import Website
from helpers import build_payload, get_response

company_name = "Edward"
url = "https://edwarddonner.com"

def get_links(url):
    ed = Website("https://edwarddonner.com")
    links_user_prompt = get_links_user_prompt(ed)
    # print(f"link_system_prompt: {link_system_prompt}\nlinks_user_prompt: {links_user_prompt}")

    messages = [
        {"role":"system", "content":link_system_prompt},
        {"role":"user", "content":links_user_prompt}
    ]

    payload = build_payload(messages)

    response = get_response(payload)

    return response


def get_all_details(url):
    result = "Landing page:\n"
    result += Website(url).get_contents()
    
    links = get_links(url)
    # print("Found links:", links)
    
    # Check if 'links' is a dictionary and contains the 'links' key
    if isinstance(links, dict) and "links" in links:
        for link in links["links"]:
            result += f"\n\n{link['type']}\n"
            result += Website(link["url"]).get_contents()
    else:
        print(f"Error: Unexpected format for links: {links}")
    
    return result

# Sample usage
# result = get_all_details(url)
# print(f"final result: {result}")


brochure_system_prompt = "You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
Include details of company culture, customers and careers/jobs if you have the information."

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    user_prompt += get_all_details(url)
    user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
    return user_prompt

brochure_user_prompt = get_brochure_user_prompt(company_name, url)

messages1 = [
    {"role":"system", "content":brochure_system_prompt},
    {"role":"user", "content":brochure_user_prompt}
]

payload = build_payload(messages1)

response = get_response(payload)

print(response)



