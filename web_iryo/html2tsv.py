# coding: utf-8

# python3 html2tsv.py

import urllib
# import urllib2
import glob
import datetime
import os
import urllib.request

current_time = datetime.datetime.today()

html_dir = 'in_html/'
p_dir = 'http://rctportal.niph.go.jp/'
directory_path = 'out_tsv/result_' + str(current_time.year) + '_' + str(current_time.month) + '_' + str(current_time.day) + '_' + str(current_time.hour) + '_' + str(current_time.minute)
UMIN_out_path = directory_path + '/umin.tsv'
JAPIC_out_path = directory_path + '/japic.tsv'
ISHIKAI_out_path = directory_path + '/ishikai.tsv'

file_list = glob.glob(html_dir + '*')

def out_UMIN(arg_page):
	out = ["" for i in range(18)]
	kokai = False
	shikenmei = 0
	shikenmei_line = ""
	shikenkanryakumei = 0
	shikenkanryakumei_line = ""
	taishoushikkan = 0
	taishoushikkan_line = ""
	kihondesain = False
	randamka = False
	kainyu1 = 0
	kainyu1_line = ""
	kainyu2 = 0
	kainyu2_line = ""
	sentakukijun = 0
	sentakukijun_line = ""
	jogaikijun = 0
	jogaikijun_line = ""
	soshikimei = 0
	soshikimei_line = ""
	jisshisekininsoshiki = 0
	jisshisekininsoshiki_line = ""
	kenkyuhiteikyousoshiki = 0
	kenkyuhiteikyousoshiki_line = ""
	shikenshintyoku = False
	tourokukumiire = False
	uketsukeid = False
	tantoshamei = False
	for line in arg_page:
		if "UMIN試験ID" in line:
			out[0] = line.split('UMIN試験ID　')[1].split('<')[0]
			continue
		if ">公開日<" in line:
			kokai = True
			continue
		if kokai == True:
			kokai = False
			out[1] = line.split('<td>')[1].split('</td>')[0]
			continue
		if ">試験名<" in line:
			shikenmei = 1
			continue
		if shikenmei == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				shikenmei = 2
			shikenmei_line = shikenmei_line + line
			if shikenmei == 2:
				out[2] = shikenmei_line
			continue
		if ">試験簡略名<" in line:
			shikenkanryakumei = 1
			continue
		if shikenkanryakumei == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				shikenkanryakumei = 2
			shikenkanryakumei_line = shikenkanryakumei_line + line
			if shikenkanryakumei == 2:
				out[3] = shikenkanryakumei_line
			continue
		if ">対象疾患<" in line:
			taishoushikkan = 1
			continue
		if taishoushikkan == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				taishoushikkan = 2
			taishoushikkan_line = taishoushikkan_line + line
			if taishoushikkan == 2:
				out[4] = taishoushikkan_line
			continue
		if ">基本デザイン<" in line:
			kihondesain = True
			continue
		if kihondesain == True:
			kihondesain = False
			out[5] = line.split('<td>')[1].split('</td>')[0]
			continue
		if randamka == True:
			randamka = False
			out[6] = line.split('<td>')[1].split('</td>')[0]
			continue
		if ">ランダム化<" in line:
			randamka = True
			continue
		if ">介入1<" in line:
			kainyu1 = 1
			continue
		if kainyu1 == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				kainyu1 = 2
			kainyu1_line = kainyu1_line + line.strip()
			if kainyu1 == 2:
				out[7] = kainyu1_line
				kainyu1 = 3
			continue
		if ">介入2<" in line:
			kainyu2 = 1
			continue
		if kainyu2 == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				kainyu2 = 2
			kainyu2_line = kainyu2_line + line.strip()
			if kainyu2 == 2:
				out[8] = kainyu2_line
				kainyu2 = 3
			continue
		if ">選択基準<" in line:
			sentakukijun = 1
			continue
		if sentakukijun == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				sentakukijun = 2
			sentakukijun_line = sentakukijun_line + line
			if sentakukijun == 2:
				out[9] = sentakukijun_line
			continue
		if ">除外基準<" in line:
			jogaikijun = 1
			continue
		if jogaikijun == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				jogaikijun = 2
			jogaikijun_line = jogaikijun_line + line
			if jogaikijun == 2:
				out[10] = jogaikijun_line
			continue
		if ">組織名<" in line:
			soshikimei = 1
			continue
		if soshikimei == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				soshikimei = 2
			soshikimei_line = soshikimei_line + line
			if soshikimei == 2:
				out[11] = soshikimei_line
			continue
		if ">担当者名<" in line:
			tantoshamei = True
			continue
		if tantoshamei == True:
			tantoshamei = False
			out[12] = line.split('<td>')[1].split('</td>')[0]
			continue
		if ">実施責任組織<" in line:
			jisshisekininsoshiki = 1
			continue
		if jisshisekininsoshiki == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				jisshisekininsoshiki = 2
			jisshisekininsoshiki_line = jisshisekininsoshiki_line + line
			if jisshisekininsoshiki == 2:
				out[13] = jisshisekininsoshiki_line
		if ">研究費提供組織<" in line:
			kenkyuhiteikyousoshiki = 1
			continue
		if kenkyuhiteikyousoshiki == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				kenkyuhiteikyousoshiki = 2
			kenkyuhiteikyousoshiki_line = kenkyuhiteikyousoshiki_line + line
			if kenkyuhiteikyousoshiki == 2:
				out[14] = kenkyuhiteikyousoshiki_line
		if ">試験進捗状況<" in line:
			shikenshintyoku = True
			continue
		if shikenshintyoku == True:
			shikenshintyoku = False
			out[15] = line.split('<td>')[1].split('</td>')[0]
			continue
		if ">登録・組み入れ開始日<" in line:
			tourokukumiire = True
			continue
		if tourokukumiire == True:
			tourokukumiire = False
			out[16] = line.split('<td>')[1].split('</td>')[0]
			continue
		if ">受付ID<" in line:
			uketsukeid = True
			continue
		if uketsukeid == True:
			uketsukeid = False
			out[17] = line.split('<td>')[1].split('</td>')[0]
			continue
	out_line = search_word + '\t'
	for out_e in out:
		out_e = out_e.replace('\t', '')
		out_e = out_e.replace('&nbsp;', '')
		out_line = out_line + out_e + '\t'
	fw_umin = open(UMIN_out_path, 'a')
	fw_umin.write(out_line.encode('cp932','ignore').decode('cp932') + '\n')
	fw_umin.close


