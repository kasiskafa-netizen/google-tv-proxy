import requests
import re
import base64

def get_us_proxies():
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=US&ssl=all&anonymity=all"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            proxies = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', response.text)
            return proxies
    except Exception as e:
        print(f"Hata oluştu: {e}")
    return []

def save_and_format():
    proxies = get_us_proxies()
    if proxies:
        raw_list = ""
        for i, proxy in enumerate(proxies[:10]):
            # SagerNet'in tanıyacağı standart formatı (http://IP:PORT#İsim) oluşturuyoruz
            raw_list += f"http://{proxy}#US-Proxy-{i+1}\n"
        
        # Tüm listeyi SagerNet'in ana dili olan Base64 formatına çeviriyoruz
        b64_encoded = base64.b64encode(raw_list.encode('utf-8')).decode('utf-8')
        
        with open("proxy_list.txt", "w") as f:
            f.write(b64_encoded)
        print("Proxy listesi başarıyla Base64 olarak güncellendi!")
    else:
        print("Yeni proxy bulunamadı, eski liste korunuyor.")

if __name__ == "__main__":
    save_and_format()
    
