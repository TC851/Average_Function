# the function gives the average back

def geKm(k1, k2, k3, k4):
    sKm = k1 + k2 + k3 + k4
    dKm = sKm / 4
    return dKm


output = 'Average:' + str(geKm(10, 33, 76, 99)) + ' ' + 'and the second one is' + ' ' + str(geKm(44, 88, 192, 205))
print(output)


# __________________________________________________________________________________________________________________

# average Fuel Consumption with a array
def averageFuelConsumption(kilometersPerTankful):
    averageConsumption = 0.0
    sumKilometers = 0.0

    for kilometer in kilometersPerTankful:
        sumKilometers += kilometer

    averageConsumption = float(sumKilometers) / len(kilometersPerTankful)

    return averageConsumption


# main

kilometers = [1212, 13, 4354, 545]

print('The average Fuel Consumption are:')
print(averageFuelConsumption(kilometers))