def out_JAPIC(arg_page):
	out = []
	kanrenid = False
	shikenmeisyou = False
	shikenshurui = False
	shikengaiyo = 0
	shikengaiyo_line = ""
	shikenyakuzai = False
	shikkanmei = False
	shikenmokuteki = 0
	shikenmokuteki_line = ""
	shikenphase = False
	taishokijun = 0
	taishokijun_line = ""
	yoteishikenkikan = False
	shikennogenjo = False
	kaishasoshiki = 0
	tantoubusho = 0
	torokubi = False
	for line in arg_page:
		if "JAPIC ID" in line:
			out.append(line.split('JAPIC ID　')[1].split('<')[0])
			continue
		if ">関連ID<" in line:
			kanrenid = True
			continue
		if kanrenid == True:
			kanrenid = False
			out.append(line.split('<td>')[1].split('</td>')[0])
			continue
		if ">試験の名称<" in line:
			shikenmeisyou = True
			continue
		if shikenmeisyou == True:
			shikenmeisyou = False
			out.append(line.split('<td>')[1].split('</td>')[0])
			continue
		if ">試験の種類<" in line:
			shikenshurui = True
			continue
		if shikenshurui == True:
			shikenshurui = False
			out.append(line.split('<td>')[1].split('</td>')[0])
			continue
		if ">試験の概要<" in line:
			shikengaiyo = 1
			continue
		if shikengaiyo == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				shikengaiyo = 2
			shikengaiyo_line = shikengaiyo_line + line
			if shikengaiyo == 2:
				out.append(shikengaiyo_line)
			continue
		if ">試験薬剤名<" in line:
			shikenyakuzai = True
			continue
		if shikenyakuzai == True:
			shikenyakuzai = False
			out.append(line.split('<td>')[1].split('</td>')[0])
			continue
		if ">疾患名<" in line:
			shikkanmei = True
			continue
		if shikkanmei == True:
			shikkanmei = False
			out.append(line.split('<td>')[1].split('</td>')[0])
			continue
		if ">試験の目的<" in line:
			shikenmokuteki = 1
			continue
		if shikenmokuteki == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				shikenmokuteki = 2
			shikenmokuteki_line = shikenmokuteki_line + line
			if shikenmokuteki == 2:
				out.append(shikenmokuteki_line)
			continue
		if ">試験のフェーズ<" in line:
			shikenphase = True
			continue
		if shikenphase == True:
			shikenphase = False
			out.append(line.split('<td>')[1].split('</td>')[0])
			continue
		if ">対象基準<" in line:
			taishokijun = 1
			continue
		if taishokijun == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				taishokijun = 2
			taishokijun_line = taishokijun_line + line
			if taishokijun == 2:
				out.append(taishokijun_line)
			continue
		if ">予定試験期間<" in line:
			yoteishikenkikan = True
			continue
		if yoteishikenkikan == True:
			yoteishikenkikan = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">試験の現状<" in line:
			shikennogenjo = True
			continue
		if shikennogenjo == True:
			shikennogenjo = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">会社名・機関名<" in line:
			kaishasoshiki = 1
			continue
		if kaishasoshiki == 1:
			kaishasoshiki = 2
			continue
		if kaishasoshiki == 2:
			kaishasoshiki = 3
			out.append(line.split('</td>')[0].strip())
			continue
		if ">担当部署名<" in line:
			tantoubusho = 1
			continue
		if tantoubusho == 1:
			tantoubusho = 2
			continue
		if tantoubusho == 2:
			tantoubusho = 3
			out.append(line.split('</td>')[0].strip())
			continue
		if ">登録日<" in line:
			torokubi = True
			continue
		if torokubi == True:
			torokubi = False
			out.append(line.split('<td>')[1].split('</td>')[0])
	out_line = search_word + '\t'
	for out_e in out:
		out_e = out_e.replace('\t', '')
		out_e = out_e.replace('&nbsp;', '')
		out_line = out_line + out_e + '\t'
	fw_japic = open(JAPIC_out_path, 'a')
	fw_japic.write(out_line.encode('cp932','ignore').decode('cp932') + '\n')
	fw_japic.close


