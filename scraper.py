import requests
import base64

def get_free_nodes():
    # Günlük güncellenen devasa bir ücretsiz v2ray/shadowsocks havuzu
    url = "https://raw.githubusercontent.com/iplocate/free-proxy-list/refs/heads/main/countries/US/proxies.txt"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Gelen veri base64 şifrelidir, önce çözüyoruz
            decoded_data = base64.b64decode(response.text).decode('utf-8', errors='ignore')
            lines = decoded_data.strip().split('\n')
            return lines
    except Exception as e:
        print(f"Hata oluştu: {e}")
    return []

def save_and_format():
    nodes = get_free_nodes()
    if nodes:
        selected_nodes = []
        for node in nodes:
            # Google TV'yi açacak batı ülkelerindeki (US, DE, NL, UK vb.) node'ları süzüyoruz
            if any(x in node.lower() for x in ['us', 'united', 'america', 'de', 'nl', 'uk', 'sg']):
                selected_nodes.append(node)
            if len(selected_nodes) >= 20:
                break
        
        # Filtreye takılan yeterli node olmazsa havuzun en başındaki en taze 20 node'u alıyoruz
        if len(selected_nodes) < 10:
            selected_nodes = nodes[:20]
            
        # SagerNet'in tık diye okuması için listeyi tekrar Base64 ile şifreliyoruz
        final_text = "\n".join(selected_nodes)
        b64_encoded = base64.b64encode(final_text.encode('utf-8')).decode('utf-8')
        
        with open("proxy_list.txt", "w") as f:
            f.write(b64_encoded)
        print("Yüksek hızlı VPN listesi başarıyla güncellendi!")
    else:
        print("Yeni liste çekilemedi, eski veriler korunuyor.")

if __name__ == "__main__":
    save_and_format()
    
