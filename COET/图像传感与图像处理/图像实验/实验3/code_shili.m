I=imread('cameraman.tif');
imshow(I) ;
J2=imnoise(I,'salt & pepper',0.04); % 叠加密度为0.04 的椒盐噪声。
figure,imshow(J2);
I_Filter1=medfilt2(J2,[3 3]); %窗口大小为3×3
figure,imshow(I_Filter1);
I_Filter2=medfilt2(J2,[5 5]); %窗口大小为5×5
figure,imshow(I_Filter2);
I_Filter3=medfilt2(J2,[7 7]); %窗口大小为7×7
figure,imshow(I_Filter3);