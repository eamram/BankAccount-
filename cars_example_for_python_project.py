#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:44:07 2021

@author: igal.nir
"""

cars = {}


class Car():
    def __init__(self, year):
        self.year = year
        self.visits = []
        
    def visit_gas_station(self, fuel_needed):
        visit = GasStationVisit(fuel_needed)
        visit.do_fuel(fuel_needed)
        self.visits.append(visit)


class GasStationVisit():
    def __init__(self, fuel_needed):
        self.fuel_needed = fuel_needed
        self.fuel_actual = None
        
    def do_fuel(self, fuel):
        # is there enoght fuel in the station??
        self.fuel_actual = self.fuel_needed


