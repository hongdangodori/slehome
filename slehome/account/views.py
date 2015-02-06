# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.http import *

from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from navbar.shared import Navbar, NavbarForAccount

from django.contrib.auth.models import User
from account.models import MyUser, BasicMemberInformation, MemberIntro, Stat

from django import forms
from account.forms import UserRegisterForm, MyUserRegisterForm, BasicMemberInformationRegisterForm
from account.forms import ChangePasswordForm
from account.forms import AccountSettingsUserForm, AccountSettingsMyUserForm, CheckPasswordForm
from account.forms import MemberIntroForm

import json
import simplejson
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist



# 가입화면의 첫 페이지 (슬기짜기 회원 인증 페이지)
def register_index(request):
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'login' in request.POST:
			navbar.user_login()
			navbar.user_setting()
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###############################################################

	# 기본 정보 입력 폼을 데이터 미입력 상태로 가져옴
	basic_member_information_register_form = BasicMemberInformationRegisterForm()
	gave_auth_key = None
	member_exists = None
	next_page = False
	message = ''
	stu_num = ''

	if request.method == "POST":
		if 'validate' in request.POST: # validate 버튼을 누르면
			data = request.POST # post 형태로 받아온 데이터를 data에 저장
			register_form = BasicMemberInformationRegisterForm(data) # 폼에 data를 입력한 상태로 불러옴
			if register_form.is_valid(): # 폼이 유효하면
				# 가입 신청자가 authorization key를 인증했는지 확인
				gave_auth_key = register_form.gave_auth_key(data)
				# 가입 신청자가 BasicMemberInformation 테이블에 존재하는지 확인하고, 존재한다면 그 데이터를 리턴
				member = register_form.get_member(gave_auth_key, data)
				if member == None:
					message = "No matching member in the Slegizzagi"
				else:
					# auth key 입력 여부와 멤버 인증 여부를 해당 멤버 row에 저장
					register_form.member_validation_update(gave_auth_key, member)
					next_page = True # 다음 페이지로 갈 수 있음
					stu_num = str(member.stu_num) # 인증한 멤버의 학번을 저장
			else:
				message = "Check your answers again"
				# state = register_form.errors

	context_dict = {
		'stu_num': stu_num,
		'next_page': next_page,
		'message': message,
		'basic_member_information_register_form': basic_member_information_register_form,
	}
	context_dict.update(navbar.context_dict())

	url = "account/register_index.html"

	return render(request, url, context_dict)



