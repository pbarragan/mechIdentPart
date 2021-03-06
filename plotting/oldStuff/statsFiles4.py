# experiments on 12/23/2014

import json
import os

files = ['data0Tue_Dec_23_22_43_56_2014.txt',
         'data0Tue_Dec_23_22_43_59_2014.txt',
         'data0Tue_Dec_23_22_44_01_2014.txt',
         'data0Tue_Dec_23_22_44_04_2014.txt',
         'data0Tue_Dec_23_22_44_07_2014.txt',
         'data0Tue_Dec_23_22_44_09_2014.txt',
         'data0Tue_Dec_23_22_44_12_2014.txt',
         'data0Tue_Dec_23_22_44_15_2014.txt',
         'data0Tue_Dec_23_22_44_17_2014.txt',
         'data0Tue_Dec_23_22_44_20_2014.txt',
         'data0Tue_Dec_23_22_44_23_2014.txt',
         'data0Tue_Dec_23_22_44_25_2014.txt',
         'data0Tue_Dec_23_22_44_28_2014.txt',
         'data0Tue_Dec_23_22_44_31_2014.txt',
         'data0Tue_Dec_23_22_44_33_2014.txt',
         'data0Tue_Dec_23_22_44_36_2014.txt',
         'data0Tue_Dec_23_22_44_39_2014.txt',
         'data0Tue_Dec_23_22_44_41_2014.txt',
         'data0Tue_Dec_23_22_44_44_2014.txt',
         'data0Tue_Dec_23_22_44_47_2014.txt',
         'data0Tue_Dec_23_22_44_49_2014.txt',
         'data0Tue_Dec_23_22_44_52_2014.txt',
         'data0Tue_Dec_23_22_44_55_2014.txt',
         'data0Tue_Dec_23_22_44_57_2014.txt',
         'data0Tue_Dec_23_22_45_00_2014.txt',
         'data0Tue_Dec_23_22_45_03_2014.txt',
         'data0Tue_Dec_23_22_45_05_2014.txt',
         'data0Tue_Dec_23_22_45_08_2014.txt',
         'data0Tue_Dec_23_22_45_11_2014.txt',
         'data0Tue_Dec_23_22_45_13_2014.txt',
         'data2Tue_Dec_23_22_45_16_2014.txt',
         'data2Tue_Dec_23_22_45_19_2014.txt',
         'data2Tue_Dec_23_22_45_22_2014.txt',
         'data2Tue_Dec_23_22_45_24_2014.txt',
         'data2Tue_Dec_23_22_45_27_2014.txt',
         'data2Tue_Dec_23_22_45_30_2014.txt',
         'data2Tue_Dec_23_22_45_32_2014.txt',
         'data2Tue_Dec_23_22_45_35_2014.txt',
         'data2Tue_Dec_23_22_45_38_2014.txt',
         'data2Tue_Dec_23_22_45_41_2014.txt',
         'data2Tue_Dec_23_22_45_43_2014.txt',
         'data2Tue_Dec_23_22_45_46_2014.txt',
         'data2Tue_Dec_23_22_45_49_2014.txt',
         'data2Tue_Dec_23_22_45_51_2014.txt',
         'data2Tue_Dec_23_22_45_54_2014.txt',
         'data2Tue_Dec_23_22_45_57_2014.txt',
         'data2Tue_Dec_23_22_45_59_2014.txt',
         'data2Tue_Dec_23_22_46_02_2014.txt',
         'data2Tue_Dec_23_22_46_05_2014.txt',
         'data2Tue_Dec_23_22_46_07_2014.txt',
         'data2Tue_Dec_23_22_46_10_2014.txt',
         'data2Tue_Dec_23_22_46_13_2014.txt',
         'data2Tue_Dec_23_22_46_15_2014.txt',
         'data2Tue_Dec_23_22_46_18_2014.txt',
         'data2Tue_Dec_23_22_46_21_2014.txt',
         'data2Tue_Dec_23_22_46_23_2014.txt',
         'data2Tue_Dec_23_22_46_26_2014.txt',
         'data2Tue_Dec_23_22_46_29_2014.txt',
         'data2Tue_Dec_23_22_46_31_2014.txt',
         'data2Tue_Dec_23_22_46_34_2014.txt',
         'data3Tue_Dec_23_22_46_37_2014.txt',
         'data3Tue_Dec_23_22_46_40_2014.txt',
         'data3Tue_Dec_23_22_46_42_2014.txt',
         'data3Tue_Dec_23_22_46_45_2014.txt',
         'data3Tue_Dec_23_22_46_48_2014.txt',
         'data3Tue_Dec_23_22_46_50_2014.txt',
         'data3Tue_Dec_23_22_46_53_2014.txt',
         'data3Tue_Dec_23_22_46_56_2014.txt',
         'data3Tue_Dec_23_22_46_58_2014.txt',
         'data3Tue_Dec_23_22_47_01_2014.txt',
         'data3Tue_Dec_23_22_47_04_2014.txt',
         'data3Tue_Dec_23_22_47_06_2014.txt',
         'data3Tue_Dec_23_22_47_09_2014.txt',
         'data3Tue_Dec_23_22_47_12_2014.txt',
         'data3Tue_Dec_23_22_47_14_2014.txt',
         'data3Tue_Dec_23_22_47_17_2014.txt',
         'data3Tue_Dec_23_22_47_20_2014.txt',
         'data3Tue_Dec_23_22_47_22_2014.txt',
         'data3Tue_Dec_23_22_47_25_2014.txt',
         'data3Tue_Dec_23_22_47_28_2014.txt',
         'data3Tue_Dec_23_22_47_30_2014.txt',
         'data3Tue_Dec_23_22_47_33_2014.txt',
         'data3Tue_Dec_23_22_47_36_2014.txt',
         'data3Tue_Dec_23_22_47_38_2014.txt',
         'data3Tue_Dec_23_22_47_41_2014.txt',
         'data3Tue_Dec_23_22_47_44_2014.txt',
         'data3Tue_Dec_23_22_47_46_2014.txt',
         'data3Tue_Dec_23_22_47_49_2014.txt',
         'data3Tue_Dec_23_22_47_52_2014.txt',
         'data3Tue_Dec_23_22_47_54_2014.txt',
         'data0Tue_Dec_23_22_51_22_2014.txt',
         'data0Tue_Dec_23_22_51_24_2014.txt',
         'data0Tue_Dec_23_22_51_25_2014.txt',
         'data0Tue_Dec_23_22_51_27_2014.txt',
         'data0Tue_Dec_23_22_51_28_2014.txt',
         'data0Tue_Dec_23_22_51_30_2014.txt',
         'data0Tue_Dec_23_22_51_32_2014.txt',
         'data0Tue_Dec_23_22_51_33_2014.txt',
         'data0Tue_Dec_23_22_51_35_2014.txt',
         'data0Tue_Dec_23_22_51_37_2014.txt',
         'data0Tue_Dec_23_22_51_38_2014.txt',
         'data0Tue_Dec_23_22_51_40_2014.txt',
         'data0Tue_Dec_23_22_51_42_2014.txt',
         'data0Tue_Dec_23_22_51_43_2014.txt',
         'data0Tue_Dec_23_22_51_45_2014.txt',
         'data0Tue_Dec_23_22_51_47_2014.txt',
         'data0Tue_Dec_23_22_51_48_2014.txt',
         'data0Tue_Dec_23_22_51_50_2014.txt',
         'data0Tue_Dec_23_22_51_51_2014.txt',
         'data0Tue_Dec_23_22_51_53_2014.txt',
         'data0Tue_Dec_23_22_51_55_2014.txt',
         'data0Tue_Dec_23_22_51_56_2014.txt',
         'data0Tue_Dec_23_22_51_58_2014.txt',
         'data0Tue_Dec_23_22_52_00_2014.txt',
         'data0Tue_Dec_23_22_52_01_2014.txt',
         'data0Tue_Dec_23_22_52_03_2014.txt',
         'data0Tue_Dec_23_22_52_05_2014.txt',
         'data0Tue_Dec_23_22_52_06_2014.txt',
         'data0Tue_Dec_23_22_52_08_2014.txt',
         'data0Tue_Dec_23_22_52_10_2014.txt',
         'data2Tue_Dec_23_22_52_11_2014.txt',
         'data2Tue_Dec_23_22_52_13_2014.txt',
         'data2Tue_Dec_23_22_52_15_2014.txt',
         'data2Tue_Dec_23_22_52_16_2014.txt',
         'data2Tue_Dec_23_22_52_18_2014.txt',
         'data2Tue_Dec_23_22_52_19_2014.txt',
         'data2Tue_Dec_23_22_52_21_2014.txt',
         'data2Tue_Dec_23_22_52_23_2014.txt',
         'data2Tue_Dec_23_22_52_24_2014.txt',
         'data2Tue_Dec_23_22_52_26_2014.txt',
         'data2Tue_Dec_23_22_52_28_2014.txt',
         'data2Tue_Dec_23_22_52_29_2014.txt',
         'data2Tue_Dec_23_22_52_31_2014.txt',
         'data2Tue_Dec_23_22_52_33_2014.txt',
         'data2Tue_Dec_23_22_52_34_2014.txt',
         'data2Tue_Dec_23_22_52_36_2014.txt',
         'data2Tue_Dec_23_22_52_38_2014.txt',
         'data2Tue_Dec_23_22_52_39_2014.txt',
         'data2Tue_Dec_23_22_52_41_2014.txt',
         'data2Tue_Dec_23_22_52_43_2014.txt',
         'data2Tue_Dec_23_22_52_44_2014.txt',
         'data2Tue_Dec_23_22_52_46_2014.txt',
         'data2Tue_Dec_23_22_52_48_2014.txt',
         'data2Tue_Dec_23_22_52_49_2014.txt',
         'data2Tue_Dec_23_22_52_51_2014.txt',
         'data2Tue_Dec_23_22_52_52_2014.txt',
         'data2Tue_Dec_23_22_52_54_2014.txt',
         'data2Tue_Dec_23_22_52_56_2014.txt',
         'data2Tue_Dec_23_22_52_57_2014.txt',
         'data2Tue_Dec_23_22_52_59_2014.txt',
         'data3Tue_Dec_23_22_53_01_2014.txt',
         'data3Tue_Dec_23_22_53_02_2014.txt',
         'data3Tue_Dec_23_22_53_04_2014.txt',
         'data3Tue_Dec_23_22_53_06_2014.txt',
         'data3Tue_Dec_23_22_53_07_2014.txt',
         'data3Tue_Dec_23_22_53_09_2014.txt',
         'data3Tue_Dec_23_22_53_11_2014.txt',
         'data3Tue_Dec_23_22_53_12_2014.txt',
         'data3Tue_Dec_23_22_53_14_2014.txt',
         'data3Tue_Dec_23_22_53_16_2014.txt',
         'data3Tue_Dec_23_22_53_17_2014.txt',
         'data3Tue_Dec_23_22_53_19_2014.txt',
         'data3Tue_Dec_23_22_53_21_2014.txt',
         'data3Tue_Dec_23_22_53_22_2014.txt',
         'data3Tue_Dec_23_22_53_24_2014.txt',
         'data3Tue_Dec_23_22_53_26_2014.txt',
         'data3Tue_Dec_23_22_53_27_2014.txt',
         'data3Tue_Dec_23_22_53_29_2014.txt',
         'data3Tue_Dec_23_22_53_31_2014.txt',
         'data3Tue_Dec_23_22_53_32_2014.txt',
         'data3Tue_Dec_23_22_53_34_2014.txt',
         'data3Tue_Dec_23_22_53_36_2014.txt',
         'data3Tue_Dec_23_22_53_37_2014.txt',
         'data3Tue_Dec_23_22_53_39_2014.txt',
         'data3Tue_Dec_23_22_53_41_2014.txt',
         'data3Tue_Dec_23_22_53_42_2014.txt',
         'data3Tue_Dec_23_22_53_44_2014.txt',
         'data3Tue_Dec_23_22_53_46_2014.txt',
         'data3Tue_Dec_23_22_53_47_2014.txt',
         'data3Tue_Dec_23_22_53_49_2014.txt',
         'data0Tue_Dec_23_22_57_02_2014.txt',
         'data0Tue_Dec_23_22_57_03_2014.txt',
         'data0Tue_Dec_23_22_57_05_2014.txt',
         'data0Tue_Dec_23_22_57_07_2014.txt',
         'data0Tue_Dec_23_22_57_08_2014.txt',
         'data0Tue_Dec_23_22_57_10_2014.txt',
         'data0Tue_Dec_23_22_57_12_2014.txt',
         'data0Tue_Dec_23_22_57_13_2014.txt',
         'data0Tue_Dec_23_22_57_15_2014.txt',
         'data0Tue_Dec_23_22_57_17_2014.txt',
         'data0Tue_Dec_23_22_57_18_2014.txt',
         'data0Tue_Dec_23_22_57_20_2014.txt',
         'data0Tue_Dec_23_22_57_22_2014.txt',
         'data0Tue_Dec_23_22_57_23_2014.txt',
         'data0Tue_Dec_23_22_57_25_2014.txt',
         'data0Tue_Dec_23_22_57_27_2014.txt',
         'data0Tue_Dec_23_22_57_28_2014.txt',
         'data0Tue_Dec_23_22_57_30_2014.txt',
         'data0Tue_Dec_23_22_57_32_2014.txt',
         'data0Tue_Dec_23_22_57_33_2014.txt',
         'data0Tue_Dec_23_22_57_35_2014.txt',
         'data0Tue_Dec_23_22_57_37_2014.txt',
         'data0Tue_Dec_23_22_57_38_2014.txt',
         'data0Tue_Dec_23_22_57_40_2014.txt',
         'data0Tue_Dec_23_22_57_42_2014.txt',
         'data0Tue_Dec_23_22_57_43_2014.txt',
         'data0Tue_Dec_23_22_57_45_2014.txt',
         'data0Tue_Dec_23_22_57_47_2014.txt',
         'data0Tue_Dec_23_22_57_48_2014.txt',
         'data0Tue_Dec_23_22_57_50_2014.txt',
         'data2Tue_Dec_23_22_57_52_2014.txt',
         'data2Tue_Dec_23_22_57_53_2014.txt',
         'data2Tue_Dec_23_22_57_55_2014.txt',
         'data2Tue_Dec_23_22_57_57_2014.txt',
         'data2Tue_Dec_23_22_57_58_2014.txt',
         'data2Tue_Dec_23_22_58_00_2014.txt',
         'data2Tue_Dec_23_22_58_02_2014.txt',
         'data2Tue_Dec_23_22_58_03_2014.txt',
         'data2Tue_Dec_23_22_58_05_2014.txt',
         'data2Tue_Dec_23_22_58_07_2014.txt',
         'data2Tue_Dec_23_22_58_08_2014.txt',
         'data2Tue_Dec_23_22_58_10_2014.txt',
         'data2Tue_Dec_23_22_58_11_2014.txt',
         'data2Tue_Dec_23_22_58_13_2014.txt',
         'data2Tue_Dec_23_22_58_15_2014.txt',
         'data2Tue_Dec_23_22_58_16_2014.txt',
         'data2Tue_Dec_23_22_58_18_2014.txt',
         'data2Tue_Dec_23_22_58_20_2014.txt',
         'data2Tue_Dec_23_22_58_21_2014.txt',
         'data2Tue_Dec_23_22_58_23_2014.txt',
         'data2Tue_Dec_23_22_58_25_2014.txt',
         'data2Tue_Dec_23_22_58_26_2014.txt',
         'data2Tue_Dec_23_22_58_28_2014.txt',
         'data2Tue_Dec_23_22_58_30_2014.txt',
         'data2Tue_Dec_23_22_58_31_2014.txt',
         'data2Tue_Dec_23_22_58_33_2014.txt',
         'data2Tue_Dec_23_22_58_35_2014.txt',
         'data2Tue_Dec_23_22_58_36_2014.txt',
         'data2Tue_Dec_23_22_58_38_2014.txt',
         'data2Tue_Dec_23_22_58_40_2014.txt',
         'data3Tue_Dec_23_22_58_41_2014.txt',
         'data3Tue_Dec_23_22_58_43_2014.txt',
         'data3Tue_Dec_23_22_58_45_2014.txt',
         'data3Tue_Dec_23_22_58_46_2014.txt',
         'data3Tue_Dec_23_22_58_48_2014.txt',
         'data3Tue_Dec_23_22_58_50_2014.txt',
         'data3Tue_Dec_23_22_58_51_2014.txt',
         'data3Tue_Dec_23_22_58_53_2014.txt',
         'data3Tue_Dec_23_22_58_55_2014.txt',
         'data3Tue_Dec_23_22_58_56_2014.txt',
         'data3Tue_Dec_23_22_58_58_2014.txt',
         'data3Tue_Dec_23_22_59_00_2014.txt',
         'data3Tue_Dec_23_22_59_01_2014.txt',
         'data3Tue_Dec_23_22_59_03_2014.txt',
         'data3Tue_Dec_23_22_59_05_2014.txt',
         'data3Tue_Dec_23_22_59_06_2014.txt',
         'data3Tue_Dec_23_22_59_08_2014.txt',
         'data3Tue_Dec_23_22_59_10_2014.txt',
         'data3Tue_Dec_23_22_59_11_2014.txt',
         'data3Tue_Dec_23_22_59_13_2014.txt',
         'data3Tue_Dec_23_22_59_14_2014.txt',
         'data3Tue_Dec_23_22_59_16_2014.txt',
         'data3Tue_Dec_23_22_59_18_2014.txt',
         'data3Tue_Dec_23_22_59_19_2014.txt',
         'data3Tue_Dec_23_22_59_21_2014.txt',
         'data3Tue_Dec_23_22_59_23_2014.txt',
         'data3Tue_Dec_23_22_59_24_2014.txt',
         'data3Tue_Dec_23_22_59_26_2014.txt',
         'data3Tue_Dec_23_22_59_28_2014.txt',
         'data3Tue_Dec_23_22_59_29_2014.txt',
         'data0Tue_Dec_23_23_01_24_2014.txt',
         'data0Tue_Dec_23_23_01_25_2014.txt',
         'data0Tue_Dec_23_23_01_27_2014.txt',
         'data0Tue_Dec_23_23_01_29_2014.txt',
         'data0Tue_Dec_23_23_01_30_2014.txt',
         'data0Tue_Dec_23_23_01_32_2014.txt',
         'data0Tue_Dec_23_23_01_34_2014.txt',
         'data0Tue_Dec_23_23_01_35_2014.txt',
         'data0Tue_Dec_23_23_01_37_2014.txt',
         'data0Tue_Dec_23_23_01_39_2014.txt',
         'data0Tue_Dec_23_23_01_41_2014.txt',
         'data0Tue_Dec_23_23_01_42_2014.txt',
         'data0Tue_Dec_23_23_01_44_2014.txt',
         'data0Tue_Dec_23_23_01_46_2014.txt',
         'data0Tue_Dec_23_23_01_47_2014.txt',
         'data0Tue_Dec_23_23_01_49_2014.txt',
         'data0Tue_Dec_23_23_01_51_2014.txt',
         'data0Tue_Dec_23_23_01_52_2014.txt',
         'data0Tue_Dec_23_23_01_54_2014.txt',
         'data0Tue_Dec_23_23_01_56_2014.txt',
         'data0Tue_Dec_23_23_01_57_2014.txt',
         'data0Tue_Dec_23_23_01_59_2014.txt',
         'data0Tue_Dec_23_23_02_01_2014.txt',
         'data0Tue_Dec_23_23_02_02_2014.txt',
         'data0Tue_Dec_23_23_02_04_2014.txt',
         'data0Tue_Dec_23_23_02_06_2014.txt',
         'data0Tue_Dec_23_23_02_07_2014.txt',
         'data0Tue_Dec_23_23_02_09_2014.txt',
         'data0Tue_Dec_23_23_02_11_2014.txt',
         'data0Tue_Dec_23_23_02_12_2014.txt',
         'data2Tue_Dec_23_23_02_14_2014.txt',
         'data2Tue_Dec_23_23_02_16_2014.txt',
         'data2Tue_Dec_23_23_02_17_2014.txt',
         'data2Tue_Dec_23_23_02_19_2014.txt',
         'data2Tue_Dec_23_23_02_21_2014.txt',
         'data2Tue_Dec_23_23_02_23_2014.txt',
         'data2Tue_Dec_23_23_02_24_2014.txt',
         'data2Tue_Dec_23_23_02_26_2014.txt',
         'data2Tue_Dec_23_23_02_28_2014.txt',
         'data2Tue_Dec_23_23_02_29_2014.txt',
         'data2Tue_Dec_23_23_02_31_2014.txt',
         'data2Tue_Dec_23_23_02_33_2014.txt',
         'data2Tue_Dec_23_23_02_34_2014.txt',
         'data2Tue_Dec_23_23_02_36_2014.txt',
         'data2Tue_Dec_23_23_02_38_2014.txt',
         'data2Tue_Dec_23_23_02_39_2014.txt',
         'data2Tue_Dec_23_23_02_41_2014.txt',
         'data2Tue_Dec_23_23_02_43_2014.txt',
         'data2Tue_Dec_23_23_02_44_2014.txt',
         'data2Tue_Dec_23_23_02_46_2014.txt',
         'data2Tue_Dec_23_23_02_48_2014.txt',
         'data2Tue_Dec_23_23_02_49_2014.txt',
         'data2Tue_Dec_23_23_02_51_2014.txt',
         'data2Tue_Dec_23_23_02_52_2014.txt',
         'data2Tue_Dec_23_23_02_54_2014.txt',
         'data2Tue_Dec_23_23_02_56_2014.txt',
         'data2Tue_Dec_23_23_02_57_2014.txt',
         'data2Tue_Dec_23_23_02_59_2014.txt',
         'data2Tue_Dec_23_23_03_01_2014.txt',
         'data2Tue_Dec_23_23_03_03_2014.txt',
         'data3Tue_Dec_23_23_03_04_2014.txt',
         'data3Tue_Dec_23_23_03_06_2014.txt',
         'data3Tue_Dec_23_23_03_08_2014.txt',
         'data3Tue_Dec_23_23_03_09_2014.txt',
         'data3Tue_Dec_23_23_03_11_2014.txt',
         'data3Tue_Dec_23_23_03_13_2014.txt',
         'data3Tue_Dec_23_23_03_14_2014.txt',
         'data3Tue_Dec_23_23_03_16_2014.txt',
         'data3Tue_Dec_23_23_03_18_2014.txt',
         'data3Tue_Dec_23_23_03_19_2014.txt',
         'data3Tue_Dec_23_23_03_21_2014.txt',
         'data3Tue_Dec_23_23_03_23_2014.txt',
         'data3Tue_Dec_23_23_03_24_2014.txt',
         'data3Tue_Dec_23_23_03_26_2014.txt',
         'data3Tue_Dec_23_23_03_28_2014.txt',
         'data3Tue_Dec_23_23_03_29_2014.txt',
         'data3Tue_Dec_23_23_03_31_2014.txt',
         'data3Tue_Dec_23_23_03_33_2014.txt',
         'data3Tue_Dec_23_23_03_34_2014.txt',
         'data3Tue_Dec_23_23_03_36_2014.txt',
         'data3Tue_Dec_23_23_03_38_2014.txt',
         'data3Tue_Dec_23_23_03_39_2014.txt',
         'data3Tue_Dec_23_23_03_41_2014.txt',
         'data3Tue_Dec_23_23_03_43_2014.txt',
         'data3Tue_Dec_23_23_03_44_2014.txt',
         'data3Tue_Dec_23_23_03_46_2014.txt',
         'data3Tue_Dec_23_23_03_48_2014.txt',
         'data3Tue_Dec_23_23_03_49_2014.txt',
         'data3Tue_Dec_23_23_03_51_2014.txt',
         'data3Tue_Dec_23_23_03_53_2014.txt',
         'data0Tue_Dec_23_23_05_38_2014.txt',
         'data0Tue_Dec_23_23_05_40_2014.txt',
         'data0Tue_Dec_23_23_05_42_2014.txt',
         'data0Tue_Dec_23_23_05_43_2014.txt',
         'data0Tue_Dec_23_23_05_45_2014.txt',
         'data0Tue_Dec_23_23_05_47_2014.txt',
         'data0Tue_Dec_23_23_05_48_2014.txt',
         'data0Tue_Dec_23_23_05_50_2014.txt',
         'data0Tue_Dec_23_23_05_52_2014.txt',
         'data0Tue_Dec_23_23_05_53_2014.txt',
         'data0Tue_Dec_23_23_05_55_2014.txt',
         'data0Tue_Dec_23_23_05_57_2014.txt',
         'data0Tue_Dec_23_23_05_58_2014.txt',
         'data0Tue_Dec_23_23_06_00_2014.txt',
         'data0Tue_Dec_23_23_06_02_2014.txt',
         'data0Tue_Dec_23_23_06_03_2014.txt',
         'data0Tue_Dec_23_23_06_05_2014.txt',
         'data0Tue_Dec_23_23_06_06_2014.txt',
         'data0Tue_Dec_23_23_06_08_2014.txt',
         'data0Tue_Dec_23_23_06_10_2014.txt',
         'data0Tue_Dec_23_23_06_11_2014.txt',
         'data0Tue_Dec_23_23_06_13_2014.txt',
         'data0Tue_Dec_23_23_06_15_2014.txt',
         'data0Tue_Dec_23_23_06_16_2014.txt',
         'data0Tue_Dec_23_23_06_18_2014.txt',
         'data0Tue_Dec_23_23_06_20_2014.txt',
         'data0Tue_Dec_23_23_06_21_2014.txt',
         'data0Tue_Dec_23_23_06_23_2014.txt',
         'data0Tue_Dec_23_23_06_25_2014.txt',
         'data0Tue_Dec_23_23_06_26_2014.txt',
         'data2Tue_Dec_23_23_06_28_2014.txt',
         'data2Tue_Dec_23_23_06_30_2014.txt',
         'data2Tue_Dec_23_23_06_31_2014.txt',
         'data2Tue_Dec_23_23_06_33_2014.txt',
         'data2Tue_Dec_23_23_06_34_2014.txt',
         'data2Tue_Dec_23_23_06_36_2014.txt',
         'data2Tue_Dec_23_23_06_38_2014.txt',
         'data2Tue_Dec_23_23_06_39_2014.txt',
         'data2Tue_Dec_23_23_06_41_2014.txt',
         'data2Tue_Dec_23_23_06_43_2014.txt',
         'data2Tue_Dec_23_23_06_44_2014.txt',
         'data2Tue_Dec_23_23_06_46_2014.txt',
         'data2Tue_Dec_23_23_06_48_2014.txt',
         'data2Tue_Dec_23_23_06_49_2014.txt',
         'data2Tue_Dec_23_23_06_51_2014.txt',
         'data2Tue_Dec_23_23_06_53_2014.txt',
         'data2Tue_Dec_23_23_06_54_2014.txt',
         'data2Tue_Dec_23_23_06_56_2014.txt',
         'data2Tue_Dec_23_23_06_58_2014.txt',
         'data2Tue_Dec_23_23_06_59_2014.txt',
         'data2Tue_Dec_23_23_07_01_2014.txt',
         'data2Tue_Dec_23_23_07_02_2014.txt',
         'data2Tue_Dec_23_23_07_04_2014.txt',
         'data2Tue_Dec_23_23_07_06_2014.txt',
         'data2Tue_Dec_23_23_07_07_2014.txt',
         'data2Tue_Dec_23_23_07_09_2014.txt',
         'data2Tue_Dec_23_23_07_11_2014.txt',
         'data2Tue_Dec_23_23_07_12_2014.txt',
         'data2Tue_Dec_23_23_07_14_2014.txt',
         'data2Tue_Dec_23_23_07_16_2014.txt',
         'data3Tue_Dec_23_23_07_17_2014.txt',
         'data3Tue_Dec_23_23_07_19_2014.txt',
         'data3Tue_Dec_23_23_07_21_2014.txt',
         'data3Tue_Dec_23_23_07_23_2014.txt',
         'data3Tue_Dec_23_23_07_24_2014.txt',
         'data3Tue_Dec_23_23_07_26_2014.txt',
         'data3Tue_Dec_23_23_07_28_2014.txt',
         'data3Tue_Dec_23_23_07_29_2014.txt',
         'data3Tue_Dec_23_23_07_31_2014.txt',
         'data3Tue_Dec_23_23_07_33_2014.txt',
         'data3Tue_Dec_23_23_07_34_2014.txt',
         'data3Tue_Dec_23_23_07_36_2014.txt',
         'data3Tue_Dec_23_23_07_37_2014.txt',
         'data3Tue_Dec_23_23_07_39_2014.txt',
         'data3Tue_Dec_23_23_07_41_2014.txt',
         'data3Tue_Dec_23_23_07_42_2014.txt',
         'data3Tue_Dec_23_23_07_44_2014.txt',
         'data3Tue_Dec_23_23_07_46_2014.txt',
         'data3Tue_Dec_23_23_07_47_2014.txt',
         'data3Tue_Dec_23_23_07_49_2014.txt',
         'data3Tue_Dec_23_23_07_51_2014.txt',
         'data3Tue_Dec_23_23_07_52_2014.txt',
         'data3Tue_Dec_23_23_07_54_2014.txt',
         'data3Tue_Dec_23_23_07_56_2014.txt',
         'data3Tue_Dec_23_23_07_57_2014.txt',
         'data3Tue_Dec_23_23_07_59_2014.txt',
         'data3Tue_Dec_23_23_08_01_2014.txt',
         'data3Tue_Dec_23_23_08_02_2014.txt',
         'data3Tue_Dec_23_23_08_04_2014.txt',
         'data3Tue_Dec_23_23_08_06_2014.txt',
         'data0Tue_Dec_23_23_09_10_2014.txt',
         'data0Tue_Dec_23_23_09_12_2014.txt',
         'data0Tue_Dec_23_23_09_14_2014.txt',
         'data0Tue_Dec_23_23_09_15_2014.txt',
         'data0Tue_Dec_23_23_09_17_2014.txt',
         'data0Tue_Dec_23_23_09_19_2014.txt',
         'data0Tue_Dec_23_23_09_20_2014.txt',
         'data0Tue_Dec_23_23_09_22_2014.txt',
         'data0Tue_Dec_23_23_09_24_2014.txt',
         'data0Tue_Dec_23_23_09_25_2014.txt',
         'data0Tue_Dec_23_23_09_27_2014.txt',
         'data0Tue_Dec_23_23_09_29_2014.txt',
         'data0Tue_Dec_23_23_09_30_2014.txt',
         'data0Tue_Dec_23_23_09_32_2014.txt',
         'data0Tue_Dec_23_23_09_34_2014.txt',
         'data0Tue_Dec_23_23_09_35_2014.txt',
         'data0Tue_Dec_23_23_09_37_2014.txt',
         'data0Tue_Dec_23_23_09_38_2014.txt',
         'data0Tue_Dec_23_23_09_40_2014.txt',
         'data0Tue_Dec_23_23_09_42_2014.txt',
         'data0Tue_Dec_23_23_09_44_2014.txt',
         'data0Tue_Dec_23_23_09_45_2014.txt',
         'data0Tue_Dec_23_23_09_47_2014.txt',
         'data0Tue_Dec_23_23_09_49_2014.txt',
         'data0Tue_Dec_23_23_09_50_2014.txt',
         'data0Tue_Dec_23_23_09_52_2014.txt',
         'data0Tue_Dec_23_23_09_54_2014.txt',
         'data0Tue_Dec_23_23_09_55_2014.txt',
         'data0Tue_Dec_23_23_09_57_2014.txt',
         'data0Tue_Dec_23_23_09_59_2014.txt',
         'data2Tue_Dec_23_23_10_00_2014.txt',
         'data2Tue_Dec_23_23_10_02_2014.txt',
         'data2Tue_Dec_23_23_10_04_2014.txt',
         'data2Tue_Dec_23_23_10_05_2014.txt',
         'data2Tue_Dec_23_23_10_07_2014.txt',
         'data2Tue_Dec_23_23_10_09_2014.txt',
         'data2Tue_Dec_23_23_10_10_2014.txt',
         'data2Tue_Dec_23_23_10_12_2014.txt',
         'data2Tue_Dec_23_23_10_13_2014.txt',
         'data2Tue_Dec_23_23_10_15_2014.txt',
         'data2Tue_Dec_23_23_10_17_2014.txt',
         'data2Tue_Dec_23_23_10_18_2014.txt',
         'data2Tue_Dec_23_23_10_20_2014.txt',
         'data2Tue_Dec_23_23_10_22_2014.txt',
         'data2Tue_Dec_23_23_10_23_2014.txt',
         'data2Tue_Dec_23_23_10_25_2014.txt',
         'data2Tue_Dec_23_23_10_27_2014.txt',
         'data2Tue_Dec_23_23_10_28_2014.txt',
         'data2Tue_Dec_23_23_10_30_2014.txt',
         'data2Tue_Dec_23_23_10_32_2014.txt',
         'data2Tue_Dec_23_23_10_33_2014.txt',
         'data2Tue_Dec_23_23_10_35_2014.txt',
         'data2Tue_Dec_23_23_10_37_2014.txt',
         'data2Tue_Dec_23_23_10_38_2014.txt',
         'data2Tue_Dec_23_23_10_40_2014.txt',
         'data2Tue_Dec_23_23_10_42_2014.txt',
         'data2Tue_Dec_23_23_10_43_2014.txt',
         'data2Tue_Dec_23_23_10_45_2014.txt',
         'data2Tue_Dec_23_23_10_47_2014.txt',
         'data2Tue_Dec_23_23_10_48_2014.txt',
         'data3Tue_Dec_23_23_10_50_2014.txt',
         'data3Tue_Dec_23_23_10_51_2014.txt',
         'data3Tue_Dec_23_23_10_53_2014.txt',
         'data3Tue_Dec_23_23_10_55_2014.txt',
         'data3Tue_Dec_23_23_10_56_2014.txt',
         'data3Tue_Dec_23_23_10_58_2014.txt',
         'data3Tue_Dec_23_23_11_00_2014.txt',
         'data3Tue_Dec_23_23_11_01_2014.txt',
         'data3Tue_Dec_23_23_11_03_2014.txt',
         'data3Tue_Dec_23_23_11_05_2014.txt',
         'data3Tue_Dec_23_23_11_06_2014.txt',
         'data3Tue_Dec_23_23_11_08_2014.txt',
         'data3Tue_Dec_23_23_11_10_2014.txt',
         'data3Tue_Dec_23_23_11_11_2014.txt',
         'data3Tue_Dec_23_23_11_13_2014.txt',
         'data3Tue_Dec_23_23_11_15_2014.txt',
         'data3Tue_Dec_23_23_11_16_2014.txt',
         'data3Tue_Dec_23_23_11_18_2014.txt',
         'data3Tue_Dec_23_23_11_19_2014.txt',
         'data3Tue_Dec_23_23_11_21_2014.txt',
         'data3Tue_Dec_23_23_11_23_2014.txt',
         'data3Tue_Dec_23_23_11_24_2014.txt',
         'data3Tue_Dec_23_23_11_26_2014.txt',
         'data3Tue_Dec_23_23_11_28_2014.txt',
         'data3Tue_Dec_23_23_11_29_2014.txt',
         'data3Tue_Dec_23_23_11_31_2014.txt',
         'data3Tue_Dec_23_23_11_33_2014.txt',
         'data3Tue_Dec_23_23_11_34_2014.txt',
         'data3Tue_Dec_23_23_11_36_2014.txt',
         'data3Tue_Dec_23_23_11_38_2014.txt',
         'data0Tue_Dec_23_23_15_12_2014.txt',
         'data0Tue_Dec_23_23_15_14_2014.txt',
         'data0Tue_Dec_23_23_15_16_2014.txt',
         'data0Tue_Dec_23_23_15_17_2014.txt',
         'data0Tue_Dec_23_23_15_19_2014.txt',
         'data0Tue_Dec_23_23_15_21_2014.txt',
         'data0Tue_Dec_23_23_15_22_2014.txt',
         'data0Tue_Dec_23_23_15_24_2014.txt',
         'data0Tue_Dec_23_23_15_26_2014.txt',
         'data0Tue_Dec_23_23_15_28_2014.txt',
         'data0Tue_Dec_23_23_15_29_2014.txt',
         'data0Tue_Dec_23_23_15_31_2014.txt',
         'data0Tue_Dec_23_23_15_32_2014.txt',
         'data0Tue_Dec_23_23_15_34_2014.txt',
         'data0Tue_Dec_23_23_15_36_2014.txt',
         'data0Tue_Dec_23_23_15_38_2014.txt',
         'data0Tue_Dec_23_23_15_39_2014.txt',
         'data0Tue_Dec_23_23_15_41_2014.txt',
         'data0Tue_Dec_23_23_15_43_2014.txt',
         'data0Tue_Dec_23_23_15_44_2014.txt',
         'data0Tue_Dec_23_23_15_46_2014.txt',
         'data0Tue_Dec_23_23_15_48_2014.txt',
         'data0Tue_Dec_23_23_15_49_2014.txt',
         'data0Tue_Dec_23_23_15_51_2014.txt',
         'data0Tue_Dec_23_23_15_53_2014.txt',
         'data0Tue_Dec_23_23_15_54_2014.txt',
         'data0Tue_Dec_23_23_15_56_2014.txt',
         'data0Tue_Dec_23_23_15_58_2014.txt',
         'data0Tue_Dec_23_23_15_59_2014.txt',
         'data0Tue_Dec_23_23_16_01_2014.txt',
         'data2Tue_Dec_23_23_16_03_2014.txt',
         'data2Tue_Dec_23_23_16_05_2014.txt',
         'data2Tue_Dec_23_23_16_06_2014.txt',
         'data2Tue_Dec_23_23_16_08_2014.txt',
         'data2Tue_Dec_23_23_16_10_2014.txt',
         'data2Tue_Dec_23_23_16_11_2014.txt',
         'data2Tue_Dec_23_23_16_13_2014.txt',
         'data2Tue_Dec_23_23_16_15_2014.txt',
         'data2Tue_Dec_23_23_16_16_2014.txt',
         'data2Tue_Dec_23_23_16_18_2014.txt',
         'data2Tue_Dec_23_23_16_20_2014.txt',
         'data2Tue_Dec_23_23_16_21_2014.txt',
         'data2Tue_Dec_23_23_16_23_2014.txt',
         'data2Tue_Dec_23_23_16_25_2014.txt',
         'data2Tue_Dec_23_23_16_26_2014.txt',
         'data2Tue_Dec_23_23_16_28_2014.txt',
         'data2Tue_Dec_23_23_16_30_2014.txt',
         'data2Tue_Dec_23_23_16_31_2014.txt',
         'data2Tue_Dec_23_23_16_33_2014.txt',
         'data2Tue_Dec_23_23_16_35_2014.txt',
         'data2Tue_Dec_23_23_16_36_2014.txt',
         'data2Tue_Dec_23_23_16_38_2014.txt',
         'data2Tue_Dec_23_23_16_40_2014.txt',
         'data2Tue_Dec_23_23_16_41_2014.txt',
         'data2Tue_Dec_23_23_16_43_2014.txt',
         'data2Tue_Dec_23_23_16_45_2014.txt',
         'data2Tue_Dec_23_23_16_46_2014.txt',
         'data2Tue_Dec_23_23_16_48_2014.txt',
         'data2Tue_Dec_23_23_16_50_2014.txt',
         'data2Tue_Dec_23_23_16_51_2014.txt',
         'data3Tue_Dec_23_23_16_53_2014.txt',
         'data3Tue_Dec_23_23_16_55_2014.txt',
         'data3Tue_Dec_23_23_16_57_2014.txt',
         'data3Tue_Dec_23_23_16_58_2014.txt',
         'data3Tue_Dec_23_23_17_00_2014.txt',
         'data3Tue_Dec_23_23_17_02_2014.txt',
         'data3Tue_Dec_23_23_17_03_2014.txt',
         'data3Tue_Dec_23_23_17_05_2014.txt',
         'data3Tue_Dec_23_23_17_07_2014.txt',
         'data3Tue_Dec_23_23_17_08_2014.txt',
         'data3Tue_Dec_23_23_17_10_2014.txt',
         'data3Tue_Dec_23_23_17_12_2014.txt',
         'data3Tue_Dec_23_23_17_13_2014.txt',
         'data3Tue_Dec_23_23_17_15_2014.txt',
         'data3Tue_Dec_23_23_17_17_2014.txt',
         'data3Tue_Dec_23_23_17_18_2014.txt',
         'data3Tue_Dec_23_23_17_20_2014.txt',
         'data3Tue_Dec_23_23_17_22_2014.txt',
         'data3Tue_Dec_23_23_17_23_2014.txt',
         'data3Tue_Dec_23_23_17_25_2014.txt',
         'data3Tue_Dec_23_23_17_27_2014.txt',
         'data3Tue_Dec_23_23_17_28_2014.txt',
         'data3Tue_Dec_23_23_17_30_2014.txt',
         'data3Tue_Dec_23_23_17_32_2014.txt',
         'data3Tue_Dec_23_23_17_33_2014.txt',
         'data3Tue_Dec_23_23_17_35_2014.txt',
         'data3Tue_Dec_23_23_17_37_2014.txt',
         'data3Tue_Dec_23_23_17_38_2014.txt',
         'data3Tue_Dec_23_23_17_40_2014.txt',
         'data3Tue_Dec_23_23_17_42_2014.txt',
         'data0Tue_Dec_23_23_18_41_2014.txt',
         'data0Tue_Dec_23_23_18_43_2014.txt',
         'data0Tue_Dec_23_23_18_45_2014.txt',
         'data0Tue_Dec_23_23_18_46_2014.txt',
         'data0Tue_Dec_23_23_18_48_2014.txt',
         'data0Tue_Dec_23_23_18_50_2014.txt',
         'data0Tue_Dec_23_23_18_51_2014.txt',
         'data0Tue_Dec_23_23_18_53_2014.txt',
         'data0Tue_Dec_23_23_18_55_2014.txt',
         'data0Tue_Dec_23_23_18_56_2014.txt',
         'data0Tue_Dec_23_23_18_58_2014.txt',
         'data0Tue_Dec_23_23_19_00_2014.txt',
         'data0Tue_Dec_23_23_19_01_2014.txt',
         'data0Tue_Dec_23_23_19_03_2014.txt',
         'data0Tue_Dec_23_23_19_05_2014.txt',
         'data0Tue_Dec_23_23_19_06_2014.txt',
         'data0Tue_Dec_23_23_19_08_2014.txt',
         'data0Tue_Dec_23_23_19_10_2014.txt',
         'data0Tue_Dec_23_23_19_11_2014.txt',
         'data0Tue_Dec_23_23_19_13_2014.txt',
         'data0Tue_Dec_23_23_19_15_2014.txt',
         'data0Tue_Dec_23_23_19_16_2014.txt',
         'data0Tue_Dec_23_23_19_18_2014.txt',
         'data0Tue_Dec_23_23_19_20_2014.txt',
         'data0Tue_Dec_23_23_19_21_2014.txt',
         'data0Tue_Dec_23_23_19_23_2014.txt',
         'data0Tue_Dec_23_23_19_25_2014.txt',
         'data0Tue_Dec_23_23_19_26_2014.txt',
         'data0Tue_Dec_23_23_19_28_2014.txt',
         'data0Tue_Dec_23_23_19_30_2014.txt',
         'data2Tue_Dec_23_23_19_31_2014.txt',
         'data2Tue_Dec_23_23_19_33_2014.txt',
         'data2Tue_Dec_23_23_19_34_2014.txt',
         'data2Tue_Dec_23_23_19_36_2014.txt',
         'data2Tue_Dec_23_23_19_38_2014.txt',
         'data2Tue_Dec_23_23_19_39_2014.txt',
         'data2Tue_Dec_23_23_19_41_2014.txt',
         'data2Tue_Dec_23_23_19_43_2014.txt',
         'data2Tue_Dec_23_23_19_44_2014.txt',
         'data2Tue_Dec_23_23_19_46_2014.txt',
         'data2Tue_Dec_23_23_19_48_2014.txt',
         'data2Tue_Dec_23_23_19_49_2014.txt',
         'data2Tue_Dec_23_23_19_51_2014.txt',
         'data2Tue_Dec_23_23_19_53_2014.txt',
         'data2Tue_Dec_23_23_19_54_2014.txt',
         'data2Tue_Dec_23_23_19_56_2014.txt',
         'data2Tue_Dec_23_23_19_57_2014.txt',
         'data2Tue_Dec_23_23_19_59_2014.txt',
         'data2Tue_Dec_23_23_20_01_2014.txt',
         'data2Tue_Dec_23_23_20_02_2014.txt',
         'data2Tue_Dec_23_23_20_04_2014.txt',
         'data2Tue_Dec_23_23_20_06_2014.txt',
         'data2Tue_Dec_23_23_20_07_2014.txt',
         'data2Tue_Dec_23_23_20_09_2014.txt',
         'data2Tue_Dec_23_23_20_11_2014.txt',
         'data2Tue_Dec_23_23_20_12_2014.txt',
         'data2Tue_Dec_23_23_20_14_2014.txt',
         'data2Tue_Dec_23_23_20_16_2014.txt',
         'data2Tue_Dec_23_23_20_17_2014.txt',
         'data2Tue_Dec_23_23_20_19_2014.txt',
         'data3Tue_Dec_23_23_20_21_2014.txt',
         'data3Tue_Dec_23_23_20_22_2014.txt',
         'data3Tue_Dec_23_23_20_24_2014.txt',
         'data3Tue_Dec_23_23_20_25_2014.txt',
         'data3Tue_Dec_23_23_20_27_2014.txt',
         'data3Tue_Dec_23_23_20_29_2014.txt',
         'data3Tue_Dec_23_23_20_30_2014.txt',
         'data3Tue_Dec_23_23_20_32_2014.txt',
         'data3Tue_Dec_23_23_20_34_2014.txt',
         'data3Tue_Dec_23_23_20_35_2014.txt',
         'data3Tue_Dec_23_23_20_37_2014.txt',
         'data3Tue_Dec_23_23_20_39_2014.txt',
         'data3Tue_Dec_23_23_20_40_2014.txt',
         'data3Tue_Dec_23_23_20_42_2014.txt',
         'data3Tue_Dec_23_23_20_44_2014.txt',
         'data3Tue_Dec_23_23_20_45_2014.txt',
         'data3Tue_Dec_23_23_20_47_2014.txt',
         'data3Tue_Dec_23_23_20_49_2014.txt',
         'data3Tue_Dec_23_23_20_50_2014.txt',
         'data3Tue_Dec_23_23_20_52_2014.txt',
         'data3Tue_Dec_23_23_20_54_2014.txt',
         'data3Tue_Dec_23_23_20_55_2014.txt',
         'data3Tue_Dec_23_23_20_57_2014.txt',
         'data3Tue_Dec_23_23_20_59_2014.txt',
         'data3Tue_Dec_23_23_21_00_2014.txt',
         'data3Tue_Dec_23_23_21_02_2014.txt',
         'data3Tue_Dec_23_23_21_04_2014.txt',
         'data3Tue_Dec_23_23_21_05_2014.txt',
         'data3Tue_Dec_23_23_21_07_2014.txt',
         'data3Tue_Dec_23_23_21_09_2014.txt',
         'data0Tue_Dec_23_23_23_37_2014.txt',
         'data0Tue_Dec_23_23_23_38_2014.txt',
         'data0Tue_Dec_23_23_23_40_2014.txt',
         'data0Tue_Dec_23_23_23_41_2014.txt',
         'data0Tue_Dec_23_23_23_43_2014.txt',
         'data0Tue_Dec_23_23_23_45_2014.txt',
         'data0Tue_Dec_23_23_23_46_2014.txt',
         'data0Tue_Dec_23_23_23_48_2014.txt',
         'data0Tue_Dec_23_23_23_50_2014.txt',
         'data0Tue_Dec_23_23_23_51_2014.txt',
         'data0Tue_Dec_23_23_23_53_2014.txt',
         'data0Tue_Dec_23_23_23_55_2014.txt',
         'data0Tue_Dec_23_23_23_56_2014.txt',
         'data0Tue_Dec_23_23_23_58_2014.txt',
         'data0Tue_Dec_23_23_24_00_2014.txt',
         'data0Tue_Dec_23_23_24_01_2014.txt',
         'data0Tue_Dec_23_23_24_03_2014.txt',
         'data0Tue_Dec_23_23_24_05_2014.txt',
         'data0Tue_Dec_23_23_24_06_2014.txt',
         'data0Tue_Dec_23_23_24_08_2014.txt',
         'data0Tue_Dec_23_23_24_10_2014.txt',
         'data0Tue_Dec_23_23_24_11_2014.txt',
         'data0Tue_Dec_23_23_24_13_2014.txt',
         'data0Tue_Dec_23_23_24_14_2014.txt',
         'data0Tue_Dec_23_23_24_16_2014.txt',
         'data0Tue_Dec_23_23_24_18_2014.txt',
         'data0Tue_Dec_23_23_24_19_2014.txt',
         'data0Tue_Dec_23_23_24_21_2014.txt',
         'data0Tue_Dec_23_23_24_23_2014.txt',
         'data0Tue_Dec_23_23_24_24_2014.txt',
         'data2Tue_Dec_23_23_24_26_2014.txt',
         'data2Tue_Dec_23_23_24_28_2014.txt',
         'data2Tue_Dec_23_23_24_29_2014.txt',
         'data2Tue_Dec_23_23_24_31_2014.txt',
         'data2Tue_Dec_23_23_24_33_2014.txt',
         'data2Tue_Dec_23_23_24_34_2014.txt',
         'data2Tue_Dec_23_23_24_36_2014.txt',
         'data2Tue_Dec_23_23_24_38_2014.txt',
         'data2Tue_Dec_23_23_24_39_2014.txt',
         'data2Tue_Dec_23_23_24_41_2014.txt',
         'data2Tue_Dec_23_23_24_43_2014.txt',
         'data2Tue_Dec_23_23_24_44_2014.txt',
         'data2Tue_Dec_23_23_24_46_2014.txt',
         'data2Tue_Dec_23_23_24_48_2014.txt',
         'data2Tue_Dec_23_23_24_49_2014.txt',
         'data2Tue_Dec_23_23_24_51_2014.txt',
         'data2Tue_Dec_23_23_24_53_2014.txt',
         'data2Tue_Dec_23_23_24_54_2014.txt',
         'data2Tue_Dec_23_23_24_56_2014.txt',
         'data2Tue_Dec_23_23_24_58_2014.txt',
         'data2Tue_Dec_23_23_24_59_2014.txt',
         'data2Tue_Dec_23_23_25_01_2014.txt',
         'data2Tue_Dec_23_23_25_03_2014.txt',
         'data2Tue_Dec_23_23_25_04_2014.txt',
         'data2Tue_Dec_23_23_25_06_2014.txt',
         'data2Tue_Dec_23_23_25_08_2014.txt',
         'data2Tue_Dec_23_23_25_09_2014.txt',
         'data2Tue_Dec_23_23_25_11_2014.txt',
         'data2Tue_Dec_23_23_25_13_2014.txt',
         'data2Tue_Dec_23_23_25_14_2014.txt',
         'data3Tue_Dec_23_23_25_16_2014.txt',
         'data3Tue_Dec_23_23_25_18_2014.txt',
         'data3Tue_Dec_23_23_25_19_2014.txt',
         'data3Tue_Dec_23_23_25_21_2014.txt',
         'data3Tue_Dec_23_23_25_23_2014.txt',
         'data3Tue_Dec_23_23_25_24_2014.txt',
         'data3Tue_Dec_23_23_25_26_2014.txt',
         'data3Tue_Dec_23_23_25_28_2014.txt',
         'data3Tue_Dec_23_23_25_29_2014.txt',
         'data3Tue_Dec_23_23_25_31_2014.txt',
         'data3Tue_Dec_23_23_25_33_2014.txt',
         'data3Tue_Dec_23_23_25_34_2014.txt',
         'data3Tue_Dec_23_23_25_36_2014.txt',
         'data3Tue_Dec_23_23_25_38_2014.txt',
         'data3Tue_Dec_23_23_25_39_2014.txt',
         'data3Tue_Dec_23_23_25_41_2014.txt',
         'data3Tue_Dec_23_23_25_43_2014.txt',
         'data3Tue_Dec_23_23_25_44_2014.txt',
         'data3Tue_Dec_23_23_25_46_2014.txt',
         'data3Tue_Dec_23_23_25_48_2014.txt',
         'data3Tue_Dec_23_23_25_49_2014.txt',
         'data3Tue_Dec_23_23_25_51_2014.txt',
         'data3Tue_Dec_23_23_25_52_2014.txt',
         'data3Tue_Dec_23_23_25_54_2014.txt',
         'data3Tue_Dec_23_23_25_56_2014.txt',
         'data3Tue_Dec_23_23_25_58_2014.txt',
         'data3Tue_Dec_23_23_25_59_2014.txt',
         'data3Tue_Dec_23_23_26_01_2014.txt',
         'data3Tue_Dec_23_23_26_02_2014.txt',
         'data3Tue_Dec_23_23_26_04_2014.txt']

print 'Number of files:',len(files)
