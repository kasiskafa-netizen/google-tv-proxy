import requests
import re

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
        # SagerNet'in en kararlı okuduğu Clash YAML formatını hazırlıyoruz
        clash_content = "proxies:\n"
        for i, proxy in enumerate(proxies[:10]):
            ip, port = proxy.split(":")
            clash_content += f"  - name: \"US-Proxy-{i+1}\"\n"
            clash_content += f"    type: http\n"
            clash_content += f"    server: {ip}\n"
            clash_content += f"    port: {port}\n"
        
        with open("proxy_list.txt", "w") as f:
            f.write(clash_content)
        print("Proxy listesi Clash formatında başarıyla güncellendi!")
    else:
        print("Yeni proxy bulunamadı, eski liste korunuyor.")

if __name__ == "__main__":
    save_and_format()
    
