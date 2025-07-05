I=imread('eight.tif');
figure,imshow(I);title('original')
J1=imnoise(I,'gaussian',0,0.02); % 受高斯噪声干扰
figure,imshow(J1);
M4=[0 1 0; 1 0 1; 0 1 0];
M4=M4/4; % 4 邻域平均滤波
I_filter1=filter2(M4,J1);
figure,imshow(I_filter1);
M8=[1 1 1; 1 0 1; 1 1 1]; % 8 邻域平均滤波
M8=M8/8;
I_filter2=filter2(M8,J1);
figure,imshow(I_filter2);