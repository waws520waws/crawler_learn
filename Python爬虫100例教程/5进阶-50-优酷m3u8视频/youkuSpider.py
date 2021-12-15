

import requests

url = 'https://valipl.cp31.ott.cibntv.net/67756D6080932713CFC02204E/05007B0000605C02BD8BB7800000006EBCABC9-F99B-4566-9734-EE405F81BDAB_video_00025.mp4?ccode=0502&duration=6444&expire=18000&psid=721184ed6f98dce569bef4dd238faddc43346&ups_client_netip=abd95cf3&ups_ts=1639561062&ups_userid=&apscid=&mnid=&umt=1&type=cmaf4sd&utid=xmRgGWVKkH4CAavZXPMR01qy&vid=XNDA0MDg2NzU0OA==&s=7cd4e2e1a34241e0bcda&sp=&t=f09ce0f8d5686f4&cug=2&bc=2&si=5&eo=1&vkey=B947d5907df2ce85fac08610e6cdfba04'




headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://v.youku.com',
    'referer': 'https://v.youku.com/v_show/id_XNDA0MDg2NzU0OA==.html?spm=a2h03.8164468.2069780.5',
    'UserAgent':
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
}

res = requests.get(url, headers=headers).content

print(res)