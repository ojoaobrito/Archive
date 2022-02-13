##############
# SWA TRAINING
##############
import os, sys

#########################################################################################################################################################################################################################
# VGG-16 (16 LAYERS) - 1 BUDGET
#########################################################################################################################################################################################################################
# run #1
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=161 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_run_1.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #2
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=161 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_run_2.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #3
os.system("python3 run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.05 --wd=5e-4 --swa --swa_start=161 --swa_lr=0.01 --cov_mat --use_test --dir=./ > vgg16_run_3.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

######################################################################################################################################################################################################################################
# (PRE)RESNET-164 (164 LAYERS) - 1 BUDGET
######################################################################################################################################################################################################################################
# run #1
os.system("python3 run_swag.py --data_path=./ --epochs=150 --dataset=CIFAR10 --save_freq=150 --model=PreResNet164 --lr_init=0.1 --wd=3e-4 --swa --swa_start=100 --swa_lr=0.01 --cov_mat --use_test --dir=./ > preresnet164_run_1.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #2
os.system("python3 run_swag.py --data_path=./ --epochs=150 --dataset=CIFAR10 --save_freq=150 --model=PreResNet164 --lr_init=0.1 --wd=3e-4 --swa --swa_start=100 --swa_lr=0.01 --cov_mat --use_test --dir=./ > preresnet164_run_2.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")

# run #3
os.system("python3 run_swag.py --data_path=./ --epochs=150 --dataset=CIFAR10 --save_freq=150 --model=PreResNet164 --lr_init=0.1 --wd=3e-4 --swa --swa_start=100 --swa_lr=0.01 --cov_mat --use_test --dir=./ > preresnet164_run_3.txt")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")
os.system("pkill -9 -f run_swag.py")