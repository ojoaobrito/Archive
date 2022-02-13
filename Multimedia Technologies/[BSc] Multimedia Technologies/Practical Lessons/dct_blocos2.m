I = imread('C:\Users\a37880\Desktop\baboon.png'); 
I1=rgb2gray(I);
I1= I1(:,1:496);

fundct2= @(block_struct) dct2(block_struct.data);
dct_bloco = blockproc(I1,[8 8], fundct2);

funquantizadct=@(block_struct) quantiza(block_struct.data);
dct_quantiza = blockproc(dct_bloco,[8 8], funquantizadct);

funidct2= @(block_struct) idct2(block_struct.data);
idct_bloco = blockproc(dct_quantiza,[8 8], funidct2);

figure(1);imshow(dct_quantiza);
figure(2)
subplot(1,2,2);imshow(idct_bloco/255);
subplot(1,2,1);imshow(I1);

%function y = zerosdct( A )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
%y=zeros(8,8);
%y(1:4,1:4)=A(1:4,1:4);
%end

function y = quantiza(A)
Q=[52 55 61 66 70 61 64 73; 63 59 66 90 109 85 69 72; 62 59 68 113 144 104 66 73; 63 58 71 122 154 106 70 69; 67 61 68 104 126 88 68 70; 79 65 60 70 77 63 58 75; 85 71 64 59 55 61 65 83; 87 79 69 68 65 76 78 94];
y=round(A./Q);
end

function y = dequantiza(A)
Q=[52 55 61 66 70 61 64 73; 63 59 66 90 109 85 69 72; 62 59 68 113 144 104 66 73; 63 58 71 122 154 106 70 69; 67 61 68 104 126 88 68 70; 79 65 60 70 77 63 58 75; 85 71 64 59 55 61 65 83; 87 79 69 68 65 76 78 94];
y=(A*Q);
end
