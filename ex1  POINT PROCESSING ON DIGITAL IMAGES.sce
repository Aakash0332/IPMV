//digital neagtive
clc;
clear all;
i=imread("C:\Users\akash\OneDrive\Desktop\IPMV\Project\image.jpg");
ig=rgb2gray(i);
subplot(1,2,1);
imshow(ig);
title("original image");
[r,c]=size(ig);
j=ig;
for x=1:1:r;
 for y=1:1:c;
 t=ig(x,y);
 j(x,y)=255-t;
 end
end
subplot(1,2,2);
imshow(j);
title("negative image");

//Contrast Stretching
clc;
clear all;
i=imread("C:\Users\Aakash\Desktop\sem6\ipmv\ex1\cameraman.png");
ig=rgb2gray(i);
subplot(1,2,1);
imshow(ig);
title("original image");
[r,c]=size(ig);
j=ig;
a=100;
b=170;
v=50;
w=200;
l=256;
p=v/a;
m=(w-v)/(b-a);
n=((l-1)-w)/((l-1)-b);
for x=1:1:r
 for y=1:1:c
 r=ig(x,y)
if(r<a)
 j(x,y)= p*r;
 
elseif(r>=a) && (r<=b)
 j(x,y)= m*(r-a)+v;
 
else
 j(x,y)= m*(r-b)+w;
 end
 end
end
subplot(1,2,2);
imshow(j);

//Logarithmic Transformation
clc;
clear all;
i=imread("C:\Users\Aakash\Desktop\sem6\ipmv\ex1\cameraman.png");
ig=rgb2gray(i);
double_value=im2double(ig);
output1=2*log(1+double_value);
output2=2.5*log(1+double_value);
output3=3*log(1+double_value);
subplot(2,2,1),imshow(ig);title('Original image');
subplot(2,2,2),imshow(output1);title('Output scaling factor 2');
subplot(2,2,3),imshow(output2);title('Output scaling factor 2.5');
subplot(2,2,4),imshow(output3);title('Output scaling factor 3');
