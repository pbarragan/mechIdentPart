# this is for the 2014/12/26 experiments
# Varying over 10, 100, 1000, 5000, 10000 particles per filter

files=['data0Fri_Dec_26_19_15_52_2014.txt',
'data0Fri_Dec_26_19_15_53_2014.txt',
'data0Fri_Dec_26_19_15_54_2014.txt',
'data0Fri_Dec_26_19_15_55_2014.txt',
'data0Fri_Dec_26_19_15_56_2014.txt',
'data0Fri_Dec_26_19_15_57_2014.txt',
'data0Fri_Dec_26_19_15_58_2014.txt',
'data0Fri_Dec_26_19_15_59_2014.txt',
'data0Fri_Dec_26_19_16_00_2014.txt',
'data0Fri_Dec_26_19_16_01_2014.txt',
'data0Fri_Dec_26_19_16_02_2014.txt',
'data0Fri_Dec_26_19_16_03_2014.txt',
'data0Fri_Dec_26_19_16_04_2014.txt',
'data0Fri_Dec_26_19_16_05_2014.txt',
'data0Fri_Dec_26_19_16_06_2014.txt',
'data0Fri_Dec_26_19_16_07_2014.txt',
'data0Fri_Dec_26_19_16_08_2014.txt',
'data0Fri_Dec_26_19_16_09_2014.txt',
'data0Fri_Dec_26_19_16_10_2014.txt',
'data0Fri_Dec_26_19_16_11_2014.txt',
'data0Fri_Dec_26_19_16_12_2014.txt',
'data0Fri_Dec_26_19_16_14_2014.txt',
'data0Fri_Dec_26_19_16_15_2014.txt',
'data0Fri_Dec_26_19_16_16_2014.txt',
'data0Fri_Dec_26_19_16_17_2014.txt',
'data0Fri_Dec_26_19_16_18_2014.txt',
'data0Fri_Dec_26_19_16_19_2014.txt',
'data0Fri_Dec_26_19_16_20_2014.txt',
'data0Fri_Dec_26_19_16_21_2014.txt',
'data0Fri_Dec_26_19_16_22_2014.txt',
'data0Fri_Dec_26_19_16_23_2014.txt',
'data0Fri_Dec_26_19_16_24_2014.txt',
'data0Fri_Dec_26_19_16_25_2014.txt',
'data0Fri_Dec_26_19_16_26_2014.txt',
'data0Fri_Dec_26_19_16_27_2014.txt',
'data0Fri_Dec_26_19_16_28_2014.txt',
'data0Fri_Dec_26_19_16_29_2014.txt',
'data0Fri_Dec_26_19_16_30_2014.txt',
'data0Fri_Dec_26_19_16_31_2014.txt',
'data0Fri_Dec_26_19_16_32_2014.txt',
'data0Fri_Dec_26_19_16_33_2014.txt',
'data0Fri_Dec_26_19_16_34_2014.txt',
'data0Fri_Dec_26_19_16_35_2014.txt',
'data0Fri_Dec_26_19_16_36_2014.txt',
'data0Fri_Dec_26_19_16_37_2014.txt',
'data0Fri_Dec_26_19_16_38_2014.txt',
'data0Fri_Dec_26_19_16_39_2014.txt',
'data0Fri_Dec_26_19_16_40_2014.txt',
'data0Fri_Dec_26_19_16_41_2014.txt',
'data0Fri_Dec_26_19_16_42_2014.txt',
'data1Fri_Dec_26_19_16_44_2014.txt',
'data1Fri_Dec_26_19_16_45_2014.txt',
'data1Fri_Dec_26_19_16_46_2014.txt',
'data1Fri_Dec_26_19_16_47_2014.txt',
'data1Fri_Dec_26_19_16_48_2014.txt',
'data1Fri_Dec_26_19_16_49_2014.txt',
'data1Fri_Dec_26_19_16_50_2014.txt',
'data1Fri_Dec_26_19_16_51_2014.txt',
'data1Fri_Dec_26_19_16_52_2014.txt',
'data1Fri_Dec_26_19_16_53_2014.txt',
'data1Fri_Dec_26_19_16_54_2014.txt',
'data1Fri_Dec_26_19_16_55_2014.txt',
'data1Fri_Dec_26_19_16_56_2014.txt',
'data1Fri_Dec_26_19_16_57_2014.txt',
'data1Fri_Dec_26_19_16_58_2014.txt',
'data1Fri_Dec_26_19_16_59_2014.txt',
'data1Fri_Dec_26_19_17_00_2014.txt',
'data1Fri_Dec_26_19_17_01_2014.txt',
'data1Fri_Dec_26_19_17_02_2014.txt',
'data1Fri_Dec_26_19_17_03_2014.txt',
'data1Fri_Dec_26_19_17_04_2014.txt',
'data1Fri_Dec_26_19_17_05_2014.txt',
'data1Fri_Dec_26_19_17_06_2014.txt',
'data1Fri_Dec_26_19_17_07_2014.txt',
'data1Fri_Dec_26_19_17_08_2014.txt',
'data1Fri_Dec_26_19_17_09_2014.txt',
'data1Fri_Dec_26_19_17_10_2014.txt',
'data1Fri_Dec_26_19_17_11_2014.txt',
'data1Fri_Dec_26_19_17_12_2014.txt',
'data1Fri_Dec_26_19_17_13_2014.txt',
'data1Fri_Dec_26_19_17_14_2014.txt',
'data1Fri_Dec_26_19_17_16_2014.txt',
'data1Fri_Dec_26_19_17_17_2014.txt',
'data1Fri_Dec_26_19_17_18_2014.txt',
'data1Fri_Dec_26_19_17_19_2014.txt',
'data1Fri_Dec_26_19_17_20_2014.txt',
'data1Fri_Dec_26_19_17_21_2014.txt',
'data1Fri_Dec_26_19_17_22_2014.txt',
'data1Fri_Dec_26_19_17_23_2014.txt',
'data1Fri_Dec_26_19_17_24_2014.txt',
'data1Fri_Dec_26_19_17_25_2014.txt',
'data1Fri_Dec_26_19_17_26_2014.txt',
'data1Fri_Dec_26_19_17_27_2014.txt',
'data1Fri_Dec_26_19_17_28_2014.txt',
'data1Fri_Dec_26_19_17_29_2014.txt',
'data1Fri_Dec_26_19_17_30_2014.txt',
'data1Fri_Dec_26_19_17_31_2014.txt',
'data1Fri_Dec_26_19_17_32_2014.txt',
'data1Fri_Dec_26_19_17_33_2014.txt',
'data1Fri_Dec_26_19_17_34_2014.txt',
'data2Fri_Dec_26_19_17_35_2014.txt',
'data2Fri_Dec_26_19_17_36_2014.txt',
'data2Fri_Dec_26_19_17_37_2014.txt',
'data2Fri_Dec_26_19_17_38_2014.txt',
'data2Fri_Dec_26_19_17_39_2014.txt',
'data2Fri_Dec_26_19_17_40_2014.txt',
'data2Fri_Dec_26_19_17_41_2014.txt',
'data2Fri_Dec_26_19_17_42_2014.txt',
'data2Fri_Dec_26_19_17_43_2014.txt',
'data2Fri_Dec_26_19_17_44_2014.txt',
'data2Fri_Dec_26_19_17_45_2014.txt',
'data2Fri_Dec_26_19_17_47_2014.txt',
'data2Fri_Dec_26_19_17_48_2014.txt',
'data2Fri_Dec_26_19_17_49_2014.txt',
'data2Fri_Dec_26_19_17_50_2014.txt',
'data2Fri_Dec_26_19_17_51_2014.txt',
'data2Fri_Dec_26_19_17_52_2014.txt',
'data2Fri_Dec_26_19_17_53_2014.txt',
'data2Fri_Dec_26_19_17_54_2014.txt',
'data2Fri_Dec_26_19_17_55_2014.txt',
'data2Fri_Dec_26_19_17_56_2014.txt',
'data2Fri_Dec_26_19_17_57_2014.txt',
'data2Fri_Dec_26_19_17_58_2014.txt',
'data2Fri_Dec_26_19_17_59_2014.txt',
'data2Fri_Dec_26_19_18_00_2014.txt',
'data2Fri_Dec_26_19_18_01_2014.txt',
'data2Fri_Dec_26_19_18_02_2014.txt',
'data2Fri_Dec_26_19_18_03_2014.txt',
'data2Fri_Dec_26_19_18_04_2014.txt',
'data2Fri_Dec_26_19_18_05_2014.txt',
'data2Fri_Dec_26_19_18_06_2014.txt',
'data2Fri_Dec_26_19_18_07_2014.txt',
'data2Fri_Dec_26_19_18_08_2014.txt',
'data2Fri_Dec_26_19_18_09_2014.txt',
'data2Fri_Dec_26_19_18_10_2014.txt',
'data2Fri_Dec_26_19_18_11_2014.txt',
'data2Fri_Dec_26_19_18_12_2014.txt',
'data2Fri_Dec_26_19_18_13_2014.txt',
'data2Fri_Dec_26_19_18_15_2014.txt',
'data2Fri_Dec_26_19_18_16_2014.txt',
'data2Fri_Dec_26_19_18_17_2014.txt',
'data2Fri_Dec_26_19_18_18_2014.txt',
'data2Fri_Dec_26_19_18_19_2014.txt',
'data2Fri_Dec_26_19_18_20_2014.txt',
'data2Fri_Dec_26_19_18_21_2014.txt',
'data2Fri_Dec_26_19_18_22_2014.txt',
'data2Fri_Dec_26_19_18_23_2014.txt',
'data2Fri_Dec_26_19_18_24_2014.txt',
'data2Fri_Dec_26_19_18_25_2014.txt',
'data2Fri_Dec_26_19_18_26_2014.txt',
'data3Fri_Dec_26_19_18_27_2014.txt',
'data3Fri_Dec_26_19_18_28_2014.txt',
'data3Fri_Dec_26_19_18_29_2014.txt',
'data3Fri_Dec_26_19_18_30_2014.txt',
'data3Fri_Dec_26_19_18_31_2014.txt',
'data3Fri_Dec_26_19_18_32_2014.txt',
'data3Fri_Dec_26_19_18_33_2014.txt',
'data3Fri_Dec_26_19_18_34_2014.txt',
'data3Fri_Dec_26_19_18_35_2014.txt',
'data3Fri_Dec_26_19_18_36_2014.txt',
'data3Fri_Dec_26_19_18_37_2014.txt',
'data3Fri_Dec_26_19_18_38_2014.txt',
'data3Fri_Dec_26_19_18_39_2014.txt',
'data3Fri_Dec_26_19_18_40_2014.txt',
'data3Fri_Dec_26_19_18_41_2014.txt',
'data3Fri_Dec_26_19_18_42_2014.txt',
'data3Fri_Dec_26_19_18_43_2014.txt',
'data3Fri_Dec_26_19_18_45_2014.txt',
'data3Fri_Dec_26_19_18_46_2014.txt',
'data3Fri_Dec_26_19_18_47_2014.txt',
'data3Fri_Dec_26_19_18_48_2014.txt',
'data3Fri_Dec_26_19_18_49_2014.txt',
'data3Fri_Dec_26_19_18_50_2014.txt',
'data3Fri_Dec_26_19_18_51_2014.txt',
'data3Fri_Dec_26_19_18_52_2014.txt',
'data3Fri_Dec_26_19_18_53_2014.txt',
'data3Fri_Dec_26_19_18_54_2014.txt',
'data3Fri_Dec_26_19_18_55_2014.txt',
'data3Fri_Dec_26_19_18_56_2014.txt',
'data3Fri_Dec_26_19_18_57_2014.txt',
'data3Fri_Dec_26_19_18_58_2014.txt',
'data3Fri_Dec_26_19_18_59_2014.txt',
'data3Fri_Dec_26_19_19_00_2014.txt',
'data3Fri_Dec_26_19_19_01_2014.txt',
'data3Fri_Dec_26_19_19_02_2014.txt',
'data3Fri_Dec_26_19_19_03_2014.txt',
'data3Fri_Dec_26_19_19_04_2014.txt',
'data3Fri_Dec_26_19_19_05_2014.txt',
'data3Fri_Dec_26_19_19_06_2014.txt',
'data3Fri_Dec_26_19_19_07_2014.txt',
'data3Fri_Dec_26_19_19_08_2014.txt',
'data3Fri_Dec_26_19_19_09_2014.txt',
'data3Fri_Dec_26_19_19_10_2014.txt',
'data3Fri_Dec_26_19_19_11_2014.txt',
'data3Fri_Dec_26_19_19_12_2014.txt',
'data3Fri_Dec_26_19_19_14_2014.txt',
'data3Fri_Dec_26_19_19_15_2014.txt',
'data3Fri_Dec_26_19_19_16_2014.txt',
'data3Fri_Dec_26_19_19_17_2014.txt',
'data3Fri_Dec_26_19_19_18_2014.txt',
'data0Fri_Dec_26_19_19_44_2014.txt',
'data0Fri_Dec_26_19_19_45_2014.txt',
'data0Fri_Dec_26_19_19_47_2014.txt',
'data0Fri_Dec_26_19_19_48_2014.txt',
'data0Fri_Dec_26_19_19_49_2014.txt',
'data0Fri_Dec_26_19_19_50_2014.txt',
'data0Fri_Dec_26_19_19_51_2014.txt',
'data0Fri_Dec_26_19_19_52_2014.txt',
'data0Fri_Dec_26_19_19_54_2014.txt',
'data0Fri_Dec_26_19_19_55_2014.txt',
'data0Fri_Dec_26_19_19_56_2014.txt',
'data0Fri_Dec_26_19_19_57_2014.txt',
'data0Fri_Dec_26_19_19_58_2014.txt',
'data0Fri_Dec_26_19_20_00_2014.txt',
'data0Fri_Dec_26_19_20_01_2014.txt',
'data0Fri_Dec_26_19_20_02_2014.txt',
'data0Fri_Dec_26_19_20_03_2014.txt',
'data0Fri_Dec_26_19_20_04_2014.txt',
'data0Fri_Dec_26_19_20_05_2014.txt',
'data0Fri_Dec_26_19_20_07_2014.txt',
'data0Fri_Dec_26_19_20_08_2014.txt',
'data0Fri_Dec_26_19_20_09_2014.txt',
'data0Fri_Dec_26_19_20_10_2014.txt',
'data0Fri_Dec_26_19_20_11_2014.txt',
'data0Fri_Dec_26_19_20_13_2014.txt',
'data0Fri_Dec_26_19_20_14_2014.txt',
'data0Fri_Dec_26_19_20_15_2014.txt',
'data0Fri_Dec_26_19_20_16_2014.txt',
'data0Fri_Dec_26_19_20_17_2014.txt',
'data0Fri_Dec_26_19_20_18_2014.txt',
'data0Fri_Dec_26_19_20_20_2014.txt',
'data0Fri_Dec_26_19_20_21_2014.txt',
'data0Fri_Dec_26_19_20_22_2014.txt',
'data0Fri_Dec_26_19_20_23_2014.txt',
'data0Fri_Dec_26_19_20_24_2014.txt',
'data0Fri_Dec_26_19_20_26_2014.txt',
'data0Fri_Dec_26_19_20_27_2014.txt',
'data0Fri_Dec_26_19_20_28_2014.txt',
'data0Fri_Dec_26_19_20_29_2014.txt',
'data0Fri_Dec_26_19_20_30_2014.txt',
'data0Fri_Dec_26_19_20_31_2014.txt',
'data0Fri_Dec_26_19_20_33_2014.txt',
'data0Fri_Dec_26_19_20_34_2014.txt',
'data0Fri_Dec_26_19_20_35_2014.txt',
'data0Fri_Dec_26_19_20_36_2014.txt',
'data0Fri_Dec_26_19_20_37_2014.txt',
'data0Fri_Dec_26_19_20_39_2014.txt',
'data0Fri_Dec_26_19_20_40_2014.txt',
'data0Fri_Dec_26_19_20_41_2014.txt',
'data0Fri_Dec_26_19_20_42_2014.txt',
'data1Fri_Dec_26_19_20_43_2014.txt',
'data1Fri_Dec_26_19_20_44_2014.txt',
'data1Fri_Dec_26_19_20_46_2014.txt',
'data1Fri_Dec_26_19_20_47_2014.txt',
'data1Fri_Dec_26_19_20_48_2014.txt',
'data1Fri_Dec_26_19_20_49_2014.txt',
'data1Fri_Dec_26_19_20_50_2014.txt',
'data1Fri_Dec_26_19_20_52_2014.txt',
'data1Fri_Dec_26_19_20_53_2014.txt',
'data1Fri_Dec_26_19_20_54_2014.txt',
'data1Fri_Dec_26_19_20_55_2014.txt',
'data1Fri_Dec_26_19_20_56_2014.txt',
'data1Fri_Dec_26_19_20_57_2014.txt',
'data1Fri_Dec_26_19_20_59_2014.txt',
'data1Fri_Dec_26_19_21_00_2014.txt',
'data1Fri_Dec_26_19_21_01_2014.txt',
'data1Fri_Dec_26_19_21_02_2014.txt',
'data1Fri_Dec_26_19_21_03_2014.txt',
'data1Fri_Dec_26_19_21_05_2014.txt',
'data1Fri_Dec_26_19_21_06_2014.txt',
'data1Fri_Dec_26_19_21_07_2014.txt',
'data1Fri_Dec_26_19_21_08_2014.txt',
'data1Fri_Dec_26_19_21_09_2014.txt',
'data1Fri_Dec_26_19_21_10_2014.txt',
'data1Fri_Dec_26_19_21_12_2014.txt',
'data1Fri_Dec_26_19_21_13_2014.txt',
'data1Fri_Dec_26_19_21_14_2014.txt',
'data1Fri_Dec_26_19_21_15_2014.txt',
'data1Fri_Dec_26_19_21_16_2014.txt',
'data1Fri_Dec_26_19_21_17_2014.txt',
'data1Fri_Dec_26_19_21_19_2014.txt',
'data1Fri_Dec_26_19_21_20_2014.txt',
'data1Fri_Dec_26_19_21_21_2014.txt',
'data1Fri_Dec_26_19_21_22_2014.txt',
'data1Fri_Dec_26_19_21_23_2014.txt',
'data1Fri_Dec_26_19_21_25_2014.txt',
'data1Fri_Dec_26_19_21_26_2014.txt',
'data1Fri_Dec_26_19_21_27_2014.txt',
'data1Fri_Dec_26_19_21_28_2014.txt',
'data1Fri_Dec_26_19_21_29_2014.txt',
'data1Fri_Dec_26_19_21_30_2014.txt',
'data1Fri_Dec_26_19_21_32_2014.txt',
'data1Fri_Dec_26_19_21_33_2014.txt',
'data1Fri_Dec_26_19_21_34_2014.txt',
'data1Fri_Dec_26_19_21_35_2014.txt',
'data1Fri_Dec_26_19_21_36_2014.txt',
'data1Fri_Dec_26_19_21_37_2014.txt',
'data1Fri_Dec_26_19_21_39_2014.txt',
'data1Fri_Dec_26_19_21_40_2014.txt',
'data1Fri_Dec_26_19_21_41_2014.txt',
'data2Fri_Dec_26_19_21_42_2014.txt',
'data2Fri_Dec_26_19_21_43_2014.txt',
'data2Fri_Dec_26_19_21_45_2014.txt',
'data2Fri_Dec_26_19_21_46_2014.txt',
'data2Fri_Dec_26_19_21_47_2014.txt',
'data2Fri_Dec_26_19_21_48_2014.txt',
'data2Fri_Dec_26_19_21_49_2014.txt',
'data2Fri_Dec_26_19_21_50_2014.txt',
'data2Fri_Dec_26_19_21_52_2014.txt',
'data2Fri_Dec_26_19_21_53_2014.txt',
'data2Fri_Dec_26_19_21_54_2014.txt',
'data2Fri_Dec_26_19_21_55_2014.txt',
'data2Fri_Dec_26_19_21_56_2014.txt',
'data2Fri_Dec_26_19_21_58_2014.txt',
'data2Fri_Dec_26_19_21_59_2014.txt',
'data2Fri_Dec_26_19_22_00_2014.txt',
'data2Fri_Dec_26_19_22_01_2014.txt',
'data2Fri_Dec_26_19_22_02_2014.txt',
'data2Fri_Dec_26_19_22_03_2014.txt',
'data2Fri_Dec_26_19_22_05_2014.txt',
'data2Fri_Dec_26_19_22_06_2014.txt',
'data2Fri_Dec_26_19_22_07_2014.txt',
'data2Fri_Dec_26_19_22_08_2014.txt',
'data2Fri_Dec_26_19_22_09_2014.txt',
'data2Fri_Dec_26_19_22_11_2014.txt',
'data2Fri_Dec_26_19_22_12_2014.txt',
'data2Fri_Dec_26_19_22_13_2014.txt',
'data2Fri_Dec_26_19_22_14_2014.txt',
'data2Fri_Dec_26_19_22_15_2014.txt',
'data2Fri_Dec_26_19_22_17_2014.txt',
'data2Fri_Dec_26_19_22_18_2014.txt',
'data2Fri_Dec_26_19_22_19_2014.txt',
'data2Fri_Dec_26_19_22_20_2014.txt',
'data2Fri_Dec_26_19_22_21_2014.txt',
'data2Fri_Dec_26_19_22_22_2014.txt',
'data2Fri_Dec_26_19_22_24_2014.txt',
'data2Fri_Dec_26_19_22_25_2014.txt',
'data2Fri_Dec_26_19_22_26_2014.txt',
'data2Fri_Dec_26_19_22_27_2014.txt',
'data2Fri_Dec_26_19_22_28_2014.txt',
'data2Fri_Dec_26_19_22_30_2014.txt',
'data2Fri_Dec_26_19_22_31_2014.txt',
'data2Fri_Dec_26_19_22_32_2014.txt',
'data2Fri_Dec_26_19_22_33_2014.txt',
'data2Fri_Dec_26_19_22_34_2014.txt',
'data2Fri_Dec_26_19_22_35_2014.txt',
'data2Fri_Dec_26_19_22_37_2014.txt',
'data2Fri_Dec_26_19_22_38_2014.txt',
'data2Fri_Dec_26_19_22_39_2014.txt',
'data2Fri_Dec_26_19_22_40_2014.txt',
'data3Fri_Dec_26_19_22_41_2014.txt',
'data3Fri_Dec_26_19_22_43_2014.txt',
'data3Fri_Dec_26_19_22_44_2014.txt',
'data3Fri_Dec_26_19_22_45_2014.txt',
'data3Fri_Dec_26_19_22_46_2014.txt',
'data3Fri_Dec_26_19_22_47_2014.txt',
'data3Fri_Dec_26_19_22_48_2014.txt',
'data3Fri_Dec_26_19_22_50_2014.txt',
'data3Fri_Dec_26_19_22_51_2014.txt',
'data3Fri_Dec_26_19_22_52_2014.txt',
'data3Fri_Dec_26_19_22_53_2014.txt',
'data3Fri_Dec_26_19_22_54_2014.txt',
'data3Fri_Dec_26_19_22_55_2014.txt',
'data3Fri_Dec_26_19_22_57_2014.txt',
'data3Fri_Dec_26_19_22_58_2014.txt',
'data3Fri_Dec_26_19_22_59_2014.txt',
'data3Fri_Dec_26_19_23_00_2014.txt',
'data3Fri_Dec_26_19_23_01_2014.txt',
'data3Fri_Dec_26_19_23_03_2014.txt',
'data3Fri_Dec_26_19_23_04_2014.txt',
'data3Fri_Dec_26_19_23_05_2014.txt',
'data3Fri_Dec_26_19_23_06_2014.txt',
'data3Fri_Dec_26_19_23_07_2014.txt',
'data3Fri_Dec_26_19_23_08_2014.txt',
'data3Fri_Dec_26_19_23_10_2014.txt',
'data3Fri_Dec_26_19_23_11_2014.txt',
'data3Fri_Dec_26_19_23_12_2014.txt',
'data3Fri_Dec_26_19_23_13_2014.txt',
'data3Fri_Dec_26_19_23_14_2014.txt',
'data3Fri_Dec_26_19_23_16_2014.txt',
'data3Fri_Dec_26_19_23_17_2014.txt',
'data3Fri_Dec_26_19_23_18_2014.txt',
'data3Fri_Dec_26_19_23_19_2014.txt',
'data3Fri_Dec_26_19_23_20_2014.txt',
'data3Fri_Dec_26_19_23_21_2014.txt',
'data3Fri_Dec_26_19_23_23_2014.txt',
'data3Fri_Dec_26_19_23_24_2014.txt',
'data3Fri_Dec_26_19_23_25_2014.txt',
'data3Fri_Dec_26_19_23_26_2014.txt',
'data3Fri_Dec_26_19_23_27_2014.txt',
'data3Fri_Dec_26_19_23_29_2014.txt',
'data3Fri_Dec_26_19_23_30_2014.txt',
'data3Fri_Dec_26_19_23_31_2014.txt',
'data3Fri_Dec_26_19_23_32_2014.txt',
'data3Fri_Dec_26_19_23_33_2014.txt',
'data3Fri_Dec_26_19_23_34_2014.txt',
'data3Fri_Dec_26_19_23_36_2014.txt',
'data3Fri_Dec_26_19_23_37_2014.txt',
'data3Fri_Dec_26_19_23_38_2014.txt',
'data3Fri_Dec_26_19_23_39_2014.txt',
'data0Fri_Dec_26_19_24_06_2014.txt',
'data0Fri_Dec_26_19_24_08_2014.txt',
'data0Fri_Dec_26_19_24_09_2014.txt',
'data0Fri_Dec_26_19_24_11_2014.txt',
'data0Fri_Dec_26_19_24_12_2014.txt',
'data0Fri_Dec_26_19_24_14_2014.txt',
'data0Fri_Dec_26_19_24_16_2014.txt',
'data0Fri_Dec_26_19_24_17_2014.txt',
'data0Fri_Dec_26_19_24_19_2014.txt',
'data0Fri_Dec_26_19_24_21_2014.txt',
'data0Fri_Dec_26_19_24_22_2014.txt',
'data0Fri_Dec_26_19_24_24_2014.txt',
'data0Fri_Dec_26_19_24_25_2014.txt',
'data0Fri_Dec_26_19_24_27_2014.txt',
'data0Fri_Dec_26_19_24_29_2014.txt',
'data0Fri_Dec_26_19_24_30_2014.txt',
'data0Fri_Dec_26_19_24_32_2014.txt',
'data0Fri_Dec_26_19_24_34_2014.txt',
'data0Fri_Dec_26_19_24_35_2014.txt',
'data0Fri_Dec_26_19_24_37_2014.txt',
'data0Fri_Dec_26_19_24_38_2014.txt',
'data0Fri_Dec_26_19_24_40_2014.txt',
'data0Fri_Dec_26_19_24_42_2014.txt',
'data0Fri_Dec_26_19_24_43_2014.txt',
'data0Fri_Dec_26_19_24_45_2014.txt',
'data0Fri_Dec_26_19_24_47_2014.txt',
'data0Fri_Dec_26_19_24_48_2014.txt',
'data0Fri_Dec_26_19_24_50_2014.txt',
'data0Fri_Dec_26_19_24_51_2014.txt',
'data0Fri_Dec_26_19_24_53_2014.txt',
'data0Fri_Dec_26_19_24_55_2014.txt',
'data0Fri_Dec_26_19_24_56_2014.txt',
'data0Fri_Dec_26_19_24_58_2014.txt',
'data0Fri_Dec_26_19_25_00_2014.txt',
'data0Fri_Dec_26_19_25_01_2014.txt',
'data0Fri_Dec_26_19_25_03_2014.txt',
'data0Fri_Dec_26_19_25_04_2014.txt',
'data0Fri_Dec_26_19_25_06_2014.txt',
'data0Fri_Dec_26_19_25_08_2014.txt',
'data0Fri_Dec_26_19_25_09_2014.txt',
'data0Fri_Dec_26_19_25_11_2014.txt',
'data0Fri_Dec_26_19_25_13_2014.txt',
'data0Fri_Dec_26_19_25_14_2014.txt',
'data0Fri_Dec_26_19_25_16_2014.txt',
'data0Fri_Dec_26_19_25_18_2014.txt',
'data0Fri_Dec_26_19_25_19_2014.txt',
'data0Fri_Dec_26_19_25_21_2014.txt',
'data0Fri_Dec_26_19_25_22_2014.txt',
'data0Fri_Dec_26_19_25_24_2014.txt',
'data0Fri_Dec_26_19_25_26_2014.txt',
'data1Fri_Dec_26_19_25_27_2014.txt',
'data1Fri_Dec_26_19_25_29_2014.txt',
'data1Fri_Dec_26_19_25_31_2014.txt',
'data1Fri_Dec_26_19_25_32_2014.txt',
'data1Fri_Dec_26_19_25_34_2014.txt',
'data1Fri_Dec_26_19_25_35_2014.txt',
'data1Fri_Dec_26_19_25_37_2014.txt',
'data1Fri_Dec_26_19_25_39_2014.txt',
'data1Fri_Dec_26_19_25_40_2014.txt',
'data1Fri_Dec_26_19_25_42_2014.txt',
'data1Fri_Dec_26_19_25_43_2014.txt',
'data1Fri_Dec_26_19_25_45_2014.txt',
'data1Fri_Dec_26_19_25_47_2014.txt',
'data1Fri_Dec_26_19_25_48_2014.txt',
'data1Fri_Dec_26_19_25_50_2014.txt',
'data1Fri_Dec_26_19_25_52_2014.txt',
'data1Fri_Dec_26_19_25_53_2014.txt',
'data1Fri_Dec_26_19_25_55_2014.txt',
'data1Fri_Dec_26_19_25_56_2014.txt',
'data1Fri_Dec_26_19_25_58_2014.txt',
'data1Fri_Dec_26_19_26_00_2014.txt',
'data1Fri_Dec_26_19_26_01_2014.txt',
'data1Fri_Dec_26_19_26_03_2014.txt',
'data1Fri_Dec_26_19_26_05_2014.txt',
'data1Fri_Dec_26_19_26_06_2014.txt',
'data1Fri_Dec_26_19_26_08_2014.txt',
'data1Fri_Dec_26_19_26_09_2014.txt',
'data1Fri_Dec_26_19_26_11_2014.txt',
'data1Fri_Dec_26_19_26_13_2014.txt',
'data1Fri_Dec_26_19_26_14_2014.txt',
'data1Fri_Dec_26_19_26_16_2014.txt',
'data1Fri_Dec_26_19_26_18_2014.txt',
'data1Fri_Dec_26_19_26_19_2014.txt',
'data1Fri_Dec_26_19_26_21_2014.txt',
'data1Fri_Dec_26_19_26_22_2014.txt',
'data1Fri_Dec_26_19_26_24_2014.txt',
'data1Fri_Dec_26_19_26_26_2014.txt',
'data1Fri_Dec_26_19_26_27_2014.txt',
'data1Fri_Dec_26_19_26_29_2014.txt',
'data1Fri_Dec_26_19_26_31_2014.txt',
'data1Fri_Dec_26_19_26_32_2014.txt',
'data1Fri_Dec_26_19_26_34_2014.txt',
'data1Fri_Dec_26_19_26_35_2014.txt',
'data1Fri_Dec_26_19_26_37_2014.txt',
'data1Fri_Dec_26_19_26_39_2014.txt',
'data1Fri_Dec_26_19_26_40_2014.txt',
'data1Fri_Dec_26_19_26_42_2014.txt',
'data1Fri_Dec_26_19_26_43_2014.txt',
'data1Fri_Dec_26_19_26_45_2014.txt',
'data1Fri_Dec_26_19_26_47_2014.txt',
'data2Fri_Dec_26_19_26_48_2014.txt',
'data2Fri_Dec_26_19_26_50_2014.txt',
'data2Fri_Dec_26_19_26_52_2014.txt',
'data2Fri_Dec_26_19_26_53_2014.txt',
'data2Fri_Dec_26_19_26_55_2014.txt',
'data2Fri_Dec_26_19_26_56_2014.txt',
'data2Fri_Dec_26_19_26_58_2014.txt',
'data2Fri_Dec_26_19_27_00_2014.txt',
'data2Fri_Dec_26_19_27_01_2014.txt',
'data2Fri_Dec_26_19_27_03_2014.txt',
'data2Fri_Dec_26_19_27_05_2014.txt',
'data2Fri_Dec_26_19_27_06_2014.txt',
'data2Fri_Dec_26_19_27_08_2014.txt',
'data2Fri_Dec_26_19_27_09_2014.txt',
'data2Fri_Dec_26_19_27_11_2014.txt',
'data2Fri_Dec_26_19_27_13_2014.txt',
'data2Fri_Dec_26_19_27_14_2014.txt',
'data2Fri_Dec_26_19_27_16_2014.txt',
'data2Fri_Dec_26_19_27_18_2014.txt',
'data2Fri_Dec_26_19_27_19_2014.txt',
'data2Fri_Dec_26_19_27_21_2014.txt',
'data2Fri_Dec_26_19_27_22_2014.txt',
'data2Fri_Dec_26_19_27_24_2014.txt',
'data2Fri_Dec_26_19_27_26_2014.txt',
'data2Fri_Dec_26_19_27_27_2014.txt',
'data2Fri_Dec_26_19_27_29_2014.txt',
'data2Fri_Dec_26_19_27_31_2014.txt',
'data2Fri_Dec_26_19_27_32_2014.txt',
'data2Fri_Dec_26_19_27_34_2014.txt',
'data2Fri_Dec_26_19_27_35_2014.txt',
'data2Fri_Dec_26_19_27_37_2014.txt',
'data2Fri_Dec_26_19_27_39_2014.txt',
'data2Fri_Dec_26_19_27_40_2014.txt',
'data2Fri_Dec_26_19_27_42_2014.txt',
'data2Fri_Dec_26_19_27_44_2014.txt',
'data2Fri_Dec_26_19_27_45_2014.txt',
'data2Fri_Dec_26_19_27_47_2014.txt',
'data2Fri_Dec_26_19_27_48_2014.txt',
'data2Fri_Dec_26_19_27_50_2014.txt',
'data2Fri_Dec_26_19_27_52_2014.txt',
'data2Fri_Dec_26_19_27_53_2014.txt',
'data2Fri_Dec_26_19_27_55_2014.txt',
'data2Fri_Dec_26_19_27_56_2014.txt',
'data2Fri_Dec_26_19_27_58_2014.txt',
'data2Fri_Dec_26_19_28_00_2014.txt',
'data2Fri_Dec_26_19_28_01_2014.txt',
'data2Fri_Dec_26_19_28_03_2014.txt',
'data2Fri_Dec_26_19_28_05_2014.txt',
'data2Fri_Dec_26_19_28_06_2014.txt',
'data2Fri_Dec_26_19_28_08_2014.txt',
'data3Fri_Dec_26_19_28_10_2014.txt',
'data3Fri_Dec_26_19_28_11_2014.txt',
'data3Fri_Dec_26_19_28_13_2014.txt',
'data3Fri_Dec_26_19_28_14_2014.txt',
'data3Fri_Dec_26_19_28_16_2014.txt',
'data3Fri_Dec_26_19_28_18_2014.txt',
'data3Fri_Dec_26_19_28_19_2014.txt',
'data3Fri_Dec_26_19_28_21_2014.txt',
'data3Fri_Dec_26_19_28_23_2014.txt',
'data3Fri_Dec_26_19_28_24_2014.txt',
'data3Fri_Dec_26_19_28_26_2014.txt',
'data3Fri_Dec_26_19_28_28_2014.txt',
'data3Fri_Dec_26_19_28_29_2014.txt',
'data3Fri_Dec_26_19_28_31_2014.txt',
'data3Fri_Dec_26_19_28_32_2014.txt',
'data3Fri_Dec_26_19_28_34_2014.txt',
'data3Fri_Dec_26_19_28_36_2014.txt',
'data3Fri_Dec_26_19_28_37_2014.txt',
'data3Fri_Dec_26_19_28_39_2014.txt',
'data3Fri_Dec_26_19_28_41_2014.txt',
'data3Fri_Dec_26_19_28_42_2014.txt',
'data3Fri_Dec_26_19_28_44_2014.txt',
'data3Fri_Dec_26_19_28_46_2014.txt',
'data3Fri_Dec_26_19_28_47_2014.txt',
'data3Fri_Dec_26_19_28_49_2014.txt',
'data3Fri_Dec_26_19_28_50_2014.txt',
'data3Fri_Dec_26_19_28_52_2014.txt',
'data3Fri_Dec_26_19_28_54_2014.txt',
'data3Fri_Dec_26_19_28_55_2014.txt',
'data3Fri_Dec_26_19_28_57_2014.txt',
'data3Fri_Dec_26_19_28_59_2014.txt',
'data3Fri_Dec_26_19_29_00_2014.txt',
'data3Fri_Dec_26_19_29_02_2014.txt',
'data3Fri_Dec_26_19_29_04_2014.txt',
'data3Fri_Dec_26_19_29_05_2014.txt',
'data3Fri_Dec_26_19_29_07_2014.txt',
'data3Fri_Dec_26_19_29_08_2014.txt',
'data3Fri_Dec_26_19_29_10_2014.txt',
'data3Fri_Dec_26_19_29_12_2014.txt',
'data3Fri_Dec_26_19_29_13_2014.txt',
'data3Fri_Dec_26_19_29_15_2014.txt',
'data3Fri_Dec_26_19_29_17_2014.txt',
'data3Fri_Dec_26_19_29_18_2014.txt',
'data3Fri_Dec_26_19_29_20_2014.txt',
'data3Fri_Dec_26_19_29_21_2014.txt',
'data3Fri_Dec_26_19_29_23_2014.txt',
'data3Fri_Dec_26_19_29_25_2014.txt',
'data3Fri_Dec_26_19_29_26_2014.txt',
'data3Fri_Dec_26_19_29_28_2014.txt',
'data3Fri_Dec_26_19_29_30_2014.txt',
'data0Fri_Dec_26_19_29_57_2014.txt',
'data0Fri_Dec_26_19_30_04_2014.txt',
'data0Fri_Dec_26_19_30_12_2014.txt',
'data0Fri_Dec_26_19_30_19_2014.txt',
'data0Fri_Dec_26_19_30_27_2014.txt',
'data0Fri_Dec_26_19_30_34_2014.txt',
'data0Fri_Dec_26_19_30_42_2014.txt',
'data0Fri_Dec_26_19_30_50_2014.txt',
'data0Fri_Dec_26_19_30_57_2014.txt',
'data0Fri_Dec_26_19_31_05_2014.txt',
'data0Fri_Dec_26_19_31_12_2014.txt',
'data0Fri_Dec_26_19_31_20_2014.txt',
'data0Fri_Dec_26_19_31_28_2014.txt',
'data0Fri_Dec_26_19_31_35_2014.txt',
'data0Fri_Dec_26_19_31_43_2014.txt',
'data0Fri_Dec_26_19_31_50_2014.txt',
'data0Fri_Dec_26_19_31_58_2014.txt',
'data0Fri_Dec_26_19_32_06_2014.txt',
'data0Fri_Dec_26_19_32_13_2014.txt',
'data0Fri_Dec_26_19_32_21_2014.txt',
'data0Fri_Dec_26_19_32_28_2014.txt',
'data0Fri_Dec_26_19_32_36_2014.txt',
'data0Fri_Dec_26_19_32_43_2014.txt',
'data0Fri_Dec_26_19_32_51_2014.txt',
'data0Fri_Dec_26_19_32_58_2014.txt',
'data0Fri_Dec_26_19_33_06_2014.txt',
'data0Fri_Dec_26_19_33_13_2014.txt',
'data0Fri_Dec_26_19_33_21_2014.txt',
'data0Fri_Dec_26_19_33_29_2014.txt',
'data0Fri_Dec_26_19_33_36_2014.txt',
'data0Fri_Dec_26_19_33_44_2014.txt',
'data0Fri_Dec_26_19_33_52_2014.txt',
'data0Fri_Dec_26_19_34_00_2014.txt',
'data0Fri_Dec_26_19_34_07_2014.txt',
'data0Fri_Dec_26_19_34_15_2014.txt',
'data0Fri_Dec_26_19_34_22_2014.txt',
'data0Fri_Dec_26_19_34_30_2014.txt',
'data0Fri_Dec_26_19_34_37_2014.txt',
'data0Fri_Dec_26_19_34_45_2014.txt',
'data0Fri_Dec_26_19_34_53_2014.txt',
'data0Fri_Dec_26_19_35_01_2014.txt',
'data0Fri_Dec_26_19_35_08_2014.txt',
'data0Fri_Dec_26_19_35_16_2014.txt',
'data0Fri_Dec_26_19_35_23_2014.txt',
'data0Fri_Dec_26_19_35_31_2014.txt',
'data0Fri_Dec_26_19_35_38_2014.txt',
'data0Fri_Dec_26_19_35_46_2014.txt',
'data0Fri_Dec_26_19_35_53_2014.txt',
'data0Fri_Dec_26_19_36_01_2014.txt',
'data0Fri_Dec_26_19_36_09_2014.txt',
'data1Fri_Dec_26_19_36_16_2014.txt',
'data1Fri_Dec_26_19_36_24_2014.txt',
'data1Fri_Dec_26_19_36_31_2014.txt',
'data1Fri_Dec_26_19_36_39_2014.txt',
'data1Fri_Dec_26_19_36_46_2014.txt',
'data1Fri_Dec_26_19_36_54_2014.txt',
'data1Fri_Dec_26_19_37_01_2014.txt',
'data1Fri_Dec_26_19_37_09_2014.txt',
'data1Fri_Dec_26_19_37_17_2014.txt',
'data1Fri_Dec_26_19_37_24_2014.txt',
'data1Fri_Dec_26_19_37_32_2014.txt',
'data1Fri_Dec_26_19_37_39_2014.txt',
'data1Fri_Dec_26_19_37_47_2014.txt',
'data1Fri_Dec_26_19_37_55_2014.txt',
'data1Fri_Dec_26_19_38_02_2014.txt',
'data1Fri_Dec_26_19_38_10_2014.txt',
'data1Fri_Dec_26_19_38_18_2014.txt',
'data1Fri_Dec_26_19_38_25_2014.txt',
'data1Fri_Dec_26_19_38_33_2014.txt',
'data1Fri_Dec_26_19_38_41_2014.txt',
'data1Fri_Dec_26_19_38_48_2014.txt',
'data1Fri_Dec_26_19_38_56_2014.txt',
'data1Fri_Dec_26_19_39_03_2014.txt',
'data1Fri_Dec_26_19_39_11_2014.txt',
'data1Fri_Dec_26_19_39_19_2014.txt',
'data1Fri_Dec_26_19_39_26_2014.txt',
'data1Fri_Dec_26_19_39_34_2014.txt',
'data1Fri_Dec_26_19_39_41_2014.txt',
'data1Fri_Dec_26_19_39_49_2014.txt',
'data1Fri_Dec_26_19_39_57_2014.txt',
'data1Fri_Dec_26_19_40_04_2014.txt',
'data1Fri_Dec_26_19_40_12_2014.txt',
'data1Fri_Dec_26_19_40_20_2014.txt',
'data1Fri_Dec_26_19_40_27_2014.txt',
'data1Fri_Dec_26_19_40_35_2014.txt',
'data1Fri_Dec_26_19_40_43_2014.txt',
'data1Fri_Dec_26_19_40_50_2014.txt',
'data1Fri_Dec_26_19_40_58_2014.txt',
'data1Fri_Dec_26_19_41_05_2014.txt',
'data1Fri_Dec_26_19_41_13_2014.txt',
'data1Fri_Dec_26_19_41_20_2014.txt',
'data1Fri_Dec_26_19_41_28_2014.txt',
'data1Fri_Dec_26_19_41_36_2014.txt',
'data1Fri_Dec_26_19_41_43_2014.txt',
'data1Fri_Dec_26_19_41_51_2014.txt',
'data1Fri_Dec_26_19_41_58_2014.txt',
'data1Fri_Dec_26_19_42_06_2014.txt',
'data1Fri_Dec_26_19_42_14_2014.txt',
'data1Fri_Dec_26_19_42_21_2014.txt',
'data1Fri_Dec_26_19_42_29_2014.txt',
'data2Fri_Dec_26_19_42_36_2014.txt',
'data2Fri_Dec_26_19_42_44_2014.txt',
'data2Fri_Dec_26_19_42_51_2014.txt',
'data2Fri_Dec_26_19_42_59_2014.txt',
'data2Fri_Dec_26_19_43_06_2014.txt',
'data2Fri_Dec_26_19_43_14_2014.txt',
'data2Fri_Dec_26_19_43_21_2014.txt',
'data2Fri_Dec_26_19_43_29_2014.txt',
'data2Fri_Dec_26_19_43_36_2014.txt',
'data2Fri_Dec_26_19_43_44_2014.txt',
'data2Fri_Dec_26_19_43_51_2014.txt',
'data2Fri_Dec_26_19_43_59_2014.txt',
'data2Fri_Dec_26_19_44_06_2014.txt',
'data2Fri_Dec_26_19_44_14_2014.txt',
'data2Fri_Dec_26_19_44_21_2014.txt',
'data2Fri_Dec_26_19_44_29_2014.txt',
'data2Fri_Dec_26_19_44_37_2014.txt',
'data2Fri_Dec_26_19_44_45_2014.txt',
'data2Fri_Dec_26_19_44_52_2014.txt',
'data2Fri_Dec_26_19_44_59_2014.txt',
'data2Fri_Dec_26_19_45_07_2014.txt',
'data2Fri_Dec_26_19_45_15_2014.txt',
'data2Fri_Dec_26_19_45_22_2014.txt',
'data2Fri_Dec_26_19_45_30_2014.txt',
'data2Fri_Dec_26_19_45_37_2014.txt',
'data2Fri_Dec_26_19_45_45_2014.txt',
'data2Fri_Dec_26_19_45_53_2014.txt',
'data2Fri_Dec_26_19_46_00_2014.txt',
'data2Fri_Dec_26_19_46_08_2014.txt',
'data2Fri_Dec_26_19_46_16_2014.txt',
'data2Fri_Dec_26_19_46_23_2014.txt',
'data2Fri_Dec_26_19_46_31_2014.txt',
'data2Fri_Dec_26_19_46_38_2014.txt',
'data2Fri_Dec_26_19_46_46_2014.txt',
'data2Fri_Dec_26_19_46_53_2014.txt',
'data2Fri_Dec_26_19_47_01_2014.txt',
'data2Fri_Dec_26_19_47_08_2014.txt',
'data2Fri_Dec_26_19_47_16_2014.txt',
'data2Fri_Dec_26_19_47_23_2014.txt',
'data2Fri_Dec_26_19_47_31_2014.txt',
'data2Fri_Dec_26_19_47_38_2014.txt',
'data2Fri_Dec_26_19_47_46_2014.txt',
'data2Fri_Dec_26_19_47_54_2014.txt',
'data2Fri_Dec_26_19_48_01_2014.txt',
'data2Fri_Dec_26_19_48_09_2014.txt',
'data2Fri_Dec_26_19_48_16_2014.txt',
'data2Fri_Dec_26_19_48_24_2014.txt',
'data2Fri_Dec_26_19_48_31_2014.txt',
'data2Fri_Dec_26_19_48_39_2014.txt',
'data2Fri_Dec_26_19_48_46_2014.txt',
'data3Fri_Dec_26_19_48_54_2014.txt',
'data3Fri_Dec_26_19_49_01_2014.txt',
'data3Fri_Dec_26_19_49_09_2014.txt',
'data3Fri_Dec_26_19_49_16_2014.txt',
'data3Fri_Dec_26_19_49_24_2014.txt',
'data3Fri_Dec_26_19_49_31_2014.txt',
'data3Fri_Dec_26_19_49_39_2014.txt',
'data3Fri_Dec_26_19_49_47_2014.txt',
'data3Fri_Dec_26_19_49_54_2014.txt',
'data3Fri_Dec_26_19_50_02_2014.txt',
'data3Fri_Dec_26_19_50_09_2014.txt',
'data3Fri_Dec_26_19_50_17_2014.txt',
'data3Fri_Dec_26_19_50_24_2014.txt',
'data3Fri_Dec_26_19_50_32_2014.txt',
'data3Fri_Dec_26_19_50_40_2014.txt',
'data3Fri_Dec_26_19_50_47_2014.txt',
'data3Fri_Dec_26_19_50_55_2014.txt',
'data3Fri_Dec_26_19_51_03_2014.txt',
'data3Fri_Dec_26_19_51_10_2014.txt',
'data3Fri_Dec_26_19_51_18_2014.txt',
'data3Fri_Dec_26_19_51_25_2014.txt',
'data3Fri_Dec_26_19_51_33_2014.txt',
'data3Fri_Dec_26_19_51_40_2014.txt',
'data3Fri_Dec_26_19_51_48_2014.txt',
'data3Fri_Dec_26_19_51_55_2014.txt',
'data3Fri_Dec_26_19_52_03_2014.txt',
'data3Fri_Dec_26_19_52_10_2014.txt',
'data3Fri_Dec_26_19_52_18_2014.txt',
'data3Fri_Dec_26_19_52_26_2014.txt',
'data3Fri_Dec_26_19_52_33_2014.txt',
'data3Fri_Dec_26_19_52_41_2014.txt',
'data3Fri_Dec_26_19_52_48_2014.txt',
'data3Fri_Dec_26_19_52_56_2014.txt',
'data3Fri_Dec_26_19_53_04_2014.txt',
'data3Fri_Dec_26_19_53_11_2014.txt',
'data3Fri_Dec_26_19_53_19_2014.txt',
'data3Fri_Dec_26_19_53_26_2014.txt',
'data3Fri_Dec_26_19_53_34_2014.txt',
'data3Fri_Dec_26_19_53_41_2014.txt',
'data3Fri_Dec_26_19_53_49_2014.txt',
'data3Fri_Dec_26_19_53_56_2014.txt',
'data3Fri_Dec_26_19_54_04_2014.txt',
'data3Fri_Dec_26_19_54_12_2014.txt',
'data3Fri_Dec_26_19_54_19_2014.txt',
'data3Fri_Dec_26_19_54_27_2014.txt',
'data3Fri_Dec_26_19_54_34_2014.txt',
'data3Fri_Dec_26_19_54_42_2014.txt',
'data3Fri_Dec_26_19_54_50_2014.txt',
'data3Fri_Dec_26_19_54_57_2014.txt',
'data3Fri_Dec_26_19_55_04_2014.txt',
'data0Fri_Dec_26_19_55_38_2014.txt',
'data0Fri_Dec_26_19_55_53_2014.txt',
'data0Fri_Dec_26_19_56_08_2014.txt',
'data0Fri_Dec_26_19_56_23_2014.txt',
'data0Fri_Dec_26_19_56_38_2014.txt',
'data0Fri_Dec_26_19_56_53_2014.txt',
'data0Fri_Dec_26_19_57_08_2014.txt',
'data0Fri_Dec_26_19_57_24_2014.txt',
'data0Fri_Dec_26_19_57_38_2014.txt',
'data0Fri_Dec_26_19_57_53_2014.txt',
'data0Fri_Dec_26_19_58_08_2014.txt',
'data0Fri_Dec_26_19_58_23_2014.txt',
'data0Fri_Dec_26_19_58_38_2014.txt',
'data0Fri_Dec_26_19_58_53_2014.txt',
'data0Fri_Dec_26_19_59_08_2014.txt',
'data0Fri_Dec_26_19_59_23_2014.txt',
'data0Fri_Dec_26_19_59_37_2014.txt',
'data0Fri_Dec_26_19_59_52_2014.txt',
'data0Fri_Dec_26_20_00_07_2014.txt',
'data0Fri_Dec_26_20_00_22_2014.txt',
'data0Fri_Dec_26_20_00_37_2014.txt',
'data0Fri_Dec_26_20_00_53_2014.txt',
'data0Fri_Dec_26_20_01_08_2014.txt',
'data0Fri_Dec_26_20_01_23_2014.txt',
'data0Fri_Dec_26_20_01_38_2014.txt',
'data0Fri_Dec_26_20_01_53_2014.txt',
'data0Fri_Dec_26_20_02_08_2014.txt',
'data0Fri_Dec_26_20_02_23_2014.txt',
'data0Fri_Dec_26_20_02_37_2014.txt',
'data0Fri_Dec_26_20_02_52_2014.txt',
'data0Fri_Dec_26_20_03_07_2014.txt',
'data0Fri_Dec_26_20_03_22_2014.txt',
'data0Fri_Dec_26_20_03_37_2014.txt',
'data0Fri_Dec_26_20_03_52_2014.txt',
'data0Fri_Dec_26_20_04_07_2014.txt',
'data0Fri_Dec_26_20_04_22_2014.txt',
'data0Fri_Dec_26_20_04_37_2014.txt',
'data0Fri_Dec_26_20_04_52_2014.txt',
'data0Fri_Dec_26_20_05_07_2014.txt',
'data0Fri_Dec_26_20_05_21_2014.txt',
'data0Fri_Dec_26_20_05_36_2014.txt',
'data0Fri_Dec_26_20_05_51_2014.txt',
'data0Fri_Dec_26_20_06_06_2014.txt',
'data0Fri_Dec_26_20_06_21_2014.txt',
'data0Fri_Dec_26_20_06_36_2014.txt',
'data0Fri_Dec_26_20_06_51_2014.txt',
'data0Fri_Dec_26_20_07_05_2014.txt',
'data0Fri_Dec_26_20_07_20_2014.txt',
'data0Fri_Dec_26_20_07_35_2014.txt',
'data0Fri_Dec_26_20_07_50_2014.txt',
'data1Fri_Dec_26_20_08_04_2014.txt',
'data1Fri_Dec_26_20_08_19_2014.txt',
'data1Fri_Dec_26_20_08_35_2014.txt',
'data1Fri_Dec_26_20_08_49_2014.txt',
'data1Fri_Dec_26_20_09_04_2014.txt',
'data1Fri_Dec_26_20_09_19_2014.txt',
'data1Fri_Dec_26_20_09_34_2014.txt',
'data1Fri_Dec_26_20_09_49_2014.txt',
'data1Fri_Dec_26_20_10_03_2014.txt',
'data1Fri_Dec_26_20_10_18_2014.txt',
'data1Fri_Dec_26_20_10_33_2014.txt',
'data1Fri_Dec_26_20_10_48_2014.txt',
'data1Fri_Dec_26_20_11_03_2014.txt',
'data1Fri_Dec_26_20_11_18_2014.txt',
'data1Fri_Dec_26_20_11_33_2014.txt',
'data1Fri_Dec_26_20_11_48_2014.txt',
'data1Fri_Dec_26_20_12_02_2014.txt',
'data1Fri_Dec_26_20_12_18_2014.txt',
'data1Fri_Dec_26_20_12_35_2014.txt',
'data1Fri_Dec_26_20_12_49_2014.txt',
'data1Fri_Dec_26_20_13_04_2014.txt',
'data1Fri_Dec_26_20_13_19_2014.txt',
'data1Fri_Dec_26_20_13_34_2014.txt',
'data1Fri_Dec_26_20_13_49_2014.txt',
'data1Fri_Dec_26_20_14_04_2014.txt',
'data1Fri_Dec_26_20_14_19_2014.txt',
'data1Fri_Dec_26_20_14_34_2014.txt',
'data1Fri_Dec_26_20_14_49_2014.txt',
'data1Fri_Dec_26_20_15_04_2014.txt',
'data1Fri_Dec_26_20_15_18_2014.txt',
'data1Fri_Dec_26_20_15_33_2014.txt',
'data1Fri_Dec_26_20_15_48_2014.txt',
'data1Fri_Dec_26_20_16_03_2014.txt',
'data1Fri_Dec_26_20_16_18_2014.txt',
'data1Fri_Dec_26_20_16_33_2014.txt',
'data1Fri_Dec_26_20_16_48_2014.txt',
'data1Fri_Dec_26_20_17_03_2014.txt',
'data1Fri_Dec_26_20_17_18_2014.txt',
'data1Fri_Dec_26_20_17_32_2014.txt',
'data1Fri_Dec_26_20_17_48_2014.txt',
'data1Fri_Dec_26_20_18_02_2014.txt',
'data1Fri_Dec_26_20_18_17_2014.txt',
'data1Fri_Dec_26_20_18_32_2014.txt',
'data1Fri_Dec_26_20_18_46_2014.txt',
'data1Fri_Dec_26_20_19_02_2014.txt',
'data1Fri_Dec_26_20_19_16_2014.txt',
'data1Fri_Dec_26_20_19_31_2014.txt',
'data1Fri_Dec_26_20_19_46_2014.txt',
'data1Fri_Dec_26_20_20_01_2014.txt',
'data1Fri_Dec_26_20_20_15_2014.txt',
'data2Fri_Dec_26_20_20_31_2014.txt',
'data2Fri_Dec_26_20_20_46_2014.txt',
'data2Fri_Dec_26_20_21_01_2014.txt',
'data2Fri_Dec_26_20_21_15_2014.txt',
'data2Fri_Dec_26_20_21_30_2014.txt',
'data2Fri_Dec_26_20_21_45_2014.txt',
'data2Fri_Dec_26_20_22_00_2014.txt',
'data2Fri_Dec_26_20_22_15_2014.txt',
'data2Fri_Dec_26_20_22_30_2014.txt',
'data2Fri_Dec_26_20_22_44_2014.txt',
'data2Fri_Dec_26_20_23_00_2014.txt',
'data2Fri_Dec_26_20_23_14_2014.txt',
'data2Fri_Dec_26_20_23_30_2014.txt',
'data2Fri_Dec_26_20_23_45_2014.txt',
'data2Fri_Dec_26_20_24_00_2014.txt',
'data2Fri_Dec_26_20_24_15_2014.txt',
'data2Fri_Dec_26_20_24_30_2014.txt',
'data2Fri_Dec_26_20_24_45_2014.txt',
'data2Fri_Dec_26_20_25_00_2014.txt',
'data2Fri_Dec_26_20_25_15_2014.txt',
'data2Fri_Dec_26_20_25_30_2014.txt',
'data2Fri_Dec_26_20_25_44_2014.txt',
'data2Fri_Dec_26_20_26_00_2014.txt',
'data2Fri_Dec_26_20_26_15_2014.txt',
'data2Fri_Dec_26_20_26_29_2014.txt',
'data2Fri_Dec_26_20_26_44_2014.txt',
'data2Fri_Dec_26_20_26_59_2014.txt',
'data2Fri_Dec_26_20_27_14_2014.txt',
'data2Fri_Dec_26_20_27_29_2014.txt',
'data2Fri_Dec_26_20_27_44_2014.txt',
'data2Fri_Dec_26_20_27_59_2014.txt',
'data2Fri_Dec_26_20_28_14_2014.txt',
'data2Fri_Dec_26_20_28_28_2014.txt',
'data2Fri_Dec_26_20_28_44_2014.txt',
'data2Fri_Dec_26_20_28_58_2014.txt',
'data2Fri_Dec_26_20_29_13_2014.txt',
'data2Fri_Dec_26_20_29_28_2014.txt',
'data2Fri_Dec_26_20_29_43_2014.txt',
'data2Fri_Dec_26_20_29_58_2014.txt',
'data2Fri_Dec_26_20_30_13_2014.txt',
'data2Fri_Dec_26_20_30_29_2014.txt',
'data2Fri_Dec_26_20_30_44_2014.txt',
'data2Fri_Dec_26_20_30_59_2014.txt',
'data2Fri_Dec_26_20_31_14_2014.txt',
'data2Fri_Dec_26_20_31_30_2014.txt',
'data2Fri_Dec_26_20_31_45_2014.txt',
'data2Fri_Dec_26_20_31_59_2014.txt',
'data2Fri_Dec_26_20_32_14_2014.txt',
'data2Fri_Dec_26_20_32_29_2014.txt',
'data2Fri_Dec_26_20_32_44_2014.txt',
'data3Fri_Dec_26_20_32_59_2014.txt',
'data3Fri_Dec_26_20_33_14_2014.txt',
'data3Fri_Dec_26_20_33_29_2014.txt',
'data3Fri_Dec_26_20_33_44_2014.txt',
'data3Fri_Dec_26_20_33_58_2014.txt',
'data3Fri_Dec_26_20_34_13_2014.txt',
'data3Fri_Dec_26_20_34_28_2014.txt',
'data3Fri_Dec_26_20_34_43_2014.txt',
'data3Fri_Dec_26_20_34_58_2014.txt',
'data3Fri_Dec_26_20_35_13_2014.txt',
'data3Fri_Dec_26_20_35_28_2014.txt',
'data3Fri_Dec_26_20_35_43_2014.txt',
'data3Fri_Dec_26_20_35_58_2014.txt',
'data3Fri_Dec_26_20_36_13_2014.txt',
'data3Fri_Dec_26_20_36_28_2014.txt',
'data3Fri_Dec_26_20_36_42_2014.txt',
'data3Fri_Dec_26_20_36_58_2014.txt',
'data3Fri_Dec_26_20_37_13_2014.txt',
'data3Fri_Dec_26_20_37_28_2014.txt',
'data3Fri_Dec_26_20_37_42_2014.txt',
'data3Fri_Dec_26_20_37_57_2014.txt',
'data3Fri_Dec_26_20_38_12_2014.txt',
'data3Fri_Dec_26_20_38_27_2014.txt',
'data3Fri_Dec_26_20_38_42_2014.txt',
'data3Fri_Dec_26_20_38_57_2014.txt',
'data3Fri_Dec_26_20_39_12_2014.txt',
'data3Fri_Dec_26_20_39_27_2014.txt',
'data3Fri_Dec_26_20_39_41_2014.txt',
'data3Fri_Dec_26_20_39_56_2014.txt',
'data3Fri_Dec_26_20_40_11_2014.txt',
'data3Fri_Dec_26_20_40_25_2014.txt',
'data3Fri_Dec_26_20_40_40_2014.txt',
'data3Fri_Dec_26_20_40_54_2014.txt',
'data3Fri_Dec_26_20_41_09_2014.txt',
'data3Fri_Dec_26_20_41_24_2014.txt',
'data3Fri_Dec_26_20_41_39_2014.txt',
'data3Fri_Dec_26_20_41_53_2014.txt',
'data3Fri_Dec_26_20_42_08_2014.txt',
'data3Fri_Dec_26_20_42_23_2014.txt',
'data3Fri_Dec_26_20_42_38_2014.txt',
'data3Fri_Dec_26_20_42_53_2014.txt',
'data3Fri_Dec_26_20_43_08_2014.txt',
'data3Fri_Dec_26_20_43_23_2014.txt',
'data3Fri_Dec_26_20_43_38_2014.txt',
'data3Fri_Dec_26_20_43_54_2014.txt',
'data3Fri_Dec_26_20_44_09_2014.txt',
'data3Fri_Dec_26_20_44_24_2014.txt',
'data3Fri_Dec_26_20_44_38_2014.txt',
'data3Fri_Dec_26_20_44_53_2014.txt',
'data3Fri_Dec_26_20_45_08_2014.txt']