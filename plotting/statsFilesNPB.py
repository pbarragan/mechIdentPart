# this was for experiments on 12/27/2014
# same as the ones from 12/26/2014 except with bias
# varying over 10, 100, 1000, 5000, 10000 particles per filter

files = ['data0Sat_Dec_27_00_38_50_2014.txt',
'data0Sat_Dec_27_00_38_51_2014.txt',
'data0Sat_Dec_27_00_38_52_2014.txt',
'data0Sat_Dec_27_00_38_54_2014.txt',
'data0Sat_Dec_27_00_38_55_2014.txt',
'data0Sat_Dec_27_00_38_56_2014.txt',
'data0Sat_Dec_27_00_38_57_2014.txt',
'data0Sat_Dec_27_00_38_58_2014.txt',
'data0Sat_Dec_27_00_38_59_2014.txt',
'data0Sat_Dec_27_00_39_00_2014.txt',
'data0Sat_Dec_27_00_39_01_2014.txt',
'data0Sat_Dec_27_00_39_02_2014.txt',
'data0Sat_Dec_27_00_39_03_2014.txt',
'data0Sat_Dec_27_00_39_04_2014.txt',
'data0Sat_Dec_27_00_39_05_2014.txt',
'data0Sat_Dec_27_00_39_06_2014.txt',
'data0Sat_Dec_27_00_39_07_2014.txt',
'data0Sat_Dec_27_00_39_08_2014.txt',
'data0Sat_Dec_27_00_39_09_2014.txt',
'data0Sat_Dec_27_00_39_10_2014.txt',
'data0Sat_Dec_27_00_39_11_2014.txt',
'data0Sat_Dec_27_00_39_12_2014.txt',
'data0Sat_Dec_27_00_39_13_2014.txt',
'data0Sat_Dec_27_00_39_14_2014.txt',
'data0Sat_Dec_27_00_39_15_2014.txt',
'data0Sat_Dec_27_00_39_16_2014.txt',
'data0Sat_Dec_27_00_39_17_2014.txt',
'data0Sat_Dec_27_00_39_18_2014.txt',
'data0Sat_Dec_27_00_39_19_2014.txt',
'data0Sat_Dec_27_00_39_20_2014.txt',
'data0Sat_Dec_27_00_39_21_2014.txt',
'data0Sat_Dec_27_00_39_22_2014.txt',
'data0Sat_Dec_27_00_39_24_2014.txt',
'data0Sat_Dec_27_00_39_25_2014.txt',
'data0Sat_Dec_27_00_39_26_2014.txt',
'data0Sat_Dec_27_00_39_27_2014.txt',
'data0Sat_Dec_27_00_39_28_2014.txt',
'data0Sat_Dec_27_00_39_29_2014.txt',
'data0Sat_Dec_27_00_39_30_2014.txt',
'data0Sat_Dec_27_00_39_31_2014.txt',
'data0Sat_Dec_27_00_39_32_2014.txt',
'data0Sat_Dec_27_00_39_33_2014.txt',
'data0Sat_Dec_27_00_39_34_2014.txt',
'data0Sat_Dec_27_00_39_35_2014.txt',
'data0Sat_Dec_27_00_39_36_2014.txt',
'data0Sat_Dec_27_00_39_37_2014.txt',
'data0Sat_Dec_27_00_39_38_2014.txt',
'data0Sat_Dec_27_00_39_39_2014.txt',
'data0Sat_Dec_27_00_39_40_2014.txt',
'data0Sat_Dec_27_00_39_41_2014.txt',
'data1Sat_Dec_27_00_39_42_2014.txt',
'data1Sat_Dec_27_00_39_43_2014.txt',
'data1Sat_Dec_27_00_39_44_2014.txt',
'data1Sat_Dec_27_00_39_45_2014.txt',
'data1Sat_Dec_27_00_39_46_2014.txt',
'data1Sat_Dec_27_00_39_47_2014.txt',
'data1Sat_Dec_27_00_39_48_2014.txt',
'data1Sat_Dec_27_00_39_49_2014.txt',
'data1Sat_Dec_27_00_39_50_2014.txt',
'data1Sat_Dec_27_00_39_51_2014.txt',
'data1Sat_Dec_27_00_39_52_2014.txt',
'data1Sat_Dec_27_00_39_54_2014.txt',
'data1Sat_Dec_27_00_39_55_2014.txt',
'data1Sat_Dec_27_00_39_56_2014.txt',
'data1Sat_Dec_27_00_39_57_2014.txt',
'data1Sat_Dec_27_00_39_58_2014.txt',
'data1Sat_Dec_27_00_39_59_2014.txt',
'data1Sat_Dec_27_00_40_00_2014.txt',
'data1Sat_Dec_27_00_40_01_2014.txt',
'data1Sat_Dec_27_00_40_02_2014.txt',
'data1Sat_Dec_27_00_40_03_2014.txt',
'data1Sat_Dec_27_00_40_04_2014.txt',
'data1Sat_Dec_27_00_40_05_2014.txt',
'data1Sat_Dec_27_00_40_06_2014.txt',
'data1Sat_Dec_27_00_40_07_2014.txt',
'data1Sat_Dec_27_00_40_08_2014.txt',
'data1Sat_Dec_27_00_40_09_2014.txt',
'data1Sat_Dec_27_00_40_10_2014.txt',
'data1Sat_Dec_27_00_40_11_2014.txt',
'data1Sat_Dec_27_00_40_12_2014.txt',
'data1Sat_Dec_27_00_40_13_2014.txt',
'data1Sat_Dec_27_00_40_14_2014.txt',
'data1Sat_Dec_27_00_40_15_2014.txt',
'data1Sat_Dec_27_00_40_16_2014.txt',
'data1Sat_Dec_27_00_40_17_2014.txt',
'data1Sat_Dec_27_00_40_18_2014.txt',
'data1Sat_Dec_27_00_40_19_2014.txt',
'data1Sat_Dec_27_00_40_20_2014.txt',
'data1Sat_Dec_27_00_40_21_2014.txt',
'data1Sat_Dec_27_00_40_22_2014.txt',
'data1Sat_Dec_27_00_40_23_2014.txt',
'data1Sat_Dec_27_00_40_24_2014.txt',
'data1Sat_Dec_27_00_40_26_2014.txt',
'data1Sat_Dec_27_00_40_27_2014.txt',
'data1Sat_Dec_27_00_40_28_2014.txt',
'data1Sat_Dec_27_00_40_29_2014.txt',
'data1Sat_Dec_27_00_40_30_2014.txt',
'data1Sat_Dec_27_00_40_31_2014.txt',
'data1Sat_Dec_27_00_40_32_2014.txt',
'data1Sat_Dec_27_00_40_33_2014.txt',
'data2Sat_Dec_27_00_40_34_2014.txt',
'data2Sat_Dec_27_00_40_35_2014.txt',
'data2Sat_Dec_27_00_40_36_2014.txt',
'data2Sat_Dec_27_00_40_37_2014.txt',
'data2Sat_Dec_27_00_40_38_2014.txt',
'data2Sat_Dec_27_00_40_39_2014.txt',
'data2Sat_Dec_27_00_40_40_2014.txt',
'data2Sat_Dec_27_00_40_41_2014.txt',
'data2Sat_Dec_27_00_40_42_2014.txt',
'data2Sat_Dec_27_00_40_43_2014.txt',
'data2Sat_Dec_27_00_40_44_2014.txt',
'data2Sat_Dec_27_00_40_45_2014.txt',
'data2Sat_Dec_27_00_40_46_2014.txt',
'data2Sat_Dec_27_00_40_47_2014.txt',
'data2Sat_Dec_27_00_40_48_2014.txt',
'data2Sat_Dec_27_00_40_49_2014.txt',
'data2Sat_Dec_27_00_40_50_2014.txt',
'data2Sat_Dec_27_00_40_51_2014.txt',
'data2Sat_Dec_27_00_40_52_2014.txt',
'data2Sat_Dec_27_00_40_53_2014.txt',
'data2Sat_Dec_27_00_40_55_2014.txt',
'data2Sat_Dec_27_00_40_56_2014.txt',
'data2Sat_Dec_27_00_40_57_2014.txt',
'data2Sat_Dec_27_00_40_58_2014.txt',
'data2Sat_Dec_27_00_40_59_2014.txt',
'data2Sat_Dec_27_00_41_00_2014.txt',
'data2Sat_Dec_27_00_41_01_2014.txt',
'data2Sat_Dec_27_00_41_02_2014.txt',
'data2Sat_Dec_27_00_41_03_2014.txt',
'data2Sat_Dec_27_00_41_04_2014.txt',
'data2Sat_Dec_27_00_41_05_2014.txt',
'data2Sat_Dec_27_00_41_06_2014.txt',
'data2Sat_Dec_27_00_41_07_2014.txt',
'data2Sat_Dec_27_00_41_08_2014.txt',
'data2Sat_Dec_27_00_41_09_2014.txt',
'data2Sat_Dec_27_00_41_10_2014.txt',
'data2Sat_Dec_27_00_41_11_2014.txt',
'data2Sat_Dec_27_00_41_12_2014.txt',
'data2Sat_Dec_27_00_41_13_2014.txt',
'data2Sat_Dec_27_00_41_14_2014.txt',
'data2Sat_Dec_27_00_41_15_2014.txt',
'data2Sat_Dec_27_00_41_16_2014.txt',
'data2Sat_Dec_27_00_41_17_2014.txt',
'data2Sat_Dec_27_00_41_18_2014.txt',
'data2Sat_Dec_27_00_41_19_2014.txt',
'data2Sat_Dec_27_00_41_20_2014.txt',
'data2Sat_Dec_27_00_41_21_2014.txt',
'data2Sat_Dec_27_00_41_23_2014.txt',
'data2Sat_Dec_27_00_41_24_2014.txt',
'data2Sat_Dec_27_00_41_25_2014.txt',
'data3Sat_Dec_27_00_41_26_2014.txt',
'data3Sat_Dec_27_00_41_27_2014.txt',
'data3Sat_Dec_27_00_41_28_2014.txt',
'data3Sat_Dec_27_00_41_29_2014.txt',
'data3Sat_Dec_27_00_41_30_2014.txt',
'data3Sat_Dec_27_00_41_31_2014.txt',
'data3Sat_Dec_27_00_41_32_2014.txt',
'data3Sat_Dec_27_00_41_33_2014.txt',
'data3Sat_Dec_27_00_41_34_2014.txt',
'data3Sat_Dec_27_00_41_35_2014.txt',
'data3Sat_Dec_27_00_41_36_2014.txt',
'data3Sat_Dec_27_00_41_37_2014.txt',
'data3Sat_Dec_27_00_41_38_2014.txt',
'data3Sat_Dec_27_00_41_39_2014.txt',
'data3Sat_Dec_27_00_41_40_2014.txt',
'data3Sat_Dec_27_00_41_41_2014.txt',
'data3Sat_Dec_27_00_41_42_2014.txt',
'data3Sat_Dec_27_00_41_43_2014.txt',
'data3Sat_Dec_27_00_41_44_2014.txt',
'data3Sat_Dec_27_00_41_45_2014.txt',
'data3Sat_Dec_27_00_41_46_2014.txt',
'data3Sat_Dec_27_00_41_47_2014.txt',
'data3Sat_Dec_27_00_41_48_2014.txt',
'data3Sat_Dec_27_00_41_49_2014.txt',
'data3Sat_Dec_27_00_41_50_2014.txt',
'data3Sat_Dec_27_00_41_51_2014.txt',
'data3Sat_Dec_27_00_41_53_2014.txt',
'data3Sat_Dec_27_00_41_54_2014.txt',
'data3Sat_Dec_27_00_41_55_2014.txt',
'data3Sat_Dec_27_00_41_56_2014.txt',
'data3Sat_Dec_27_00_41_57_2014.txt',
'data3Sat_Dec_27_00_41_58_2014.txt',
'data3Sat_Dec_27_00_41_59_2014.txt',
'data3Sat_Dec_27_00_42_00_2014.txt',
'data3Sat_Dec_27_00_42_01_2014.txt',
'data3Sat_Dec_27_00_42_02_2014.txt',
'data3Sat_Dec_27_00_42_03_2014.txt',
'data3Sat_Dec_27_00_42_04_2014.txt',
'data3Sat_Dec_27_00_42_05_2014.txt',
'data3Sat_Dec_27_00_42_06_2014.txt',
'data3Sat_Dec_27_00_42_07_2014.txt',
'data3Sat_Dec_27_00_42_08_2014.txt',
'data3Sat_Dec_27_00_42_09_2014.txt',
'data3Sat_Dec_27_00_42_10_2014.txt',
'data3Sat_Dec_27_00_42_11_2014.txt',
'data3Sat_Dec_27_00_42_12_2014.txt',
'data3Sat_Dec_27_00_42_13_2014.txt',
'data3Sat_Dec_27_00_42_14_2014.txt',
'data3Sat_Dec_27_00_42_15_2014.txt',
'data3Sat_Dec_27_00_42_16_2014.txt',
'data0Sat_Dec_27_00_42_43_2014.txt',
'data0Sat_Dec_27_00_42_44_2014.txt',
'data0Sat_Dec_27_00_42_45_2014.txt',
'data0Sat_Dec_27_00_42_46_2014.txt',
'data0Sat_Dec_27_00_42_48_2014.txt',
'data0Sat_Dec_27_00_42_49_2014.txt',
'data0Sat_Dec_27_00_42_50_2014.txt',
'data0Sat_Dec_27_00_42_51_2014.txt',
'data0Sat_Dec_27_00_42_52_2014.txt',
'data0Sat_Dec_27_00_42_53_2014.txt',
'data0Sat_Dec_27_00_42_55_2014.txt',
'data0Sat_Dec_27_00_42_56_2014.txt',
'data0Sat_Dec_27_00_42_57_2014.txt',
'data0Sat_Dec_27_00_42_58_2014.txt',
'data0Sat_Dec_27_00_42_59_2014.txt',
'data0Sat_Dec_27_00_43_01_2014.txt',
'data0Sat_Dec_27_00_43_02_2014.txt',
'data0Sat_Dec_27_00_43_03_2014.txt',
'data0Sat_Dec_27_00_43_04_2014.txt',
'data0Sat_Dec_27_00_43_05_2014.txt',
'data0Sat_Dec_27_00_43_06_2014.txt',
'data0Sat_Dec_27_00_43_08_2014.txt',
'data0Sat_Dec_27_00_43_09_2014.txt',
'data0Sat_Dec_27_00_43_10_2014.txt',
'data0Sat_Dec_27_00_43_11_2014.txt',
'data0Sat_Dec_27_00_43_12_2014.txt',
'data0Sat_Dec_27_00_43_14_2014.txt',
'data0Sat_Dec_27_00_43_15_2014.txt',
'data0Sat_Dec_27_00_43_16_2014.txt',
'data0Sat_Dec_27_00_43_17_2014.txt',
'data0Sat_Dec_27_00_43_18_2014.txt',
'data0Sat_Dec_27_00_43_19_2014.txt',
'data0Sat_Dec_27_00_43_21_2014.txt',
'data0Sat_Dec_27_00_43_22_2014.txt',
'data0Sat_Dec_27_00_43_23_2014.txt',
'data0Sat_Dec_27_00_43_24_2014.txt',
'data0Sat_Dec_27_00_43_25_2014.txt',
'data0Sat_Dec_27_00_43_27_2014.txt',
'data0Sat_Dec_27_00_43_28_2014.txt',
'data0Sat_Dec_27_00_43_29_2014.txt',
'data0Sat_Dec_27_00_43_30_2014.txt',
'data0Sat_Dec_27_00_43_31_2014.txt',
'data0Sat_Dec_27_00_43_32_2014.txt',
'data0Sat_Dec_27_00_43_34_2014.txt',
'data0Sat_Dec_27_00_43_35_2014.txt',
'data0Sat_Dec_27_00_43_36_2014.txt',
'data0Sat_Dec_27_00_43_37_2014.txt',
'data0Sat_Dec_27_00_43_38_2014.txt',
'data0Sat_Dec_27_00_43_40_2014.txt',
'data0Sat_Dec_27_00_43_41_2014.txt',
'data1Sat_Dec_27_00_43_42_2014.txt',
'data1Sat_Dec_27_00_43_43_2014.txt',
'data1Sat_Dec_27_00_43_44_2014.txt',
'data1Sat_Dec_27_00_43_45_2014.txt',
'data1Sat_Dec_27_00_43_47_2014.txt',
'data1Sat_Dec_27_00_43_48_2014.txt',
'data1Sat_Dec_27_00_43_49_2014.txt',
'data1Sat_Dec_27_00_43_50_2014.txt',
'data1Sat_Dec_27_00_43_51_2014.txt',
'data1Sat_Dec_27_00_43_53_2014.txt',
'data1Sat_Dec_27_00_43_54_2014.txt',
'data1Sat_Dec_27_00_43_55_2014.txt',
'data1Sat_Dec_27_00_43_56_2014.txt',
'data1Sat_Dec_27_00_43_57_2014.txt',
'data1Sat_Dec_27_00_43_58_2014.txt',
'data1Sat_Dec_27_00_44_00_2014.txt',
'data1Sat_Dec_27_00_44_01_2014.txt',
'data1Sat_Dec_27_00_44_02_2014.txt',
'data1Sat_Dec_27_00_44_03_2014.txt',
'data1Sat_Dec_27_00_44_04_2014.txt',
'data1Sat_Dec_27_00_44_06_2014.txt',
'data1Sat_Dec_27_00_44_07_2014.txt',
'data1Sat_Dec_27_00_44_08_2014.txt',
'data1Sat_Dec_27_00_44_09_2014.txt',
'data1Sat_Dec_27_00_44_10_2014.txt',
'data1Sat_Dec_27_00_44_11_2014.txt',
'data1Sat_Dec_27_00_44_13_2014.txt',
'data1Sat_Dec_27_00_44_14_2014.txt',
'data1Sat_Dec_27_00_44_15_2014.txt',
'data1Sat_Dec_27_00_44_16_2014.txt',
'data1Sat_Dec_27_00_44_17_2014.txt',
'data1Sat_Dec_27_00_44_18_2014.txt',
'data1Sat_Dec_27_00_44_20_2014.txt',
'data1Sat_Dec_27_00_44_21_2014.txt',
'data1Sat_Dec_27_00_44_22_2014.txt',
'data1Sat_Dec_27_00_44_23_2014.txt',
'data1Sat_Dec_27_00_44_24_2014.txt',
'data1Sat_Dec_27_00_44_26_2014.txt',
'data1Sat_Dec_27_00_44_27_2014.txt',
'data1Sat_Dec_27_00_44_28_2014.txt',
'data1Sat_Dec_27_00_44_29_2014.txt',
'data1Sat_Dec_27_00_44_30_2014.txt',
'data1Sat_Dec_27_00_44_31_2014.txt',
'data1Sat_Dec_27_00_44_33_2014.txt',
'data1Sat_Dec_27_00_44_34_2014.txt',
'data1Sat_Dec_27_00_44_35_2014.txt',
'data1Sat_Dec_27_00_44_36_2014.txt',
'data1Sat_Dec_27_00_44_37_2014.txt',
'data1Sat_Dec_27_00_44_39_2014.txt',
'data1Sat_Dec_27_00_44_40_2014.txt',
'data2Sat_Dec_27_00_44_41_2014.txt',
'data2Sat_Dec_27_00_44_42_2014.txt',
'data2Sat_Dec_27_00_44_43_2014.txt',
'data2Sat_Dec_27_00_44_44_2014.txt',
'data2Sat_Dec_27_00_44_46_2014.txt',
'data2Sat_Dec_27_00_44_47_2014.txt',
'data2Sat_Dec_27_00_44_48_2014.txt',
'data2Sat_Dec_27_00_44_49_2014.txt',
'data2Sat_Dec_27_00_44_50_2014.txt',
'data2Sat_Dec_27_00_44_52_2014.txt',
'data2Sat_Dec_27_00_44_53_2014.txt',
'data2Sat_Dec_27_00_44_54_2014.txt',
'data2Sat_Dec_27_00_44_55_2014.txt',
'data2Sat_Dec_27_00_44_56_2014.txt',
'data2Sat_Dec_27_00_44_58_2014.txt',
'data2Sat_Dec_27_00_44_59_2014.txt',
'data2Sat_Dec_27_00_45_00_2014.txt',
'data2Sat_Dec_27_00_45_01_2014.txt',
'data2Sat_Dec_27_00_45_02_2014.txt',
'data2Sat_Dec_27_00_45_03_2014.txt',
'data2Sat_Dec_27_00_45_05_2014.txt',
'data2Sat_Dec_27_00_45_06_2014.txt',
'data2Sat_Dec_27_00_45_07_2014.txt',
'data2Sat_Dec_27_00_45_08_2014.txt',
'data2Sat_Dec_27_00_45_09_2014.txt',
'data2Sat_Dec_27_00_45_11_2014.txt',
'data2Sat_Dec_27_00_45_12_2014.txt',
'data2Sat_Dec_27_00_45_13_2014.txt',
'data2Sat_Dec_27_00_45_14_2014.txt',
'data2Sat_Dec_27_00_45_15_2014.txt',
'data2Sat_Dec_27_00_45_16_2014.txt',
'data2Sat_Dec_27_00_45_18_2014.txt',
'data2Sat_Dec_27_00_45_19_2014.txt',
'data2Sat_Dec_27_00_45_20_2014.txt',
'data2Sat_Dec_27_00_45_21_2014.txt',
'data2Sat_Dec_27_00_45_22_2014.txt',
'data2Sat_Dec_27_00_45_24_2014.txt',
'data2Sat_Dec_27_00_45_25_2014.txt',
'data2Sat_Dec_27_00_45_26_2014.txt',
'data2Sat_Dec_27_00_45_27_2014.txt',
'data2Sat_Dec_27_00_45_28_2014.txt',
'data2Sat_Dec_27_00_45_29_2014.txt',
'data2Sat_Dec_27_00_45_31_2014.txt',
'data2Sat_Dec_27_00_45_32_2014.txt',
'data2Sat_Dec_27_00_45_33_2014.txt',
'data2Sat_Dec_27_00_45_34_2014.txt',
'data2Sat_Dec_27_00_45_35_2014.txt',
'data2Sat_Dec_27_00_45_37_2014.txt',
'data2Sat_Dec_27_00_45_38_2014.txt',
'data2Sat_Dec_27_00_45_39_2014.txt',
'data3Sat_Dec_27_00_45_40_2014.txt',
'data3Sat_Dec_27_00_45_41_2014.txt',
'data3Sat_Dec_27_00_45_43_2014.txt',
'data3Sat_Dec_27_00_45_44_2014.txt',
'data3Sat_Dec_27_00_45_45_2014.txt',
'data3Sat_Dec_27_00_45_46_2014.txt',
'data3Sat_Dec_27_00_45_47_2014.txt',
'data3Sat_Dec_27_00_45_48_2014.txt',
'data3Sat_Dec_27_00_45_50_2014.txt',
'data3Sat_Dec_27_00_45_51_2014.txt',
'data3Sat_Dec_27_00_45_52_2014.txt',
'data3Sat_Dec_27_00_45_53_2014.txt',
'data3Sat_Dec_27_00_45_54_2014.txt',
'data3Sat_Dec_27_00_45_56_2014.txt',
'data3Sat_Dec_27_00_45_57_2014.txt',
'data3Sat_Dec_27_00_45_58_2014.txt',
'data3Sat_Dec_27_00_45_59_2014.txt',
'data3Sat_Dec_27_00_46_00_2014.txt',
'data3Sat_Dec_27_00_46_01_2014.txt',
'data3Sat_Dec_27_00_46_03_2014.txt',
'data3Sat_Dec_27_00_46_04_2014.txt',
'data3Sat_Dec_27_00_46_05_2014.txt',
'data3Sat_Dec_27_00_46_06_2014.txt',
'data3Sat_Dec_27_00_46_07_2014.txt',
'data3Sat_Dec_27_00_46_09_2014.txt',
'data3Sat_Dec_27_00_46_10_2014.txt',
'data3Sat_Dec_27_00_46_11_2014.txt',
'data3Sat_Dec_27_00_46_12_2014.txt',
'data3Sat_Dec_27_00_46_13_2014.txt',
'data3Sat_Dec_27_00_46_14_2014.txt',
'data3Sat_Dec_27_00_46_16_2014.txt',
'data3Sat_Dec_27_00_46_17_2014.txt',
'data3Sat_Dec_27_00_46_18_2014.txt',
'data3Sat_Dec_27_00_46_19_2014.txt',
'data3Sat_Dec_27_00_46_20_2014.txt',
'data3Sat_Dec_27_00_46_22_2014.txt',
'data3Sat_Dec_27_00_46_23_2014.txt',
'data3Sat_Dec_27_00_46_24_2014.txt',
'data3Sat_Dec_27_00_46_25_2014.txt',
'data3Sat_Dec_27_00_46_26_2014.txt',
'data3Sat_Dec_27_00_46_27_2014.txt',
'data3Sat_Dec_27_00_46_29_2014.txt',
'data3Sat_Dec_27_00_46_30_2014.txt',
'data3Sat_Dec_27_00_46_31_2014.txt',
'data3Sat_Dec_27_00_46_32_2014.txt',
'data3Sat_Dec_27_00_46_33_2014.txt',
'data3Sat_Dec_27_00_46_35_2014.txt',
'data3Sat_Dec_27_00_46_36_2014.txt',
'data3Sat_Dec_27_00_46_37_2014.txt',
'data3Sat_Dec_27_00_46_38_2014.txt',
'data0Sat_Dec_27_00_47_05_2014.txt',
'data0Sat_Dec_27_00_47_07_2014.txt',
'data0Sat_Dec_27_00_47_08_2014.txt',
'data0Sat_Dec_27_00_47_10_2014.txt',
'data0Sat_Dec_27_00_47_12_2014.txt',
'data0Sat_Dec_27_00_47_13_2014.txt',
'data0Sat_Dec_27_00_47_15_2014.txt',
'data0Sat_Dec_27_00_47_17_2014.txt',
'data0Sat_Dec_27_00_47_18_2014.txt',
'data0Sat_Dec_27_00_47_20_2014.txt',
'data0Sat_Dec_27_00_47_22_2014.txt',
'data0Sat_Dec_27_00_47_23_2014.txt',
'data0Sat_Dec_27_00_47_25_2014.txt',
'data0Sat_Dec_27_00_47_27_2014.txt',
'data0Sat_Dec_27_00_47_28_2014.txt',
'data0Sat_Dec_27_00_47_30_2014.txt',
'data0Sat_Dec_27_00_47_31_2014.txt',
'data0Sat_Dec_27_00_47_33_2014.txt',
'data0Sat_Dec_27_00_47_35_2014.txt',
'data0Sat_Dec_27_00_47_36_2014.txt',
'data0Sat_Dec_27_00_47_38_2014.txt',
'data0Sat_Dec_27_00_47_40_2014.txt',
'data0Sat_Dec_27_00_47_41_2014.txt',
'data0Sat_Dec_27_00_47_43_2014.txt',
'data0Sat_Dec_27_00_47_45_2014.txt',
'data0Sat_Dec_27_00_47_46_2014.txt',
'data0Sat_Dec_27_00_47_48_2014.txt',
'data0Sat_Dec_27_00_47_50_2014.txt',
'data0Sat_Dec_27_00_47_51_2014.txt',
'data0Sat_Dec_27_00_47_53_2014.txt',
'data0Sat_Dec_27_00_47_55_2014.txt',
'data0Sat_Dec_27_00_47_56_2014.txt',
'data0Sat_Dec_27_00_47_58_2014.txt',
'data0Sat_Dec_27_00_48_00_2014.txt',
'data0Sat_Dec_27_00_48_01_2014.txt',
'data0Sat_Dec_27_00_48_03_2014.txt',
'data0Sat_Dec_27_00_48_05_2014.txt',
'data0Sat_Dec_27_00_48_06_2014.txt',
'data0Sat_Dec_27_00_48_08_2014.txt',
'data0Sat_Dec_27_00_48_09_2014.txt',
'data0Sat_Dec_27_00_48_11_2014.txt',
'data0Sat_Dec_27_00_48_13_2014.txt',
'data0Sat_Dec_27_00_48_14_2014.txt',
'data0Sat_Dec_27_00_48_16_2014.txt',
'data0Sat_Dec_27_00_48_18_2014.txt',
'data0Sat_Dec_27_00_48_19_2014.txt',
'data0Sat_Dec_27_00_48_21_2014.txt',
'data0Sat_Dec_27_00_48_23_2014.txt',
'data0Sat_Dec_27_00_48_24_2014.txt',
'data0Sat_Dec_27_00_48_26_2014.txt',
'data1Sat_Dec_27_00_48_28_2014.txt',
'data1Sat_Dec_27_00_48_29_2014.txt',
'data1Sat_Dec_27_00_48_31_2014.txt',
'data1Sat_Dec_27_00_48_32_2014.txt',
'data1Sat_Dec_27_00_48_34_2014.txt',
'data1Sat_Dec_27_00_48_36_2014.txt',
'data1Sat_Dec_27_00_48_37_2014.txt',
'data1Sat_Dec_27_00_48_39_2014.txt',
'data1Sat_Dec_27_00_48_41_2014.txt',
'data1Sat_Dec_27_00_48_42_2014.txt',
'data1Sat_Dec_27_00_48_44_2014.txt',
'data1Sat_Dec_27_00_48_46_2014.txt',
'data1Sat_Dec_27_00_48_47_2014.txt',
'data1Sat_Dec_27_00_48_49_2014.txt',
'data1Sat_Dec_27_00_48_50_2014.txt',
'data1Sat_Dec_27_00_48_52_2014.txt',
'data1Sat_Dec_27_00_48_54_2014.txt',
'data1Sat_Dec_27_00_48_55_2014.txt',
'data1Sat_Dec_27_00_48_57_2014.txt',
'data1Sat_Dec_27_00_48_59_2014.txt',
'data1Sat_Dec_27_00_49_00_2014.txt',
'data1Sat_Dec_27_00_49_02_2014.txt',
'data1Sat_Dec_27_00_49_04_2014.txt',
'data1Sat_Dec_27_00_49_05_2014.txt',
'data1Sat_Dec_27_00_49_07_2014.txt',
'data1Sat_Dec_27_00_49_08_2014.txt',
'data1Sat_Dec_27_00_49_10_2014.txt',
'data1Sat_Dec_27_00_49_12_2014.txt',
'data1Sat_Dec_27_00_49_13_2014.txt',
'data1Sat_Dec_27_00_49_15_2014.txt',
'data1Sat_Dec_27_00_49_17_2014.txt',
'data1Sat_Dec_27_00_49_18_2014.txt',
'data1Sat_Dec_27_00_49_20_2014.txt',
'data1Sat_Dec_27_00_49_22_2014.txt',
'data1Sat_Dec_27_00_49_23_2014.txt',
'data1Sat_Dec_27_00_49_25_2014.txt',
'data1Sat_Dec_27_00_49_27_2014.txt',
'data1Sat_Dec_27_00_49_28_2014.txt',
'data1Sat_Dec_27_00_49_30_2014.txt',
'data1Sat_Dec_27_00_49_31_2014.txt',
'data1Sat_Dec_27_00_49_33_2014.txt',
'data1Sat_Dec_27_00_49_35_2014.txt',
'data1Sat_Dec_27_00_49_36_2014.txt',
'data1Sat_Dec_27_00_49_38_2014.txt',
'data1Sat_Dec_27_00_49_40_2014.txt',
'data1Sat_Dec_27_00_49_41_2014.txt',
'data1Sat_Dec_27_00_49_43_2014.txt',
'data1Sat_Dec_27_00_49_45_2014.txt',
'data1Sat_Dec_27_00_49_46_2014.txt',
'data1Sat_Dec_27_00_49_48_2014.txt',
'data2Sat_Dec_27_00_49_49_2014.txt',
'data2Sat_Dec_27_00_49_51_2014.txt',
'data2Sat_Dec_27_00_49_53_2014.txt',
'data2Sat_Dec_27_00_49_54_2014.txt',
'data2Sat_Dec_27_00_49_56_2014.txt',
'data2Sat_Dec_27_00_49_58_2014.txt',
'data2Sat_Dec_27_00_49_59_2014.txt',
'data2Sat_Dec_27_00_50_01_2014.txt',
'data2Sat_Dec_27_00_50_03_2014.txt',
'data2Sat_Dec_27_00_50_04_2014.txt',
'data2Sat_Dec_27_00_50_06_2014.txt',
'data2Sat_Dec_27_00_50_08_2014.txt',
'data2Sat_Dec_27_00_50_09_2014.txt',
'data2Sat_Dec_27_00_50_11_2014.txt',
'data2Sat_Dec_27_00_50_13_2014.txt',
'data2Sat_Dec_27_00_50_14_2014.txt',
'data2Sat_Dec_27_00_50_16_2014.txt',
'data2Sat_Dec_27_00_50_17_2014.txt',
'data2Sat_Dec_27_00_50_19_2014.txt',
'data2Sat_Dec_27_00_50_21_2014.txt',
'data2Sat_Dec_27_00_50_22_2014.txt',
'data2Sat_Dec_27_00_50_24_2014.txt',
'data2Sat_Dec_27_00_50_26_2014.txt',
'data2Sat_Dec_27_00_50_27_2014.txt',
'data2Sat_Dec_27_00_50_29_2014.txt',
'data2Sat_Dec_27_00_50_31_2014.txt',
'data2Sat_Dec_27_00_50_32_2014.txt',
'data2Sat_Dec_27_00_50_34_2014.txt',
'data2Sat_Dec_27_00_50_35_2014.txt',
'data2Sat_Dec_27_00_50_37_2014.txt',
'data2Sat_Dec_27_00_50_39_2014.txt',
'data2Sat_Dec_27_00_50_40_2014.txt',
'data2Sat_Dec_27_00_50_42_2014.txt',
'data2Sat_Dec_27_00_50_44_2014.txt',
'data2Sat_Dec_27_00_50_45_2014.txt',
'data2Sat_Dec_27_00_50_47_2014.txt',
'data2Sat_Dec_27_00_50_49_2014.txt',
'data2Sat_Dec_27_00_50_50_2014.txt',
'data2Sat_Dec_27_00_50_52_2014.txt',
'data2Sat_Dec_27_00_50_54_2014.txt',
'data2Sat_Dec_27_00_50_55_2014.txt',
'data2Sat_Dec_27_00_50_57_2014.txt',
'data2Sat_Dec_27_00_50_59_2014.txt',
'data2Sat_Dec_27_00_51_00_2014.txt',
'data2Sat_Dec_27_00_51_02_2014.txt',
'data2Sat_Dec_27_00_51_03_2014.txt',
'data2Sat_Dec_27_00_51_05_2014.txt',
'data2Sat_Dec_27_00_51_07_2014.txt',
'data2Sat_Dec_27_00_51_08_2014.txt',
'data2Sat_Dec_27_00_51_10_2014.txt',
'data3Sat_Dec_27_00_51_12_2014.txt',
'data3Sat_Dec_27_00_51_13_2014.txt',
'data3Sat_Dec_27_00_51_15_2014.txt',
'data3Sat_Dec_27_00_51_17_2014.txt',
'data3Sat_Dec_27_00_51_18_2014.txt',
'data3Sat_Dec_27_00_51_20_2014.txt',
'data3Sat_Dec_27_00_51_22_2014.txt',
'data3Sat_Dec_27_00_51_23_2014.txt',
'data3Sat_Dec_27_00_51_25_2014.txt',
'data3Sat_Dec_27_00_51_27_2014.txt',
'data3Sat_Dec_27_00_51_28_2014.txt',
'data3Sat_Dec_27_00_51_30_2014.txt',
'data3Sat_Dec_27_00_51_31_2014.txt',
'data3Sat_Dec_27_00_51_33_2014.txt',
'data3Sat_Dec_27_00_51_35_2014.txt',
'data3Sat_Dec_27_00_51_36_2014.txt',
'data3Sat_Dec_27_00_51_38_2014.txt',
'data3Sat_Dec_27_00_51_40_2014.txt',
'data3Sat_Dec_27_00_51_41_2014.txt',
'data3Sat_Dec_27_00_51_43_2014.txt',
'data3Sat_Dec_27_00_51_45_2014.txt',
'data3Sat_Dec_27_00_51_46_2014.txt',
'data3Sat_Dec_27_00_51_48_2014.txt',
'data3Sat_Dec_27_00_51_50_2014.txt',
'data3Sat_Dec_27_00_51_51_2014.txt',
'data3Sat_Dec_27_00_51_53_2014.txt',
'data3Sat_Dec_27_00_51_55_2014.txt',
'data3Sat_Dec_27_00_51_56_2014.txt',
'data3Sat_Dec_27_00_51_58_2014.txt',
'data3Sat_Dec_27_00_51_59_2014.txt',
'data3Sat_Dec_27_00_52_01_2014.txt',
'data3Sat_Dec_27_00_52_03_2014.txt',
'data3Sat_Dec_27_00_52_04_2014.txt',
'data3Sat_Dec_27_00_52_06_2014.txt',
'data3Sat_Dec_27_00_52_08_2014.txt',
'data3Sat_Dec_27_00_52_09_2014.txt',
'data3Sat_Dec_27_00_52_11_2014.txt',
'data3Sat_Dec_27_00_52_13_2014.txt',
'data3Sat_Dec_27_00_52_14_2014.txt',
'data3Sat_Dec_27_00_52_16_2014.txt',
'data3Sat_Dec_27_00_52_18_2014.txt',
'data3Sat_Dec_27_00_52_19_2014.txt',
'data3Sat_Dec_27_00_52_21_2014.txt',
'data3Sat_Dec_27_00_52_23_2014.txt',
'data3Sat_Dec_27_00_52_24_2014.txt',
'data3Sat_Dec_27_00_52_26_2014.txt',
'data3Sat_Dec_27_00_52_27_2014.txt',
'data3Sat_Dec_27_00_52_29_2014.txt',
'data3Sat_Dec_27_00_52_31_2014.txt',
'data3Sat_Dec_27_00_52_32_2014.txt',
'data0Sat_Dec_27_00_53_00_2014.txt',
'data0Sat_Dec_27_00_53_07_2014.txt',
'data0Sat_Dec_27_00_53_15_2014.txt',
'data0Sat_Dec_27_00_53_22_2014.txt',
'data0Sat_Dec_27_00_53_30_2014.txt',
'data0Sat_Dec_27_00_53_38_2014.txt',
'data0Sat_Dec_27_00_53_46_2014.txt',
'data0Sat_Dec_27_00_53_53_2014.txt',
'data0Sat_Dec_27_00_54_01_2014.txt',
'data0Sat_Dec_27_00_54_08_2014.txt',
'data0Sat_Dec_27_00_54_16_2014.txt',
'data0Sat_Dec_27_00_54_24_2014.txt',
'data0Sat_Dec_27_00_54_31_2014.txt',
'data0Sat_Dec_27_00_54_39_2014.txt',
'data0Sat_Dec_27_00_54_46_2014.txt',
'data0Sat_Dec_27_00_54_54_2014.txt',
'data0Sat_Dec_27_00_55_02_2014.txt',
'data0Sat_Dec_27_00_55_10_2014.txt',
'data0Sat_Dec_27_00_55_17_2014.txt',
'data0Sat_Dec_27_00_55_25_2014.txt',
'data0Sat_Dec_27_00_55_33_2014.txt',
'data0Sat_Dec_27_00_55_40_2014.txt',
'data0Sat_Dec_27_00_55_48_2014.txt',
'data0Sat_Dec_27_00_55_56_2014.txt',
'data0Sat_Dec_27_00_56_03_2014.txt',
'data0Sat_Dec_27_00_56_11_2014.txt',
'data0Sat_Dec_27_00_56_18_2014.txt',
'data0Sat_Dec_27_00_56_26_2014.txt',
'data0Sat_Dec_27_00_56_34_2014.txt',
'data0Sat_Dec_27_00_56_42_2014.txt',
'data0Sat_Dec_27_00_56_49_2014.txt',
'data0Sat_Dec_27_00_56_57_2014.txt',
'data0Sat_Dec_27_00_57_05_2014.txt',
'data0Sat_Dec_27_00_57_12_2014.txt',
'data0Sat_Dec_27_00_57_20_2014.txt',
'data0Sat_Dec_27_00_57_27_2014.txt',
'data0Sat_Dec_27_00_57_35_2014.txt',
'data0Sat_Dec_27_00_57_43_2014.txt',
'data0Sat_Dec_27_00_57_50_2014.txt',
'data0Sat_Dec_27_00_57_58_2014.txt',
'data0Sat_Dec_27_00_58_06_2014.txt',
'data0Sat_Dec_27_00_58_14_2014.txt',
'data0Sat_Dec_27_00_58_21_2014.txt',
'data0Sat_Dec_27_00_58_29_2014.txt',
'data0Sat_Dec_27_00_58_38_2014.txt',
'data0Sat_Dec_27_00_58_45_2014.txt',
'data0Sat_Dec_27_00_58_53_2014.txt',
'data0Sat_Dec_27_00_59_01_2014.txt',
'data0Sat_Dec_27_00_59_08_2014.txt',
'data0Sat_Dec_27_00_59_16_2014.txt',
'data1Sat_Dec_27_00_59_24_2014.txt',
'data1Sat_Dec_27_00_59_31_2014.txt',
'data1Sat_Dec_27_00_59_39_2014.txt',
'data1Sat_Dec_27_00_59_46_2014.txt',
'data1Sat_Dec_27_00_59_54_2014.txt',
'data1Sat_Dec_27_01_00_02_2014.txt',
'data1Sat_Dec_27_01_00_10_2014.txt',
'data1Sat_Dec_27_01_00_17_2014.txt',
'data1Sat_Dec_27_01_00_25_2014.txt',
'data1Sat_Dec_27_01_00_32_2014.txt',
'data1Sat_Dec_27_01_00_40_2014.txt',
'data1Sat_Dec_27_01_00_48_2014.txt',
'data1Sat_Dec_27_01_00_55_2014.txt',
'data1Sat_Dec_27_01_01_03_2014.txt',
'data1Sat_Dec_27_01_01_11_2014.txt',
'data1Sat_Dec_27_01_01_18_2014.txt',
'data1Sat_Dec_27_01_01_26_2014.txt',
'data1Sat_Dec_27_01_01_34_2014.txt',
'data1Sat_Dec_27_01_01_41_2014.txt',
'data1Sat_Dec_27_01_01_49_2014.txt',
'data1Sat_Dec_27_01_01_56_2014.txt',
'data1Sat_Dec_27_01_02_04_2014.txt',
'data1Sat_Dec_27_01_02_12_2014.txt',
'data1Sat_Dec_27_01_02_19_2014.txt',
'data1Sat_Dec_27_01_02_27_2014.txt',
'data1Sat_Dec_27_01_02_35_2014.txt',
'data1Sat_Dec_27_01_02_42_2014.txt',
'data1Sat_Dec_27_01_02_50_2014.txt',
'data1Sat_Dec_27_01_02_58_2014.txt',
'data1Sat_Dec_27_01_03_06_2014.txt',
'data1Sat_Dec_27_01_03_13_2014.txt',
'data1Sat_Dec_27_01_03_21_2014.txt',
'data1Sat_Dec_27_01_03_29_2014.txt',
'data1Sat_Dec_27_01_03_36_2014.txt',
'data1Sat_Dec_27_01_03_44_2014.txt',
'data1Sat_Dec_27_01_03_51_2014.txt',
'data1Sat_Dec_27_01_03_59_2014.txt',
'data1Sat_Dec_27_01_04_07_2014.txt',
'data1Sat_Dec_27_01_04_14_2014.txt',
'data1Sat_Dec_27_01_04_22_2014.txt',
'data1Sat_Dec_27_01_04_30_2014.txt',
'data1Sat_Dec_27_01_04_37_2014.txt',
'data1Sat_Dec_27_01_04_45_2014.txt',
'data1Sat_Dec_27_01_04_53_2014.txt',
'data1Sat_Dec_27_01_05_01_2014.txt',
'data1Sat_Dec_27_01_05_08_2014.txt',
'data1Sat_Dec_27_01_05_16_2014.txt',
'data1Sat_Dec_27_01_05_24_2014.txt',
'data1Sat_Dec_27_01_05_32_2014.txt',
'data1Sat_Dec_27_01_05_39_2014.txt',
'data2Sat_Dec_27_01_05_47_2014.txt',
'data2Sat_Dec_27_01_05_55_2014.txt',
'data2Sat_Dec_27_01_06_03_2014.txt',
'data2Sat_Dec_27_01_06_10_2014.txt',
'data2Sat_Dec_27_01_06_18_2014.txt',
'data2Sat_Dec_27_01_06_26_2014.txt',
'data2Sat_Dec_27_01_06_34_2014.txt',
'data2Sat_Dec_27_01_06_41_2014.txt',
'data2Sat_Dec_27_01_06_49_2014.txt',
'data2Sat_Dec_27_01_06_56_2014.txt',
'data2Sat_Dec_27_01_07_04_2014.txt',
'data2Sat_Dec_27_01_07_12_2014.txt',
'data2Sat_Dec_27_01_07_20_2014.txt',
'data2Sat_Dec_27_01_07_27_2014.txt',
'data2Sat_Dec_27_01_07_35_2014.txt',
'data2Sat_Dec_27_01_07_43_2014.txt',
'data2Sat_Dec_27_01_07_50_2014.txt',
'data2Sat_Dec_27_01_07_58_2014.txt',
'data2Sat_Dec_27_01_08_05_2014.txt',
'data2Sat_Dec_27_01_08_13_2014.txt',
'data2Sat_Dec_27_01_08_21_2014.txt',
'data2Sat_Dec_27_01_08_28_2014.txt',
'data2Sat_Dec_27_01_08_36_2014.txt',
'data2Sat_Dec_27_01_08_44_2014.txt',
'data2Sat_Dec_27_01_08_51_2014.txt',
'data2Sat_Dec_27_01_08_59_2014.txt',
'data2Sat_Dec_27_01_09_07_2014.txt',
'data2Sat_Dec_27_01_09_14_2014.txt',
'data2Sat_Dec_27_01_09_22_2014.txt',
'data2Sat_Dec_27_01_09_30_2014.txt',
'data2Sat_Dec_27_01_09_38_2014.txt',
'data2Sat_Dec_27_01_09_46_2014.txt',
'data2Sat_Dec_27_01_09_54_2014.txt',
'data2Sat_Dec_27_01_10_01_2014.txt',
'data2Sat_Dec_27_01_10_09_2014.txt',
'data2Sat_Dec_27_01_10_17_2014.txt',
'data2Sat_Dec_27_01_10_25_2014.txt',
'data2Sat_Dec_27_01_10_32_2014.txt',
'data2Sat_Dec_27_01_10_40_2014.txt',
'data2Sat_Dec_27_01_10_47_2014.txt',
'data2Sat_Dec_27_01_10_55_2014.txt',
'data2Sat_Dec_27_01_11_03_2014.txt',
'data2Sat_Dec_27_01_11_10_2014.txt',
'data2Sat_Dec_27_01_11_18_2014.txt',
'data2Sat_Dec_27_01_11_25_2014.txt',
'data2Sat_Dec_27_01_11_33_2014.txt',
'data2Sat_Dec_27_01_11_40_2014.txt',
'data2Sat_Dec_27_01_11_48_2014.txt',
'data2Sat_Dec_27_01_11_56_2014.txt',
'data2Sat_Dec_27_01_12_03_2014.txt',
'data3Sat_Dec_27_01_12_11_2014.txt',
'data3Sat_Dec_27_01_12_19_2014.txt',
'data3Sat_Dec_27_01_12_26_2014.txt',
'data3Sat_Dec_27_01_12_34_2014.txt',
'data3Sat_Dec_27_01_12_42_2014.txt',
'data3Sat_Dec_27_01_12_50_2014.txt',
'data3Sat_Dec_27_01_12_57_2014.txt',
'data3Sat_Dec_27_01_13_05_2014.txt',
'data3Sat_Dec_27_01_13_13_2014.txt',
'data3Sat_Dec_27_01_13_20_2014.txt',
'data3Sat_Dec_27_01_13_28_2014.txt',
'data3Sat_Dec_27_01_13_35_2014.txt',
'data3Sat_Dec_27_01_13_43_2014.txt',
'data3Sat_Dec_27_01_13_51_2014.txt',
'data3Sat_Dec_27_01_13_59_2014.txt',
'data3Sat_Dec_27_01_14_06_2014.txt',
'data3Sat_Dec_27_01_14_14_2014.txt',
'data3Sat_Dec_27_01_14_22_2014.txt',
'data3Sat_Dec_27_01_14_29_2014.txt',
'data3Sat_Dec_27_01_14_37_2014.txt',
'data3Sat_Dec_27_01_14_44_2014.txt',
'data3Sat_Dec_27_01_14_53_2014.txt',
'data3Sat_Dec_27_01_15_00_2014.txt',
'data3Sat_Dec_27_01_15_08_2014.txt',
'data3Sat_Dec_27_01_15_16_2014.txt',
'data3Sat_Dec_27_01_15_24_2014.txt',
'data3Sat_Dec_27_01_15_31_2014.txt',
'data3Sat_Dec_27_01_15_39_2014.txt',
'data3Sat_Dec_27_01_15_47_2014.txt',
'data3Sat_Dec_27_01_15_55_2014.txt',
'data3Sat_Dec_27_01_16_03_2014.txt',
'data3Sat_Dec_27_01_16_10_2014.txt',
'data3Sat_Dec_27_01_16_18_2014.txt',
'data3Sat_Dec_27_01_16_26_2014.txt',
'data3Sat_Dec_27_01_16_33_2014.txt',
'data3Sat_Dec_27_01_16_41_2014.txt',
'data3Sat_Dec_27_01_16_49_2014.txt',
'data3Sat_Dec_27_01_16_57_2014.txt',
'data3Sat_Dec_27_01_17_04_2014.txt',
'data3Sat_Dec_27_01_17_12_2014.txt',
'data3Sat_Dec_27_01_17_19_2014.txt',
'data3Sat_Dec_27_01_17_27_2014.txt',
'data3Sat_Dec_27_01_17_35_2014.txt',
'data3Sat_Dec_27_01_17_43_2014.txt',
'data3Sat_Dec_27_01_17_51_2014.txt',
'data3Sat_Dec_27_01_17_58_2014.txt',
'data3Sat_Dec_27_01_18_06_2014.txt',
'data3Sat_Dec_27_01_18_13_2014.txt',
'data3Sat_Dec_27_01_18_21_2014.txt',
'data3Sat_Dec_27_01_18_29_2014.txt',
'data0Sat_Dec_27_01_19_02_2014.txt',
'data0Sat_Dec_27_01_19_17_2014.txt',
'data0Sat_Dec_27_01_19_32_2014.txt',
'data0Sat_Dec_27_01_19_47_2014.txt',
'data0Sat_Dec_27_01_20_03_2014.txt',
'data0Sat_Dec_27_01_20_18_2014.txt',
'data0Sat_Dec_27_01_20_33_2014.txt',
'data0Sat_Dec_27_01_20_48_2014.txt',
'data0Sat_Dec_27_01_21_04_2014.txt',
'data0Sat_Dec_27_01_21_19_2014.txt',
'data0Sat_Dec_27_01_21_35_2014.txt',
'data0Sat_Dec_27_01_21_50_2014.txt',
'data0Sat_Dec_27_01_22_05_2014.txt',
'data0Sat_Dec_27_01_22_21_2014.txt',
'data0Sat_Dec_27_01_22_36_2014.txt',
'data0Sat_Dec_27_01_22_50_2014.txt',
'data0Sat_Dec_27_01_23_06_2014.txt',
'data0Sat_Dec_27_01_23_22_2014.txt',
'data0Sat_Dec_27_01_23_37_2014.txt',
'data0Sat_Dec_27_01_23_52_2014.txt',
'data0Sat_Dec_27_01_24_07_2014.txt',
'data0Sat_Dec_27_01_24_23_2014.txt',
'data0Sat_Dec_27_01_24_38_2014.txt',
'data0Sat_Dec_27_01_24_53_2014.txt',
'data0Sat_Dec_27_01_25_08_2014.txt',
'data0Sat_Dec_27_01_25_23_2014.txt',
'data0Sat_Dec_27_01_25_38_2014.txt',
'data0Sat_Dec_27_01_25_53_2014.txt',
'data0Sat_Dec_27_01_26_08_2014.txt',
'data0Sat_Dec_27_01_26_24_2014.txt',
'data0Sat_Dec_27_01_26_39_2014.txt',
'data0Sat_Dec_27_01_26_54_2014.txt',
'data0Sat_Dec_27_01_27_09_2014.txt',
'data0Sat_Dec_27_01_27_24_2014.txt',
'data0Sat_Dec_27_01_27_39_2014.txt',
'data0Sat_Dec_27_01_27_54_2014.txt',
'data0Sat_Dec_27_01_28_09_2014.txt',
'data0Sat_Dec_27_01_28_24_2014.txt',
'data0Sat_Dec_27_01_28_39_2014.txt',
'data0Sat_Dec_27_01_28_54_2014.txt',
'data0Sat_Dec_27_01_29_09_2014.txt',
'data0Sat_Dec_27_01_29_24_2014.txt',
'data0Sat_Dec_27_01_29_40_2014.txt',
'data0Sat_Dec_27_01_29_55_2014.txt',
'data0Sat_Dec_27_01_30_10_2014.txt',
'data0Sat_Dec_27_01_30_25_2014.txt',
'data0Sat_Dec_27_01_30_41_2014.txt',
'data0Sat_Dec_27_01_30_56_2014.txt',
'data0Sat_Dec_27_01_31_11_2014.txt',
'data0Sat_Dec_27_01_31_26_2014.txt',
'data1Sat_Dec_27_01_31_41_2014.txt',
'data1Sat_Dec_27_01_31_56_2014.txt',
'data1Sat_Dec_27_01_32_12_2014.txt',
'data1Sat_Dec_27_01_32_27_2014.txt',
'data1Sat_Dec_27_01_32_42_2014.txt',
'data1Sat_Dec_27_01_32_57_2014.txt',
'data1Sat_Dec_27_01_33_12_2014.txt',
'data1Sat_Dec_27_01_33_27_2014.txt',
'data1Sat_Dec_27_01_33_43_2014.txt',
'data1Sat_Dec_27_01_33_57_2014.txt',
'data1Sat_Dec_27_01_34_12_2014.txt',
'data1Sat_Dec_27_01_34_27_2014.txt',
'data1Sat_Dec_27_01_34_43_2014.txt',
'data1Sat_Dec_27_01_34_57_2014.txt',
'data1Sat_Dec_27_01_35_12_2014.txt',
'data1Sat_Dec_27_01_35_27_2014.txt',
'data1Sat_Dec_27_01_35_43_2014.txt',
'data1Sat_Dec_27_01_35_58_2014.txt',
'data1Sat_Dec_27_01_36_14_2014.txt',
'data1Sat_Dec_27_01_36_29_2014.txt',
'data1Sat_Dec_27_01_36_44_2014.txt',
'data1Sat_Dec_27_01_36_59_2014.txt',
'data1Sat_Dec_27_01_37_14_2014.txt',
'data1Sat_Dec_27_01_37_28_2014.txt',
'data1Sat_Dec_27_01_37_43_2014.txt',
'data1Sat_Dec_27_01_37_58_2014.txt',
'data1Sat_Dec_27_01_38_13_2014.txt',
'data1Sat_Dec_27_01_38_28_2014.txt',
'data1Sat_Dec_27_01_38_43_2014.txt',
'data1Sat_Dec_27_01_38_58_2014.txt',
'data1Sat_Dec_27_01_39_14_2014.txt',
'data1Sat_Dec_27_01_39_29_2014.txt',
'data1Sat_Dec_27_01_39_44_2014.txt',
'data1Sat_Dec_27_01_40_00_2014.txt',
'data1Sat_Dec_27_01_40_15_2014.txt',
'data1Sat_Dec_27_01_40_30_2014.txt',
'data1Sat_Dec_27_01_40_45_2014.txt',
'data1Sat_Dec_27_01_41_00_2014.txt',
'data1Sat_Dec_27_01_41_16_2014.txt',
'data1Sat_Dec_27_01_41_31_2014.txt',
'data1Sat_Dec_27_01_41_46_2014.txt',
'data1Sat_Dec_27_01_42_01_2014.txt',
'data1Sat_Dec_27_01_42_15_2014.txt',
'data1Sat_Dec_27_01_42_31_2014.txt',
'data1Sat_Dec_27_01_42_46_2014.txt',
'data1Sat_Dec_27_01_43_01_2014.txt',
'data1Sat_Dec_27_01_43_16_2014.txt',
'data1Sat_Dec_27_01_43_31_2014.txt',
'data1Sat_Dec_27_01_43_46_2014.txt',
'data1Sat_Dec_27_01_44_01_2014.txt',
'data2Sat_Dec_27_01_44_16_2014.txt',
'data2Sat_Dec_27_01_44_31_2014.txt',
'data2Sat_Dec_27_01_44_46_2014.txt',
'data2Sat_Dec_27_01_45_02_2014.txt',
'data2Sat_Dec_27_01_45_17_2014.txt',
'data2Sat_Dec_27_01_45_33_2014.txt',
'data2Sat_Dec_27_01_45_47_2014.txt',
'data2Sat_Dec_27_01_46_02_2014.txt',
'data2Sat_Dec_27_01_46_17_2014.txt',
'data2Sat_Dec_27_01_46_33_2014.txt',
'data2Sat_Dec_27_01_46_47_2014.txt',
'data2Sat_Dec_27_01_47_02_2014.txt',
'data2Sat_Dec_27_01_47_19_2014.txt',
'data2Sat_Dec_27_01_47_33_2014.txt',
'data2Sat_Dec_27_01_47_49_2014.txt',
'data2Sat_Dec_27_01_48_04_2014.txt',
'data2Sat_Dec_27_01_48_19_2014.txt',
'data2Sat_Dec_27_01_48_35_2014.txt',
'data2Sat_Dec_27_01_48_49_2014.txt',
'data2Sat_Dec_27_01_49_05_2014.txt',
'data2Sat_Dec_27_01_49_20_2014.txt',
'data2Sat_Dec_27_01_49_35_2014.txt',
'data2Sat_Dec_27_01_49_49_2014.txt',
'data2Sat_Dec_27_01_50_05_2014.txt',
'data2Sat_Dec_27_01_50_21_2014.txt',
'data2Sat_Dec_27_01_50_36_2014.txt',
'data2Sat_Dec_27_01_50_50_2014.txt',
'data2Sat_Dec_27_01_51_05_2014.txt',
'data2Sat_Dec_27_01_51_20_2014.txt',
'data2Sat_Dec_27_01_51_35_2014.txt',
'data2Sat_Dec_27_01_51_50_2014.txt',
'data2Sat_Dec_27_01_52_06_2014.txt',
'data2Sat_Dec_27_01_52_21_2014.txt',
'data2Sat_Dec_27_01_52_36_2014.txt',
'data2Sat_Dec_27_01_52_51_2014.txt',
'data2Sat_Dec_27_01_53_06_2014.txt',
'data2Sat_Dec_27_01_53_21_2014.txt',
'data2Sat_Dec_27_01_53_36_2014.txt',
'data2Sat_Dec_27_01_53_51_2014.txt',
'data2Sat_Dec_27_01_54_06_2014.txt',
'data2Sat_Dec_27_01_54_20_2014.txt',
'data2Sat_Dec_27_01_54_36_2014.txt',
'data2Sat_Dec_27_01_54_51_2014.txt',
'data2Sat_Dec_27_01_55_05_2014.txt',
'data2Sat_Dec_27_01_55_21_2014.txt',
'data2Sat_Dec_27_01_55_36_2014.txt',
'data2Sat_Dec_27_01_55_51_2014.txt',
'data2Sat_Dec_27_01_56_06_2014.txt',
'data2Sat_Dec_27_01_56_21_2014.txt',
'data2Sat_Dec_27_01_56_36_2014.txt',
'data3Sat_Dec_27_01_56_51_2014.txt',
'data3Sat_Dec_27_01_57_07_2014.txt',
'data3Sat_Dec_27_01_57_22_2014.txt',
'data3Sat_Dec_27_01_57_37_2014.txt',
'data3Sat_Dec_27_01_57_52_2014.txt',
'data3Sat_Dec_27_01_58_07_2014.txt',
'data3Sat_Dec_27_01_58_22_2014.txt',
'data3Sat_Dec_27_01_58_37_2014.txt',
'data3Sat_Dec_27_01_58_53_2014.txt',
'data3Sat_Dec_27_01_59_08_2014.txt',
'data3Sat_Dec_27_01_59_23_2014.txt',
'data3Sat_Dec_27_01_59_39_2014.txt',
'data3Sat_Dec_27_01_59_54_2014.txt',
'data3Sat_Dec_27_02_00_10_2014.txt',
'data3Sat_Dec_27_02_00_25_2014.txt',
'data3Sat_Dec_27_02_00_40_2014.txt',
'data3Sat_Dec_27_02_00_55_2014.txt',
'data3Sat_Dec_27_02_01_10_2014.txt',
'data3Sat_Dec_27_02_01_25_2014.txt',
'data3Sat_Dec_27_02_01_40_2014.txt',
'data3Sat_Dec_27_02_01_55_2014.txt',
'data3Sat_Dec_27_02_02_10_2014.txt',
'data3Sat_Dec_27_02_02_25_2014.txt',
'data3Sat_Dec_27_02_02_40_2014.txt',
'data3Sat_Dec_27_02_02_55_2014.txt',
'data3Sat_Dec_27_02_03_10_2014.txt',
'data3Sat_Dec_27_02_03_26_2014.txt',
'data3Sat_Dec_27_02_03_41_2014.txt',
'data3Sat_Dec_27_02_03_56_2014.txt',
'data3Sat_Dec_27_02_04_11_2014.txt',
'data3Sat_Dec_27_02_04_26_2014.txt',
'data3Sat_Dec_27_02_04_42_2014.txt',
'data3Sat_Dec_27_02_04_57_2014.txt',
'data3Sat_Dec_27_02_05_12_2014.txt',
'data3Sat_Dec_27_02_05_27_2014.txt',
'data3Sat_Dec_27_02_05_42_2014.txt',
'data3Sat_Dec_27_02_05_57_2014.txt',
'data3Sat_Dec_27_02_06_12_2014.txt',
'data3Sat_Dec_27_02_06_27_2014.txt',
'data3Sat_Dec_27_02_06_41_2014.txt',
'data3Sat_Dec_27_02_06_56_2014.txt',
'data3Sat_Dec_27_02_07_12_2014.txt',
'data3Sat_Dec_27_02_07_27_2014.txt',
'data3Sat_Dec_27_02_07_41_2014.txt',
'data3Sat_Dec_27_02_07_56_2014.txt',
'data3Sat_Dec_27_02_08_12_2014.txt',
'data3Sat_Dec_27_02_08_27_2014.txt',
'data3Sat_Dec_27_02_08_42_2014.txt',
'data3Sat_Dec_27_02_08_57_2014.txt',
'data3Sat_Dec_27_02_09_12_2014.txt']
