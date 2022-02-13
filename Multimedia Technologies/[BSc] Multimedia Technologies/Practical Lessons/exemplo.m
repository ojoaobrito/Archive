I = imread('C:\Users\a37880\Desktop\baboon.png');

%I1 = imread(‘Rosa1024.png’); 
 
I1=rgb2gray(I);
I1= I1(:,1:496);

fundct2= @(block_struct) dct2(block_struct.data);
dct_bloco = blockproc(I1,[8 8], fundct2);

funzerosdct=@(block_struct) zerosdct(block_struct.data);
dct_zeros = blockproc(dct_bloco,[8 8], funzerosdct);

funidct2= @(block_struct) idct2(block_struct.data);
idct_bloco = blockproc(dct_zeros,[8 8], funidct2);

figure(1);imshow(dct_zeros);
figure(2)
subplot(1,2,2);imshow(idct_bloco/255);
subplot(1,2,1);imshow(I1);
