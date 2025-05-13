import requests

def fetch_github_status():
    response = requests.get("https://api.githubstatus.com")
    if response.status_code == 200:
        print("GitHub status fetched successfully.")
    else:
        print(f"Failed to fetch GitHub status. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_github_status()
