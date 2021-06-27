H = figure;

% plot不显示
% set(0,'DefaultFigureVisible', 'off')

set(gca,'xtick',[],'xticklabel',[]);

% 设置图片大小
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperUnits', 'points');
set(gcf, 'PaperPosition', [0 0 640 640]);

plot(1:4,5:8);
axis off
print(H,'-djpeg','-r200','Figure1');
