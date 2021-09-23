

# This file was *autogenerated* from the file a.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2589151862704631 = Integer(2589151862704631); _sage_const_22744527108269603 = Integer(22744527108269603); _sage_const_33101134559088127 = Integer(33101134559088127); _sage_const_30330064677397106 = Integer(30330064677397106); _sage_const_34774653527304355 = Integer(34774653527304355); _sage_const_1873565385871977 = Integer(1873565385871977); _sage_const_7076040309507051 = Integer(7076040309507051); _sage_const_17111111319247966 = Integer(17111111319247966); _sage_const_16655999255635591 = Integer(16655999255635591); _sage_const_5577128496135160 = Integer(5577128496135160); _sage_const_41478278870110973 = Integer(41478278870110973); _sage_const_26377181197362203 = Integer(26377181197362203); _sage_const_38147169712097929 = Integer(38147169712097929); _sage_const_40792013820945943 = Integer(40792013820945943); _sage_const_44972065526054272 = Integer(44972065526054272); _sage_const_16908167638976159 = Integer(16908167638976159); _sage_const_39364517840890813 = Integer(39364517840890813); _sage_const_5693072268649241 = Integer(5693072268649241); _sage_const_21554791169574163 = Integer(21554791169574163); _sage_const_15374712324012304 = Integer(15374712324012304); _sage_const_30009666972966142 = Integer(30009666972966142); _sage_const_16197755898052853 = Integer(16197755898052853); _sage_const_23148540857874881 = Integer(23148540857874881); _sage_const_8393565068338059 = Integer(8393565068338059); _sage_const_15307614786559186 = Integer(15307614786559186); _sage_const_11939369677670332 = Integer(11939369677670332); _sage_const_19810072142519101 = Integer(19810072142519101); _sage_const_12255153107431413 = Integer(12255153107431413); _sage_const_21551275514628962 = Integer(21551275514628962); _sage_const_13518286826475737 = Integer(13518286826475737); _sage_const_4110128525695481 = Integer(4110128525695481); _sage_const_1932316813394001 = Integer(1932316813394001); _sage_const_10892331539843429 = Integer(10892331539843429); _sage_const_4218439696826517 = Integer(4218439696826517); _sage_const_8436879393653034 = Integer(8436879393653034); _sage_const_12065333899426039 = Integer(12065333899426039); _sage_const_11002990466342533 = Integer(11002990466342533); _sage_const_19046950232451202 = Integer(19046950232451202); _sage_const_32363799882977519 = Integer(32363799882977519); _sage_const_2600040660156800 = Integer(2600040660156800); _sage_const_44213234480313002 = Integer(44213234480313002); _sage_const_18349536247727483 = Integer(18349536247727483); _sage_const_21722000975299256 = Integer(21722000975299256); _sage_const_14229616585345558 = Integer(14229616585345558); _sage_const_22911050607752621 = Integer(22911050607752621); _sage_const_43602828190329844 = Integer(43602828190329844); _sage_const_31366037512858411 = Integer(31366037512858411); _sage_const_15581587440074294 = Integer(15581587440074294); _sage_const_44660731050187366 = Integer(44660731050187366); _sage_const_9997558449245386 = Integer(9997558449245386); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_5 = Integer(5); _sage_const_7 = Integer(7); _sage_const_100 = Integer(100); _sage_const_1 = Integer(1)# answer: 2

beta = [_sage_const_2589151862704631 , _sage_const_22744527108269603 , _sage_const_33101134559088127 , _sage_const_30330064677397106 , _sage_const_34774653527304355 , _sage_const_1873565385871977 , _sage_const_7076040309507051 , _sage_const_17111111319247966 , _sage_const_16655999255635591 , _sage_const_5577128496135160 , _sage_const_41478278870110973 , _sage_const_26377181197362203 , _sage_const_38147169712097929 , _sage_const_40792013820945943 , _sage_const_44972065526054272 , _sage_const_16908167638976159 , _sage_const_39364517840890813 , _sage_const_5693072268649241 , _sage_const_21554791169574163 , _sage_const_15374712324012304 , _sage_const_30009666972966142 , _sage_const_16197755898052853 , _sage_const_23148540857874881 , _sage_const_8393565068338059 , _sage_const_15307614786559186 , _sage_const_11939369677670332 , _sage_const_19810072142519101 , _sage_const_12255153107431413 , _sage_const_21551275514628962 , _sage_const_13518286826475737 , _sage_const_4110128525695481 , _sage_const_1932316813394001 , _sage_const_10892331539843429 , _sage_const_4218439696826517 , _sage_const_8436879393653034 , _sage_const_12065333899426039 , _sage_const_11002990466342533 , _sage_const_19046950232451202 , _sage_const_32363799882977519 , _sage_const_2600040660156800 , _sage_const_44213234480313002 , _sage_const_18349536247727483 , _sage_const_21722000975299256 , _sage_const_14229616585345558 , _sage_const_22911050607752621 , _sage_const_43602828190329844 , _sage_const_31366037512858411 , _sage_const_15581587440074294 , _sage_const_44660731050187366 , _sage_const_9997558449245386 ]
c = beta[_sage_const_0 ] + beta[_sage_const_2 ] + beta[_sage_const_3 ] + beta[_sage_const_5 ] + beta[_sage_const_7 ] + _sage_const_100 

mat = []
for i in range(len(beta)+_sage_const_1 ):
	v = []
	for j in range(len(beta)+_sage_const_1 ):
		if i == j:
			v.append(_sage_const_1 )
		else:
			v.append(_sage_const_0 )
	if i == len(beta):
		v[-_sage_const_1 ] = -c
	else:
		v[-_sage_const_1 ] = beta[i]
	mat.append(v)

mat = matrix(ZZ, mat).LLL()
print(mat)
# v = mat[0]
# 
# print(v)
# for i in range(len(v)):
# 	if v[i] == 1:
# 		print(i)