# 실제 가입 페이지
def register_real(request, stu_num):
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'login' in request.POST:
			navbar.user_login()
			navbar.user_setting()
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###############################################################

	message = ""
	user_register_form = ""
	my_user_register_form = ""
	error_dict = ""
	warning = ""

	# url의 숫자를 학번으로 받아와서, 해당 학번을 가진 멤버가 BasicMemberInformation 테이블에 존재하는지 확인
	try:
		member = BasicMemberInformation.objects.get(stu_num=stu_num)
		# 해당 학번을 가진 멤버가 인증 과정을 거쳤는지 확인
		if member.completed_validation:
			# 해당 학번을 가진 멤버가 계정을 생성하지 않은 상태라면, 계정 생성 페이지를 띄움
			if not member.generated_account:
				url = "account/register_real.html"
				# User 모델과 관련된 가입 폼을 데이터 미입력 상태로 가져옴
				user_register_form = UserRegisterForm()
				# MyUser 모델과 관련된 가입 폼을, 이름과 학번을 변경할 수 없는 초기값으로 설정한 상태에서 생성
				my_user_register_form = MyUserRegisterForm(initial={'fullname': member.fullname, 'stu_num': member.stu_num})

				if request.method == "POST": # 유저가 계정 생성 버튼을 눌렀다면
					if 'create_account' in request.POST:
						data = request.POST.copy() # POST 형태로 받아온 데이터를 복사
						# 데이터에 이름과 학번을 초기값으로 설정
						data['fullname'] = member.fullname
						data['stu_num'] = member.stu_num
						# 가입 폼에 데이터를 입력한 상태로 불러옴
						user_register_form = UserRegisterForm(data)
						my_user_register_form = MyUserRegisterForm(data)
						if user_register_form.is_valid() and my_user_register_form.is_valid(): # 두 폼이 모두 유효하면
							# 유저 생성
							user_instance = user_register_form.save(commit=True) # User 테이블의 row 생성하고 저장
							my_user_instance = my_user_register_form.save(commit=False) # MyUser 테이블의 row 생성
							my_user_instance.user = user_instance # 생성된 MyUser 테이블의 row를 저장된 User 테이블의 row와 이어 줌
							my_user_instance.save() # MyUser 테이블의 row 저장
							# 학번과 인증 키 입력 여부를 받아옴
							sent_stu_num = member.stu_num
							gave_auth_key = member.gave_auth_key
							user_register_form.is_active_update(gave_auth_key, sent_stu_num) # 해당 멤버 계정의 active 여부를 결정
							# 해당 멤버가 계정을 생성했음을 저장
							member.generated_account = True
							member.save()
							return HttpResponseRedirect("/sle/") # 메인 화면으로 리디렉트
						else: # 폼에 에러가 존재하면
							# 폼의 에러를 딕셔너리 형태로 가져옴
							error_dict = user_register_form.errors.as_data()
							error_dict.update(my_user_register_form.errors.as_data())
							# 에러 메시지 설정
							""" ***** 에러 메시지를 세분화해야 함 ***** """
							warning = "▲ Error occurred"
			# 해당 학번의 멤버가 이미 계정을 생성한 상태라면
			else:
				url = "account/register_prohibit.html"
				message = "You have already created an account."
		# url에 입력된 숫자를 학번으로 가진 멤버가 존재하지만 인증을 완료하지 않았다면
		else:
			url = "account/register_prohibit.html"
			message = "You haven't yet completed account validation."
	# url에 입력된 숫자를 학번으로 가진 멤버가 없을 시, 잘못된 접근이라는 메시지를 띄움
	except (BasicMemberInformation.DoesNotExist):
		url = "account/register_prohibit.html"
		message = "Invalid Approach"

	context_dict = {
		'message': message,
		'user_register_form': user_register_form,
		'my_user_register_form': my_user_register_form,
		"error_dict": error_dict,
		'warning': warning,
	}

	context_dict.update(navbar.context_dict())

	return render(request, url, context_dict)



