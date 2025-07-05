I1 = imread('bacteria.BMP');
I2 = imread('cameraman.tif');
I3 = imread('4-11.jpg');

figure;

% 边缘检测
subplot(3, 3, 1);
imshow(I1);
title('图1');

BW1_prewitt = edge(I1, 'prewitt', 0.04);
subplot(3, 3, 2);
imshow(BW1_prewitt);
title('Prewitt边缘检测');

BW1_log = edge(I1, 'log', 0.003);
subplot(3, 3, 3);
imshow(BW1_log);
title('LOG边缘检测');

BW1_canny = edge(I1, 'canny', 0.2);
subplot(3, 3, 4);
imshow(BW1_canny);
title('Canny边缘检测');

% 阈值分割
subplot(3, 3, 5);
imshow(I2);
title('图2');

% 检查 I2 是否为灰度图像
if size(I2, 3) == 1
    I2_gray = I2; % 如果 I2 已经是灰度图像，则直接使用
else
    I2_gray = rgb2gray(I2); % 否则转换为灰度图像
end

level = graythresh(I2_gray); % 计算全局阈值
BW2 = imbinarize(I2_gray, level);
subplot(3, 3, 6);
imshow(BW2);
title('阈值分割');

% 对第三张图像进行空间聚类方法的图像分割
subplot(3, 3, 7);
imshow(I3);
title('图3');

if size(I3, 3) == 1
    I3_gray = I3;
else
    I3_gray = rgb2gray(I3);
end

[y, x] = size(I3_gray);
d1 = zeros(y, x);
d2 = d1;
myI = double(I3_gray);
I0 = zeros(y, x);
for i = 1:x
    for j = 1:y
        % 根据欧式距离聚类
        d1(j, i) = sqrt((myI(j, i) - 180)^2);
        d2(j, i) = sqrt((myI(j, i) - 200)^2);
        if (d1(j, i) >= d2(j, i))
            I0(j, i) = 1;
        end
    end
end
subplot(3, 3, 8);
imshow(I0);
title('空间聚类');

subplot(3, 3, 9);
imhist(I3_gray);
title('灰度直方图');
