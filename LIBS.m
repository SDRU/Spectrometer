%%% This code reads out spectra and prepares data for tissue classification
clear all
defaultdir = 'c:\Users\Sandra Drusova\Nextcloud\Postdoc\Data\20220609 LIBS tissues\';

tissues = {'Meat','SoftBone','HardBone'};
for tissue = 1:length(tissues)    
    
    allfiles=dir([defaultdir,'*',tissues{tissue},'*']); 
    allnames={allfiles.name};
    N = length(allnames);

    eval([tissues{tissue},' = [];'])
    for i = 1:N
        Spectra=importdata([defaultdir,allnames{i}],'\t');
        eval([tissues{tissue},'=[',tissues{tissue}, ',Spectra];'])
    end
    eval([tissues{tissue},'(:,52)=[];'])
end

%% Machine learning labelling
% CUBIC SVM worked the best, 91.3 % training accuracy
% baseline removal, scaling
nr_pulses = 100;
cut1 = 292;
cut2 = 1770;

HB = HardBone(cut1:cut2,2:nr_pulses+1);
for i=1:nr_pulses
    % baseline removal
    [~, HB(:,i)]=baseline(HB(:,i));
    % scaling
    HB(:,i)=HB(:,i)/max(HB(:,i));
end
% Labelling for machine learning
HB(cut2-cut1+2,:)=1;

SB = SoftBone(cut1:cut2,2:nr_pulses+1);
for i=1:nr_pulses
    [~, SB(:,i)]=baseline(SB(:,i));
    SB(:,i)=SB(:,i)/max(SB(:,i));
end
SB(cut2-cut1+2,:)=2;

M = Meat(cut1:cut2,2:nr_pulses+1);
for i=1:nr_pulses
    [~, M(:,i)]=baseline(M(:,i));
    M(:,i)=M(:,i)/max(M(:,i));
end
M(cut2-cut1+2,:)=3;

% use machine learning on Data, last column are labels
Data = [HB,SB,M]';



%%
figure
nr_pulses = 100;

cut1 = 292;
cut2 = 1768;

HB = mean(HardBone(cut1:cut2,2:nr_pulses+1),2);
[Base, HB]=baseline(HB);
HB=HB/max(HB);
SB = mean(SoftBone(cut1:cut2,2:nr_pulses+1),2);
[Base, SB]=baseline(SB);
SB=SB/max(SB);
M = mean(Meat(cut1:cut2,2:nr_pulses+1),2);
[Base, M]=baseline(M);
M=M/max(M);

plot(HardBone(cut1:cut2,1),HB)
hold on
plot(SoftBone(cut1:cut2,1),SB)
hold on
plot(Meat(cut1:cut2,1),M)
legend('HardBone','SoftBone','Meat')
xlabel('Wavelength [nm]')
ylabel('Normalized intensity')
