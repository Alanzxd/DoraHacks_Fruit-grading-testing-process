I= imread('c:\GoodApple3.bmp');
I2= rgb2gray(I);
J= imadjust(I2，[0.1 0.2]，[]); %图像增强
Y=im2bw(J，0.9999);
Y=~Y;
[l，m]=bwlabel(Y ，8);
status=regionprops(l，'BoundingBox');
imshow(Y);
hold on;
for i=1:m
rectangle('position'，status(i).BoundingBox，'edgecolor'，'r');
end