# 계정 설정 메뉴의 첫 화면
@login_required
def account_index(request):
	navbar = NavbarForAccount(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###############################################################
	context_dict = {}
	url = "account/account_index.html"
	###############################################################

	context_dict.update(navbar.context_dict())
	
	return render(request, url, context_dict)



# 계정 설정 변경 화면
@login_required
def account_settings(request):
	navbar = NavbarForAccount(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###############################################################
	# 현재 유저 정보를 가져옴
	account_user = request.user
	# 현재 데이터베이스에 저장된 값들을 초기값으로 설정
	user_initial = {'email': account_user.email}
	my_user_initial = {
		'nickname': account_user.myuser.nickname,
		'birthday': account_user.myuser.birthday,
		'phone_num': account_user.myuser.phone_num,
	}

	# 폼에 초기값을 입력한 상태로 불러옴
	account_settings_user_form = AccountSettingsUserForm(initial=user_initial)
	account_settings_my_user_form = AccountSettingsMyUserForm(initial=my_user_initial)
	# 패스워드 확인 폼을 데이터 미입력 상태로 불러옴
	check_password_form = CheckPasswordForm()

	# 사용될 변수 목록
	warning = ""
	successfully_changed = False
	error_dict = {}

	if request.method == "POST":
		if 'change_account_settings' in request.POST: # 계정 설정 변경 버튼을 눌렀으면
			data = request.POST.copy()
			# 현재 유저 인스턴스와 연결하여, 입력한 데이터를 포함한 폼을 불러옴
			account_settings_user_form = AccountSettingsUserForm(data, initial=user_initial, instance=account_user)
			account_settings_my_user_form = AccountSettingsMyUserForm(data, initial=my_user_initial, instance=account_user.myuser)
			check_password_form = CheckPasswordForm(data)
			# 폼에 유저가 입력한 내용이 초기값과 다르면 (data와 user_initial 혹은 my_user_initial이 다르면)
			if account_settings_user_form.has_changed() or account_settings_my_user_form.has_changed():
				# 폼 세 개가 모두 유효하면
				if (account_settings_my_user_form.is_valid()) and account_settings_user_form.is_valid() and check_password_form.is_valid():
					if check_password_form.check_password(account_user): # 유저가 입력한 것이 현재 패스워드가 맞으면
						# 폼에 입력한 내용들을 현재 유저 인스턴스의 데이터베이스에 저장
						account_settings_user_form.save()
						account_settings_my_user_form.save()
						# 변경 여부를 참으로 바꿈
						successfully_changed = True
						navbar.user_setting() # navbar에 표시되는 유저 이름을 재설정
					# 패스워드가 틀리면
					else:
						error_dict.update(check_password_form.errors.as_data())
						warning = "▲ Wrong password"
				# 폼에 에러가 존재하면
				else:
					# 폼의 에러를 딕셔너리 형태로 가져옴
					error_dict.update(account_settings_user_form.errors.as_data())
					error_dict.update(account_settings_my_user_form.errors.as_data())
					error_dict.update(check_password_form.errors.as_data())
					# 에러 메시지 설정
					""" ***** 에러 메시지를 세분화해야 함 ***** """
					warning = "▲ Error occurred"
			# 폼에 입력된 내용에 변화가 없으면
			else:
				warning = "No Change Detected"

	context_dict = {
		'account_settings_user_form': account_settings_user_form,
		'account_settings_my_user_form': account_settings_my_user_form,
		'check_password_form': check_password_form,
		'warning': warning,
		'successfully_changed': successfully_changed,
		'error_dict': error_dict,
	}
	url = "account/account_account_settings.html"
	###############################################################

	context_dict.update(navbar.context_dict())
	
	return render(request, url, context_dict)



# 패스워드 변경 화면
@login_required
def change_password(request):
	navbar = NavbarForAccount(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###############################################################
	password_change_form = ChangePasswordForm() # 패스워드 변경 폼을 데이터 미입력 상태로 불러옴
	account_user = request.user # 현재 유저
	warning = ""

	if request.method == "POST":
		if 'password_change' in request.POST: # 패스워드 변경 버튼을 눌렀으면
			data = request.POST
			password_change_form = ChangePasswordForm(data) # 패스워드 변경 폼에 입력한 데이터를 넣어 불러옴
			if password_change_form.is_valid(): # 폼이 유효하면
				# 유저가 입력한 것이 현재 패스워드가 맞는지 확인
				right_password = password_change_form.check_current_password(account_user)
				if right_password: # 현재 패스워드가 맞으면
					# 새 패스워드의 입력과 재입력이 일치하는지 확인
					password_match = password_change_form.check_password_match()
					if password_match:# 두 패스워드가 일치하면
						password_change_form.change_password(account_user) # 패스워드 변경
						return HttpResponseRedirect("/sle/") # 메인 페이지로 리디렉트
					# 두 패스워드가 일치하지 않으면
					else:
						warning = "New passwords do not match"
				# 현재 패스워드가 틀리면
				else:
					warning = "Wrong password"
			# 폼이 유효하지 않으면
			else:
				warning = "Empty form(s)"

	context_dict = {
		'password_change_form': password_change_form,
		'warning': warning,
	}
	url = "account/account_change_password.html"
	###############################################################

	context_dict.update(navbar.context_dict())
	
	return render(request, url, context_dict)



# 자기소개 설정 페이지
@login_required
def edit_introduction(request):
	navbar = NavbarForAccount(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###############################################################
	account_user = request.user

	# 현재 데이터베이스에 저장된 intro를 초기값으로 설정
	try:
		member_intro_initial = {'intro': account_user.memberintro.intro}
	# 저장된 intro가 없으면 빈 intro를 생성하고 초기값으로 설정
	except:
		MemberIntro.objects.create(user=account_user, intro="")
		member_intro_initial = {'intro': ""}

	# 자기소개 form 불러오기
	member_intro_form = MemberIntroForm(initial=member_intro_initial)

	# 저장된 스탯이 있으면 정렬해서 쿼리셋 형태로 불러옴
	try:
		stat_queryset = account_user.memberintro.stat_set.all() # order_by('-stat_value', 'stat_name')
	# 저장된 스텟이 없으면 빈 리스트 생성
	except:
		stat_queryset = []

	stat_list = [] # 스탯 리스트 초기화

	num = 0 # 인덱스로 쓰임
	# 쿼리셋에 element가 존재하면
	if len(stat_queryset) > 0:
		for stat in stat_queryset:
			# 인덱스와 스탯 정보를 리스트에 저장
			stat_list.append({"num": num, "stat": stat,})
			num += 1

	# 데이터베이스에 존재하는 스텟 element 수를 확인하는 데 쓰임
	list_length = len(stat_list)
	difference = 4-list_length

	# 4에서 모자라는 요소 수만큼 emptpy element를 추가해 줌
	if difference > 0:
		for i in range(difference):
			stat_list.append({"num": abs(list_length-i), "stat": None,})

	photo_link=account_user.memberintro.photolink

	context_dict = {
		'member_intro_form': member_intro_form,
		'stat_list': stat_list,
		'photo_link':photo_link,
	}
	url = "account/account_edit_introduction.html"
	###############################################################

	context_dict.update(navbar.context_dict())
	
	return render(request, url, context_dict)



@login_required
def save_intro(request):
	user = request.user
	# ajax에서 자기소개 데이터를 받아옴
	data_intro = request.POST.get('introduction')

	# 이미 저장된 자기소개가 있으면 그 위에 덮어씀
	try:
		member_intro = MemberIntro.objects.get(user=user)
		member_intro.intro = data_intro
		member_intro.save()
	# 저장된 자기소개가 없으면 새로 만듦
	except:
		MemberIntro.objects.create(user=user, intro=data_intro)

	str_message = '"' + data_intro + '"' + ' 메시지가 저장되었습니다.'
	data = {'message': str_message,} # alert로 띄울 메시지 전달
	return HttpResponse(simplejson.dumps(data), content_type="application/json")



@login_required
def save_stat(request):
	user = request.user

	# ajax에서 stat과 관련된 데이터를 받아옴
	data_stat_name = request.POST.get('stat_name')
	data_stat_value = request.POST.get('stat_value')
	data_stat_num = request.POST.get('stat_num')
	data_stat_list = request.POST.get('stat_list')

	n = int(data_stat_num) # 인덱스
	message = ""

	# 스텟 값과 이름 폼이 비어 있지 않으면
	if data_stat_value != None and data_stat_name != "":
		# 저장된 스텟 데이터들이 있으면 쿼리셋 형태로 가져옴
		try:
			stat_instance = Stat.objects.select_related().filter(
				member_intro=user.memberintro
			) # .order_by('-stat_value', 'stat_name')
			# 존재하는 스텟 인스턴스를 업데이트하여 저장
			try:
				si = stat_instance[n]
				si.stat_name = data_stat_name
				si.stat_value = data_stat_value
				si.save()
			# 해당 인덱스의 인스턴스가 없으면 새로 만들어 저장
			except:
				si = Stat.objects.create(
					member_intro = user.memberintro,
					stat_name = data_stat_name,
					stat_value = data_stat_value,
				)
		# 저장된 스텟 데이터들이 없으면 새로 만들어 저장
		except:
			si = Stat.objects.create(
				member_intro = user.memberintro,
				stat_name = data_stat_name,
				stat_value = data_stat_value,
			)
		message = '"' + data_stat_name + '" 스텟에 ' + '"' + data_stat_value + '"을 저장하였습니다.'

	# 스텟 폼이 비어 있으면 에러 메시지를 전달
	else:
		message = '"' + data_stat_name + '" 스텟에 ' + '"' + data_stat_value + '"은 입력 칸이 비어 있으므로 저장되지 않습니다.'

	# 인덱스와 메시지를 전달
	data = {'n': n, 'message': message,}
	return HttpResponse(simplejson.dumps(data), content_type="application/json")