def out_ISHIKAI(arg_page):
	out = []
	ippanmukeshikenmei = 0
	ippanmukeshikenmei_line = ""
	seishikishikenmei = 0
	seishikishikenmei_line = ""
	gaiyo = 0
	gaiyo_line = ""
	shuyomokuteki = 0
	shuyomokuteki_line = ""
	shikendesign = False
	taishonoshurui = False
	moukenka = False
	randomka = False
	shikenphasee = False
	shikennoseishitsu = False
	mokutekiniyoru = False
	taishoshikkanmataha = 0
	taishoshikkanmataha_line = ""
	kainyumeishou = 0
	toyokeiro = 0
	protocol = False
	rinri = False
	shokaikumiire = False
	shikenkaishi = False
	shuyohyouka = 0
	shuyohyouka_line = ""
	kenjouhikensya = False
	sentakukijunn = 0
	sentakukijunn_line = ""
	jogaikijunn = 0
	jogaikijunn_line = ""
	sankaboshu = False
	shikenshinchoku = False
	shuyoirai = 0
	shuyoirai_line = ""
	kyodoirai = 0
	kyodoirai_line = ""
	shikinteikyo = 0
	tantosha = False
	shozokusoshiki = False
	shozokubusho = 0
	shikensekininishi = False
	shikenidd = 0
	hakkou = 0
	shokaitodoke = False
	for line in arg_page:
		if "日本医師会ID" in line:
			out.append(line.split('日本医師会ID　')[1].split('<')[0])
			continue
		if ">一般向け試験名<" in line:
			ippanmukeshikenmei = 1
			continue
		if ippanmukeshikenmei == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				ippanmukeshikenmei = 2
			ippanmukeshikenmei_line = ippanmukeshikenmei_line + line
			if ippanmukeshikenmei == 2:
				out.append(ippanmukeshikenmei_line)
			continue
		if ">正式試験名<" in line:
			seishikishikenmei = 1
			continue
		if seishikishikenmei == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				seishikishikenmei = 2
			seishikishikenmei_line = seishikishikenmei_line + line
			if seishikishikenmei == 2:
				out.append(seishikishikenmei_line)
			continue
		if ">概要<" in line:
			gaiyo = 1
			continue
		if gaiyo == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				gaiyo = 2
			gaiyo_line = gaiyo_line + line
			if gaiyo == 2:
				out.append(gaiyo_line)
			continue
		if ">主要目的<" in line:
			shuyomokuteki = 1
			continue
		if shuyomokuteki == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				shuyomokuteki = 2
			shuyomokuteki_line = shuyomokuteki_line + line
			if shuyomokuteki == 2:
				out.append(shuyomokuteki_line)
			continue
		if ">試験デザイン<" in line:
			shikendesign = True
			continue
		if shikendesign == True:
			shikendesign = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">対照の種類<" in line:
			taishonoshurui = True
			continue
		if taishonoshurui == True:
			taishonoshurui = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">盲検化の方法<" in line:
			moukenka = True
			continue
		if moukenka == True:
			moukenka = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">ランダム化<" in line:
			randomka = True
			continue
		if randomka == True:
			randomka = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if "<td>試験フェーズ</td>" in line:
			shikenphasee = True
			continue
		if shikenphasee == True:
			shikenphasee = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">試験の性質<" in line:
			shikennoseishitsu = True
			continue
		if shikennoseishitsu == True:
			shikennoseishitsu = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">目的による試験の分類<" in line:
			mokutekiniyoru = True
			continue
		if mokutekiniyoru == True:
			mokutekiniyoru = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">対象疾患または課題<" in line:
			taishoshikkanmataha = 1
			continue
		if taishoshikkanmataha == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				taishoshikkanmataha = 2
			taishoshikkanmataha_line = taishoshikkanmataha_line + line
			if taishoshikkanmataha == 2:
				out.append(taishoshikkanmataha_line)
			continue
		if ">介入の名称<" in line:
			if kainyumeishou == 3:
				continue
			kainyumeishou = 1
			continue
		if kainyumeishou == 1:
			kainyumeishou = 2
			continue
		if kainyumeishou == 2:
			kainyumeishou = 3
			out.append(line.split('</td>')[0].strip())
			continue
		if ">投与経路／適用部位<" in line:
			if toyokeiro == 3:
				continue
			toyokeiro = 1
			continue
		if toyokeiro == 1:
			toyokeiro = 2
			continue
		if toyokeiro == 2:
			toyokeiro = 3
			out.append(line.split('</td>')[0].strip())
			continue
		if ">プロトコール確定日<" in line:
			protocol = True
			continue
		if protocol == True:
			protocol = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">倫理委員会／治験審査委員会の初回開催日（予定日）<" in line:
			rinri = True
			continue
		if rinri == True:
			rinri = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">初回組入れ日（予定日）<" in line:
			shokaikumiire = True
			continue
		if shokaikumiire == True:
			shokaikumiire = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">試験開始日（予定日）<" in line:
			shikenkaishi = True
			continue
		if shikenkaishi == True:
			shikenkaishi = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">主要評価項目<" in line:
			shuyohyouka = 1
			continue
		if shuyohyouka == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				shuyohyouka = 2
			shuyohyouka_line = shuyohyouka_line + line
			if shuyohyouka == 2:
				out.append(shuyohyouka_line)
			continue
		if ">健常被験者の組入れ<" in line:
			kenjouhikensya = True
			continue
		if kenjouhikensya == True:
			kenjouhikensya = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">選択基準<" in line:
			sentakukijunn = 1
			continue
		if sentakukijunn == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				sentakukijunn = 2
			sentakukijunn_line = sentakukijunn_line + line
			if sentakukijunn == 2:
				out.append(sentakukijunn_line)
			continue
		if ">除外基準<" in line:
			jogaikijunn = 1
			continue
		if jogaikijunn == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				jogaikijunn = 2
			jogaikijunn_line = jogaikijunn_line + line
			if jogaikijunn == 2:
				out.append(jogaikijunn_line)
			continue
		if ">参加者募集状況<" in line:
			sankaboshu = True
			continue
		if sankaboshu == True:
			sankaboshu = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">試験の進捗<" in line:
			shikenshinchoku = True
			continue
		if shikenshinchoku == True:
			shikenshinchoku = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">主要依頼者<" in line:
			shuyoirai = 1
			continue
		if shuyoirai == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				shuyoirai = 2
			shuyoirai_line = shuyoirai_line + line
			if shuyoirai == 2:
				out.append(shuyoirai_line)
			continue
		if ">共同依頼者<" in line:
			kyodoirai = 1
			continue
		if kyodoirai == 1:
			if "<td>" in line:
				line = line.split('<td>')[1]
			if "<br />" in line:
				line = line.split('<br />')[0].strip() + "_"
			if "</td>" in line:
				line = line.split('</td>')[0].strip()
				kyodoirai = 2
			kyodoirai_line = kyodoirai_line + line
			if kyodoirai == 2:
				out.append(kyodoirai_line)
			continue
		if ">資金提供組織<" in line:
			shikinteikyo = 1
			continue
		if shikinteikyo == 1:
			shikinteikyo = 2
			continue
		if shikinteikyo == 2:
			shikinteikyo = 3
			if len(out) == 28:
				out[27] = out[27] + " : " + line.split('</td>')[0].strip()
			else:
				out.append(line.split('</td>')[0].strip())
			continue
		if ">担当者<" in line:
			tantosha = True
			continue
		if tantosha == True:
			tantosha = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">所属組織<" in line:
			shozokusoshiki = True
			continue
		if shozokusoshiki == True:
			shozokusoshiki = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">所属部署<" in line:
			if shozokubusho == 2:
				continue
			shozokubusho = 1
			continue
		if shozokubusho == 1:
			shozokubusho = 2
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">試験責任医師<" in line:
			shikensekininishi = True
			continue
		if shikensekininishi == True:
			shikensekininishi = False
			out.append(line.split('<td>')[1].split('</td>')[0])
		if ">試験ID<" in line:
			if shikenidd == 3:
				continue
			shikenidd = 1
			continue
		if shikenidd == 1:
			shikenidd = 2
			continue
		if shikenidd == 2:
			shikenidd = 3
			out.append(line.split('</td>')[0].strip())
			continue
		if ">発行機関名<" in line:
			if hakkou == 3:
				continue
			hakkou = 1
			continue
		if hakkou == 1:
			hakkou = 2
			continue
		if hakkou == 2:
			hakkou = 3
			out.append(line.split('</td>')[0].strip())
			continue
		if ">初回届出日<" in line:
			shokaitodoke = True
			continue
		if shokaitodoke == True:
			shokaitodoke = False
			out.append(line.split('<td>')[1].split('</td>')[0])
	out_line = search_word + '\t'
	for out_e in out:
		out_e = out_e.replace('\t', '')
		out_e = out_e.replace('&nbsp;', '')
		out_line = out_line + out_e + '\t'
	fw_ishikai = open(ISHIKAI_out_path, 'a')
	fw_ishikai.write(out_line.encode('cp932','ignore').decode('cp932') + '\n')
	fw_ishikai.close

os.mkdir(directory_path)

for html_f in file_list:
	fr = open(html_f,'r', encoding='utf8')
	first_line = True
	for line in fr:
		if first_line is True:
			search_word = line.strip()
			first_line = False
			continue
		if '詳細' not in line:
			continue
		url_l = p_dir + line.split('"')[5]
#		req = urllib.Request(url_l)
#		response = urllib.urlopen(req)
		response = urllib.request.urlopen(url_l)
		the_page = response.read()
		the_page = str(the_page, encoding='utf8')
		lines_page = the_page.split('\r')
		if 'UMIN' in lines_page[25]:
			out_UMIN(lines_page)
		if 'JAPIC' in lines_page[25]:
			out_JAPIC(lines_page)
		if '日本医師会' in lines_page[25]:
			out_ISHIKAI(lines_page)





