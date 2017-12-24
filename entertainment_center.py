# coding:utf-8  

import fresh_tomatoes
import media

"""Movie模型类"""

#生成网页
def showMoviePage():
	life_is_beautiful = media.Movie("Life is Beautiful",
		"https://github.com/timelessg/udacity-p2/blob/master/res/\
		life_is_beautiful_ver1.jpg?raw=true",
		"https://www.youtube.com/watch?v=8CTjcVr9Iao")
	schindlers_list = media.Movie("Schindler's List",
		"https://github.com/timelessg/udacity-p2/blob/master/res/\
		schindlers_List_movie.jpg?raw=true",
		"https://www.youtube.com/watch?v=iarykvuRCkc")
	the_legend_of_1900 = media.Movie("The Legend of 1900",
		"https://github.com/timelessg/udacity-p2/blob/master/res/\
		TLO1900.jpg?raw=true",
		"https://www.youtube.com/watch?v=2uf-LDlZMFE")
	dunkirk = media.Movie("Dunkirk",
		"https://github.com/timelessg/udacity-p2/blob/master/res/\
		dunkirk_2017_Poster.jpg?raw=true",
		"https://www.youtube.com/watch?v=YSfRHhPVr9Q")
	silenced = media.Movie("熔炉",
		"https://github.com/timelessg/udacity-p2/blob/master/res/\
		silenced.jpg?raw=true",
		"https://www.youtube.com/watch?v=clWx4ssu050")
	infernal = media.Movie("无间道",
		"https://github.com/timelessg/udacity-p2/blob/master/res/\
		Infernal_Affairs.jpg?raw=true",
		"https://www.youtube.com/watch?v=08YrmFqWJ8E")

	fresh_tomatoes.open_movies_page([life_is_beautiful,
		schindlers_list,the_legend_of_1900,dunkirk,silenced,infernal])

showMoviePage()