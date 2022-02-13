run_swag.py --data_path=./ --epochs=200 --dataset=CIFAR10 --save_freq=200 --model=VGG16 --lr_init=0.01 --wd=5e-4 --swa --swa_start=150 --swa_lr=0.01 --cov_mat --use_test --dir=./ --act_fun=mish
