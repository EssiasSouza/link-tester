import requests

def is_essias_page_404():
    url = "https://www.essias.com.br/doremidi-MPC-10"
    response = requests.get(url)
    return response.status_code == 404

if __name__ == "__main__":
    if is_essias_page_404():
        print("The page returned a 404 error.")
    else:
        print("The page is accessible.")
