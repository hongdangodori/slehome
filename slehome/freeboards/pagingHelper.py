class pagingHelper:
# 페이지가 총 몇개인지 세어주는 class.

	# 초기화
	def __init__(self):
		self.totalPages = 0
		self.totalPageList = 0


	def getTotalPageList(self, totalCnt, rowsPerPage):
		"""
		총 게시물 수를 rowsPerPage로 나누어 그 몫만큼 페이지를 만든다.
		단, 나누어 떨어지지 않는 경우 나머지 게시물들을 담을 page를 +1 해준다.
		page list를 return한다. 
		"""
		quotient = int(totalCnt/rowsPerPage)

		# 나누어 떨어지는 경우
		if((totalCnt % rowsPerPage) == 0):
			self.totalPages = quotient
			print('getTotalPage #1')

		# 나머지가 존재하는 경우
		else:
			self.totalPages = quotient+1;
			print('getTotalPage #2')

		# page list 반환
		self.totalPageList=[]
		for j in range(self.totalPages):
			self.totalPageList.append(j+1)
		return self.totalPageList

