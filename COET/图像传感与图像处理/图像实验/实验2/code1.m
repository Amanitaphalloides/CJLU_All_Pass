% 读取原图像
I = imread('blood1.tif');

% 显示原始图像
figure;
imshow(I);
title('原始图像');

% 显示原始图像的直方图
figure;
imhist(I);
title('原始图像的直方图');

% 将彩色图像转换为灰度图像
grayImage = rgb2gray(I);

% 显示灰度图像
figure;
imshow(grayImage);
title('灰度图像');

% 显示灰度图像的直方图
figure;
imhist(grayImage);
title('灰度图像的直方图');

% 使用 imadjust 函数对灰度图像进行调整
J = imadjust(grayImage, [0.15 0.9], [0 1]);

% 显示调整后的图像
figure;
imshow(J);
title('调整后的灰度图像');

% 显示调整后的图像的直方图
figure;
imhist(J);
title('调整后的灰度图像的直方图');
