numImagePairs = 29;
imageFiles1 = cell(numImagePairs, 1);
imageFiles2 = cell(numImagePairs, 1);
imageDir = fullfile('Fotos2');
for i = 1:numImagePairs
    imageFiles1{i} = fullfile(imageDir, sprintf('left%02d.png', i));
    imageFiles2{i} = fullfile(imageDir, sprintf('right%02d.png', i));
end
 
images1 = cast([], 'uint8');
images2 = cast([], 'uint8');
for i = 1:numel(imageFiles1)
    im = imread(imageFiles1{i});
    images1(:, :, :, i) = im;
    
    im = imread(imageFiles2{i});
    images2(:, :, :, i) = im;
end

[imagePoints, boardSize] = detectCheckerboardPoints(images1, images2);

figure; imshow(images1(:,:,:,1), 'InitialMagnification', 50);
hold on;
plot(imagePoints(:, 1, 1, 1), imagePoints(:, 2, 1, 1), '*-g');
title('Successful Checkerboard Detection');

squareSize = 108; % millimeters
worldPoints = generateCheckerboardPoints(boardSize, squareSize);

stereoParams = estimateCameraParameters(imagePoints, worldPoints);

figure; showReprojectionErrors(stereoParams);

I1 = imread('Fotos2\final_left.png');
I2 = imread('Fotos2\final_right.png');

[J1, J2] = rectifyStereoImages(I1, I2, stereoParams);

figure; imshow(cat(3, I1(:,:,1), I2(:,:,2:3)), 'InitialMagnification', 50);
title('Before Rectification');

figure; imshow(cat(3, J1(:,:,1), J2(:,:,2:3)), 'InitialMagnification', 50);
title('After Rectification');

J3 = histeq(J1);
J4 = histeq(J2);


disparityRange = [-160 368];
disparityMap = disparity(rgb2gray(J3), rgb2gray(J4),'DisparityRange',disparityRange,'Blocksize', 15);
figure; imshow(disparityMap);
colormap(jet);
colorbar;
title('Disparity Map');

pointCloud = reconstructScene(disparityMap, stereoParams);

pointCloud = pointCloud ./ 1000;

[reducedColorImage, reducedColorMap] = rgb2ind(J1, 128);

hFig = figure; hold on;
set(hFig, 'Position', [1 1 840   630]);
hAxes = gca;

X = pointCloud(:, :, 1);
Y = pointCloud(:, :, 2);
Z = pointCloud(:, :, 3);

for i = 1:size(reducedColorMap, 1)
    
    x = X(reducedColorImage == i-1);
    y = Y(reducedColorImage == i-1);
    z = Z(reducedColorImage == i-1);
    
    if isempty(x)
        continue;
    end

    
    idx = isfinite(x);
    x = x(idx);
    y = y(idx);
    z = z(idx);
    
    
    maxZ = 7;
    minZ = 3;
    x = x(z > minZ & z < maxZ);
    y = y(z > minZ & z < maxZ);
    z = z(z > minZ & z < maxZ);
    
    plot3(hAxes, x, y, z, '.', 'MarkerEdgeColor', reducedColorMap(i, :));
    hold on;
end


grid on;
cameratoolbar show;
axis vis3d
axis equal;
set(hAxes,'YDir','reverse', 'ZDir', 'reverse');
camorbit(-20, 25, 'camera', [0 1 0]);

displayEndOfDemoMessage(mfilename)
