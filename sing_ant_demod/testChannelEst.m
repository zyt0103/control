clear all;
close all;
clc;

global Training StartFlag EndFlag DataLength os
F_initPar;
repeatNum = 10;
delay = 0 : 10 : 100;
doppler = -4000 : 200 : 4000;

% delay = 100;
% doppler = 4000;
EbNo_dB = 20;
sigma = sqrt(0.5*os/10^(EbNo_dB/10));
% delayMat = zeros(length(delay), length(doppler));
% dopMat = zeros(length(delay), length(doppler));
allDelay = zeros(length(delay), length(doppler), repeatNum);
allDop = zeros(length(delay), length(doppler), repeatNum);
for rr = 1 : 1 : repeatNum
	disp(rr);
	for dd = 1 : 1 : length(delay)
		for ff = 1 : 1 : length(doppler)
			tic;
			data = [Training StartFlag round(rand(1, DataLength)) EndFlag];
			sig = F_aisModul(data, 24, delay(dd), doppler(ff), 1);
			sig = [zeros(1, delay(dd)), sig];
			noise = sigma*randn(1,length(sig)) + 1j*sigma*randn(1,length(sig));
			sig = sig + noise;
			[delayEst, dopplerEst, hEst] = F_channelEstimation(sig);
			allDelay(dd, ff, rr) = delayEst;
			allDop(dd, ff, rr) = dopplerEst;
% 			if delayEst - 100 == delay(dd)
% 				delayMat(dd, ff) = delayMat(dd, ff) + 1;
% 			end
% 			if abs(dopplerEst - doppler(ff)) <= 0.5
% 				dopMat(dd, ff) = dopMat(dd, ff) + 1;
% 			end
			toc;
		end
	end
end
allDelay = allDelay / repeatNum;
allDop = allDop / repeatNum;
allDelay = sum(allDelay, 3);
allDop = sum(allDop, 3);
% figure;bar3(delayMat);
% figure;bar3(dopMat);
save('channelEst.mat', 'allDelay', 'allDop', 'delay', 'doppler', 'EbNo_dB', 'repeatNum');