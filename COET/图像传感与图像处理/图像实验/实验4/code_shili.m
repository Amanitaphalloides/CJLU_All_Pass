I = imread('bacteria.BMP');
BW1 = edge(I,'prewitt',0.04); % 0.04 为梯度阈值
figure(1);
imshow(I);
figure(2);
imshow(BW1);
I = imread('原图像');
BW1 = edge(I,'log',0.003); % σ=2
imshow(BW1);title('σ=2')
BW1 = edge(I,'log',0.003,3); % σ=3
figure, imshow(BW1);title('σ=3')
I = imread('原图像');
imshow(I);
BW1 = edge(I,'canny',0.2);
figure,imshow(BW1);