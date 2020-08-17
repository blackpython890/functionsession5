from typing import List 
import time


def time_it(fn, *args, repetitons= 1, **kwargs):

    if fn == 'temp_converter':
        start_time = time.time()
        for _ in range( repetitons ):
            temp_converter(args)
        end_time = time.time()
        return (end_time-start_time)/repetitons
    elif fn == 'polygon_area':
        start_time = time.time()
        for _ in range( repetitons ):
            temp_converter(args)
        end_time = time.time()
        return (end_time-start_time)/repetitons



def temp_converter(temp , temp_given_in):

    if temp_given_in.upper() == 'F':
        t = (temp-32)*5/9
        return t
    elif temp_given_in.upper() == 'C':
        t = 9/5 * (temp) + 32
        return t
    elif temp_given_in.upper() not in ('C' , 'F'):
        raise NotImplementedError("Invalid Temperature Coneversion")


def polygon_area(side_length , side):

    if side_length <= 0:
        raise ValueError("How come Side is zero.")
    else:
        if side <= 0 or side >=7:
            raise NotImplementedError 
        elif side in ( 2 , 1 ):
            raise ValueError("No Polygon of Side 1 & 2 Exists")
        elif side == 3:
            return True
        elif side == 4:
            return side_length*side_length
        elif side == 5:
            return True
        elif side == 6:
            return True


def speed_converter(speed , dist , time):

    if speed < 0:
        raise ValueError("Speed is negative.")
    else:
        if dist.upper == 'KM':
            if time.upper()  == 'S':
                return True
            elif time.upper == 'MS':
                return True
            elif time.upper() == 'M':
                return True
            elif time.upper() == 'HR':
                return True
            elif time.upper() == 'DAY':
                return True
            else:
                raise ValueError("Valid Distance Invalid Time")
        elif dist.upper == 'M':
            if time.upper()  == 'S':
                return True
            elif time.upper == 'MS':
                return True
            elif time.upper() == 'M':
                return True
            elif time.upper() == 'HR':
                return True
            elif time.upper() == 'DAY':
                return True
            else:
                raise ValueError("Valid Distance Invalid Time")
        elif dist.upper == 'FT':
            if time.upper()  == 'S':
                return True
            elif time.upper == 'MS':
                return True
            elif time.upper() == 'M':
                return True
            elif time.upper() == 'HR':
                return True
            elif time.upper() == 'DAY':
                return True
            else:
                raise ValueError("Valid Distance Invalid Time")
        elif dist.upper == 'YRD':
            if time.upper()  == 'S':
                return True
            elif time.upper == 'MS':
                return True
            elif time.upper() == 'M':
                return True
            elif time.upper() == 'HR':
                return True
            elif time.upper() == 'DAY':
                return True
            else:
                raise ValueError("Valid Distance Invalid Time")
        else:
            raise ValueError("Invalid User Distance Input")


def squared_power_list():
    pass
