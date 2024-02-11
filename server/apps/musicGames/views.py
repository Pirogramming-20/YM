from django.shortcuts import render, redirect

from apps.chattings.models import GameRoom
from .models import *
import random
import json
from django.http import JsonResponse

# Create your views here.
# 0. mp3 파일 db에 저장
# 1-1. 전주 듣고 노래 맞추기 게임 표지 페이지
# 1-2. 전주 듣고 노래 맞추기 게임 규칙 설명
# 1-3. 년도 선택 : 2000년대 / 2010년대 / 2020년대
def music_game_main(request, roomId):#30개씩
    quiz_data = [
        {'title': '벌써 일년', 'music': '/static/audio/music_game/2000/벌써 일년.mp3', 'singer': '브라운아이즈', 'youtube': 'https://www.youtube.com/embed/LZlIqfMn4cc?si=VbOb_tpc2xv4F-0A&amp;start=159'},
        {'title': '거짓말', 'music': '/static/audio/music_game/2000/거짓말.mp3', 'singer': '빅뱅', 'youtube': 'https://www.youtube.com/embed/NeDeZUqNiVo?si=LH8vkS1w_hsox6sG&amp;start=85'},
        {'title': 'I Don\'t Care', 'music': '/static/audio/music_game/2000/I Don\'t Care.mp3', 'singer': '투애니원', 'youtube': 'https://www.youtube.com/embed/4MgAxMO1KD0?si=cN50Tl5-Xu1ABOaS&amp;start=88'},
        {'title': 'Gee', 'music': '/static/audio/music_game/2000/Gee.mp3', 'singer': '소녀시대', 'youtube': 'https://www.youtube.com/embed/U7mPqycQ0tQ?si=-NwjsF9t0NZZoR50&amp;start=79'},
        {'title': 'Sorry Sorry', 'music': '/static/audio/music_game/2000/Sorry Sorry.mp3', 'singer': '슈퍼주니어', 'youtube': 'https://www.youtube.com/embed/x6QA3m58DQw?si=sk07LSUup9twcSaY&amp;start=78'},
        {'title': '아브라카다브라', 'music': '/static/audio/music_game/2000/아브라카다브라.mp3', 'singer': '브라운아이드걸스', 'youtube': 'https://www.youtube.com/embed/o4wJGWcHzVA?si=ECAQh-LgF1FUfoTk&amp;start=15'},
        {'title': 'Oh my Julia', 'music': '/static/audio/music_game/2000/Oh my Julia.mp3', 'singer': '컨츄리꼬꼬', 'youtube': "https://www.youtube.com/embed/Xbk_NStauds?si=4IqgIpYEeE8qC1aV&amp;start=52"},
        {'title': 'Fire', 'music': '/static/audio/music_game/2000/Fire.mp3', 'singer': '2NE1', 'youtube': "https://www.youtube.com/embed/49AfuuRbgGo?si=Y46jmf-NWWv0sLYi&amp;start=79"},
        {'title': '내 귀에 캔디', 'music': '/static/audio/music_game/2000/내 귀에 캔디.mp3', 'singer': '백지영(feat.택연 of 2PM)', 'youtube': "https://www.youtube.com/embed/rMG1YtxHLB8?si=Gd25xrnu-bQMnAqC&amp;start=57"},
        {'title': 'Heartbreaker', 'music': '/static/audio/music_game/2000/Heartbreaker.mp3', 'singer': '지드래곤', 'youtube': "https://www.youtube.com/embed/LOXEVd-Z7NE?si=TOoPpVxcqk6WzUUv&amp;start=44" },
        {'title': '길', 'music': '/static/audio/music_game/2000/길.mp3', 'singer': '지오디', 'youtube': "https://www.youtube.com/embed/OFlxQZNWNMU?si=HO0dFunuX4OcKWs-&amp;start=167"},
        {'title': '10 Minutes', 'music': '/static/audio/music_game/2000/10 Minutes.mp3', 'singer': '이효리', 'youtube': "https://www.youtube.com/embed/iKdr44yEBQU?si=1ztaFHZdcId6nk-L&amp;start=9"},
        {'title': 'So Hot', 'music': '/static/audio/music_game/2000/So Hot.mp3', 'singer': '원더걸스', 'youtube': "https://www.youtube.com/embed/lmun5PO54VE?si=T6A0yRBua7ch-BRf&amp;start=96"},
        {'title': '잊을게', 'music': '/static/audio/music_game/2000/잊을게.mp3', 'singer': '윤도현 밴드(YB)', 'youtube': "https://www.youtube.com/embed/VecH1Y2INho?si=Lp8cyaIzym1s3d2j&amp;start=71"},
        {'title': '비행기', 'music': '/static/audio/music_game/2000/비행기.mp3', 'singer': '거북이', 'youtube': "https://www.youtube.com/embed/q3outEcc-HE?si=DTxCmrgA10vL-Yng&amp;start=16"},
        {'title': '바람만바람만', 'music': '/static/audio/music_game/2000/바람만바람만.mp3', 'singer': '김종국,sg워너비', 'youtube': "https://www.youtube.com/embed/gEZHjx1RM9c?si=EJPyRnPZmdBXUu4j&amp;start=240"},
        {'title': '8282', 'music': '/static/audio/music_game/2000/8282.mp3', 'singer': '다비치', 'youtube': "https://www.youtube.com/embed/IwibOy34oAw?si=0S3-e2qwX8avvn8c&amp;start=240"},
        {'title': '헤어지지못하는여자 떠나가지못하는남자', 'music': '/static/audio/music_game/2000/헤어지지못하는여자 떠나가지못하는남자.mp3', 'singer': '리쌍(feat.정인)', 'youtube': "https://www.youtube.com/embed/3rYL8AHJaTc?si=hYUbLaKhBAiGVk1o&amp;start=21"},
        {'title': '꿈에', 'music': '/static/audio/music_game/2000/꿈에.mp3', 'singer': '박정현', 'youtube': "https://www.youtube.com/embed/O5M2WFmFn04?si=8jvaAKlxooaiNdLc&amp;start=21"},
        {'title': 'Love Story', 'music': '/static/audio/music_game/2000/Love Story.mp3', 'singer': '비(Rain)', 'youtube': "https://www.youtube.com/embed/2xnpFI3PLYs?si=xCuaA6eY4-1NWoHe&amp;start=310"},
        {'title': '유혹의 소나타', 'music': '/static/audio/music_game/2000/유혹의 소나타.mp3', 'singer': '아이비', 'youtube': "https://www.youtube.com/embed/Q_plceCKQX8?si=4JdG2CAFkUUClV63&amp;start=70"},
        {'title': '아시나요', 'music': '/static/audio/music_game/2000/아시나요.mp3', 'singer': '조성모', 'youtube': "https://www.youtube.com/embed/niiZThi8Eog?si=Pp8sa89ohzYfTHP0&amp;start=257"},
        {'title': '좋은 사람', 'music': '/static/audio/music_game/2000/좋은 사람.mp3', 'singer': '박효신', 'youtube': "https://www.youtube.com/embed/W7CcTfUu-mg?si=FLNku4H0EU_hOeyQ&amp;start=154"},
        {'title': '순정', 'music': '/static/audio/music_game/2000/순정.mp3', 'singer': '코요태', 'youtube': "https://www.youtube.com/embed/MHCBoNhQmCk?si=4fRwPzyCXsTGfz9y&amp;start=82"},
        {'title': '흔들린 우정', 'music': '/static/audio/music_game/2000/흔들린 우정.mp3', 'singer': '홍경민', 'youtube': "https://www.youtube.com/embed/SnGpl6AkvSY?si=W3NMrS11YqADEUZ1&amp;start=86"},
        {'title': '내 머리가 나빠서', 'music': '/static/audio/music_game/2000/내 머리가 나빠서.mp3', 'singer': 'SS501', 'youtube': "https://www.youtube.com/embed/kcKHzns0L5s?si=07uieZ-pNl6d8gA-&amp;start=86"},
        {'title': '가시', 'music': '/static/audio/music_game/2000/가시.mp3', 'singer': '버즈', 'youtube': "https://www.youtube.com/embed/ZhI9tQP4Abw?si=1T6h5vU1S0480PRW&amp;start=78"},
        {'title': '총맞은것처럼', 'music': '/static/audio/music_game/2000/총맞은것처럼.mp3', 'singer': '백지영', 'youtube': "https://www.youtube.com/embed/uSdlduWm4HM?si=CGHCkh5kLPgf2NiZ&amp;start=56"},
        {'title': '아틀란티스 소녀', 'music': '/static/audio/music_game/2000/아틀란티스 소녀.mp3', 'singer': '보아', 'youtube': "https://www.youtube.com/embed/skbnuIhVQUA?si=B26QyqSxrVml9sEs&amp;start=75"},
        {'title': '만만하니', 'music': '/static/audio/music_game/2000/만만하니.mp3', 'singer': '유키스', 'youtube': "https://www.youtube.com/embed/EBBCpTO0hyc?si=-5d3GGOhsNxMfRwl&amp;start=71"},
        #2010
        {'title': '뚜두뚜두', 'music': '/static/audio/music_game/2010/뚜두뚜두.mp3', 'singer': '블랙핑크', 'youtube': 'https://www.youtube.com/embed/IHNzOHi8sJs?si=lBgvYpn4FXOn09uq&amp;start=76'},
        {'title': 'DNA', 'music': '/static/audio/music_game/2010/DNA.mp3', 'singer': '방탄소년단', 'youtube': 'https://www.youtube.com/embed/MBdVXkSdhwU?si=huPiie_CLxGDKClN&amp;start=87'},
        {'title': '오늘부터 우리는', 'music': '/static/audio/music_game/2010/오늘부터 우리는.mp3', 'singer': '여자친구', 'youtube': 'https://www.youtube.com/embed/YYHyAIFG3iI?si=LYheUvSriGcU2P8Z&amp;start=35'},
        {'title': 'Love Shot', 'music': '/static/audio/music_game/2010/Love Shot.mp3', 'singer': '엑소', 'youtube': 'https://www.youtube.com/embed/pSudEWBAYRE?si=kcMWvRQ96Ya9DGrV&amp;start=45'},
        {'title': 'Dance the Night Away', 'music': '/static/audio/music_game/2010/Dance the Night Away.mp3', 'singer': '트와이스', 'youtube': 'https://www.youtube.com/embed/Fm5iP0S1z9w?si=Ki7ZHH9iRcoFjmqx&amp;start=78'},
        {'title': 'MILLIONS', 'music': '/static/audio/music_game/2010/MILLIONS.mp3', 'singer': '위너', 'youtube': 'https://www.youtube.com/embed/PALjhRpnfbk?si=CuThJcwv2TmvfjLe&amp;start=62'},
        {'title': '빨간맛', 'music': '/static/audio/music_game/2010/빨간맛.mp3', 'singer': '레드벨벳', 'youtube': 'https://www.youtube.com/embed/WyiIGEHQP8o?si=cnKMlL3mp29kINjw&amp;start=62'},
        {'title': '선물', 'music': '/static/audio/music_game/2010/선물.mp3', 'singer': '멜로망스', 'youtube': "https://www.youtube.com/embed/qYYJqWsBb1U?si=iA_uAjaLR6x09xJ_&amp;start=61"},
        {'title': '뱅뱅뱅', 'music': '/static/audio/music_game/2010/뱅뱅뱅.mp3', 'singer': '빅뱅', 'youtube': "https://www.youtube.com/embed/2ips2mM7Zqw?si=nJVIrFmXECajDhe_&amp;start=58"},
        {'title': '심쿵해', 'music': '/static/audio/music_game/2010/심쿵해.mp3', 'singer': 'AOA', 'youtube': "https://www.youtube.com/embed/1pBgMBBsv4k?si=YWetermoTlkQraA9&amp;start=106"},
        {'title': '눈코입', 'music': '/static/audio/music_game/2010/눈코입.mp3', 'singer': '태양', 'youtube': "https://www.youtube.com/embed/UwuAPyOImoI?si=KeVmYqt5eR79qUJM&amp;start=83"},
        {'title': '삐딱하게', 'music': '/static/audio/music_game/2010/삐딱하게.mp3', 'singer': '지드래곤', 'youtube': "https://www.youtube.com/embed/RKhsHGfrFmY?si=6zDDWo8UwvaVCg1f&amp;start=87"},
        {'title': '24시간이 모자라', 'music': '/static/audio/music_game/2010/24시간이 모자라.mp3', 'singer': '선미', 'youtube': "https://www.youtube.com/embed/2UmDrsMlXXg?si=dOKUJCT2Xhn6dr_Z&amp;start=8"},
        {'title': '강남스타일', 'music': '/static/audio/music_game/2010/강남스타일.mp3', 'singer': '싸이', 'youtube': "https://www.youtube.com/embed/9bZkp7q19f0?si=R2gOJqsYX8uzT_cn&amp;start=69"},
        {'title': '내가 제일 잘 나가', 'music': '/static/audio/music_game/2010/내가 제일 잘 나가.mp3', 'singer': '2NE1', 'youtube': "https://www.youtube.com/embed/j7_lSP8Vc3o?si=yd0gHmb3alCiuLnP&amp;start=84"},
        {'title': 'Bad Girl Good Girl', 'music': '/static/audio/music_game/2010/Bad Girl Good Girl.mp3', 'singer': '미쓰에이', 'youtube': "https://www.youtube.com/embed/8TeeJvcBdLA?si=v03MyDCjkIfBuTi0&amp;start=66"},
        {'title': 'Give it to me', 'music': '/static/audio/music_game/2010/Give it to me.mp3', 'singer': '미쓰에이', 'youtube': "https://www.youtube.com/embed/p6XLNsJ9YrA?si=OS1IOlmwNbFAPRWK&amp;start=57"},
        {'title': 'Way Back Home', 'music': '/static/audio/music_game/2010/Way Back Home.mp3', 'singer': '숀', 'youtube': "https://www.youtube.com/embed/amOSaNX7KJg?si=pc6BjT8myYcFTVSe&amp;start=57"},
        {'title': '삐삐', 'music': '/static/audio/music_game/2010/삐삐.mp3', 'singer': '아이유', 'youtube': "https://www.youtube.com/embed/nM0xDI5R50E?si=9Zuh23iAuzUzvlgS&amp;start=47"},
        {'title': '장난 아냐', 'music': '/static/audio/music_game/2010/장난 아냐.mp3', 'singer': '틴 탑', 'youtube': "https://www.youtube.com/embed/hHd_8iZFvK8?si=wEc954YEH5dKBdN2&amp;start=81"},
        {'title': '좋니', 'music': '/static/audio/music_game/2010/좋니.mp3', 'singer': '윤종신', 'youtube': "https://www.youtube.com/embed/b1kQvZhQ6_M?si=H2MIEgNJyUbqvbgk&amp;start=66"},
        {'title': '불타오르네', 'music': '/static/audio/music_game/2010/불타오르네.mp3', 'singer': '방탄소년단', 'youtube': "https://www.youtube.com/embed/ALj5MKjy2BU?si=lNR8y1TZ1eBd7A1B&amp;start=66"},
        {'title': '내꺼 하자', 'music': '/static/audio/music_game/2010/내꺼 하자.mp3', 'singer': '인피니트', 'youtube': "https://www.youtube.com/embed/tqC8AmuZuLI?si=sDTXufvWM_A3Aiob&amp;start=50"},
        {'title': '뿜뿜', 'music': '/static/audio/music_game/2010/뿜뿜.mp3', 'singer': '모모랜드', 'youtube': "https://www.youtube.com/embed/JQGRg8XBnB4?si=m8hVR4Oru8oHotDQ&amp;start=68"},
        {'title': '나혼자', 'music': '/static/audio/music_game/2010/나혼자.mp3', 'singer': '씨스타', 'youtube': "https://www.youtube.com/embed/E0ZHXVp_wUE?si=3a9pBMtCj2zHT6YL&amp;start=66"},
        {'title': 'cheer up', 'music': '/static/audio/music_game/2010/cheer up.mp3', 'singer': '트와이스', 'youtube': "https://www.youtube.com/embed/c7rCyll5AeY?si=PZ1Wiu1a1EdPO7lu&amp;start=67"},
        {'title': '후유증', 'music': '/static/audio/music_game/2010/후유증.mp3', 'singer': '제국의 아이들', 'youtube': "https://www.youtube.com/embed/J6xPw2UWNQg?si=nH9dSpSMaPElorcf&amp;start=67"},
        {'title': '썸띵', 'music': '/static/audio/music_game/2010/썸띵.mp3', 'singer': '걸스데이', 'youtube': "https://www.youtube.com/embed/JO7qQ7peKeM?si=i7gzRs_Hyevuu0Yg&amp;start=92"},
        {'title': '벚꽃 엔딩', 'music': '/static/audio/music_game/2010/벚꽃 엔딩.mp3', 'singer': '버스커 버스커', 'youtube': "https://www.youtube.com/embed/tXV7dfvSefo?si=eZNRLxWkyOTUJGjt&amp;start=80"},
        {'title': '200%', 'music': '/static/audio/music_game/2010/200%.mp3', 'singer': '악동뮤지션', 'youtube': "https://www.youtube.com/embed/0Oi8jDMvd_w?si=LL9In3GwPUM1FFo0&amp;start=56"},
        #2020
        {'title': 'ETA', 'music': '/static/audio/music_game/2020/ETA.mp3', 'singer': '뉴진스', 'youtube':'https://www.youtube.com/embed/jOTfBlKSQYY?si=JTk8_6t8s4C2T1Ci&amp;start=70'},
        {'title': '파이팅 해야지', 'music': '/static/audio/music_game/2020/파이팅 해야지.mp3', 'singer': '부석순', 'youtube':'https://www.youtube.com/embed/mBXBOLG06Wc?si=fyyjoqEu0yQL4O9H&amp;start=46'},
        {'title': '사건의 지평선', 'music': '/static/audio/music_game/2020/사건의 지평선.mp3', 'singer': '윤하', 'youtube': 'https://www.youtube.com/embed/BBdC1rl5sKY?si=JUL3Fizzx7teDtvR&amp;start=95'},
        {'title': 'Drama', 'music': '/static/audio/music_game/2020/Drama.mp3', 'singer': '에스파', 'youtube': 'https://www.youtube.com/embed/D8VEhcPeSlc?si=gCguu-inj3xt1w9L&amp;start=57'},
        {'title': 'Not Shy', 'music': '/static/audio/music_game/2020/Not Shy.mp3', 'singer': '있지', 'youtube': 'https://www.youtube.com/embed/wTowEKjDGkU?si=wVwJgFY18rhP95q2&amp;start=81'},
        {'title': '낙하', 'music': '/static/audio/music_game/2020/낙하.mp3', 'singer': '악동뮤지션', 'youtube': 'https://www.youtube.com/embed/EtiPbWzUY9o?si=dFZJr_u-0xzn8TMB&amp;start=51'},
        {'title': '아무노래', 'music': '/static/audio/music_game/2020/아무노래.mp3', 'singer': '지코', 'youtube': "https://www.youtube.com/embed/UuV2BmJ1p_I?si=M9ogffzyMc1Fh0-A&amp;start=27"},
        {'title': 'Rush Hour', 'music': '/static/audio/music_game/2020/Rush Hour.mp3', 'singer': '크러쉬', 'youtube': "https://www.youtube.com/embed/PS0qkO5qty0?si=PbHWneVDcmbBMPAU&amp;start=52"},
        {'title': 'Step Back', 'music': '/static/audio/music_game/2020/Step Back.mp3', 'singer': '갓 더 비트', 'youtube': "https://www.youtube.com/embed/ZvUBMXuVP78?si=-J-7VvSidsouwlEe&amp;start=74"},
        {'title': '봄여름가을겨울', 'music': '/static/audio/music_game/2020/봄여름가을겨울.mp3', 'singer': '빅뱅', 'youtube': "https://www.youtube.com/embed/eN5mG_yMDiM?si=IJweNI5mzELlJCek&amp;start=3"},
        {'title': '시작', 'music': '/static/audio/music_game/2020/시작.mp3', 'singer': '가호', 'youtube': "https://www.youtube.com/embed/6LDg0YGYVw4?si=VYIUyjUkHmUuMIHI&amp;start=43"},
        {'title': '음악의 신', 'music': '/static/audio/music_game/2020/음악의 신.mp3', 'singer': '세븐틴', 'youtube': "https://www.youtube.com/embed/zSQ48zyWZrY?si=-cJscmc9yb0TC-ps&amp;start=88"},
        {'title': '헤어지자 말해요', 'music': '/static/audio/music_game/2020/헤어지자 말해요.mp3', 'singer': '박재정', 'youtube': "https://www.youtube.com/embed/yFlxYHjHYAw?si=4D50eTbHdJp6ZIMa&amp;start=88"},
        {'title': 'CHRISTIAN', 'music': '/static/audio/music_game/2020/CHRISTIAN.mp3', 'singer': '지올팍', 'youtube': "https://www.youtube.com/embed/Dqlr8EDunCM?si=JuIXWL1osJGAZOzE&amp;start=50"},
        {'title': 'Smoke', 'music': '/static/audio/music_game/2020/Smoke.mp3', 'singer': '다이나믹 듀오, 이영지', 'youtube': "https://www.youtube.com/embed/iuIzniSa1Hs?si=_vsxaf9BXTTuKr2i&amp;start=39"},
        {'title': 'Seven', 'music': '/static/audio/music_game/2020/Seven.mp3', 'singer': '정국', 'youtube': "https://www.youtube.com/embed/1QYBiNRu1ok?si=hA1ddyu_sLWIt3bk&amp;start=45"},
        {'title': 'Perfect Night', 'music': '/static/audio/music_game/2020/Perfect Night.mp3', 'singer': '르세라핌', 'youtube': "https://www.youtube.com/embed/oKBwWQI-IoI?si=qS09g9XhXV8Psj8O&amp;start=35"},
        {'title': 'Get A Guitar', 'music': '/static/audio/music_game/2020/Get A Guitar.mp3', 'singer': '라이즈', 'youtube': "https://www.youtube.com/embed/iUw3LPM7OBU?si=fk2UGNqyS5GnS2HC&amp;start=18"},
        {'title': '가나다라', 'music': '/static/audio/music_game/2020/가나다라.mp3', 'singer': '박재범(feat. 아이유)', 'youtube': "https://www.youtube.com/embed/gFb1TftvdoM?si=Momm89t24eUpwicX&amp;start=256"},
        {'title': '사랑인가 봐', 'music': '/static/audio/music_game/2020/사랑인가 봐.mp3', 'singer': '멜로망스', 'youtube': "https://www.youtube.com/embed/UoBsiQW23IY?si=viuPtsQua3FzLvQs&amp;start=44"},
        {'title': 'Baddie', 'music': '/static/audio/music_game/2020/Baddie.mp3', 'singer': '아이브', 'youtube': "https://www.youtube.com/embed/Da4P2uT4mVc?si=3b8MB8St_LNDiMT7&amp;start=57"},
        {'title': '사랑은 늘 도망가', 'music': '/static/audio/music_game/2020/사랑은 늘 도망가.mp3', 'singer': '임영웅', 'youtube': "https://www.youtube.com/embed/LKQ-18LoFQk?si=YeHPIilLxok0wwlX&amp;start=58"},
        {'title': 'Weekend', 'music': '/static/audio/music_game/2020/Weekend.mp3', 'singer': '태연', 'youtube': "https://www.youtube.com/embed/RmuL-BPFi2Q?si=ZIVVIx6F5iVz1q82&amp;start=65"},
        {'title': 'ASAP', 'music': '/static/audio/music_game/2020/ASAP.mp3', 'singer': '스테이씨', 'youtube': "https://www.youtube.com/embed/NsY-9MCOIAQ?si=jBxu5VAd6Jw4kkza&amp;start=44"},
        {'title': 'Vancouver', 'music': '/static/audio/music_game/2020/Vancouver.mp3', 'singer': 'BIG Naughty(서동현)', 'youtube': "https://www.youtube.com/embed/mev609MxcRE?si=uqKlhm4PEHDv913f&amp;start=59"},
        {'title': '신호등', 'music': '/static/audio/music_game/2020/신호등.mp3', 'singer': '이무진', 'youtube': "https://www.youtube.com/embed/SK6Sm2Ki9tI?si=N_T3anxVtOxgRvC2&amp;start=79"},
        {'title': 'Next Level', 'music': '/static/audio/music_game/2020/Next Level.mp3', 'singer': '에스파', 'youtube': "https://www.youtube.com/embed/4TWR90KJl84?si=qt5bTBoti6TBlWBu&amp;start=51"},
        {'title': '다시 여기 바닷가', 'music': '/static/audio/music_game/2020/다시 여기 바닷가.mp3', 'singer': '싹쓰리', 'youtube': "https://www.youtube.com/embed/ESKfHHtiSjs?si=LHUV3yDMQ51TmP0Y&amp;start=86"},
        {'title': '마리아', 'music': '/static/audio/music_game/2020/마리아.mp3', 'singer': '화사', 'youtube': "https://www.youtube.com/embed/tDukIfFzX18?si=MbiheaqO5cxE3ibo&amp;start=72"},
        {'title': '에잇', 'music': '/static/audio/music_game/2020/에잇.mp3', 'singer': '아이유', 'youtube': "https://www.youtube.com/embed/TgOu00Mf3kI?si=UnDMTW8-xseaBP1d&amp;start=63"},
    ]
    
    for data in quiz_data:
        MusicGame.objects.get_or_create(title=data['title'], music=data['music'], singer=data['singer'], youtube=data['youtube'])
    
    if roomId == 0:
        if request.method == 'POST':
            count = int(request.POST['count'])
            time = int(request.POST['time'])
            ctx = {
            'roomId' : roomId,
            'count':count
            }
            
            if time == 2000:
                return redirect('/music/{0}/music_game_2000/{1}'.format(roomId,count))
            elif time == 2010:
                return redirect('/music/{0}/music_game_2010/{1}'.format(roomId,count))
            elif time == 2020:
                return redirect('/music/{0}/music_game_2020/{1}'.format(roomId,count))
        ctx = {
            'roomId' : roomId,
            }
        return render(request, 'musicGames/music_game_main.html', ctx)

    room = GameRoom.objects.get(id=roomId)
    if request.method == 'POST':
        count = int(request.POST['count'])
        time = int(request.POST['time'])
        ctx = {
        'roomId' : roomId,
        'room':room,
        'count':count
        }
        
        if time == 2000:
            return redirect('/music/{0}/music_game_2000/{1}'.format(roomId,count))
        elif time == 2010:
            return redirect('/music/{0}/music_game_2010/{1}'.format(roomId,count))
        elif time == 2020:
            return redirect('/music/{0}/music_game_2020/{1}'.format(roomId,count))
        
    
    ctx = {
        'roomId' : roomId,
        'room':room,
        }
    return render(request, 'musicGames/music_game_main.html', ctx)


