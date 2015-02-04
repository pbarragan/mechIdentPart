# this is for the 12/14/2015 experiments

import json
import os

# 023
# /home/barragan/data12112014new//data/2014_12_13/data2Sat_Dec_13_19_06_08_2014.txt
# 024
# /home/barragan/data12112014new//data/2014_12_13/data2Sat_Dec_13_19_06_13_2014.txt
# 026
# /home/barragan/data12112014new//data/2014_12_13/data2Sat_Dec_13_19_06_41_2014.txt
# 120
# /home/barragan/data12112014new//data/2014_12_13/data2Sat_Dec_13_19_15_27_2014.txt
# 121
# /home/barragan/data12112014new//data/2014_12_13/data2Sat_Dec_13_19_15_36_2014.txt
# 123
# /home/barragan/data12112014new//data/2014_12_13/data2Sat_Dec_13_19_16_01_2014.txt
# 125
# /home/barragan/data12112014new//data/2014_12_13/data2Sat_Dec_13_19_16_27_2014.txt
# 126
# /home/barragan/data12112014new//data/2014_12_13/data2Sat_Dec_13_19_16_32_2014.txt

faults = [23,24,26,60,61,63,65,66]

filesReplace = ['data2Sat_Dec_13_20_33_41_2014.txt',
                'data2Sat_Dec_13_20_34_48_2014.txt',
                'data2Sat_Dec_13_20_35_26_2014.txt',
                'data2Sat_Dec_13_20_36_20_2014.txt',
                'data2Sat_Dec_13_20_37_12_2014.txt',
                'data2Sat_Dec_13_20_37_33_2014.txt',
                'data2Sat_Dec_13_20_37_59_2014.txt',
                'data2Sat_Dec_13_20_38_44_2014.txt']

