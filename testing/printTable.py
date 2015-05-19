
# sim

# w/o misclassifications
print 'sim w/o mis'

misC = [5, 0, 2, 0, 6]
misCpM = [[0, 0, 0, 0, 5], [0, 0, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0], [6, 0, 0, 0, 0]]
avgE = [0.0, 0.0, 0.05211775181426432, 0.0094434947500909479, 0.098875107730717199]
stdE = [0.0, 0.0, 0.068236884720676572, 0.0059831475741941318, 0.058634350564657767]

printString=''
for a,s in zip(avgE,stdE):
    printString+=str.format('{0:.3f}',a)+' & '+str.format('{0:.3f}',s)+' & '

print printString

# w/ misclassifications
print 'sim w/ mis'

misC = [5, 0, 2, 0, 6]
misCpM = [[0, 0, 0, 0, 5], [0, 0, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0], [6, 0, 0, 0, 0]]
avgE = [0.014221621479083894, 0.0, 0.052961705904827995, 0.0094434947500909479, 0.099789256738926635]
stdE = [0.047433555577279921, 0.0, 0.06698720072634369, 0.0059831475741941318, 0.05541174093795604]

printString=''
for a,s in zip(avgE,stdE):
    printString+=str.format('{0:.3f}',a)+' & '+str.format('{0:.3f}',s)+' & '

print printString

# robot

# w/o misclassifications
print 'robot w/o mis'

misC = [5, 0, 2, 0, 6]
misCpM = [[0, 0, 0, 0, 5], [0, 0, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0], [6, 0, 0, 0, 0]]
avgE = [0.0, 0.0, 0.13221146618455182, 0.0093752580332401147, 0.080365211838967832]
stdE = [0.0, 0.0, 0.1016059181801393, 0.0098950882339561286, 0.052157951747273994]

printString=''
for a,s in zip(avgE,stdE):
    printString+=str.format('{0:.3f}',a)+' & '+str.format('{0:.3f}',s)+' & '

print printString

# w/ misclassifications
print 'robot w/ mis'

misC = [5, 0, 2, 0, 6]
misCpM = [[0, 0, 0, 0, 5], [0, 0, 0, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0], [6, 0, 0, 0, 0]]
avgE = [0.023052652841646044, 0.0, 0.14302610115835901, 0.0093752580332401147, 0.080365211838967832]
stdE = [0.046253333123738985, 0.0, 0.08211886001318236, 0.0098950882339561286, 0.052157951747273994]

printString=''
for a,s in zip(avgE,stdE):
    printString+=str.format('{0:.3f}',a)+' & '+str.format('{0:.3f}',s)+' & '

print printString
