# -*- coding: utf-8 -*-

import string;
import os;


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
	ustri = stri;
	comparison = [p[0] for p in dic];
	shadda = "\u{0651}";
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



