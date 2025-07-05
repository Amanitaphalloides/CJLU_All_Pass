I=imread('cameraman.tif');
imhist(I); % 观察灰度直方图， 确定阈值
I1=im2bw(I,128/255); % im2bw 函数需要将灰度值转换到[0,1]范围内
figure,imshow(I1);