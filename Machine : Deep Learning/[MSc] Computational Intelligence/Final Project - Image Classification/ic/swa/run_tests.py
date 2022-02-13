##############
# SWA TRAINING
##############
import os, sys

###########################################################################################################################################################################################################################
# VGG-16 (16 LAYERS) - 1 BUDGET - relu,0.05,0.01
###########################################################################################################################################################################################################################
# run #1
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_1_run_1.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #2
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_1_run_2.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #3
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_1_run_3.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

##########################################################################################################################################################################################################################################
# VGG-16 (16 LAYERS) - 1 BUDGET - mish,0.05,0.01
##########################################################################################################################################################################################################################################
# run #1
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_2_run_1.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #2
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_2_run_2.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #3
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_2_run_3.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

#############################################################################################################################################################################################################################
# VGG-16 (16 LAYERS) - 1 BUDGET - relu,0.001,0.001
#############################################################################################################################################################################################################################
# run #1
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.001 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.001 --cov_mat --use_test --dir=./ > vgg16_3_run_1.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #2
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.001 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.001 --cov_mat --use_test --dir=./ > vgg16_3_run_2.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #3
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.001 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.001 --cov_mat --use_test --dir=./ > vgg16_3_run_3.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

############################################################################################################################################################################################################################################
# VGG-16 (16 LAYERS) - 1 BUDGET - mish,0.001,0.001
############################################################################################################################################################################################################################################
# run #1
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.001 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.001 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_4_run_1.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #2
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.001 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.001 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_4_run_2.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #3
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.001 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.001 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_4_run_3.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

###########################################################################################################################################################################################################################
# VGG-16 (16 LAYERS) - 1 BUDGET - relu,0.01,0.01
###########################################################################################################################################################################################################################
# run #1
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.01 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_5_run_1.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #2
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.01 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_5_run_2.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #3
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.01 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_5_run_3.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

##########################################################################################################################################################################################################################################
# VGG-16 (16 LAYERS) - 1 BUDGET - mish,0.01,0.01
##########################################################################################################################################################################################################################################
# run #1
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.01 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_6_run_1.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #2
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.01 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_6_run_2.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #3
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.01 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ --act_fun=mish > vgg16_6_run_3.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")