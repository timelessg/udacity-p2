# coding:utf-8  

class Movie():
	"""Movie模型类"""
	def __init__(self, title,poster_image_url,trailer_url):
		 """Movie构造方法"""
		 self.title = title #电影名称
		 self.poster_image_url = poster_image_url #电影海报URL
		 self.trailer_url = trailer_url #电影预告URL