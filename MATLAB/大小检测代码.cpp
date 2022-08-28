img=imread('c:\apple.bmp');
rgb = im2double(img);
r = rgb(:， :， 1);
g = rgb(:， :， 2);
b = rgb(:， :， 3);
K=rgb2hsv(rgb);
imshow(K);%显示 HSV 图
s=K(:，:，2);
s=im2bw(s，0.2); %二值化
imshow(s);%显示二值化图
[l，m]=bwlabel(s，8); %标记
status=regionprops(l，'BoundingBox');
hold on;
for i=1:m
rectangle('position'，status(i).BoundingBox，'edgecolor'，'r');
end
hold off;
x=status(2，1).BoundingBox; %读取矩形的长宽
X=max(x); %取最大值
