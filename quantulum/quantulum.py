from quantulum3 import parser
import re

def units_prediction(text):
    units_list = []
    quants_list = ["dimensionless", "per second per milliampere per litre per litre"]
    text = " ".join(text.split())
    quants = parser.parse(text)
    for quant in quants:        
        if (quant.unit.name == "dimensionless" or quant.unit.name == "dime" or quant.unit.name == "year" 
                or quant.unit.name == "years" or quant.unit.name == "count" or quant.unit.name == "exayear" 
                or quant.unit.name == "brazilian real" or quant.unit.name == "barn" or quant.unit.name == "set"
                or quant.unit.name == "percentage" or quant.unit.name == "day" or quant.unit.name == "dollar"
                or quant.unit.name == "second" or quant.unit.name == "minute" or quant.unit.name == "hour"
                or quant.unit.name == "degree angle" or quant.unit.name == "month" or quant.unit.name == "terayear barye teraampere"
                or quant.unit.name == "per centavo to the 9 per newton per hour to the 709 per year" 
                or quant.unit.name == "bit" or quant.unit.name == "bit" or quant.unit.name == "bit"
                or quant.unit.name == "centavo ampere gross" or quant.unit.name == "turn" or quant.unit.name == "centavo ampere gauss"
                or quant.unit.name == "indian rupee" or quant.unit.name == "euro" or quant.unit.name == "gauss atomic mass unit pint year"
                or quant.unit.name == "year ampere-turn" or quant.unit.name == "pair" or quant.unit.name == "second atomic mass unit barn set"
                or quant.unit.name == "ampere-turn" or quant.unit.name == "femtoampere barn south african rand year" or quant.unit.name.startswith("atomic mass unit siemens")
                or quant.unit.name == "second litre attobarn" or quant.unit.name == "tonne hour" or quant.unit.name == "litre acre second"
                or quant.unit.name.startswith("per mile to the") or quant.unit.name == "year ampere-turn" or quant.unit.name == "year ampere-turn"
                or quant.unit.name == "year ampere-turn" or quant.unit.name == "year ampere-turn" or quant.unit.name == "year ampere-turn"
                   ): 
                   
            pass
    
        else:
            units_value = [quant.surface, quant.unit.name, quant.unit.entity.name]
            units_list.append(units_value)
    return units_list
  
  
text = "para para roadmap on neuromorphic computing and engineering current and future challenge very encouraging electrical result of fully front end of line integrated fefet device featuring switching speed 50ns at 5v pulse voltage have been reported recently based on 1mbit memory array ."
units_list = units_prediction(text)
units_list

'''
 op = [['50ns', 'nanosecond', 'time'],
 ['5v', 'volt', 'electric potential'],
 ['1mbit', 'megabit', 'data storage']]
 '''
