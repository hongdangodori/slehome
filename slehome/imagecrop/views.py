from django.shortcuts import render
from PIL import Image
import random
import os,sys
from django.http import HttpResponse
from account.models import MemberIntro, PhotoLink
# Create your views here.

def test_jcrop(request):
	if request.method =="POST":
		x=int(request.POST["x1"])
		y=int(request.POST["y1"])
		w=int(request.POST["w"])
		h=int(request.POST["h"])
		image_path=request.POST["image_path"]
		im=Image.open("/home/sle"+image_path)
		width, height = im.size

		x=x*width//566
		y=y*width//566
		w=w*width//566
		h=h*width//566
		# rew=0
		# reh=0
		# if width > height:
		# 	rew=500
		# 	reh=500*height//width
		# else:
		# 	reh=500
		# 	rew=500*width//height

		# new_im=im.resize((rew,reh))
		# im.close()
		# new_im.save('%s/%s' % (UPLOAD_DIR, dummy_name),format="jpeg")

		croped_im=im.crop((x,y,x+w,y+h))
		croped_im.save("/home/sle"+image_path,format="jpeg")
		l=image_path.split('/')
		account_user=request.user
		photo_link=account_user.memberintro.photolink
		if len(photo_link.file_name) > 0:
			if os.path.isfile("/home/sle"+photo_link.upload_path+photo_link.file_name):
				os.remove("/home/sle"+photo_link.upload_path+photo_link.file_name)
		photo_link.file_name=l[3]
		photo_link.upload_path='/'+l[1]+'/'+l[2]+'/'
		photo_link.save()

		c={"alert":"프로필 사진이 업로드 되었습니다.","location":"/sle/account/edit_introduction/"}
		return render(request,"wiki/alert.html",c)
	else:
		c={}
		return render(request,"mkprofile/jcropTest.html",c)



def upload_profile_image(request):
	page_name=""
	c = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'	#파일 업로드시 필요한 임의의 문자열을 제공하기 위한 string
	if request.method == 'POST':	#post가 있을 경우
		member_intro=request.user.memberintro
		photo_link=member_intro.photolink
		dummy_name =''
		is_exist = True
		while is_exist == True:	#파일 이름을 임의의 문자열로 만드는데 동일한 이름의 파일이 있을 경우 다른 랜덤한 문자열을 만듬
			dummy_name=''.join(random.sample(c,10))
			f=PhotoLink.objects.filter(file_name=dummy_name)
			if len(f) == 0 :
				is_exist = False

		UPLOAD_DIR = '/home/sle/media/member'
		if 'file' in request.FILES:	#post로 받은 파일이 있을 경우 이름과 파일을 받음
			file = request.FILES['file']
			file_name = file._name
			if file.size < 2000000:
				l=file_name.split('.')
				dummy_name=dummy_name+'.'+l[len(l)-1]
				fp = open('%s/%s' % (UPLOAD_DIR, dummy_name) , 'wb')	#파일을 저장
				for chunk in file.chunks():
					fp.write(chunk)
				fp.close()

				# while os.path.isfile('%s/%s' % (UPLOAD_DIR, dummy_name)) == False:
				# 	pass
				# im=Image.open('%s/%s' % (UPLOAD_DIR, dummy_name))
				# width, height = im.size
				# rew=0
				# reh=0
				# if width > height:
				# 	rew=500
				# 	reh=500*height//width
				# else:
				# 	reh=500
				# 	rew=500*width//height

				# new_im=im.resize((rew,reh))
				# im.close()
				# new_im.save('%s/%s' % (UPLOAD_DIR, dummy_name),format="jpeg")


				
				# photo_link.file_name=dummy_name
				# photo_link.upload_path=UPLOAD_DIR
				# photo_link.save()

				return HttpResponse("/media/member/"+dummy_name) #파일을 올리고 이전 페이지로 이동
			else:
				return HttpResponse("파일의 크기는 2Mb를 넘을 수 없습니다.") #파일을 올리고 이전 페이지로 이동
	else: #파일 업로드 실패시
		c={'alert':'파일 업로드가 실패했습니다.','location':'/sle/wiki/page/'+page_name}
		return render(request,"mkprofile/dragUploadTest.html",c)


def del_photo(request):
	if request.method =="POST":
		path=request.POST["photo_name"]
		if len(path) > 0:
			if os.path.isfile("/home/sle"+path):
				os.remove("/home/sle"+path)
				return HttpResponse("success")

		return HttpResponse("success")
