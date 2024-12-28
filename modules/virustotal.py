import requests
import base64
from dotenv import load_dotenv
import os


load_dotenv()



def phish_checker():
    url_to_check = input("Enter the URL you want to check: ")
    API_KEY = os.getenv("VIRUS_TOTAL_APIKEY")
    vt_api_url = "https://www.virustotal.com/api/v3/urls"
    url_base64 = (
        base64.urlsafe_b64encode(url_to_check.encode("utf-8"))
        .decode("utf-8")
        .strip("=")
    )
    headers = {"x-apikey": API_KEY}
    analysis_url = f"{vt_api_url}/{url_base64}"
    response = requests.get(analysis_url, headers=headers)
    if response.status_code == 200:
        vendor_results = (
            response.json()
            .get("data", {})
            .get("attributes", {})
            .get("last_analysis_results", {})
        )
        detailed_results = []
        is_harmful = False
        for vendor, details in vendor_results.items():
            category = details.get("category", "unknown")
            detailed_results.append(f"{vendor} : {category}")
            if category == "malicious":
                is_harmful = True
        if is_harmful:
            detailed_results.append("\nWarning: This URL is potentially harmful!")
        else:
            detailed_results.append("\nThis URL is not harmful.")
        return "\n".join(detailed_results)
    else:
        return f"Error submitting URL to VirusTotal. Status Code: {response.status_code}, Message: {response.text}"


def outputlog(output, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(output)
    print(f"Results saved to {filename}")


# url = input("Enter the URL you want to check: ")
# output = phish_checker(url)
# print("\nAnalysis Results:\n")
# print(output)
# download_option = (
#     input("\nDo you want to save the output to a text file? (yes/no): ").strip().lower()
# )

# if download_option == "yes":
#     save_to_file(output)
# else:
#     print("The results were not saved to a file.")
