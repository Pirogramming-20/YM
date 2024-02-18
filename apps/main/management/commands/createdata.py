from django.core.management.base import BaseCommand
from apps.bodyGames.models import *
from apps.chatGames.models import *
from apps.figure.models import *
from apps.fourWords.models import *
from apps.lookInside.models import *
from apps.movieGames.models import *
from apps.mudoGames.models import *
from apps.musicGames.models import *

class Command(BaseCommand):
    help = 'Create base data for quiz'

    def handle(self, *args, **options):
        #몸으로 말해요 게임
        quiz_data_bodyGames = [
            #동물
            {'type' : 'animal', 'word' : '토끼'},
            {'type' : 'animal', 'word' : '고양이'},
            {'type' : 'animal', 'word' : '강아지'},
            {'type' : 'animal', 'word' : '말'},
            {'type' : 'animal', 'word' : '쥐'},
            {'type' : 'animal', 'word' : '개구리'},
            {'type' : 'animal', 'word' : '닭'},
            {'type' : 'animal', 'word' : '호랑이'},
            {'type' : 'animal', 'word' : '사자'},
            {'type' : 'animal', 'word' : '원숭이'},
            {'type' : 'animal', 'word' : '코끼리'},
            {'type' : 'animal', 'word' : '늑대'},
            {'type' : 'animal', 'word' : '게'},
            {'type' : 'animal', 'word' : '펭귄'},
            {'type' : 'animal', 'word' : '거북이'},
            {'type' : 'animal', 'word' : '악어'},
            {'type' : 'animal', 'word' : '사슴'},
            {'type' : 'animal', 'word' : '상어'},
            {'type' : 'animal', 'word' : '나무늘보'},
            {'type' : 'animal', 'word' : '목도리도마뱀'},
            {'type' : 'animal', 'word' : '캥거루'},
            {'type' : 'animal', 'word' : '오리'},
            {'type' : 'animal', 'word' : '코뿔소'},
            {'type' : 'animal', 'word' : '돌고래'},
            {'type' : 'animal', 'word' : '코알라'},
            {'type' : 'animal', 'word' : '고릴라'},
            {'type' : 'animal', 'word' : '타조'},
            {'type' : 'animal', 'word' : '기린'},
            {'type' : 'animal', 'word' : '문어'},
            {'type' : 'animal', 'word' : '곰'},
            #음식
            {'type' : 'food', 'word' : '치킨'},
            {'type' : 'food', 'word' : '김밥'},
            {'type' : 'food', 'word' : '아이스크림'},
            {'type' : 'food', 'word' : '햄버거'},
            {'type' : 'food', 'word' : '짜장면'},
            {'type' : 'food', 'word' : '빵'},
            {'type' : 'food', 'word' : '떡볶이'},
            {'type' : 'food', 'word' : '김치'},
            {'type' : 'food', 'word' : '바나나'},
            {'type' : 'food', 'word' : '레몬'},
            {'type' : 'food', 'word' : '포도'},
            {'type' : 'food', 'word' : '수박'},
            {'type' : 'food', 'word' : '라면'},
            {'type' : 'food', 'word' : '삼겹살'},
            {'type' : 'food', 'word' : '비빔밥'},
            {'type' : 'food', 'word' : '돼지국밥'},
            {'type' : 'food', 'word' : '산낙지'},
            {'type' : 'food', 'word' : '초밥'},
            {'type' : 'food', 'word' : '김치'},
            {'type' : 'food', 'word' : '회'},
            {'type' : 'food', 'word' : '군고구마'},
            {'type' : 'food', 'word' : '피자'},
            {'type' : 'food', 'word' : '마라탕'},
            {'type' : 'food', 'word' : '닭발'},
            {'type' : 'food', 'word' : '돈까스'},
            {'type' : 'food', 'word' : '탕후루'},
            {'type' : 'food', 'word' : '와플'},
            {'type' : 'food', 'word' : '샌드위치'},
            {'type' : 'food', 'word' : '도넛'},
            {'type' : 'food', 'word' : '파스타'},
            #물건
            {'type' : 'thing', 'word' : '열쇠'},
            {'type' : 'thing', 'word' : '옷장'},
            {'type' : 'thing', 'word' : '시계'},
            {'type' : 'thing', 'word' : '핸드폰'},
            {'type' : 'thing', 'word' : '신문'},
            {'type' : 'thing', 'word' : '소파'},
            {'type' : 'thing', 'word' : '에어컨'},
            {'type' : 'thing', 'word' : '선풍기'},
            {'type' : 'thing', 'word' : '청소기'},
            {'type' : 'thing', 'word' : '노트북'},
            {'type' : 'thing', 'word' : '창문'},
            {'type' : 'thing', 'word' : '카메라'},
            {'type' : 'thing', 'word' : '침대'},
            {'type' : 'thing', 'word' : '칫솔'},
            {'type' : 'thing', 'word' : '수건'},
            {'type' : 'thing', 'word' : '비누'},
            {'type' : 'thing', 'word' : '크레파스'},
            {'type' : 'thing', 'word' : '축구공'},
            {'type' : 'thing', 'word' : '스케치북'},
            {'type' : 'thing', 'word' : '우산'},
            {'type' : 'thing', 'word' : '목걸이'},
            {'type' : 'thing', 'word' : '장화'},
            {'type' : 'thing', 'word' : '가방'},
            {'type' : 'thing', 'word' : '책상'},
            {'type' : 'thing', 'word' : '의자'},
            {'type' : 'thing', 'word' : '휴지'},
            {'type' : 'thing', 'word' : '텀블러'},
            {'type' : 'thing', 'word' : '안경'},
            {'type' : 'thing', 'word' : '거울'},
            {'type' : 'thing', 'word' : '마우스'},
            #직업
            {'type' : 'job', 'word' : '마술사'},
            {'type' : 'job', 'word' : '경찰'},
            {'type' : 'job', 'word' : '요리사'},
            {'type' : 'job', 'word' : '소방관'},
            {'type' : 'job', 'word' : '간호사'},
            {'type' : 'job', 'word' : '프로게이머'},
            {'type' : 'job', 'word' : '개발자'},
            {'type' : 'job', 'word' : '모델'},
            {'type' : 'job', 'word' : '아나운서'},
            {'type' : 'job', 'word' : '의사'},
            {'type' : 'job', 'word' : '작가'},
            {'type' : 'job', 'word' : '피아니스트'},
            {'type' : 'job', 'word' : '변호사'},
            {'type' : 'job', 'word' : '배우'},
            {'type' : 'job', 'word' : '헬스 트레이너'},
            {'type' : 'job', 'word' : '영화 감독'},
            {'type' : 'job', 'word' : '댄서'},
            {'type' : 'job', 'word' : '농부'},
            {'type' : 'job', 'word' : '판사'},
            {'type' : 'job', 'word' : '지휘자'},
            {'type' : 'job', 'word' : '바리스타'},
            {'type' : 'job', 'word' : '사진작가'},
            {'type' : 'job', 'word' : '복서'},
            {'type' : 'job', 'word' : '수영 선수'},
            {'type' : 'job', 'word' : '농구 선수'},
            {'type' : 'job', 'word' : '야구 선수'},
            {'type' : 'job', 'word' : '화가'},
            {'type' : 'job', 'word' : '미용사'},
            {'type' : 'job', 'word' : '우주비행사'},
            {'type' : 'job', 'word' : '건축가'},
            #속담
            {'type' : 'proverb', 'word' : '지렁이도 밟으면 꿈틀한다'},
            {'type' : 'proverb', 'word' : '낫 놓고 ㄱ자도 모른다'},
            {'type' : 'proverb', 'word' : '낮말은 새가 듣고 밤말은 쥐가 듣는다'},
            {'type' : 'proverb', 'word' : '소 귀에 경 읽기'},
            {'type' : 'proverb', 'word' : '하룻강아지 범 무서운 줄 모른다'},
            {'type' : 'proverb', 'word' : '서당개 3년이면 풍월을 읊는다'},
            {'type' : 'proverb', 'word' : '윗물이 맑아야 아랫물이 맑다'},
            {'type' : 'proverb', 'word' : '등잔 밑이 어둡다'},
            {'type' : 'proverb', 'word' : '누워서 침 뱉기'},
            {'type' : 'proverb', 'word' : '누워서 떡 먹기'},
            {'type' : 'proverb', 'word' : '식은 죽 먹기'},
            {'type' : 'proverb', 'word' : '소 잃고 외양간 고치기'},
            {'type' : 'proverb', 'word' : '가는 말이 고와야 오는 말이 곱다'},
            {'type' : 'proverb', 'word' : '미운 놈 떡 하나 더 준다'},
            {'type' : 'proverb', 'word' : '작은 고추가 더 맵다'},
            {'type' : 'proverb', 'word' : '돌다리도 두들겨보고 건너라'},
            {'type' : 'proverb', 'word' : '세살 버릇 여든까지 간다'},
            {'type' : 'proverb', 'word' : '하늘이 무너져도 솟아날 구멍은 있다'},
            {'type' : 'proverb', 'word' : '티끌 모아 태산'},
            {'type' : 'proverb', 'word' : '발 없는 말이 천리 간다'},
            {'type' : 'proverb', 'word' : '시작이 반이다'},
            {'type' : 'proverb', 'word' : '백지장도 맞들면 낫다'},
            {'type' : 'proverb', 'word' : '바늘 가는데 실 간다'},
            {'type' : 'proverb', 'word' : '고래 싸움에 새우 등 터진다'},
            {'type' : 'proverb', 'word' : '원수는 외나무 다리에서 만난다'},
            {'type' : 'proverb', 'word' : '바늘 도둑이 소 도둑 된다'},
            {'type' : 'proverb', 'word' : '콩 심은 데 콩 나고 팥 심은 데 팥 난다'},
            {'type' : 'proverb', 'word' : '사공이 많으면 배가 산으로 간다'},
            {'type' : 'proverb', 'word' : '믿는 도끼에 발등 찍힌다'},
            {'type' : 'proverb', 'word' : '강 건너 불구경 하듯 한다'},
        ]   

        for data in quiz_data_bodyGames:
            if data['type'] == 'animal':
                BodyGame_animal.objects.get_or_create(word=data['word'])
            elif data['type'] == 'food':
                BodyGame_food.objects.get_or_create(word=data['word'])
            elif data['type'] == 'thing':
                BodyGame_thing.objects.get_or_create(word=data['word'])
            elif data['type'] == 'job':
                BodyGame_job.objects.get_or_create(word=data['word'])
            elif data['type'] == 'proverb':
                BodyGame_proverb.objects.get_or_create(word=data['word'])

        #채팅 빨리 보내기 게임
        for i in range(1,16,1):
            img_path = f"/static/image/chatGames/{i}.jpg"
            ChatGame.objects.get_or_create(chatText=img_path)

        #인물 퀴즈
        name_list_figure = ['강다니엘', '강하늘', '거미', '고두심', '기안84', '김연아', '김연자','김우빈','나문희','노사연',
                '다현', '디카프리오','라이언','마릴린먼로','모모','모차르트','문재인','박건후','박건후','박보검','방귀대장뿡뿡이',
                '베토벤', '보아', '뿡뿡이', '세일러문', '세종대왕', '손흥민', '송가인', '송은이', '송중기', '아만다 사이프리드',
                '아이린', '아이유', '어피치', '엠마왓슨', '예성', '온유', '옹성우', '유관순', '육성재', '이명박',
                '이상민', '이순재', '이효리', '장윤주', '저스틴비버', '전지현', '전진', '정우성', '유노윤호', '조세호',
                '조이', '조정석', '최순실', '카리나', '펭수', '하니', '한채아', '한혜진', '허경영', '홍진영']
        for i in range(len(name_list_figure)):
            Figure.objects.get_or_create(name=name_list_figure[i])
            figure = Figure.objects.get(name=name_list_figure[i])
            figure.image_path = f"/static/image/figure/{figure.name}.jpg"
            figure.save()

        #네글자 퀴즈
        answer_list = ['샌드위치', '연지곤지', '차돌박이', '바리스타', '신속정확', '표고버섯', '대한민국', '급속충전', '양념치킨', '취중진담',
            '미세먼지', '드래곤볼', '십중팔구', '고진감래', '생로병사', '신서유기', '흔들의자', '코카콜라', '삼시세끼', '브라우니', 
            '비트코인', '방방곡곡', '도원결의', '스파게티', '비타오백', '누네띠네', '어장관리', '버터구이', '업데이트', '카페베네',
            '붉은노을', '낄끼빠빠', '스타워즈', '백설공주', '오토바이', '파인애플', '스타필드', '사자성어', '비밀번호', '계좌번호',
            '생년월일', '고객센터', '알레르기', '현장학습', '뭉게구름', '호랑나비', '종이접기', '주의사항', '탄수화물', '삼각김밥',
            '소녀시대', '미끄럼틀', '원두커피', '하모니카', '신용카드', '타임오버', '하드캐리', '아카시아', '플라스틱', '마요네즈',]
    
        for i in range(len(answer_list)):
            four_instance,created = Four.objects.get_or_create(answer=answer_list[i])
            four_instance.two_save()
        
        #음악 게임
        quiz_data_musicGames = [
            {'year' : '2000', 'title': '벌써 일년', 'music': '/static/audio/music_game/2000/벌써 일년.mp3', 'singer': '브라운아이즈', 'youtube': 'https://www.youtube.com/embed/LZlIqfMn4cc?si=VbOb_tpc2xv4F-0A&amp;start=159'},
            {'year' : '2000', 'title': '거짓말', 'music': '/static/audio/music_game/2000/거짓말.mp3', 'singer': '빅뱅', 'youtube': 'https://www.youtube.com/embed/NeDeZUqNiVo?si=LH8vkS1w_hsox6sG&amp;start=85'},
            {'year' : '2000', 'title': 'I Don\'t Care', 'music': '/static/audio/music_game/2000/I Don\'t Care.mp3', 'singer': '투애니원', 'youtube': 'https://www.youtube.com/embed/4MgAxMO1KD0?si=cN50Tl5-Xu1ABOaS&amp;start=88'},
            {'year' : '2000', 'title': 'Gee', 'music': '/static/audio/music_game/2000/Gee.mp3', 'singer': '소녀시대', 'youtube': 'https://www.youtube.com/embed/U7mPqycQ0tQ?si=-NwjsF9t0NZZoR50&amp;start=79'},
            {'year' : '2000', 'title': 'Sorry Sorry', 'music': '/static/audio/music_game/2000/Sorry Sorry.mp3', 'singer': '슈퍼주니어', 'youtube': 'https://www.youtube.com/embed/x6QA3m58DQw?si=sk07LSUup9twcSaY&amp;start=78'},
            {'year' : '2000', 'title': '아브라카다브라', 'music': '/static/audio/music_game/2000/아브라카다브라.mp3', 'singer': '브라운아이드걸스', 'youtube': 'https://www.youtube.com/embed/o4wJGWcHzVA?si=ECAQh-LgF1FUfoTk&amp;start=15'},
            {'year' : '2000', 'title': 'Oh my Julia', 'music': '/static/audio/music_game/2000/Oh my Julia.mp3', 'singer': '컨츄리꼬꼬', 'youtube': "https://www.youtube.com/embed/Xbk_NStauds?si=4IqgIpYEeE8qC1aV&amp;start=52"},
            {'year' : '2000', 'title': 'Fire', 'music': '/static/audio/music_game/2000/Fire.mp3', 'singer': '2NE1', 'youtube': "https://www.youtube.com/embed/49AfuuRbgGo?si=Y46jmf-NWWv0sLYi&amp;start=79"},
            {'year' : '2000', 'title': '내 귀에 캔디', 'music': '/static/audio/music_game/2000/내 귀에 캔디.mp3', 'singer': '백지영(feat.택연 of 2PM)', 'youtube': "https://www.youtube.com/embed/rMG1YtxHLB8?si=Gd25xrnu-bQMnAqC&amp;start=57"},
            {'year' : '2000', 'title': 'Heartbreaker', 'music': '/static/audio/music_game/2000/Heartbreaker.mp3', 'singer': '지드래곤', 'youtube': "https://www.youtube.com/embed/LOXEVd-Z7NE?si=TOoPpVxcqk6WzUUv&amp;start=44" },
            {'year' : '2000', 'title': '길', 'music': '/static/audio/music_game/2000/길.mp3', 'singer': '지오디', 'youtube': "https://www.youtube.com/embed/OFlxQZNWNMU?si=HO0dFunuX4OcKWs-&amp;start=167"},
            {'year' : '2000', 'title': '10 Minutes', 'music': '/static/audio/music_game/2000/10 Minutes.mp3', 'singer': '이효리', 'youtube': "https://www.youtube.com/embed/iKdr44yEBQU?si=1ztaFHZdcId6nk-L&amp;start=9"},
            {'year' : '2000', 'title': 'So Hot', 'music': '/static/audio/music_game/2000/So Hot.mp3', 'singer': '원더걸스', 'youtube': "https://www.youtube.com/embed/wiAI6AUtltE?si=kuIL1jriv1OBCqm8&amp;start=54"},
            {'year' : '2000', 'title': '잊을게', 'music': '/static/audio/music_game/2000/잊을게.mp3', 'singer': '윤도현 밴드(YB)', 'youtube': "https://www.youtube.com/embed/VecH1Y2INho?si=Lp8cyaIzym1s3d2j&amp;start=71"},
            {'year' : '2000', 'title': '비행기', 'music': '/static/audio/music_game/2000/비행기.mp3', 'singer': '거북이', 'youtube': "https://www.youtube.com/embed/q3outEcc-HE?si=DTxCmrgA10vL-Yng&amp;start=16"},
            {'year' : '2000', 'title': '바람만바람만', 'music': '/static/audio/music_game/2000/바람만바람만.mp3', 'singer': '김종국,sg워너비', 'youtube': "https://www.youtube.com/embed/gEZHjx1RM9c?si=EJPyRnPZmdBXUu4j&amp;start=240"},
            {'year' : '2000', 'title': '8282', 'music': '/static/audio/music_game/2000/8282.mp3', 'singer': '다비치', 'youtube': "https://www.youtube.com/embed/IwibOy34oAw?si=0S3-e2qwX8avvn8c&amp;start=240"},
            {'year' : '2000', 'title': '헤어지지못하는여자 떠나가지못하는남자', 'music': '/static/audio/music_game/2000/헤어지지못하는여자 떠나가지못하는남자.mp3', 'singer': '리쌍(feat.정인)', 'youtube': "https://www.youtube.com/embed/3rYL8AHJaTc?si=hYUbLaKhBAiGVk1o&amp;start=21"},
            {'year' : '2000', 'title': '꿈에', 'music': '/static/audio/music_game/2000/꿈에.mp3', 'singer': '박정현', 'youtube': "https://www.youtube.com/embed/O5M2WFmFn04?si=8jvaAKlxooaiNdLc&amp;start=21"},
            {'year' : '2000', 'title': 'Love Story', 'music': '/static/audio/music_game/2000/Love Story.mp3', 'singer': '비(Rain)', 'youtube': "https://www.youtube.com/embed/2xnpFI3PLYs?si=xCuaA6eY4-1NWoHe&amp;start=310"},
            {'year' : '2000', 'title': '유혹의 소나타', 'music': '/static/audio/music_game/2000/유혹의 소나타.mp3', 'singer': '아이비', 'youtube': "https://www.youtube.com/embed/Q_plceCKQX8?si=4JdG2CAFkUUClV63&amp;start=70"},
            {'year' : '2000', 'title': '아시나요', 'music': '/static/audio/music_game/2000/아시나요.mp3', 'singer': '조성모', 'youtube': "https://www.youtube.com/embed/niiZThi8Eog?si=Pp8sa89ohzYfTHP0&amp;start=257"},
            {'year' : '2000', 'title': '좋은 사람', 'music': '/static/audio/music_game/2000/좋은 사람.mp3', 'singer': '박효신', 'youtube': "https://www.youtube.com/embed/W7CcTfUu-mg?si=FLNku4H0EU_hOeyQ&amp;start=154"},
            {'year' : '2000', 'title': '순정', 'music': '/static/audio/music_game/2000/순정.mp3', 'singer': '코요태', 'youtube': "https://www.youtube.com/embed/MHCBoNhQmCk?si=4fRwPzyCXsTGfz9y&amp;start=82"},
            {'year' : '2000', 'title': '흔들린 우정', 'music': '/static/audio/music_game/2000/흔들린 우정.mp3', 'singer': '홍경민', 'youtube': "https://www.youtube.com/embed/SnGpl6AkvSY?si=W3NMrS11YqADEUZ1&amp;start=86"},
            {'year' : '2000', 'title': '내 머리가 나빠서', 'music': '/static/audio/music_game/2000/내 머리가 나빠서.mp3', 'singer': 'SS501', 'youtube': "https://www.youtube.com/embed/kcKHzns0L5s?si=07uieZ-pNl6d8gA-&amp;start=86"},
            {'year' : '2000', 'title': '가시', 'music': '/static/audio/music_game/2000/가시.mp3', 'singer': '버즈', 'youtube': "https://www.youtube.com/embed/ZhI9tQP4Abw?si=1T6h5vU1S0480PRW&amp;start=78"},
            {'year' : '2000', 'title': '총맞은것처럼', 'music': '/static/audio/music_game/2000/총맞은것처럼.mp3', 'singer': '백지영', 'youtube': "https://www.youtube.com/embed/uSdlduWm4HM?si=CGHCkh5kLPgf2NiZ&amp;start=56"},
            {'year' : '2000', 'title': '아틀란티스 소녀', 'music': '/static/audio/music_game/2000/아틀란티스 소녀.mp3', 'singer': '보아', 'youtube': "https://www.youtube.com/embed/skbnuIhVQUA?si=B26QyqSxrVml9sEs&amp;start=75"},
            {'year' : '2000', 'title': '만만하니', 'music': '/static/audio/music_game/2000/만만하니.mp3', 'singer': '유키스', 'youtube': "https://www.youtube.com/embed/EBBCpTO0hyc?si=-5d3GGOhsNxMfRwl&amp;start=71"},
            #2010
            {'year' : '2010', 'title': '뚜두뚜두', 'music': '/static/audio/music_game/2010/뚜두뚜두.mp3', 'singer': '블랙핑크', 'youtube': 'https://www.youtube.com/embed/IHNzOHi8sJs?si=lBgvYpn4FXOn09uq&amp;start=76'},
            {'year' : '2010', 'title': 'DNA', 'music': '/static/audio/music_game/2010/DNA.mp3', 'singer': '방탄소년단', 'youtube': 'https://www.youtube.com/embed/MBdVXkSdhwU?si=huPiie_CLxGDKClN&amp;start=87'},
            {'year' : '2010', 'title': '오늘부터 우리는', 'music': '/static/audio/music_game/2010/오늘부터 우리는.mp3', 'singer': '여자친구', 'youtube': 'https://www.youtube.com/embed/YYHyAIFG3iI?si=LYheUvSriGcU2P8Z&amp;start=35'},
            {'year' : '2010', 'title': 'Love Shot', 'music': '/static/audio/music_game/2010/Love Shot.mp3', 'singer': '엑소', 'youtube': 'https://www.youtube.com/embed/pSudEWBAYRE?si=kcMWvRQ96Ya9DGrV&amp;start=45'},
            {'year' : '2010', 'title': 'Dance the Night Away', 'music': '/static/audio/music_game/2010/Dance the Night Away.mp3', 'singer': '트와이스', 'youtube': 'https://www.youtube.com/embed/Fm5iP0S1z9w?si=Ki7ZHH9iRcoFjmqx&amp;start=78'},
            {'year' : '2010', 'title': 'MILLIONS', 'music': '/static/audio/music_game/2010/MILLIONS.mp3', 'singer': '위너', 'youtube': 'https://www.youtube.com/embed/PALjhRpnfbk?si=CuThJcwv2TmvfjLe&amp;start=62'},
            {'year' : '2010', 'title': '빨간맛', 'music': '/static/audio/music_game/2010/빨간맛.mp3', 'singer': '레드벨벳', 'youtube': 'https://www.youtube.com/embed/WyiIGEHQP8o?si=cnKMlL3mp29kINjw&amp;start=62'},
            {'year' : '2010', 'title': '선물', 'music': '/static/audio/music_game/2010/선물.mp3', 'singer': '멜로망스', 'youtube': "https://www.youtube.com/embed/qYYJqWsBb1U?si=iA_uAjaLR6x09xJ_&amp;start=61"},
            {'year' : '2010', 'title': '뱅뱅뱅', 'music': '/static/audio/music_game/2010/뱅뱅뱅.mp3', 'singer': '빅뱅', 'youtube': "https://www.youtube.com/embed/2ips2mM7Zqw?si=nJVIrFmXECajDhe_&amp;start=58"},
            {'year' : '2010', 'title': '심쿵해', 'music': '/static/audio/music_game/2010/심쿵해.mp3', 'singer': 'AOA', 'youtube': "https://www.youtube.com/embed/1pBgMBBsv4k?si=YWetermoTlkQraA9&amp;start=106"},
            {'year' : '2010', 'title': '눈코입', 'music': '/static/audio/music_game/2010/눈코입.mp3', 'singer': '태양', 'youtube': "https://www.youtube.com/embed/UwuAPyOImoI?si=KeVmYqt5eR79qUJM&amp;start=83"},
            {'year' : '2010', 'title': '삐딱하게', 'music': '/static/audio/music_game/2010/삐딱하게.mp3', 'singer': '지드래곤', 'youtube': "https://www.youtube.com/embed/RKhsHGfrFmY?si=6zDDWo8UwvaVCg1f&amp;start=87"},
            {'year' : '2010', 'title': '24시간이 모자라', 'music': '/static/audio/music_game/2010/24시간이 모자라.mp3', 'singer': '선미', 'youtube': "https://www.youtube.com/embed/2UmDrsMlXXg?si=dOKUJCT2Xhn6dr_Z&amp;start=8"},
            {'year' : '2010', 'title': '강남스타일', 'music': '/static/audio/music_game/2010/강남스타일.mp3', 'singer': '싸이', 'youtube': "https://www.youtube.com/embed/9bZkp7q19f0?si=R2gOJqsYX8uzT_cn&amp;start=69"},
            {'year' : '2010', 'title': '내가 제일 잘 나가', 'music': '/static/audio/music_game/2010/내가 제일 잘 나가.mp3', 'singer': '2NE1', 'youtube': "https://www.youtube.com/embed/j7_lSP8Vc3o?si=yd0gHmb3alCiuLnP&amp;start=84"},
            {'year' : '2010', 'title': 'Bad Girl Good Girl', 'music': '/static/audio/music_game/2010/Bad Girl Good Girl.mp3', 'singer': '미쓰에이', 'youtube': "https://www.youtube.com/embed/8TeeJvcBdLA?si=v03MyDCjkIfBuTi0&amp;start=66"},
            {'year' : '2010', 'title': 'Give it to me', 'music': '/static/audio/music_game/2010/Give it to me.mp3', 'singer': '미쓰에이', 'youtube': "https://www.youtube.com/embed/p6XLNsJ9YrA?si=OS1IOlmwNbFAPRWK&amp;start=57"},
            {'year' : '2010', 'title': 'Way Back Home', 'music': '/static/audio/music_game/2010/Way Back Home.mp3', 'singer': '숀', 'youtube': "https://www.youtube.com/embed/amOSaNX7KJg?si=pc6BjT8myYcFTVSe&amp;start=57"},
            {'year' : '2010', 'title': '삐삐', 'music': '/static/audio/music_game/2010/삐삐.mp3', 'singer': '아이유', 'youtube': "https://www.youtube.com/embed/nM0xDI5R50E?si=9Zuh23iAuzUzvlgS&amp;start=47"},
            {'year' : '2010', 'title': '장난 아냐', 'music': '/static/audio/music_game/2010/장난 아냐.mp3', 'singer': '틴 탑', 'youtube': "https://www.youtube.com/embed/hHd_8iZFvK8?si=wEc954YEH5dKBdN2&amp;start=81"},
            {'year' : '2010', 'title': '좋니', 'music': '/static/audio/music_game/2010/좋니.mp3', 'singer': '윤종신', 'youtube': "https://www.youtube.com/embed/b1kQvZhQ6_M?si=H2MIEgNJyUbqvbgk&amp;start=66"},
            {'year' : '2010', 'title': '불타오르네', 'music': '/static/audio/music_game/2010/불타오르네.mp3', 'singer': '방탄소년단', 'youtube': "https://www.youtube.com/embed/ALj5MKjy2BU?si=lNR8y1TZ1eBd7A1B&amp;start=66"},
            {'year' : '2010', 'title': '내꺼 하자', 'music': '/static/audio/music_game/2010/내꺼 하자.mp3', 'singer': '인피니트', 'youtube': "https://www.youtube.com/embed/tqC8AmuZuLI?si=sDTXufvWM_A3Aiob&amp;start=50"},
            {'year' : '2010', 'title': '뿜뿜', 'music': '/static/audio/music_game/2010/뿜뿜.mp3', 'singer': '모모랜드', 'youtube': "https://www.youtube.com/embed/JQGRg8XBnB4?si=m8hVR4Oru8oHotDQ&amp;start=68"},
            {'year' : '2010', 'title': '나혼자', 'music': '/static/audio/music_game/2010/나혼자.mp3', 'singer': '씨스타', 'youtube': "https://www.youtube.com/embed/E0ZHXVp_wUE?si=3a9pBMtCj2zHT6YL&amp;start=66"},
            {'year' : '2010', 'title': 'cheer up', 'music': '/static/audio/music_game/2010/cheer up.mp3', 'singer': '트와이스', 'youtube': "https://www.youtube.com/embed/c7rCyll5AeY?si=PZ1Wiu1a1EdPO7lu&amp;start=67"},
            {'year' : '2010', 'title': '후유증', 'music': '/static/audio/music_game/2010/후유증.mp3', 'singer': '제국의 아이들', 'youtube': "https://www.youtube.com/embed/J6xPw2UWNQg?si=nH9dSpSMaPElorcf&amp;start=67"},
            {'year' : '2010', 'title': '썸띵', 'music': '/static/audio/music_game/2010/썸띵.mp3', 'singer': '걸스데이', 'youtube': "https://www.youtube.com/embed/JO7qQ7peKeM?si=i7gzRs_Hyevuu0Yg&amp;start=92"},
            {'year' : '2010', 'title': '벚꽃 엔딩', 'music': '/static/audio/music_game/2010/벚꽃 엔딩.mp3', 'singer': '버스커 버스커', 'youtube': "https://www.youtube.com/embed/tXV7dfvSefo?si=eZNRLxWkyOTUJGjt&amp;start=80"},
            {'year' : '2010', 'title': '200%', 'music': '/static/audio/music_game/2010/200%.mp3', 'singer': '악동뮤지션', 'youtube': "https://www.youtube.com/embed/0Oi8jDMvd_w?si=LL9In3GwPUM1FFo0&amp;start=56"},
            #2020
            {'year' : '2020', 'title': 'ETA', 'music': '/static/audio/music_game/2020/ETA.mp3', 'singer': '뉴진스', 'youtube':'https://www.youtube.com/embed/jOTfBlKSQYY?si=JTk8_6t8s4C2T1Ci&amp;start=70'},
            {'year' : '2020', 'title': '파이팅 해야지', 'music': '/static/audio/music_game/2020/파이팅 해야지.mp3', 'singer': '부석순', 'youtube':'https://www.youtube.com/embed/mBXBOLG06Wc?si=fyyjoqEu0yQL4O9H&amp;start=46'},
            {'year' : '2020', 'title': '사건의 지평선', 'music': '/static/audio/music_game/2020/사건의 지평선.mp3', 'singer': '윤하', 'youtube': 'https://www.youtube.com/embed/BBdC1rl5sKY?si=JUL3Fizzx7teDtvR&amp;start=95'},
            {'year' : '2020', 'title': 'Drama', 'music': '/static/audio/music_game/2020/Drama.mp3', 'singer': '에스파', 'youtube': 'https://www.youtube.com/embed/D8VEhcPeSlc?si=gCguu-inj3xt1w9L&amp;start=57'},
            {'year' : '2020', 'title': 'Not Shy', 'music': '/static/audio/music_game/2020/Not Shy.mp3', 'singer': '있지', 'youtube': 'https://www.youtube.com/embed/wTowEKjDGkU?si=wVwJgFY18rhP95q2&amp;start=81'},
            {'year' : '2020', 'title': '낙하', 'music': '/static/audio/music_game/2020/낙하.mp3', 'singer': '악동뮤지션', 'youtube': 'https://www.youtube.com/embed/EtiPbWzUY9o?si=dFZJr_u-0xzn8TMB&amp;start=51'},
            {'year' : '2020', 'title': '아무노래', 'music': '/static/audio/music_game/2020/아무노래.mp3', 'singer': '지코', 'youtube': "https://www.youtube.com/embed/UuV2BmJ1p_I?si=M9ogffzyMc1Fh0-A&amp;start=27"},
            {'year' : '2020', 'title': 'Rush Hour', 'music': '/static/audio/music_game/2020/Rush Hour.mp3', 'singer': '크러쉬', 'youtube': "https://www.youtube.com/embed/PS0qkO5qty0?si=PbHWneVDcmbBMPAU&amp;start=52"},
            {'year' : '2020', 'title': 'Step Back', 'music': '/static/audio/music_game/2020/Step Back.mp3', 'singer': '갓 더 비트', 'youtube': "https://www.youtube.com/embed/ZvUBMXuVP78?si=-J-7VvSidsouwlEe&amp;start=74"},
            {'year' : '2020', 'title': '봄여름가을겨울', 'music': '/static/audio/music_game/2020/봄여름가을겨울.mp3', 'singer': '빅뱅', 'youtube': "https://www.youtube.com/embed/eN5mG_yMDiM?si=IJweNI5mzELlJCek&amp;start=3"},
            {'year' : '2020', 'title': '시작', 'music': '/static/audio/music_game/2020/시작.mp3', 'singer': '가호', 'youtube': "https://www.youtube.com/embed/6LDg0YGYVw4?si=VYIUyjUkHmUuMIHI&amp;start=43"},
            {'year' : '2020', 'title': '음악의 신', 'music': '/static/audio/music_game/2020/음악의 신.mp3', 'singer': '세븐틴', 'youtube': "https://www.youtube.com/embed/zSQ48zyWZrY?si=-cJscmc9yb0TC-ps&amp;start=88"},
            {'year' : '2020', 'title': '헤어지자 말해요', 'music': '/static/audio/music_game/2020/헤어지자 말해요.mp3', 'singer': '박재정', 'youtube': "https://www.youtube.com/embed/yFlxYHjHYAw?si=4D50eTbHdJp6ZIMa&amp;start=88"},
            {'year' : '2020', 'title': 'CHRISTIAN', 'music': '/static/audio/music_game/2020/CHRISTIAN.mp3', 'singer': '지올팍', 'youtube': "https://www.youtube.com/embed/Dqlr8EDunCM?si=JuIXWL1osJGAZOzE&amp;start=50"},
            {'year' : '2020', 'title': 'Smoke', 'music': '/static/audio/music_game/2020/Smoke.mp3', 'singer': '다이나믹 듀오, 이영지', 'youtube': "https://www.youtube.com/embed/iuIzniSa1Hs?si=_vsxaf9BXTTuKr2i&amp;start=39"},
            {'year' : '2020', 'title': 'Seven', 'music': '/static/audio/music_game/2020/Seven.mp3', 'singer': '정국', 'youtube': "https://www.youtube.com/embed/1QYBiNRu1ok?si=hA1ddyu_sLWIt3bk&amp;start=45"},
            {'year' : '2020', 'title': 'Perfect Night', 'music': '/static/audio/music_game/2020/Perfect Night.mp3', 'singer': '르세라핌', 'youtube': "https://www.youtube.com/embed/oKBwWQI-IoI?si=qS09g9XhXV8Psj8O&amp;start=35"},
            {'year' : '2020', 'title': 'Get A Guitar', 'music': '/static/audio/music_game/2020/Get A Guitar.mp3', 'singer': '라이즈', 'youtube': "https://www.youtube.com/embed/iUw3LPM7OBU?si=fk2UGNqyS5GnS2HC&amp;start=18"},
            {'year' : '2020', 'title': '가나다라', 'music': '/static/audio/music_game/2020/가나다라.mp3', 'singer': '박재범(feat. 아이유)', 'youtube': "https://www.youtube.com/embed/gFb1TftvdoM?si=Momm89t24eUpwicX&amp;start=256"},
            {'year' : '2020', 'title': '사랑인가 봐', 'music': '/static/audio/music_game/2020/사랑인가 봐.mp3', 'singer': '멜로망스', 'youtube': "https://www.youtube.com/embed/UoBsiQW23IY?si=viuPtsQua3FzLvQs&amp;start=44"},
            {'year' : '2020', 'title': 'Baddie', 'music': '/static/audio/music_game/2020/Baddie.mp3', 'singer': '아이브', 'youtube': "https://www.youtube.com/embed/Da4P2uT4mVc?si=3b8MB8St_LNDiMT7&amp;start=57"},
            {'year' : '2020', 'title': '사랑은 늘 도망가', 'music': '/static/audio/music_game/2020/사랑은 늘 도망가.mp3', 'singer': '임영웅', 'youtube': "https://www.youtube.com/embed/LKQ-18LoFQk?si=YeHPIilLxok0wwlX&amp;start=58"},
            {'year' : '2020', 'title': 'Weekend', 'music': '/static/audio/music_game/2020/Weekend.mp3', 'singer': '태연', 'youtube': "https://www.youtube.com/embed/RmuL-BPFi2Q?si=ZIVVIx6F5iVz1q82&amp;start=65"},
            {'year' : '2020', 'title': 'ASAP', 'music': '/static/audio/music_game/2020/ASAP.mp3', 'singer': '스테이씨', 'youtube': "https://www.youtube.com/embed/NsY-9MCOIAQ?si=jBxu5VAd6Jw4kkza&amp;start=44"},
            {'year' : '2020', 'title': 'Vancouver', 'music': '/static/audio/music_game/2020/Vancouver.mp3', 'singer': 'BIG Naughty(서동현)', 'youtube': "https://www.youtube.com/embed/mev609MxcRE?si=uqKlhm4PEHDv913f&amp;start=59"},
            {'year' : '2020', 'title': '신호등', 'music': '/static/audio/music_game/2020/신호등.mp3', 'singer': '이무진', 'youtube': "https://www.youtube.com/embed/SK6Sm2Ki9tI?si=N_T3anxVtOxgRvC2&amp;start=79"},
            {'year' : '2020', 'title': 'Next Level', 'music': '/static/audio/music_game/2020/Next Level.mp3', 'singer': '에스파', 'youtube': "https://www.youtube.com/embed/4TWR90KJl84?si=qt5bTBoti6TBlWBu&amp;start=51"},
            {'year' : '2020', 'title': '다시 여기 바닷가', 'music': '/static/audio/music_game/2020/다시 여기 바닷가.mp3', 'singer': '싹쓰리', 'youtube': "https://www.youtube.com/embed/ESKfHHtiSjs?si=LHUV3yDMQ51TmP0Y&amp;start=86"},
            {'year' : '2020', 'title': '마리아', 'music': '/static/audio/music_game/2020/마리아.mp3', 'singer': '화사', 'youtube': "https://www.youtube.com/embed/tDukIfFzX18?si=MbiheaqO5cxE3ibo&amp;start=72"},
            {'year' : '2020', 'title': '에잇', 'music': '/static/audio/music_game/2020/에잇.mp3', 'singer': '아이유', 'youtube': "https://www.youtube.com/embed/TgOu00Mf3kI?si=UnDMTW8-xseaBP1d&amp;start=63"},
        ]
    
        for data in quiz_data_musicGames:
            if data['year'] == '2000':
                MusicGame_2000.objects.get_or_create(title=data['title'], music=data['music'], singer=data['singer'], youtube=data['youtube'])
            elif data['year'] == '2010':
                MusicGame_2010.objects.get_or_create(title=data['title'], music=data['music'], singer=data['singer'], youtube=data['youtube'])
            elif data['year'] == '2020':
                MusicGame_2020.objects.get_or_create(title=data['title'], music=data['music'], singer=data['singer'], youtube=data['youtube'])
    
        #무도 게임
        line_list = ['세브란스 병원엔 왜', '제발 가랑이 밑으로 들어가게 해주세요', '어 그래', '차씨 차씨 차씨 연예인을 대보자', '두 분은 연인이세요', '실례가 안 된다면 아이스크림 하나만 사주십시오', '해정발산기슭곰발냄새타령부인인사잘해',
                '700만 대추인들이 만든거야', '싸브레', '북쪽에 계신', '차이나타운은 온통 빡빡이야', '필승 Yes I can', '아우 장난치지말고 빨리 자장면 주세요!!', '아버지 나를낳으시고 바지적삼 다적시셨네',
                '늦었다고 생각할 때가 진짜 너무 늦었다', '입 닫고 빵이나 먹어', '장모 거세게 반데라스', '나온다 그랬더라 어떻게 됐더라', '바나나맛 우유 그만 먹으라고', '농약 안 쳤을 걸', '야 남자가 무슨 빨간 머리냐', '날 동정하지 마세요', '나 이런 게 무서워하네', 
                '하모예 와이러는데 이카는데', '우리 할아버진 할머니가 두 분이셨어', '형보다 잘할걸', '무야호', '건방지게 끼어들었네요', '십 년이 지났다 주나야 년 뭐했냐', '인생을 판 사람을 어떻게 이겨요', '나 이제 그만할 건데', '스프', '술 마시고 뭘 타는지 보라고',
                '치열하겠는데', '민서를 올바르게 키울 생각이 없다', '면일어나지 못했더라면', '특별히 공부도 못하고 대가리만 큰 사람', '아픈척해서 인기 끌려고 그러시는 거죠', '아유... 하기싫어...', '내가 뭣땜에 대체 뭘 위해서']
        for i in range(len(line_list)):
            Mudo.objects.get_or_create(line=line_list[i])
            mudo = Mudo.objects.get(line=line_list[i])
            mudo.image_path = f"/static/image/mudo/{mudo.line}.jpg"
            mudo.save()

        #영화 게임
        quiz_data_movieGames = [
            {'title': '1987', 'scene': '/static/image/movie_game/1987.png', 'line': '책상을 탁 치니 억 하고 쓰러졌답니다'},
            {'title': '관상', 'scene': '/static/image/movie_game/관상.png', 'line': '어찌 내가 왕이 될 상인가?'},
            {'title': '극한직업', 'scene': '/static/image/movie_game/극한직업.png', 'line': '지금까지 이런 맛은 없었다. 이것은 갈비인가 통닭인가. 예~ 수원왕갈비통닭입니다.'},
            {'title': '기생충', 'scene': '/static/image/movie_game/기생충.png', 'line': '제시카 외동딸 일리노이 시카고 과 선배는 김진모 그는 네 사촌'},
            {'title': '달콤한인생', 'scene': '/static/image/movie_game/달콤한인생.png', 'line': '넌 나에게 모욕감을 줬어'},
            {'title': '말죽거리잔혹사', 'scene': '/static/image/movie_game/말죽거리잔혹사.png', 'line': '니가 그렇게 싸움을 잘해?'},
            {'title': '범죄도시', 'scene': '/static/image/movie_game/범죄도시.png', 'line': '어 아직 싱글이야'},
            {'title': '범죄와의전쟁', 'scene': '/static/image/movie_game/범죄와의전쟁.png', 'line': '느그 서장 남천동 살제? 내가 임마! 느그 서장이랑 임마!'},
            {'title': '암살', 'scene': '/static/image/movie_game/암살.png', 'line': '내 몸 속에 일본놈들의 총알이 여섯개나 박혀 있습니다'},
            {'title': '더글로리', 'scene': '/static/image/movie_game/더글로리.png', 'line': '화이팅 박연진! 브라보! 멋지다 연진아~'},
            {'title': '타짜', 'scene': '/static/image/movie_game/타짜.png', 'line': '싸늘하다 가슴에 비수가 날아와 꽂힌다'},
            {'title': '살인의 추억', 'scene': '/static/image/movie_game/살인의 추억.png', 'line': '밥은 먹고 다니냐?'},
            {'title': '어게인 마이 라이프', 'scene': '/static/image/movie_game/어게인 마이 라이프.png', 'line': '진행시켜'},
            {'title': '천국의 계단', 'scene': '/static/image/movie_game/천국의 계단.png', 'line': '사랑은, 돌아오는 거야!'},
            {'title': '야인시대', 'scene': '/static/image/movie_game/야인시대.png', 'line': '내가, 내가 고자라니!'},
            {'title': '상속자들', 'scene': '/static/image/movie_game/상속자들.png', 'line': '나, 너 좋아하냐?'},
            {'title': '친구', 'scene': '/static/image/movie_game/친구.png', 'line': '아부지 뭐하시노'},
            {'title': '박하사탕', 'scene': '/static/image/movie_game/박하사탕.png', 'line': '나 다시 돌아갈래~'},
            {'title': '내 머리속의 지우개', 'scene': '/static/image/movie_game/내 머리속의 지우개.png', 'line': '이거 마시면 나랑 사귀는 거다'},
            {'title': '말아톤', 'scene': '/static/image/movie_game/말아톤.png', 'line': '초원이 다리는 백만 불 짜리 다리'},
            {'title': '타짜2', 'scene': '/static/image/movie_game/타짜2.png', 'line': '쏠 수 있어!'},
            {'title': '부부의 세계', 'scene': '/static/image/movie_game/부부의세계.png', 'line': '사랑에 빠진 게 죄는 아니잖아!'},
            {'title': '아이리스', 'scene': '/static/image/movie_game/아이리스.png', 'line': '아악 안돼'},
            {'title': '신세계', 'scene': '/static/image/movie_game/신세계.png', 'line': '드루와, 드루와!'},
            {'title': '추격자', 'scene': '/static/image/movie_game/추격자.png', 'line': '야 4885, 너지?'},
            {'title': '파리의 연인', 'scene': '/static/image/movie_game/파리의 연인.png', 'line': '말을 못 해, 저 남자가 내 사람이다. 저 남자가 내 애인이다 왜 말을 못 하냐고!'},
            {'title': '오로라 공주', 'scene': '/static/image/movie_game/오로라 공주.png', 'line': '암세포도 생명이잖아요'},
            {'title': '베테랑', 'scene': '/static/image/movie_game/베테랑.png', 'line': '어이가 없네?'},
            {'title': '엽기적인 그녀', 'scene': '/static/image/movie_game/엽기적인 그녀.png', 'line': '견우야, 미안해! 나도 어쩔 수 없는 여자인가봐'},
            {'title': '내부자들', 'scene': '/static/image/movie_game/내부자들.png', 'line': '모히또 가가지고 몰디브나 한 잔 할라니까'},
            {'title': '곡성', 'scene': '/static/image/movie_game/곡성.png', 'line': '뭣이 중헌디'},
            {'title': '오징어 게임', 'scene': '/static/image/movie_game/오징어 게임.png', 'line': '하, 씨발⋯ 기훈이형!'},
            {'title': '아저씨', 'scene': '/static/image/movie_game/아저씨.png', 'line': '아직 한 발 남았다'},
            {'title': '지붕뚫고 하이킥', 'scene': '/static/image/movie_game/지붕뚫고 하이킥.png', 'line': '이 빵꾸똥꾸야!'},
            {'title': '올드보이', 'scene': '/static/image/movie_game/올드보이.png', 'line': '누구냐, 넌'},
            {'title': '모래시계', 'scene': '/static/image/movie_game/모래시계.png', 'line': '이렇게 하면 널 가질 수 있을 거라 생각했어'},
            {'title': '아저씨', 'scene': '/static/image/movie_game/아저씨2.png', 'line': '나 전당포 한다, 금이빨은 받아. 금이빨 빼고 모조리 씹어먹어줄게'},
            {'title': '친구', 'scene': '/static/image/movie_game/친구2.png', 'line': '니가 가라 하와이'},
            {'title': '신세계', 'scene': '/static/image/movie_game/신세계2.png', 'line': '이러면 완전히 나가린데..'},
            {'title': '친구', 'scene': '/static/image/movie_game/친구3.png', 'line': '마이 무따 아이가, 고마 해라'},
            {'title': '최고의 사랑', 'scene': '/static/image/movie_game/최고의 사랑.png', 'line': '극뽁~'},
            {'title': '태조 왕건', 'scene': '/static/image/movie_game/태조 왕건.png', 'line': '누구인가? 누가 기침소리를 내었는가?'},
            {'title': '부당거래', 'scene': '/static/image/movie_game/부당거래.png', 'line': '호의가 계속 되면, 그게 권리인 줄 알아요'},
            {'title': '봄날은 간다', 'scene': '/static/image/movie_game/봄날은 간다.png', 'line': '어떻게 사랑이 변하니...'},
            {'title': '달콤한 인생', 'scene': '/static/image/movie_game/달콤한 인생2.png', 'line': '말해봐요, 나한테 왜 그랬어요?'},
            {'title': '말죽거리 잔혹사', 'scene': '/static/image/movie_game/말죽거리 잔혹사2.png', 'line': '현수야, 이것 좀 만져 봐'},
            {'title': '내부자들', 'scene': '/static/image/movie_game/내부자들2.png', 'line': '어짜피 대중들은 개 돼지입니다'},
            {'title': '다모', 'scene': '/static/image/movie_game/다모.png', 'line': '아프냐, 나도 아프다'},
            {'title': '청년경찰', 'scene': '/static/image/movie_game/청년경찰.png', 'line': '야 내가 소고기 사줄게'},
            {'title': '사랑했나봐', 'scene': '/static/image/movie_game/사랑했나봐.png', 'line': '예나... 선정이 딸이에요'},
        ]

        for data in quiz_data_movieGames:
            MovieGame.objects.get_or_create(title=data['title'], scene=data['scene'], line=data['line'])
        
        #철가방 게임
        name_list_lookInside = [
            '목장갑','고무장갑','컵','텀블러','마우스','키보드','휴지','물티슈','가습기','베개','이불','빨래건조대','스탠드','젓가락','숟가락','전자레인지','가스레인지','부탄가스','책상','의자','연필','지우개','볼펜','노트북','핸드폰','지갑','토스트기','후라이팬','냄비','접시'
            ]
        for i in range(len(name_list_lookInside)):
            LookInside.objects.get_or_create(name=name_list_lookInside[i])
            lookInside = LookInside.objects.get(name=name_list_lookInside[i])
            lookInside.image_path = f"/static/image/lookInside/{lookInside.name}.jpg"
            lookInside.save()
