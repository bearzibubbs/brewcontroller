#!/usr/bin/python
#
# This file is part of IvPID.
# Copyright (C) 2015 Ivmech Mechatronics Ltd. <bilgi@ivmech.com>
#
# IvPID is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IvPID is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#title           :test_pid.py
#description     :python pid controller test
#author          :Caner Durmusoglu
#date            :20151218
#version         :0.1
#notes           :
#python_version  :2.7
#dependencies    : matplotlib, numpy, scipy
#==============================================================================

import pid as PID
import time
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline, make_interp_spline #  Switched to BSpline

""" 
General plan:
 Need to intake a set point, let's make that a constant for now. 
 Once we have a set point, we need to have a clean start. so should run pid.clear()
 so we'll start with error=0 
 while program is running, 
 initiate db connection
 get temperature from db
 get setPoint from db

 run PID.update(feedback=0)

 """


if __name__ == "__main__":
    test_pid(1, 4, 0.0001, L=100)
#    test_pid(0.8, L=50)