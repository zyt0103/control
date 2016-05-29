function [delay,freq,syn_mat] = Update_Delay_Freq_4os_update(sig,delay_id,freq_id,standard)

rb = 9600;
os = 4;
syn_length = 32*4;
siglen = length(sig);
u = sqrt(sum(abs(fft(sig)).^2));
% sig = sig./rx;
num_zero = length(standard) - syn_length;
freq_precision = rb/((num_zero + syn_length)/4);

standard_fft = zeros(length(freq_id),length(standard));

for ii = 1:length(freq_id)
    standard_fft(ii,:) = circshift(fft(standard.'),freq_id(ii));
end

for ii = 1:length(delay_id)
    sig_window = [sig(delay_id(ii):(32*os + delay_id(ii)-1)),zeros(1,num_zero)];
    sig_window_fft = fft(sig_window);
    %     syn_mat(ii,:)=...
    %             sig_window_fft*standard_fft'./sqrt(sum(abs(sig_window_fft).^2));
    syn_mat(ii,:)=...
        sig_window_fft*standard_fft';
end
r_xx = xcorr(standard);
[~,max_pos] = max(r_xx);
% r_x = r_xx(max_pos-127:max_pos+128);
 r_x = r_xx(max_pos-25:max_pos+25);
fft_r_x = fft(r_x);

[m,del_p] =max(abs(syn_mat(delay_id,:)));
[num,pos]=sort(m);
peak_freq = pos(end:-1:end-1);
for num_freq = 1:length(peak_freq)
    freq_tmp =  peak_freq(num_freq);
    delay_tmp = del_p(freq_tmp);
    idx = delay_tmp-25:delay_tmp+25;
%     idx = delay_tmp-127:delay_tmp+128;
    if idx(1)<1
        tmp = find(idx<1);
        idx_i = max(tmp)+1:length(idx);
        idx = 1:idx(end);
    elseif idx(end)>size(syn_mat,1)
        tmp = find(idx>size(syn_mat,1));
        idx_i = 1:min(tmp)-1;
        idx = idx(1):size(syn_mat,1);
    else
        idx_i = 1:length(idx);
    end
    corr_mat = fft(syn_mat(idx,freq_tmp));
    h_tmp(num_freq) = fft_r_x(idx_i)*corr_mat./sqrt(sum(abs(corr_mat).^2));
end
[n,p] = max(abs(h_tmp));
freq_tmp =  peak_freq(p);
delay_tmp = del_p(freq_tmp);

freq = freq_precision*freq_id(freq_tmp);
delay=delay_tmp;

% [mm,pp] = max(abs(syn_mat(delay_id,:)));
% [num,pos]=sort(mm)
% figure;plot(delay_id,abs(syn_mat(:,45)))
%
% r_xx = xcorr(standard);
% [~,pp] = max(r_xx);
% r_xx = r_xx(pp-127:pp+128);
% fft_r_xx = fft(r_xx);
% corr_mat = fft(syn_mat((pp(28)-127):(pp(28)+128),28));
% h_tmp_1 = fft_r_xx*corr_mat;
% abs(h_tmp_1)
% (pp(45)-127):(pp(45)+128)
% figure;plot(abs(r_xx(pp-127:pp+128)))