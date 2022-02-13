###############
# MISH TRAINING
###############
import os, sys

####################################################################################
# DENSENET-121 (121 LAYERS) - 1 BUDGET - SWISH
####################################################################################
# run #1

os.system("python3 densenet121.py swish > densenet121_swish_run_1.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Swish.csv","train_log_DenseNet121_Swish_run_1.csv")

# run #2
os.system("python3 densenet121.py swish > densenet121_swish_run_2.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Swish.csv","train_log_DenseNet121_Swish_run_2.csv")

# run #3
os.system("python3 densenet121.py swish > densenet121_swish_run_3.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Swish.csv","train_log_DenseNet121_Swish_run_3.csv")

##################################################################################
# DENSENET-121 (121 LAYERS) - 1 BUDGET - RELU
##################################################################################
# run #1
os.system("python3 densenet121.py relu > densenet121_relu_run_1.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Relu.csv","train_log_DenseNet121_Relu_run_1.csv")

# run #2
os.system("python3 densenet121.py relu > densenet121_relu_run_2.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Relu.csv","train_log_DenseNet121_Relu_run_2.csv")

# run #3
os.system("python3 densenet121.py relu > densenet121_relu_run_3.txt")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.system("pkill -9 -f densenet121.py")
os.rename("train_log_DenseNet121_Relu.csv","train_log_DenseNet121_Relu_run_3.csv")