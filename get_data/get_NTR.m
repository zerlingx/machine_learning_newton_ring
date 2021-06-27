% 注：这里是牛顿环的反射光，即中间是黑的

clear,clc,close all;
% Lambda,光的波长,nm
Lambda = 600;
Lambda = Lambda * 1e-9;
% R,透镜的曲率半径,mm
R = 700;
R = R * 1e-3;
I0 = 1;

cnt = 0;
for k = 0.7:0.01:1.3
cnt = cnt + 1;

Screen_length = sqrt(10*R*Lambda);
[Screen_x,Screen_y] = meshgrid(linspace(-Screen_length,Screen_length,800));
Newton_r = abs(Screen_x + 1i*Screen_y);
Newton_r = Newton_r*k;

I_delta = (Newton_r.^2)*pi/R/Lambda;
I = 2*I0*(sin(I_delta)).^2;
I = I./max(max(I));
I = I*64;

H = figure;
set(0,'DefaultFigureVisible', 'off')

set(gca,'xtick',[],'xticklabel',[]);
set(gca,'LooseInset',get(gca,'TightInset'));
set(gca,'looseInset',[0 0 0 0]);
set(gca,'Position',[0 0 1 1]);

set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperUnits', 'points');
% set(gcf, 'PaperPosition', [0 0 81 81]); %这个尺寸刚好225*225
set(gcf, 'PaperPosition', [0 0 100 100]); %278*278

image(Screen_x(1,:),Screen_y(:,1),I);
colormap gray;
axis off
print(H,'-djpeg','-r200',"../raw_NTR_img/img_"+num2str(cnt));
% colorbar;
% xlabel('空间坐标x'),ylabel('空间坐标y');
% title('牛顿环光强空间分布');

end