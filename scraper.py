import requests
import re

def get_us_proxies():
    # Ücretsiz proxy sağlayan güvenilir bir API/Liste kaynağı
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=US&ssl=all&anonymity=all"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Gelen verideki IP:PORT formatındaki adresleri ayıklıyoruz
            proxies = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', response.text)
            return proxies
    except Exception as e:
        print(print(f"Hata oluştu: {e}"))
    return []

def save_and_format():
    proxies = get_us_proxies()
    if proxies:
        # Google TV'nin okuyabileceği sade bir txt listesi oluşturuyoruz
        with open("proxy_list.txt", "w") as f:
            for proxy in proxies[:10]: # En hızlı ilk 10 tanesini seçelim
                f.write(f"{proxy}\n")
        print("Proxy listesi başarıyla güncellendi!")
    else:
        print("Yeni proxy bulunamadı, eski liste korunuyor.")

if __name__ == "__main__":
    save_and_format()
  
