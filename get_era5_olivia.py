# Joseph B. Zambon
# 25 February 2020
# jbzambon@ncsu.edu
#
# Program to download ERA-5 for 1-August 2016 through 1-November 2018 for Olivia
#   After finishing, run nco commands listed at bottom of this code.

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind',
        ],
        'year': '2016',
        'month': [
            '08', '09', '10',
            '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'area'          : [36.0, -77.25, 34.5, -74.75], # North, West, South, East. Default: global
        'grid'          : [0.25, 0.25], # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'format': 'netcdf',
    },
    '2016.nc')

c.retrieve(
'reanalysis-era5-single-levels',
{
    'product_type': 'reanalysis',
    'variable': [
        '10m_u_component_of_wind', '10m_v_component_of_wind',
    ],
    'year': '2017',
    'month': [
        '01', '02', '03',
        '04', '05', '06',
        '07',
        '08', '09', '10',
        '11', '12',
    ],
    'day': [
        '01', '02', '03',
        '04', '05', '06',
        '07', '08', '09',
        '10', '11', '12',
        '13', '14', '15',
        '16', '17', '18',
        '19', '20', '21',
        '22', '23', '24',
        '25', '26', '27',
        '28', '29', '30',
        '31',
    ],
    'area'          : [36.0, -77.25, 34.5, -74.75], # North, West, South, East. Default: global
    'grid'          : [0.25, 0.25], # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
    'time': [
        '00:00', '01:00', '02:00',
        '03:00', '04:00', '05:00',
        '06:00', '07:00', '08:00',
        '09:00', '10:00', '11:00',
        '12:00', '13:00', '14:00',
        '15:00', '16:00', '17:00',
        '18:00', '19:00', '20:00',
        '21:00', '22:00', '23:00',
    ],
    'format': 'netcdf',
},
'2017.nc')

c.retrieve(
'reanalysis-era5-single-levels',
{
    'product_type': 'reanalysis',
    'variable': [
        '10m_u_component_of_wind', '10m_v_component_of_wind',
    ],
    'year': '2018',
    'month': [
        '01', '02', '03',
        '04', '05', '06',
        '07',
        '08', '09', '10',
    ],
    'day': [
        '01', '02', '03',
        '04', '05', '06',
        '07', '08', '09',
        '10', '11', '12',
        '13', '14', '15',
        '16', '17', '18',
        '19', '20', '21',
        '22', '23', '24',
        '25', '26', '27',
        '28', '29', '30',
        '31',
    ],
    'area'          : [36.0, -77.25, 34.5, -74.75], # North, West, South, East. Default: global
    'grid'          : [0.25, 0.25], # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
    'time': [
        '00:00', '01:00', '02:00',
        '03:00', '04:00', '05:00',
        '06:00', '07:00', '08:00',
        '09:00', '10:00', '11:00',
        '12:00', '13:00', '14:00',
        '15:00', '16:00', '17:00',
        '18:00', '19:00', '20:00',
        '21:00', '22:00', '23:00',
    ],
    'format': 'netcdf',
},
'2018a.nc')

c.retrieve(
'reanalysis-era5-single-levels',
{
    'product_type': 'reanalysis',
    'variable': [
        '10m_u_component_of_wind', '10m_v_component_of_wind',
    ],
    'year': '2018',
    'month': [
        '11',
    ],
    'day': [
        '01',
    ],
    'area'          : [36.0, -77.25, 34.5, -74.75], # North, West, South, East. Default: global
    'grid'          : [0.25, 0.25], # Latitude/longitude grid: east-west (longitude) and north-south resolution (latitude). Default: 0.25 x 0.25
    'time': [
        '00:00',
    ],
    'format': 'netcdf',
},
'2018b.nc')

# Concatenate the individual files into one
#     Complete after downloading the individual files
# ncks -O --mk_rec time 2016.nc 2016.nc
# ncks -O --mk_rec time 2017.nc 2017.nc
# ncks -O --mk_rec time 2018a.nc 2018a.nc
# ncks -O --mk_rec time 2018b.nc 2018b.nc
# ncrcat 2016.nc 2017.nc 2018a.nc 2018b.nc -o aug16_nov18.nc

