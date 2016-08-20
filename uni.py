# -*- coding: utf-8 -*-

import string;
import os;

dic = [[u"\u0627",u"\uFE83",u"\uFE84","alif",["A"]
],[u"\u0623","A hamza",["'a"]
],[u"\u0628","bA",["b"]
],[u"\u062A","tA",["t"]
],[u"\u062B","tA",["_t"]
],[u"\u062C","jim",["j","^g"]
],[u"\u062D","hA",[".h"]
],[u"\u062E","_hA",["x","_h"]
],[u"\u062F","dAl",["d"]
],[u"\u0630","_dAl",["_d"]
],[u"\u0631","rA",["r"]
],[u"\u0632","Zayin",["z"]
],[u"\u0633","sin",["s"]
],[u"\u0634","sin",["^s"]
],[u"\u0635","sAd",[".s"]
],[u"\u0636","dAd",[".d"]
],[u"\u0637","tA",[".t"]
],[u"\u0638","zA",[".z"]
],[u"\u0639","ayn",["`"]
],[u"\u063A","gayn",[".g"]
],[u"\u0641","fA",["f"]
],[u"\u0642","qAf",["q"]
],[u"\u0643","kAf",["k"]
],[u"\u0644","lAm",["l"]
],[u"\u0645","mim",["m"]
],[u"\u0646","nun",["n"]
],[u"\u0647","hA",["h"]
],[u"\u0648","wAw",["w","U"]
],[u"\u064A","yA",["y","I"]
],[u"\u0622","alif maddah",["'A"]
],[u"\u0629","Tamarbutah",["T"]
],[u"\u0649","alif mmaqsura",["_A"]
],[u"\u0621","hamza",["'|"]
],[u"\u0626","ya hamza",["'y"]
],[u"\u0625","alif down hamza",["'i"]
],[u"\u0624","wAw hamza",["'u"]
],[u"\u064B","aN",["aN"]
],[u"\u064C","uN",["uN"]
],[u"\u064D","iN",["iN"]
],[u"\u064E","a",["a"]
],[u"\u064F","u",["u","o"]
],[u"\u0650","i",["i","e"]
],[u"\u0651","shadda",[" "]
],[u"\u061F","question mark",["?"]
],[u"\u060C","coma",[","]
],[u"\u0660","0",["0"]
],[u"\u0661","1",["1"]
],[u"\u0662","2",["2"]
],[u"\u0663","3",["3"]
],[u"\u0664","4",["4"]
],[u"\u0665","5",["5"]
],[u"\u0666","6",["6"]
],[u"\u0667","7",["7"]
],[u"\u0668","8",["8"]
],[u"\u0669","9",["9"]
],[u"\u066A","%",["%"]
],[u"\u061B",";",[";"]
],[u"\u065C",".arabic",["."]
],[u"\u002E",".ascii",["."]
],[u"\u0640","-",["-"]
],[u"\n","-",["\\\\"]
],[" ","space",[" "]
],["\t","tab",[" "]
]];

def search(list_of_list,to_find):
	for i in range(len(list_of_list)):
		if to_find in list_of_list[i]:
			#print elem;
			return (True,i);
	return (False,False);
def ar_error(stri,j,maxlength=4):
	lstri = len(stri);
	if (j>=maxlength):
		low = maxlength;
	else:
		low = j;
	if (j+maxlength)>=lstri:
		high = lstri-1-j;
	else: 
		high =maxlength; 
	print("Error in : ..."+stri[j-low:j]+"*"+stri[j:j+high]+"...");



def to_arabtex(stri):
	if type(stri) is unicode:
		ustri = stri;
	else:
		ustri = unicode(stri,"UTF-8");
	comparison = [p[0] for p in dic];
	shadda = u"\u0651";
	arastring="";
	for i in range(len(ustri)):
		if ustri[i]==shadda and i!=0:
			if stri[i-1] in short_vowels:
				arastring+=to_arabtex(ustri[i-1]);
		for j in range(len(comparison)):
			if ustri[i]==comparison[j]:
				arastring+=dic[j][-1][0];
				continue;

	return arastring;


def to_arabic(stri):
	u8stri= "";
	short_vowels = dic[39:42][0];
	consonants = dic[0:36][0];
	punctuation = ["\n", " ", "\t",","];
	comparison = [p[-1] for p in dic];
	abc = list(string.ascii_lowercase);
	ignore_one=False;
	for j in range(len(stri)):
		if ignore_one:
			ignore_one=False;
			#print "Double!!"+char+" "+str(j);
			continue;
		char = stri[j];
		if char in punctuation:
			u8stri +=char.decode("UTF-8");
			continue;
		else:
			if (j-1) != len(stri):
				(found, ind) = search(comparison,stri[j:j+2]);
				if found:
					u8stri+=dic[ind][0];
					ignore_one=True;
					continue;
			(found, ind) = search(comparison,char);
			if found:
				u8stri+=dic[ind][0];
				#print char + u8stri;
				continue;
		ar_error(stri,j);
		return False;				
	return u8stri;

# text = "man a'nA lia'qula lakum mA a'qulu lakum\nwa AnA lam a'kun .hajarAaN\n.saqalathu AlmyAhu Ua a'.sba.ha Uaji`AaN\nUa lA qa.sabAaN, _taqbatho AlryA.hu \n Ua a'.sba.ha nAyAaN";
# text+="\na'nA lA`ibo Alnardi\n a'rba.ho .hynaN Ua a'xsaru .hynaN\nUa lakin man a'nA lia'qula lakum mA a'qulu lakum";
# text+="\n\nwa limA_d_dA a'nA a'nta sammaytany yuwsuf'aN wa hm yuqa`uniy\n f'y Aljib w AthmwA Al_dyb w Al_dyb Ar.hm min Axwaty "
# ara = to_arabic(text);
# print(ara);
# artext = raw_input();
# normal = to_arabtex(artext);
# print(normal);


f = open("test.txt","r");
g = open("arabtex_text.tex","w")
g.write("\documentclass[12pt]{article}\n\n\usepackage{arabtex}\n\n\\begin{document}\n");
g.write("\setarab\n\\vocalize\n\\arabtrue\n\\begin{RLtext}\n\n");
for line in f:
	arabtex = to_arabtex(line);
	g.write(arabtex);
	print line;
	print arabtex;
g.write("\n\n\end{RLtext}\n\n\end{document}");
f.close();
g.close();

os.system("pdflatex arabtex_text.tex");
os.system("rm arabtex_text.log arabtex_text.aux");
os.system("open arabtex_text.pdf");

#f = open("text.txt".encode("ascii"),"w");
#f.write(ara);
#f.close();

