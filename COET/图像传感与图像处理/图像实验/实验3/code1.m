% 读取三张不同的图像
I1 = imread('bacteria.BMP');
I2 = imread('cameraman.tif');
I3 = imread('4-11.jpg');

% 创建一个窗口来显示所有结果
figure;

% 对第一张图像进行边缘检测
subplot(3, 3, 1);
imshow(I1);
title('Original Image 1');

BW1_prewitt = edge(I1, 'prewitt', 0.04);
subplot(3, 3, 2);
imshow(BW1_prewitt);
title('Prewitt Edge Detection');

BW1_log = edge(I1, 'log', 0.003);
subplot(3, 3, 3);
imshow(BW1_log);
title('LOG Edge Detection');

BW1_canny = edge(I1, 'canny', 0.2);
subplot(3, 3, 4);
imshow(BW1_canny);
title('Canny Edge Detection');

% 对第二张图像进行阈值分割
subplot(3, 3, 5);
imshow(I2);
title('Original Image 2');

I2_gray = rgb2gray(I2); % 转换为灰度图像
level = graythresh(I2_gray); % 计算全局阈值
BW2 = imbinarize(I2_gray, level);
subplot(3, 3, 6);
imshow(BW2);
title('Threshold Segmentation');

% 对第三张图像进行空间聚类方法的图像分割
subplot(3, 3, 7);
imshow(I3);
title('Original Image 3');

I3_gray = rgb2gray(I3); % 转换为灰度图像
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
title('Spatial Clustering');

% 显示RGB空间的灰度直方图，确定两个聚类中心(180,180,180)和(200,200,200)
subplot(3, 3, 9);
imhist(double(I3_gray));
title('Gray Level Histogram');
