R = uint8(zeros(256,256,3)); R(:,:,1)=255;
G = uint8(zeros(256,256,3)); R(:,:,2)=255;
B = uint8(zeros(256,256,3)); R(:,:,3)=255;

for i= 1 : 256
    R(i,:,1) = i-1;
end

for i= 1 : 256
    G(i,:,2) = i-1;
end

for i= 1 : 256
    B(i,:,3) = i-1;
end

I=imread('C:\Users\a37880\Desktop\Fig6_08.png'); %cubo RGB
imshow(I(:,:,1)); %informação do vermelho
imshow(I(:,:,2)); %informação do verde
imshow(I(:,:,3)); %informação do azul

A=RGBToCMY(200,255,1);

function [c,m,y] = RGBToCMY(r,g,b)
c=1-(r/255);
m=1-(g/255);
y=1-(b/255);
end