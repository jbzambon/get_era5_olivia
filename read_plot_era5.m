%  Program to read in Era-5 reanalysis NetCDF data and return meteorological winds
%   also does some plotting for fun
%
%  Joseph B. Zambon
%  27 February 2020
%  jbzambon@ncsu.edu

clear all; close all;

ncfile = 'aug16_nov18.nc';  % define NetCDF input file

%  Load u10, v10
u10 = ncread(ncfile,'u10');
v10 = ncread(ncfile,'v10');

%  Get time dimension
time = ncread(ncfile,'time');  %defaults as an integer due to dataset
time = double(time);           % change to double for arithmetic below

% Time dimension units (from ncdump -h)...
%   hours since 1900-01-01 00:00:00.0
% Convert time dimension to datenum reference (1 Jan 0000)
time = time / 24;  % Convert hours to days
datenum_time = datenum(time + datenum(1900,1,1));

% Check this if you want to...
disp(datestr(datenum_time(1),0));  %start time
disp(datestr(datenum_time(end),0)); %end time

% Convert U,V to Speed and Meteorological Direction (where wind is coming FROM)
wspd = sqrt(u10 .^ 2 + v10 .^ 2);
wdir = atan2d(u10,v10) + 180;

% Plot spatial area of wind speed at first timestep
figure(1)
pcolor(squeeze(wspd(:,:,1)));shading flat; caxis([0 10]); colorbar;

% Plot time-series of wind plots at first grid cell, every 10 days, 240 hours
figure(2);
quiver(datenum_time(1:240:end),zeros(size(datenum_time(1:240:end),1),1),squeeze(u10(1,1,1:240:end)),squeeze(v10(1,1,1:240:end)),'AutoScale','off')
axis([min(datenum_time) max(datenum_time) -10 10])
datetick('x','dd/mmm/yy')
hold on;
yline(0);
