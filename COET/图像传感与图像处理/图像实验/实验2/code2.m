I = imread('pout.tif'); % 读取MATLAB自带的图像
imshow(I);
title('原始图像');
figure, imhist(I);
title('原始图像的直方图');

% 均衡化
[J, T] = histeq(I, 64); % 图像灰度扩展到0~255，但是只有64个灰度级
figure, imshow(J);
title('均衡化后的图像（64个灰度级）');
figure, imhist(J);
title('均衡化后的图像的直方图（64个灰度级）');
figure, plot((0:255)/255, T); % 转移函数的变换曲线
title('转移函数曲线（64个灰度级）');

% 使用不同的灰度级进行均衡化
J = histeq(I, 32); % 图像灰度扩展到0~255，但是只有32个灰度级
figure, imshow(J);
title('均衡化后的图像（32个灰度级）');
figure, imhist(J);
title('均衡化后的图像的直方图（32个灰度级）');
