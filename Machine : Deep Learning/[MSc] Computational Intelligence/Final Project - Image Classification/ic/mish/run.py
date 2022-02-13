###############
# MISH TRAINING
###############
import os, sys

##################################################################################
# INCEPTION-V3 (48 LAYERS) - 1 BUDGET
##################################################################################
# run #1
os.system("python3 inceptionv3.py > inceptionv3_run_1.txt")
os.system("pkill -9 -f inceptionv3.py")
os.system("pkill -9 -f inceptionv3.py")
os.system("pkill -9 -f inceptionv3.py")
os.rename("train_log_InceptionV3_Mish.csv","train_log_InceptionV3_Mish_run_1.csv")

# run #2
os.system("python3 inceptionv3.py > inceptionv3_run_2.txt")
os.system("pkill -9 -f inceptionv3.py")
os.system("pkill -9 -f inceptionv3.py")
os.system("pkill -9 -f inceptionv3.py")
os.rename("train_log_InceptionV3_Mish.csv","train_log_InceptionV3_Mish_run_2.csv")

# run #3
os.system("python3 inceptionv3.py > inceptionv3_run_3.txt")
os.system("pkill -9 -f inceptionv3.py")
os.system("pkill -9 -f inceptionv3.py")
os.system("pkill -9 -f inceptionv3.py")
os.rename("train_log_InceptionV3_Mish.csv","train_log_InceptionV3_Mish_run_3.csv")

##################################################################################
# DENSENET-121 (121 LAYERS) - 1 BUDGET
##################################################################################
# run #1
os.system("python3 densenet121.py > densenet121_run_1.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Mish.csv","train_log_DenseNet121_Mish_run_1.csv")

# run #2
os.system("python3 densenet121.py > densenet121_run_2.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Mish.csv","train_log_DenseNet121_Mish_run_2.csv")

# run #3
os.system("python3 densenet121.py > densenet121_run_3.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Mish.csv","train_log_DenseNet121_Mish_run_3.csv")