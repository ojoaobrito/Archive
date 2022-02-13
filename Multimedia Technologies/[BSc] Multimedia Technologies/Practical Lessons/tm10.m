xyloObj = VideoReader('xylophone.mp4');
nFrames = xyloObj.NumberOfFrames;
vidHeight = xyloObj.Height;
vidWidth = xyloObj.Width;
movX(1:nFrames) = ...
struct('cdata',zeros(vidHeight,vidWidth, 3,'uint8'),...
'colormap',[]);
for k = 1 : nFrames
movX(k).cdata = read(xyloObj,nFrames-k+1); %video invertido
end

im=imread('C:\Users\a37880\Desktop\baboon.png');
im=(imresize(im,0.5));
movX(10).cdata=(im);

implay(movX,20) %para mudar os fps, é só colocar outro valor em vez de "20"

imagem=movX(20:1:20); %frame específica do vídeo
implay(imagem); %mostrar a imagem acima

imDiferenca=(movX(51).cdata-movX(50).cdata); %diferença entre a frame 51 e a 50
implay(imDiferenca); %mostrar a imagem acima



xyloObj = VideoReader('rhinos.avi');
nFrames2 = xyloObj.NumberOfFrames;
vidHeight2 = xyloObj.Height;
vidWidth2 = xyloObj.Width;
movR(1:nFrames2) = ...
struct('cdata',zeros(vidHeight2,vidWidth2, 3,'uint8'),...
'colormap',[]);
for k = 1 : nFrames2
movR(k).cdata = read(xyloObj,k);
end
implay(movR);
imshow(abs(movR(1).cdata - movR(11).cdata), []);



clear all
clc
load mri
movM = immovie(D,map);
implay(movM)
load mri
montage(D,map)
figure
montage(D, map, 'Indices', 1:9);



fileFolder = fullfile(matlabroot,'toolbox','images','imdata');
dirOutput = dir(fullfile(fileFolder,'AT3_1m4_*.tif'));
fileNames = {dirOutput.name};
N = length(fileNames);
info = imfinfo(fileNames{1});
montage(fileNames, 'Size', [2 5]);
movC(1:N) = ...
struct('cdata',zeros(info.YResolution,info.XResolution, 3,'uint8'),...
'colormap',[]);
for k = 1 : N
movC(k).cdata = imread(fileNames{k});
end
implay(movC)