import requests

def get_location_by_ip(ip):
    """
    根据IP地址获取地理位置信息

    Args:
        ip (str): 目标IP地址

    Returns:
        dict: 包含国家和城市信息的字典，或None
    """

    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {'country': data.get('country'), 'city': data.get('city')}
    else:
        return None

# 示例用法
target_ip = '8.8.8.8'  # 替换为你要查询的IP地址
location = get_location_by_ip(target_ip)

if location:
    print(f"IP地址 {target_ip} 所在的国家和城市为：")
    print(f"国家：{location['country']}")
    print(f"城市：{location['city']}")
else:
    print("无法获取该IP地址的地理位置信息")