files = ['data0Sat_Dec_13_19_00_23_2014.txt',
'data0Sat_Dec_13_19_00_38_2014.txt',
'data0Sat_Dec_13_19_00_53_2014.txt',
'data0Sat_Dec_13_19_01_08_2014.txt',
'data0Sat_Dec_13_19_01_23_2014.txt',
'data0Sat_Dec_13_19_01_38_2014.txt',
'data0Sat_Dec_13_19_01_53_2014.txt',
'data0Sat_Dec_13_19_02_08_2014.txt',
'data0Sat_Dec_13_19_02_23_2014.txt',
'data0Sat_Dec_13_19_02_38_2014.txt',
'data1Sat_Dec_13_19_02_53_2014.txt',
'data1Sat_Dec_13_19_03_08_2014.txt',
'data1Sat_Dec_13_19_03_22_2014.txt',
'data1Sat_Dec_13_19_03_37_2014.txt',
'data1Sat_Dec_13_19_03_52_2014.txt',
'data1Sat_Dec_13_19_04_07_2014.txt',
'data1Sat_Dec_13_19_04_22_2014.txt',
'data1Sat_Dec_13_19_04_38_2014.txt',
'data1Sat_Dec_13_19_04_52_2014.txt',
'data1Sat_Dec_13_19_05_07_2014.txt',
'data2Sat_Dec_13_19_05_23_2014.txt',
'data2Sat_Dec_13_19_05_38_2014.txt',
'data2Sat_Dec_13_19_05_53_2014.txt',
'data2Sat_Dec_13_19_06_08_2014.txt',
'data2Sat_Dec_13_19_06_13_2014.txt',
'data2Sat_Dec_13_19_06_25_2014.txt',
'data2Sat_Dec_13_19_06_41_2014.txt',
'data2Sat_Dec_13_19_06_46_2014.txt',
'data2Sat_Dec_13_19_07_01_2014.txt',
'data2Sat_Dec_13_19_07_16_2014.txt',
'data3Sat_Dec_13_19_07_32_2014.txt',
'data3Sat_Dec_13_19_07_46_2014.txt',
'data3Sat_Dec_13_19_08_02_2014.txt',
'data3Sat_Dec_13_19_08_17_2014.txt',
'data3Sat_Dec_13_19_08_32_2014.txt',
'data3Sat_Dec_13_19_08_48_2014.txt',
'data3Sat_Dec_13_19_09_03_2014.txt',
'data3Sat_Dec_13_19_09_18_2014.txt',
'data3Sat_Dec_13_19_09_33_2014.txt',
'data3Sat_Dec_13_19_09_48_2014.txt',
'data0Sat_Dec_13_19_10_25_2014.txt',
'data0Sat_Dec_13_19_10_40_2014.txt',
'data0Sat_Dec_13_19_10_55_2014.txt',
'data0Sat_Dec_13_19_11_10_2014.txt',
'data0Sat_Dec_13_19_11_25_2014.txt',
'data0Sat_Dec_13_19_11_40_2014.txt',
'data0Sat_Dec_13_19_11_55_2014.txt',
'data0Sat_Dec_13_19_12_10_2014.txt',
'data0Sat_Dec_13_19_12_25_2014.txt',
'data0Sat_Dec_13_19_12_40_2014.txt',
'data1Sat_Dec_13_19_12_55_2014.txt',
'data1Sat_Dec_13_19_13_11_2014.txt',
'data1Sat_Dec_13_19_13_25_2014.txt',
'data1Sat_Dec_13_19_13_40_2014.txt',
'data1Sat_Dec_13_19_13_56_2014.txt',
'data1Sat_Dec_13_19_14_11_2014.txt',
'data1Sat_Dec_13_19_14_26_2014.txt',
'data1Sat_Dec_13_19_14_41_2014.txt',
'data1Sat_Dec_13_19_14_56_2014.txt',
'data1Sat_Dec_13_19_15_11_2014.txt',
'data2Sat_Dec_13_19_15_27_2014.txt',
'data2Sat_Dec_13_19_15_36_2014.txt',
'data2Sat_Dec_13_19_15_46_2014.txt',
'data2Sat_Dec_13_19_16_01_2014.txt',
'data2Sat_Dec_13_19_16_11_2014.txt',
'data2Sat_Dec_13_19_16_27_2014.txt',
'data2Sat_Dec_13_19_16_32_2014.txt',
'data2Sat_Dec_13_19_16_46_2014.txt',
'data2Sat_Dec_13_19_17_01_2014.txt',
'data2Sat_Dec_13_19_17_16_2014.txt',
'data3Sat_Dec_13_19_17_31_2014.txt',
'data3Sat_Dec_13_19_17_46_2014.txt',
'data3Sat_Dec_13_19_18_01_2014.txt',
'data3Sat_Dec_13_19_18_16_2014.txt',
'data3Sat_Dec_13_19_18_32_2014.txt',
'data3Sat_Dec_13_19_18_47_2014.txt',
'data3Sat_Dec_13_19_19_02_2014.txt',
'data3Sat_Dec_13_19_19_16_2014.txt',
'data3Sat_Dec_13_19_19_31_2014.txt',
'data3Sat_Dec_13_19_19_47_2014.txt',
'data0Sat_Dec_13_19_20_23_2014.txt',
'data0Sat_Dec_13_19_20_38_2014.txt',
'data0Sat_Dec_13_19_20_53_2014.txt',
'data0Sat_Dec_13_19_21_09_2014.txt',
'data0Sat_Dec_13_19_21_24_2014.txt',
'data0Sat_Dec_13_19_21_39_2014.txt',
'data0Sat_Dec_13_19_21_55_2014.txt',
'data0Sat_Dec_13_19_22_10_2014.txt',
'data0Sat_Dec_13_19_22_25_2014.txt',
'data0Sat_Dec_13_19_22_40_2014.txt',
'data1Sat_Dec_13_19_22_55_2014.txt',
'data1Sat_Dec_13_19_23_11_2014.txt',
'data1Sat_Dec_13_19_23_26_2014.txt',
'data1Sat_Dec_13_19_23_41_2014.txt',
'data1Sat_Dec_13_19_23_56_2014.txt',
'data1Sat_Dec_13_19_24_12_2014.txt',
'data1Sat_Dec_13_19_24_26_2014.txt',
'data1Sat_Dec_13_19_24_42_2014.txt',
'data1Sat_Dec_13_19_24_57_2014.txt',
'data1Sat_Dec_13_19_25_12_2014.txt',
'data2Sat_Dec_13_19_25_27_2014.txt',
'data2Sat_Dec_13_19_25_41_2014.txt',
'data2Sat_Dec_13_19_25_57_2014.txt',
'data2Sat_Dec_13_19_26_12_2014.txt',
'data2Sat_Dec_13_19_26_27_2014.txt',
'data2Sat_Dec_13_19_26_42_2014.txt',
'data2Sat_Dec_13_19_26_58_2014.txt',
'data2Sat_Dec_13_19_27_13_2014.txt',
'data2Sat_Dec_13_19_27_28_2014.txt',
'data2Sat_Dec_13_19_27_43_2014.txt',
'data3Sat_Dec_13_19_27_59_2014.txt',
'data3Sat_Dec_13_19_28_14_2014.txt',
'data3Sat_Dec_13_19_28_29_2014.txt',
'data3Sat_Dec_13_19_28_44_2014.txt',
'data3Sat_Dec_13_19_28_59_2014.txt',
'data3Sat_Dec_13_19_29_14_2014.txt',
'data3Sat_Dec_13_19_29_29_2014.txt',
'data3Sat_Dec_13_19_29_45_2014.txt',
'data3Sat_Dec_13_19_30_00_2014.txt',
'data3Sat_Dec_13_19_30_16_2014.txt',
'data0Sat_Dec_13_19_30_54_2014.txt',
'data0Sat_Dec_13_19_31_09_2014.txt',
'data0Sat_Dec_13_19_31_24_2014.txt',
'data0Sat_Dec_13_19_31_39_2014.txt',
'data0Sat_Dec_13_19_31_54_2014.txt',
'data0Sat_Dec_13_19_32_10_2014.txt',
'data0Sat_Dec_13_19_32_25_2014.txt',
'data0Sat_Dec_13_19_32_40_2014.txt',
'data0Sat_Dec_13_19_32_55_2014.txt',
'data0Sat_Dec_13_19_33_10_2014.txt',
'data1Sat_Dec_13_19_33_25_2014.txt',
'data1Sat_Dec_13_19_33_40_2014.txt',
'data1Sat_Dec_13_19_33_55_2014.txt',
'data1Sat_Dec_13_19_34_10_2014.txt',
'data1Sat_Dec_13_19_34_26_2014.txt',
'data1Sat_Dec_13_19_34_41_2014.txt',
'data1Sat_Dec_13_19_34_56_2014.txt',
'data1Sat_Dec_13_19_35_11_2014.txt',
'data1Sat_Dec_13_19_35_26_2014.txt',
'data1Sat_Dec_13_19_35_41_2014.txt',
'data2Sat_Dec_13_19_35_57_2014.txt',
'data2Sat_Dec_13_19_36_12_2014.txt',
'data2Sat_Dec_13_19_36_27_2014.txt',
'data2Sat_Dec_13_19_36_42_2014.txt',
'data2Sat_Dec_13_19_36_57_2014.txt',
'data2Sat_Dec_13_19_37_12_2014.txt',
'data2Sat_Dec_13_19_37_27_2014.txt',
'data2Sat_Dec_13_19_37_43_2014.txt',
'data2Sat_Dec_13_19_37_58_2014.txt',
'data2Sat_Dec_13_19_38_14_2014.txt',
'data3Sat_Dec_13_19_38_29_2014.txt',
'data3Sat_Dec_13_19_38_44_2014.txt',
'data3Sat_Dec_13_19_38_59_2014.txt',
'data3Sat_Dec_13_19_39_14_2014.txt',
'data3Sat_Dec_13_19_39_30_2014.txt',
'data3Sat_Dec_13_19_39_45_2014.txt',
'data3Sat_Dec_13_19_40_00_2014.txt',
'data3Sat_Dec_13_19_40_15_2014.txt',
'data3Sat_Dec_13_19_40_31_2014.txt',
'data3Sat_Dec_13_19_40_46_2014.txt'
]

for f in [files[x] for x in faults]:
    print f

for i,fR in zip(faults,filesReplace):
    files[i]=fR

for f in [files[x] for x in faults]:
    print f

#exeDir = os.path.abspath(os.path.dirname(__file__))
#print exeDir
#f = open(exeDir+'/fileNames.txt','w')
#json.dump(files,f)

#a = [[0,[0,0],[0,0]],[0,[0,0],[0,0]]]
#b = [[1,[1,1],[1,1]]]

#json.dump({'a':a,'b':b},f)
#f.close()

#f2 = open(exeDir+'/fileNames.txt','r')

#files2 = json.load(f2)


#print len(files2)
#print files2
#print files2['a']

#for f in [files2[x] for x in faults]:
#    print f
