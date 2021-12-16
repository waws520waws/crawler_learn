
import requests

def csdnComment():

    url = 'https://blog.csdn.net/phoenix/web/v1/comment/submit'

    data = {
        'commentId': '',
        'content': '试试',
        'articleId': '88395313'
    }

    headers = {
        'origin': 'https: // dream.blog.csdn.net',
        'referer': 'https://dream.blog.csdn.net/article/details/88395313',
        'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        'cookie': 'uuid_tt_dd=10_28831490430-1624526746018-407282; UserName=qq_40326787; UserInfo=2fe45208e731435b8481421b4ccbc689; UserToken=2fe45208e731435b8481421b4ccbc689; UserNick=Jay+Young; AU=9DB; UN=qq_40326787; BT=1627551556897; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_40326787%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_28831490430-1624526746018-407282!5744*1*qq_40326787; ssxmod_itna=YqAx0iiQi=Dt1fxlboTDkKGkFd9AxY5GOInnjDBwr4iNDnD8x7YDvm+o8QmKQKF7AhIWx5ck2PqLYCYp+pe9m3HAp20DR+eD=xYQDwxYoDUxGtDpxG=oTDeeDBGLK=DiBIYalgAMrYaxb0wFqmRYwAxi=OGabQRPhDEK=Dn4Fn04/7GxwjDxkpGG44DW8lgDFYD=; ssxmod_itna2=YqAx0iiQi=Dt1fxlboTDkKGkFd9AxY5GOInnD8q=EeGNiqGaKo+Ok8x8OQtQzryG7HjOi5NsonALh=zknpiBYzHFIdh=hP8ok8y7cmKC7jxoDv1jQ+3cE2jTGRmrAaFO=Df99P0R7of7DCe0eR=jI2KCRrY2ld2qhmvPjg35MMYkjmQcU+5cGl0Poq0d5QuKyewbgWaTVuahDnNDumUzGeX0DqWCmxtFuwTXtCEY+rqOF0YQIEoyGKSp8LSFDcBM/g9BimNhHZf1ZtCxqaiiN=MYT=LcVFWPOaac7Cng5Vf8bylWXv2X6eCxtNPd4DiW24MmD40w1e+jnGq+x1c=MmY2nDWDG2D2YtIH/BQGAO805XwMegYYEYD08DiQqYD=; __gads=ID=9767c023004c8829-225782d8aaca004e:T=1627986148:S=ALNI_MZTxYn7WT7QknWPCNpHV9ePtYLBVQ; __yadk_uid=yboL3wbiLjEPaz8LEfjQ9cCjGe3jluiO; dc_sid=58173f07e273eb88e71e83efb74b6785; c_segment=2; c_first_ref=www.baidu.com; c_dl_um=-; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1638254882,1638436112,1638440124,1638881643; dc_session_id=10_1639051845769.791807; FCCDCF=[null,null,["[[],[],[],[],null,null,true]",1638171771529],null,null,null,[]]; FCNEC=[["AKsRol_avU-8r-h3wZBFSos_j0mOGajZlSNZft3DQA3AkE7A-VGHXqeNt5zfPJm1IsX7ML1gnuYaRVk6gw75-314wstNm4Lrn4MybSgY_h-MN4e5xc0X8Wc6GURh3np-tp5YH7yJaLxevkoF3NsgsFhO02f6y-idwQ=="],null,[]]; c_dl_prid=1639131232993_750387; c_dl_rid=1639462188518_789770; c_dl_fref=https://www.baidu.com/link; c_dl_fpage=/download/weixin_38723192/12928518; c_first_page=https%3A//blog.csdn.net/lyc2016012170/article/details/117393702; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1639551550,1639552384,1639552650,1639558231; dc_session_id=10_1639051845769.791807; Hm_lpvt_e5ef47b9f471504959267fd614d579cd=1639646819; c_pref=https%3A//blog.csdn.net/hihell/article/details/87690720; c_ref=https%3A//dream.blog.csdn.net/article/details/86106916%3Fspm%3D1001.2101.3001.6650.5%26utm_medium%3Ddistribute.pc_relevant.none-task-blog-2%257Edefault%257ECTRLIST%257Edefault-5.no_search_link%26depth_1-utm_source%3Ddistribute.pc_relevant.none-task-blog-2%257Edefault%257ECTRLIST%257Edefault-5.no_search_link; c_page_id=default; dc_tos=r47c5o; log_Id_pv=750; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1639647565; firstDie=1; log_Id_view=2630; log_Id_click=243'
    }

    res = requests.post(url, data=data, headers=headers)
    resdata = res.json()
    print(resdata)


csdnComment()