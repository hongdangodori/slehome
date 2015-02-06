from instagram.client import InstagramAPI # instagram을 사용하기 위한 module 차후에 옮길 예정

from photo.models import Photos, PhotoComments

from datetime import timedelta, datetime

class Instagram :

	api = InstagramAPI(client_id='1118900683bb413993f5e374ac9ea021', client_secret='d20ea751a7be44adb41ac19d3ad6b42c')		# instagram api
	user_id = '1663516127'		# instagram 아이디
	media = []		# 미디어 담을 리스트
	timestamp = datetime.now()		# 갱신시간 타임스탬프
	second_delay = 3600		# 갱신 딜레이

	def getMedia() :		# 사진들 인스타그램에서 불러오기
		recent_media, _next = Instagram.api.user_recent_media(user_id=Instagram.user_id, count=50)		# 최대 50개 미디어 불러오기
		while _next :		# 50 개 다음 미디어가 있으면 계속 불러오기
			more_media, _next = Instagram.api.user_recent_media(with_next_url=_next)		# 다음 주소
			recent_media.extend(more_media)		# 미디어 추가하기

		return recent_media

	def renewMedia() :		# 미디어 갱신하기
		if len(Instagram.media) == 0 or Photos.objects.all().count() == 0 :		# 미디어가 아예 없으면 미디어 받기
			Instagram.media = Instagram.getMedia()
			Instagram.setDB()

		elif (datetime.now() - Instagram.timestamp).seconds >= Instagram.second_delay :		# 최근 들어온 시간과 최근 갱신 된 시간의 차와 갱신시간을 비교
			Instagram.timestamp = datetime.now()		# 갱신 된 시간 변경

			recent_media, _next = Instagram.api.user_recent_media(user_id=Instagram.user_id, count=1)		# 미디어 하나 불러오기
			if len(Photos.objects.filter(link=recent_media[0].images['standard_resolution'].url)) < 1 :		# 최근 미디어와 같은지 비교
				Instagram.media = Instagram.getMedia()		# 다르면 미디어 갱신하기
				Instagram.setDB()

	def getData() :
		Instagram.renewMedia()
		return [{'photo':m.images['standard_resolution'].url, 'pub_date':m.created_time + timedelta(hours=8)} for m in Instagram.media]

	def setDB() :
		for m in Instagram.media :
			if len(Photos.objects.filter(link=m.images['standard_resolution'].url)) < 1 :
				photo = Photos(link=m.images['standard_resolution'].url, pub_date=m.created_time + timedelta(hours=8))
				photo.save()