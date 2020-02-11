import pandas as pd
import numpy as np
df = pd.read_csv('./simpletabulation3.csv', sep='|')

#print(df.info())
#print(df['Id'].head())
#print(df['Id'][0])

#print(df.shape)
gp = [1435254666, 588616678,135352227,257068234,2099226249,1616956984,1592269710,1182663077,871442980,521142341,2060008965]
#print(df['0'].head(20))
#g = np.int64(df['0'][4])
#gp[g] = "a"
#print(gp)
#for i in range(0,33465):
#	if(df['0'][i] == df['0'][i+1]):
#		df['ParentId'][i+1] = df['Id'][i]
#		gp[np.int64(df['0'][i])] = df['Id'][i]
#	elif(df['0'][i]+1 == df['0'][i+1]):
#		df['ParentId'][i+1] = df['Id'][i]
#       df['GP'][i] = df['Id'][i-1]
#g=0
for i in range(0,33459):
	#print(df['Id'][i])
	g = np.int64(df['0'][i])
	#print(gp[g])
	#print(g)
	gp[g] = df['Id'][i]
	if(df['0'][i]-1 == df['0'][i+1]):
		#print(df['0'][i])
		d = np.int64(df['0'][i])-2
		#print(d)
		df['1435254666'][i+1] = gp[np.int64(df['0'][i])-2]
	elif(df['0'][i] == df['0'][i+1]):
		#print(df['0'][i])
		d = np.int64(df['0'][i])-1
		#print(d)
		df['1435254666'][i+1] = df['1435254666'][i]
	else: 
		df['1435254666'][i+1] = df['Id'][i]	
		
#print(gp)
#print(df['1435254666'].head(20))

df.rename(columns = {'0' : 'Level'}, inplace = True)
df.rename(columns = {'1435254666' : 'ParentId'}, inplace = True)
df.rename(columns = {'Foundation URI' : 'FoundationURI'}, inplace = True)
df.rename(columns = {'Linearization (release) URI' : 'LinearizationURI'}, inplace = True)

#print(df['noOfNonResidualChildren'].head())
#print(df.info())
df2 = pd.DataFrame(data = df, columns = ['FoundationURI', 'LinearizationURI', 'Id', 'BlockCode', 'ParentId', 'Level', 'Title', 'ClassKind', 'DepthInKind', 'IsResidual','PrimaryLocation', 'ChapterNo','BrowserLink', 'isLeaf','noOfNonResidualChildren','Version'])
df1 = pd.DataFrame(data = df, columns =['Id','ParentId','Level','DepthInKind','BlockCode'])
df1.to_csv('ICDtree.tsv', sep = '\t')
df2.to_csv('ICD.tsv', sep='\t')


