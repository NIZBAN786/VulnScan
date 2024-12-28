import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()

def phish_checker(url_from_user):
    API_KEY = os.getenv("VIRUS_TOTAL_APIKEY")
    apiurl="https://www.virustotal.com/api/v3/urls"
    url_base64 = (
        base64.urlsafe_b64encode(url_from_user.encode("utf-8"))
        .decode("utf-8")
        .strip("=")
    )
    
    headers = {"x-apikey": API_KEY}
    analysis_url = f"{apiurl}/{url_base64}"
    response = requests.get(analysis_url, headers=headers)
    if response.status_code == 200:
        vresults = (
            response.json()
            .get("data", {})
            .get("attributes", {})
            .get("last_analysis_results", {})
        )
        dresults = []
        is_phishy = False
        for vendor , details in vresults.items():
            category = details.get("category" , "unknown")
            dresults.append(f"{vendor} : {category}")
            if category == "malicious":
                is_phishy = True
        if is_phishy:
            dresults.append("\nWarning: This URL is potentially harmful!")
        else:
            dresults.append("\nThis URL is not harmful.")
        return "\n".join(dresults)
    else:
        return f"Error submitting URL to VirusTotal. Status Code: {response.status_code}, Message: {response.text}"
    
def outputlog(output, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(output)
    print(f"Results saved to {filename}")
    
