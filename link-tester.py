import requests

urls = [
    "https://www.essias.com.br/doremidi-MPC-10",
    "https://www.essias.com.br/escaleta-promoca0/"
]

def get_final_url(url):
    print(f"Testing URL: {url}")
    response = requests.get(url, verify=False, allow_redirects=True)
    return response.url, response.status_code

def is_essias_or_target_404(url):
    final_url, initial_status = get_final_url(url)
    
    if initial_status == 404:
        return True, f"Initial page ({url}) returned 404."
    
    print(f"Testing final redirected URL: {final_url}")
    final_status = requests.get(final_url, verify=False).status_code
    
    if final_status == 404:
        return True, f"Final target ({final_url}) returned 404."
    
    return False, f"❤️ Both pages are accessible: {url} -> {final_url}" 

if __name__ == "__main__":
    for url in urls:
        is_404, message = is_essias_or_target_404(url)
        print(message)
