#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ==============================================================================
# あなたは、巻数が全 N 巻の古い本を集めています。
#
# 古本屋に訪れたあなたは売られている各巻のうち買うべきなのは何巻かを知りたいです。
#
# あなたの持っている巻のリストと、中古本屋で売られている巻のリストを入力として与えられたとき、
# あなたの買うべき巻のリストを出力してください。
#
# ==============================================================================
# 入力される値
#
# 入力は標準入力にて以下のフォーマットで与えられます。
#
#
# N
# M1
# x_1 x_2 ... x_M1
# M2
# y_1 y_2 ... y_M2
#
#
# N は、ある本の出版されている巻の総数です。
# 出版されているのは、1 巻から始まり、N 巻までです。
#
# M1 は、あなたの持っている巻の総数を表します。
# 次の行には、あなたの持っている巻のリストが与えられます。
#
# M2 は、中古本屋で売られている巻のリストの総数を表します。
# 次の行には、中古本屋で売られている巻のリストが与えられます。
#
# ==============================================================================
# 条件
#
# すべてのテストケースにおいて、以下の条件をみたします。
#
#
# 1 ≦ N ≦ 1000
# 1 ≦ M1, M2 ≦ N
# 1 ≦ x_i, y_i ≦ N
#
# ==============================================================================
# 期待する出力
#
# あなたの買うべき巻を小さい順に空白区切りで出力してください。
# ただし、買うべき巻がない場合は None と出力してください。
# 


import argparse


def makeBuyItemlist(own, items):
	return [x for x in items if x not in own]

def main():
	parser = argparse.ArgumentParser(description='Find volumes you should buy.')
	parser.add_argument('args', nargs=argparse.REMAINDER, type=int, help='N M1 x_1 ... x_M1 M2 y_1 ... y_M2')
	args = parser.parse_args()
	
	total    = args.args[0]
	del args.args[:1]
	
	ownNum   = args.args[0]
	del args.args[:1]
	ownList  = args.args[0:ownNum]
	del args.args[:ownNum]
	#print 'ownList', ownList
	
	itemNum  = args.args[0]
	del args.args[:1]
	itemList = args.args[:itemNum]
	#print 'itemList', itemList
	
	buyItemList = makeBuyItemlist(ownList, itemList)
	if buyItemList == []:
		print "None"
	else:
		for item in buyItemList:
			print item,

if __name__ == '__main__':
	main()

