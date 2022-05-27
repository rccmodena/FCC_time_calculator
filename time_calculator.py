#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

DAYS_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def convert_time_12_24(time):
    '''
    Convert format 12 hour to 24 hours.
    Example: 3:00 PM -> 15:00
    '''
    time, period = time.split()
    hours, minutes = [int(val) for val in time.split(':')]

    if hours == 12 and period == "AM":
        hours = 0

    elif period == "PM":
        hours += 12
    
    return f"{hours}:{str(minutes).zfill(2)}"


def convert_time_24_12(time):
    '''
    Convert format 24 hour to 12 hours.
    Example: 15:00 -> 3:00 PM
    '''
    hours, minutes = [int(val) for val in time.split(':')]

    hours = hours % 24
    period = "AM"

    if hours == 0:
        hours = 12

    elif hours == 12:
        period = "PM"

    elif hours > 12:
        period = "PM"
        hours = hours % 12
    
    return f"{hours}:{str(minutes).zfill(2)} {period}"


def increase_hours(start, duration):
    '''
    Increase start date by duration.
    Important: the hours must be in 24h format.
    '''
    h1, m1 = [int(val) for val in start.split(':')]
    h2, m2 = [int(val) for val in duration.split(':')]

    m_final = (m1 + m2) % 60
    h_increment = (m1 + m2) // 60


    h_final = h1 + h2 + h_increment

    if h_final > 0:
        h_final = h_final % 24

    days = (h1 + h2 + h_increment) // 24

    return [f"{h_final}:{str(m_final).zfill(2)}", days]


def add_time(start, duration, dow=None):
    time, days = increase_hours(convert_time_12_24(start), duration)

    time_final = convert_time_24_12(time)

    if dow is not None:
        dow_int = (DAYS_WEEK.index(dow.capitalize()) + days) % 7
        dow_final = DAYS_WEEK[dow_int]

        time_final += f", {dow_final}"

    if days == 1:
        time_final += " (next day)"

    elif days > 1:
        time_final += f" ({days} days later)"
    
    return time_final