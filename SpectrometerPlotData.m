clear all
close all

load('c:\Users\Sandra Drusova\Nextcloud\Postdoc\Data\WavelengthsHDXSpectrometer.mat')

defaultdir='c:\Users\Sandra Drusova\Nextcloud\Postdoc\Data\20210910 HDX test\Bone\';

allfiles=dir([defaultdir,'HDX*']); 
allnames={allfiles.name};
I1=[];

for i=1:length(allnames)
    data=readtable([defaultdir,allnames{i}]);
    I1=[I1,data.Var2];
end

defaultdir='c:\Users\Sandra Drusova\Nextcloud\Postdoc\Data\20210910 HDX test\Bacon\';

allfiles=dir([defaultdir,'HDX*']); 
allnames={allfiles.name};
I2=[];

for i=1:length(allnames)
    data=readtable([defaultdir,allnames{i}]);
    I2=[I2,data.Var2];
end

% defaultdir='c:\Users\Sandra Drusova\Nextcloud\Postdoc\Data\20210914 HDX test\Meat2\';
% 
% allfiles=dir([defaultdir,'HDX*']); 
% allnames={allfiles.name};
% I3=[];
% 
% for i=1:length(allnames)
%     data=readtable([defaultdir,allnames{i}]);
%     I3=[I3,data.Var2];
% end

%% figure section

plot(W,mean(I1,2))
hold on
plot(W,mean(I2,2))
% hold on
% plot(W,mean(I3,2))
legend("Bone","Bone marrow","Meat")