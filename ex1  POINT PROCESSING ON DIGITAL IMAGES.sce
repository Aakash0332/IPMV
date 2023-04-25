//digital neagtive
clc;
clear all;
i=imread("C:\Users\shubh\Downloads\img.png");
ig=rgb2gray(i);
subplot(1,2,1);
imshow(ig);
title("original image");
[r,c]=size(ig);
for x=1:1:r;
 for y=1:1:c;
 j(x,y)=255-ig(x,y); //
 end
end
subplot(1,2,2);
imshow(j);
title("negative image");

//Contrast Stretching
clc;
clear all;
i=imread("C:\Users\shubh\Downloads\img.png");
ig=rgb2gray(i);
subplot(1,2,1);
imshow(ig);
title("original image");

[r,c]=size(ig);
j=ig;
r1=100;
r2=170;
s1=50;
s2=200;
l=256;
m1=s1/r1;
m2=(s2-s1)/(r2-r1);
m3=((l-1)-s2)/((l-1)-r2);
for x=1:1:r
 for y=1:1:c
 r=ig(x,y)
 
if(r<r1)
 j(x,y)= m1*r;
 
elseif(r>=r1) && (r<=r2)
 j(x,y)= m2*(r-r1)+s1;
 
else
 j(x,y)= m3*(r-r2)+s2;
 end
 end
end
subplot(1,2,2);
title("contrast streach");
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
