function error = Main(signal_id, protocol, sync_type)
tic;
%author：lzm
%amend date: 2015.5.6
%goal: To orgalize the code for the single demode;

%debug part;
debug = 0;
%dirName = 'F:\研究生\星载AIS\信号数据\无冲突信号\15dB 3\AISSig_s\h600_t12_v10_e15';


if debug ~= 1
    dirName = ['../AIS/DATA/aisSig', '/', signal_id];
%     dirName = sigpath;
    resultPath = [dirName, '/demodResult_1ant/'];
    mkdir(resultPath);
    sigFile = dir(dirName);
    fileName = cell(1, length(sigFile));
    fileNum = 1;
    for ii = 1 : 1 : length(sigFile)
        if sigFile(ii).isdir == 0 && ~strcmp(sigFile(ii).name, '.') ...
                && ~strcmp(sigFile(ii).name, '..') ...
                && strcmp(sigFile(ii).name(1 : 1 : 6), 'AISsig')
            % 不记录文件夹和非信号文件
            fileName{fileNum} = sigFile(ii).name;
            fileNum = fileNum + 1;
        end
    end
    fileName(fileNum : end) = [];       % 删除剩余的cell
    fileNum = fileNum - 1;

    F_initPar;
    for fileIdx = 1 : 1 : fileNum
        load([dirName '/' fileName{fileIdx}]);
        demodResult = F_aisDemod(sig);
        resultFileName = ['AISResult', fileName{fileIdx}(7: end-4)];
        save([resultPath, resultFileName, '_result.mat'], 'demodResult');
    end
else
    [fileName, pathName] = uigetfile('*.mat', '选择信号mat文件', 'E:\AIS\信号解调\差分解调加均衡\data');
    resultPath = [pathName, 'demodResult\'];
    mkdir(resultPath);
    load([pathName '\' fileName]);
    startLoc = 34000;
    sigIn = sig(startLoc : startLoc+2048, 3);
% 	sigIn = sig_out_noise;
% 		figure;
% 		subplot(4,1,1);plot(abs(sig(:,1)));
% 		subplot(4,1,2);plot(abs(sig(:,2)));
% 		subplot(4,1,3);plot(abs(sig(:,3)));
% 		subplot(4,1,4);plot(abs(sig(:,4)));
        figure;
        plot(abs(sigIn));
        drawnow;
    F_initPar;
    demodResult = F_aisDemod(sigIn);
    save([resultPath fileName '_debugresult_ant1.mat'], 'demodResult');
end

error = 0;
toc;
end