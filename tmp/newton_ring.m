% 模拟牛顿环干涉图样
clear,clc,close all;
% 基本参数输入及处理
% 样例输入：Lambda = 632.8;  R = 855;
Lambda = input('输入光的波长（单位为nm）：');
Lambda = Lambda * 1e-9;                 %波长单位转为：m
R = input('输入透镜的曲率半径（单位为mm）：');
R = R * 1e-3;                           %透镜的曲率半径单位转为：m
I0 = 1;                                 %入射光的光强

Screen_length = sqrt(10*R*Lambda);      %定义干涉仿真范围
[Screen_x,Screen_y] = meshgrid(linspace(-Screen_length,Screen_length,800));
Newton_r = abs(Screen_x + 1i*Screen_y);
% Newton_r = Newton_r*0.6;

I_delta = (Newton_r.^2)*pi/R/Lambda;
I = 2*I0*(sin(I_delta)).^2;
I = I./max(max(I));                      %光强分布归一化

% 牛顿环光强分布图
I = I*64;                                %光强归一,扩大显示
image(Screen_x(1,:),Screen_y(:,1),I);    %设置x和y的像素，显示数值
colormap gray;                            %妆点色彩
colorbar;
xlabel('空间坐标x'),ylabel('空间坐标y');
title('牛顿环光强空间分布');   
