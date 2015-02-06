from django.shortcuts import render, render_to_response, redirect
from django.http import *

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf

from django.db.models import Count

from navbar.models import Title, MenuList, MenuListForNonmembers
from account.models import MyUser, AccountSettingsMenuList
from navbar.forms import LoginForm



# login과 logout을 둘 다 지원하는 내비게이션 바 (메인 페이지에서 쓰임)
class Navbar:

	# 홈페이지 왼쪽 상단에 쓰이는 title
	try:
		title = Title.objects.get(num=0)
	except:
		title = "Slegizzagi"

	# menu 리스트
	menu_list = MenuList.objects.annotate(Count('menu'))\
						.order_by('display_ord')
	menu_list_for_nonmembers = MenuListForNonmembers.objects.annotate(Count('menu'))\
													.order_by('display_ord')
	
	# main 페이지의 경로
	base_path = "http://54.169.79.59/sle/"

	# 함수를 사용하여 값을 재설정할 변수들
	user = ""
	nickname = ""
	request = ""

	# login과 관련된 변수들
	login_form = LoginForm() # navbar.forms의 LoginForm
	error_state = None

	# (navbar instance).request를 view에서 받는 request와 동일하게 초기 설정
	def __init__(self, request):
		self.request = request

	# 현재 웹페이지의 경로를 가져옴
	def get_current_path(self):
		self.current_path = self.request.path

	# 현재 유저 정보를 받아서 nickname을 설정
	def user_setting(self):
		self.user = self.request.user
		if self.user is not None:
			if self.user.is_authenticated():
				# 유저로 등록되어 있을 시, 데이터베이스에 저장된 닉네임을 가져옴
				self.nickname = self.user.myuser.nickname
			else:
				# 유저로 등록되어 있지 않을 시, guest로 닉네임 설정
				self.nickname = "guest"

	# 로그인을 위한 함수
	def user_login(self):
		# form에 정보를 입력
		self.login_form = LoginForm(self.request.POST)
		# form이 유효한지 확인
		if self.login_form.is_valid():
			# form이 유효하면 입력된 아이디와 패스워드를 가져옴
			user_id = self.login_form.cleaned_data['user_id']
			user_password = self.login_form.cleaned_data['user_password']
			# 입력된 아이디와 패스워드를 사용하여 인증 여부 확인
			self.user = authenticate(username=user_id, password=user_password)
			# 인증되는 계정이 존재하면 로그인하고 메인화면으로 리디렉트
			if self.user is not None:
				login(self.request, self.user)
				return HttpResponseRedirect('/sle')
			else:
				# 인증되는 계정이 없으면 에러 메세지를 띄움
				self.error_state = "wrong_id_or_password"
		else:
			# form이 유효하지 않으면 에러 메세지를 띄움
			self.error_state = "forms_not_filled"

	# 로그아웃을 위한 함수
	def user_logout(self):
		logout(self.request) # 로그아웃
		return HttpResponseRedirect('/sle') # 메인화면으로 리디렉트

	# navbar에서 사용된 컨텍스트 딕셔너리
	def context_dict(self):
		context_dict = {
			'title': self.title,
			'menu_list': self.menu_list,
			'menu_list_for_nonmembers': self.menu_list_for_nonmembers,
			'user': self.user,
			'nickname': self.nickname,
			'login_form': self.login_form,
			'error_state': self.error_state,
			'current_path': self.current_path,
			'base_path': self.base_path,
		}
		return context_dict # 딕셔너리 형태로 리턴



# 로그아웃만 지원하는 내비게이션 바
class NavbarForMembers:

	# 홈페이지 왼쪽 상단에 쓰이는 title
	try:
		title = Title.objects.get(num=0)
	except:
		title = "Slegizzagi"

	# menu 리스트
	menu_list = MenuList.objects.annotate(Count('menu'))\
						.order_by('display_ord')
	
	# main 페이지의 경로
	base_path = "http://54.169.79.59/sle/"

	# 함수를 사용하여 값을 재설정할 변수들
	user = ""
	nickname = ""
	request = ""

	# (navbar instance).request를 view에서 받는 request와 동일하게 초기 설정
	def __init__(self, request):
		self.request = request

	# 현재 웹페이지의 경로를 가져옴
	def get_current_path(self):
		self.current_path = self.request.path

	# 현재 유저 정보를 받아서 nickname을 설정
	def user_setting(self):
		self.user = self.request.user
		if self.user is not None:
			if self.user.is_authenticated():
				# 유저로 등록되어 있을 시, 데이터베이스에 저장된 닉네임을 가져옴
				self.nickname = self.user.myuser.nickname
			else:
				# 유저로 등록되어 있지 않을 시, guest로 닉네임 설정
				self.nickname = "guest"

	# 로그아웃을 위한 함수
	def user_logout(self):
		logout(self.request) # 로그아웃
		return HttpResponseRedirect('/sle') # 메인화면으로 리디렉트

	# navbar에서 사용된 컨텍스트 딕셔너리
	def context_dict(self):
		context_dict = {
			'title': self.title,
			'menu_list': self.menu_list,
			'user': self.user,
			'nickname': self.nickname,
			'current_path': self.current_path,
			'base_path': self.base_path,
		}
		return context_dict # 딕셔너리 형태로 리턴

	# def call_main_nav(self):
	# 	self.get_current_path()
	# 	self.user_setting()

	# 	context_dict={}
	# 	context_dict.update(self.context_dict())
	# 	return context_dict



# Account 메뉴를 위한 내비게이션 바
class NavbarForAccount:

	# 홈페이지 왼쪽 상단에 쓰이는 title
	try:
		title = Title.objects.get(num=0)
	except:
		title = "Slegizzagi"

	# menu 리스트
	menu_list = MenuList.objects.annotate(Count('menu'))\
						.order_by('display_ord')
	
	# main 페이지의 경로
	base_path = "http://54.169.79.59/sle/"

	# account 메뉴 관련 변수들
	account_menu_list = AccountSettingsMenuList.objects.annotate(Count('menu'))\
											.order_by('display_ord') # account 메뉴의 서브메뉴 리스트
	account_base_path = "http://54.169.79.59/sle/account/" # account 메뉴의 경로

	# 함수를 사용하여 값을 재설정할 변수들
	user = ""
	nickname = ""
	request = ""

	# (navbar instance).request를 view에서 받는 request와 동일하게 초기 설정
	def __init__(self, request):
		self.request = request

	# 현재 웹페이지의 경로를 가져옴
	def get_current_path(self):
		self.current_path = self.request.path

	# 현재 유저 정보를 받아서 nickname을 설정
	def user_setting(self):
		self.user = self.request.user
		if self.user is not None:
			if self.user.is_authenticated():
				# 유저로 등록되어 있을 시, 데이터베이스에 저장된 닉네임을 가져옴
				self.nickname = self.user.myuser.nickname
			else:
				# 유저로 등록되어 있지 않을 시, guest로 닉네임 설정
				self.nickname = "guest"

	# 로그아웃을 위한 함수
	def user_logout(self):
		logout(self.request) # 로그아웃
		return HttpResponseRedirect('/sle') # 메인화면으로 리디렉트

	# navbar에서 사용된 컨텍스트 딕셔너리
	def context_dict(self):
		context_dict = {
			'title': self.title,
			'menu_list': self.menu_list,
			'user': self.user,
			'nickname': self.nickname,
			'current_path': self.current_path,
			'base_path': self.base_path,
			'account_menu_list': self.account_menu_list,
			'account_base_path': self.account_base_path,
		}
		return context_dict # 딕셔너리 형태로 리턴