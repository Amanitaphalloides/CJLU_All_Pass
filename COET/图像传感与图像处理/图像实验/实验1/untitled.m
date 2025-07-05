img = imread('grey.bmp');

if size(img, 3) == 3
    img = rgb2gray(img);
end

figure;

subplot(2, 3, 1);
imshow(img);
title('原图');

F = fft2(double(img));
Fshift = fftshift(F);
magnitude_spectrum = log(1 + abs(Fshift));

subplot(2, 3, 2);
imshow(magnitude_spectrum, []);
title('频谱图');

[M, N] = size(img);
filters = zeros(M, N);
for u = 1:M
    for v = 1:N
        D = sqrt((u - M/2)^2 + (v - N/2)^2);
        if D <= 50
            filters(u, v) = 1;
        end
    end
end

radii = [5, 10, 25, 50];

for i = 1:length(radii)
    D0 = radii(i);
    filter = zeros(M, N);
    for u = 1:M
        for v = 1:N
            D = sqrt((u - M/2)^2 + (v - N/2)^2);
            if D <= D0
                filter(u, v) = 1;
            end
        end
    end
    G = Fshift .* filter;
    G_inverse_shift = ifftshift(G);
    img_back = ifft2(G_inverse_shift);
    img_back = real(img_back);
    img_back = uint8(img_back);
    
    subplot(2, 3, i+2);
    imshow(img_back, []);
    title(['滤波后图像，半径为', num2str(D0)]);
end
