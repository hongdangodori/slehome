class pagingHelper:
	"paging helper lass"

	def getTotalPageList(self, totalCnt, rowsPerPage):
		quotient = int(totalCnt/rowsPerPage)
		if((totalCnt % rowsPerPage) == 0):
			self.totalPages = quotient
			print('getTotalPage #1')

		else:
			self.totalPages = quotient+1;
			print('getTotalPage #2')

		self.totalPageList=[]
		for j in range(self.totalPages):
			self.totalPageList.append(j+1)

		return self.totalPageList

	def __init__(self):
		self.totalPages = 0
		self.totalPageList = 0