# 2. 첫 문제 보여주는 페이지
# 3. 다음 버튼 눌렀을 때 : ajax로 구현
# 4. 우선 게임 종료 시 게임 표지 페이지로 이동 : ajax로 구현
def music_game_start_2000(request, roomId, count):
    if(roomId == 0):
        quiz_id_int_list = random.sample(range(1,31),count)
    else:
        music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2000')) + 1), count)
        music_game_query_2000 = MusicGame.objects.filter(music__contains='2000')
        first_music_2000 = music_game_query_2000.first()
        first_music_id_2000 = int(first_music_2000.id)
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_music
        quiz_id_str_list = list(map(int,quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]
    
    music = MusicGame.objects.filter(music__contains='2000')
    music_game = [music[quiz_id_int_list[0]-1].id]
    for quiz_id in quiz_id_int_list[1:]:
        music_game_now =music[quiz_id-1].id
        music_game.append(music_game_now)

    quiz_id = music_game.pop(0)
    music_game.append(quiz_id)
    quiz = MusicGame.objects.get(id = quiz_id)
    
    if roomId == 0:
        ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'count' : count,
        'music_game' : music_game,
        'quiz_id':quiz_id
        }
        return render(request, 'musicGames/music_game_start_2000.html', ctx)
    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'room':room,
        'count' : count,
        'music_game' : music_game,
        'quiz_id':quiz_id
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def music_game_start_2010(request, roomId, count):
    if(roomId == 0):
        quiz_id_int_list = random.sample(range(1,31),count)
    else:
        music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2010')) + 1), count)
        music_game_query_2010 = MusicGame.objects.filter(music__contains='2010')
        first_music_2010 = music_game_query_2010.first()
        first_music_id_2010 = int(first_music_2010.id)
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_music
        quiz_id_str_list = list(map(int,quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    
    music = MusicGame.objects.filter(music__contains='2010')
    music_game = [music[quiz_id_int_list[0]-1].id]
    for quiz_id in quiz_id_int_list[1:]:
        music_game_now =music[quiz_id-1].id
        music_game.append(music_game_now)


    quiz_id = music_game.pop(0)
    music_game.append(quiz_id)
    quiz = MusicGame.objects.get(id = quiz_id)

    if roomId == 0:
        ctx = {
        'quiz' : quiz,
        'count' : count,
        'roomId' : roomId,
        'music_game' : music_game,
        'quiz_id':quiz_id
        }
        return render(request, 'musicGames/music_game_start_2000.html', ctx)

    ctx = {
        'quiz' : quiz,
        'roomId' : roomId,
        'music_game' : music_game,
        'quiz_id':quiz_id
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def music_game_start_2020(request, count,roomId):
    if(roomId == 0):
        quiz_id_int_list = random.sample(range(1,31),count)
    else:
        music_game_ids = random.sample(range(1, len(MusicGame.objects.filter(music__contains='2020')) + 1), count)
        music_game_query_2020 = MusicGame.objects.filter(music__contains='2020')
        first_music_2020 = music_game_query_2020.first()
        first_music_id_2020 = int(first_music_2020.id)
        room = GameRoom.objects.get(id=roomId)
        quiz_id_list = room.ran_music
        quiz_id_str_list = list(map(int,quiz_id_list.split(",")))
        quiz_id_int_list = quiz_id_str_list[:count]

    music = MusicGame.objects.filter(music__contains='2020')
    music_game = [music[quiz_id_int_list[0]-1].id]
    for quiz_id in quiz_id_int_list[1:]:
        music_game_now =music[quiz_id-1].id
        music_game.append(music_game_now)

    quiz_id = music_game.pop(0)
    music_game.append(quiz_id)
    quiz = MusicGame.objects.get(id = quiz_id)

    if roomId == 0:
        ctx = {
        'quiz' : quiz,
        'count' : count,
        'roomId' : roomId,
        'music_game' : music_game,
        'quiz_id':quiz_id
        }
        return render(request, 'musicGames/music_game_start_2000.html', ctx)

    ctx = {
        'quiz' : quiz,
        'count' : count,
        'roomId' : roomId,
        'room':room,
        'music_game' : music_game,
        'quiz_id':quiz_id
    }
    return render(request, 'musicGames/music_game_start_2000.html', ctx)

def next_quiz(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])
    quiz_id = game_list.pop(0)
    game_list.append(quiz_id)

    quiz = MusicGame.objects.get(id=quiz_id)
    music = quiz.music
    youtube = quiz.youtube

    return JsonResponse({'id' : quiz_id, 'music' : music, 'youtube' : youtube, 'game_list':game_list})


def before_quiz(request):
    req = json.loads(request.body)
    quiz_id = (req['id'])
    game_list=(req['game_list'])

    next_quiz_id = game_list.pop()
    game_list.insert(0,next_quiz_id)
    quiz_id = game_list[-1]

    quiz = MusicGame.objects.get(id=quiz_id)
    music = quiz.music
    youtube = quiz.youtube

    return JsonResponse({'id' : quiz_id, 'music' : music, 'youtube' : youtube, 'game_list':game_list})

def answer(request):
    print("here")
    req = json.loads(request.body)
    quiz_id = (req['id'])

    quiz = MusicGame.objects.get(id=quiz_id)
    title = quiz.title
    singer = quiz.singer

    return JsonResponse({'id' : quiz_id, 'title' : title, 'singer' : singer})