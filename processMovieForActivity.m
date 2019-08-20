%
%

close all
clear

% v = VideoReader('1.mov');
% v = VideoReader('2.mov');
% v = VideoReader('3.mov');
v = VideoReader('6.mov');
% v = VideoReader('Day 4.mov');
% v = VideoReader('Day 9.mov');
% v = VideoReader('Day 15.mov');
% v = VideoReader('Day 19.mov');

I1=readFrame(v);
I1=rgb2gray(I1);
% I1=imcrop(I1,[462.5100  227.5100  931.9800  529.9800]);
% I1=imcrop(I1,[459.5100  182.5100  951.9800  546.9800]);
% I1=imcrop(I1,[412.5100  218.5100  960.9800  543.9800]);
I1=imcrop(I1,[534.5100  356.5100  948.9800  552.9800]);
% I1=imcrop(I1,[466.5    114.5    1403    800.0]);
% I1=imcrop(I1,[432.5    113.5    1445    806.0]);
% I1=imcrop(I1,[611.5    171.5    1104    628.0]);
% I1=imcrop(I1,[614.5    176.5    1088    615.0]);
figure; imshow(I1,[])

[M,N]=size(I1);
[U,V]=meshgrid([1:N],[1:M]);
D= sqrt((U-(N+1)/2).^2+(V-(M+1)/2).^2);
D0=2;
n=2; 
one=ones(M,N);
H = 1./(one+(D./D0).^(2*n));
G=fftshift(fft2(I1)).*H;
g=real(ifft2(ifftshift(G)));
out=double(I1)-g;
I1=uint8((255.0/(max(out(:))-min(out(:)))).*(out-min(out(:))));

th=imbinarize(I1,'Adaptive','Sensitivity',0.4);
figure; imshow(I1,[])
figure; imshow(th,[])
figure; imshow(imoverlay(I1,th,'r'),[])

[outL,outN]=bwlabel(th);

fstats=regionprops('table',outL,'Area','BoundingBox');
bboxes=fstats.BoundingBox;

Things = insertShape(I1,'Rectangle',bboxes,'LineWidth',3);
figure; imshow(Things,[]);
fig=gcf;

v.CurrentTime=v.CurrentTime+15;
I2=readFrame(v);
I2=rgb2gray(I2);
% I2=imcrop(I2,[462.5100  227.5100  931.9800  529.9800]);
% I2=imcrop(I2,[459.5100  182.5100  951.9800  546.9800]);
% I2=imcrop(I2,[412.5100  218.5100  960.9800  543.9800]);
I2=imcrop(I2,[534.5100  356.5100  948.9800  552.9800]);
% I2=imcrop(I2,[466.5    114.5    1403    800.0]);
% I2=imcrop(I2,[432.5    113.5    1445    806.0]);
% I2=imcrop(I2,[611.5    171.5    1104    628.0]);
% I2=imcrop(I2,[614.5     176.5    1088    615.0]);

G=fftshift(fft2(I2)).*H;
g=real(ifft2(ifftshift(G)));
out=double(I2)-g;
I2=uint8((255.0/(max(out(:))-min(out(:)))).*(out-min(out(:))));
co=0;
figure
fig1=gcf;
for i=1:size(fstats,1)
    if fstats.Area(i) < 30 || fstats.Area(i) > 300
        continue
    end
    xmin = bboxes(i,1);
    ymin = bboxes(i,2);
    xmax = xmin + bboxes(i,3) - 1;
    ymax = ymin + bboxes(i,4) - 1;
    expansionAmount = 0.00;
    xmin = (1-expansionAmount) * xmin;
    ymin = (1-expansionAmount) * ymin;
    xmax = (1+expansionAmount) * xmax;
    ymax = (1+expansionAmount) * ymax;
    xmin = max(xmin, 1);
    ymin = max(ymin, 1);
    xmax = min(xmax, size(I1,2));
    ymax = min(ymax, size(I1,1));
    win = [xmin ymin xmax-xmin+1 ymax-ymin+1];
    exThings = insertShape(I1,'Rectangle',win,'LineWidth',3, 'Color','r');
    figure(fig); imshow(exThings,[]);
    
    sub1=imgaussfilt(imcrop(I1,win),0.5);
    sub2=imgaussfilt(imcrop(I2,win),0.5);
    Idiff12=abs(single(sub1)-single(sub2));
    
    Idiff12=uint8((255.0/(max(Idiff12(:))-min(Idiff12(:)))).*(Idiff12-min(Idiff12(:))));
    sub1=uint8((255.0/(max(sub1(:))-min(sub1(:)))).*(sub1-min(sub1(:))));
    
    figure(fig1); 
    subplot(2,3,1); imshow(sub1,[])
    subplot(2,3,2); imshow(sub2,[])
    subplot(2,3,3); imshow(Idiff12,[])
    subplot(2,3,4); imshow(imbinarize(sub1),[])
    subplot(2,3,5); imshow(imbinarize(sub2),[])
    C=normxcorr2(sub1,sub2);
    C(C<0)=0;
    C=1-C;
    [M,N]=size(sub1);
    co=co+1;
    change(co,1)=i;
    change(co,2)=C(M,N);
    title(['Corr = ',num2str(C(M,N))]);
    subplot(2,3,6); imshow(imbinarize(Idiff12),[])
    Cj=jaccard(imbinarize(sub1),imbinarize(Idiff12));
%     co=co+1;
%     change(co,1)=i;
%     change(co,2)=Cj;
    title(['IoU = ',num2str(Cj)]);
    pause
end
cmap=colormap('jet')*255;
xmin=min(change(:,2));
xmax=max(change(:,2));
tmap=@(t) ((64-1)/(xmax-xmin))*(t-xmin)+1;
map_c = fix(tmap(change(:,2)));
figure
box=bboxes(change(:,1),:);
boxc=[cmap(map_c,1),cmap(map_c,2),cmap(map_c,3)];
Things = insertShape(I1,'Rectangle',box,'LineWidth',3,'Color',boxc);
imshow(Things,[])
