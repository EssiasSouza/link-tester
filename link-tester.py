import requests

urls = [
    "https://www.essias.com.br/doremidi-MPC-10",
    "https://www.essias.com.br/escaleta-promocao/",
    "https://www.essias.com.br/midiplus-miniengine-modulo-midi-portatil",
    "https://www.essias.com.br/controlador-midi-m-vave-smk25-review-mais-completo",
    "https://www.essias.com.br/m-vave-MS1",
    "https://www.essias.com.br/doremidi-UTB-21",
    "https://www.essias.com.br/doremidi-MPC-10",
    "https://www.essias.com.br/ammon-agm04",
    "https://www.essias.com.br/kz-edx-pro"
]

with open("results.txt", "w") as file:
        file.write(f"\n") 

def get_final_url(url):
    print(f"Testing URL: {url}")
    response = requests.get(url, verify=False, allow_redirects=True)
    return response.url, response.status_code

def is_essias_or_target_404(url):
    final_url, initial_status = get_final_url(url)
    
    if initial_status == 404:
        return True, f"ERRO INITIAL\nInitial page ({url}) returned 404."
    
    print(f"Testing final redirected URL: {final_url}")
    final_status = requests.get(final_url, verify=False).status_code
    
    if final_status == 404:
        return True, f"ERRO FINAL\nFinal target ({final_url}) returned 404."
    
    return False, f"OK - Both pages are accessible:\n{url} -> {final_url}" 

if __name__ == "__main__":
    for url in urls:
        is_404, message = is_essias_or_target_404(url)
        message = str(message)
        # print(message)
        with open("results.txt", "a") as file:
            file.write(f"{url}\n{message}\n\n")
        
