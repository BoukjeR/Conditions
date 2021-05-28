# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, milking_status, location, season, slurry, grass_status):
    if location == 'pasture' and (time_of_day == 'night' or weather == 'rainy'):
        print('take cows to cowshed')
    elif location == 'pasture' and (milking_status == True or (slurry == True and (weather == 'rainy' or weather == 'neutral')) or (grass_status == True and season == 'spring' and weather == 'sunny')):
        print('take cows to cowshed')
    if milking_status == True and (location == 'pasture' or location == 'cowshed'):
        print('milk cows')
    elif slurry == True and (weather == 'rainy' or weather == 'neutral') and (location == 'pasture' or location == 'cowshed'):
        print('fertilize pasture')
    elif grass_status == True and season == 'spring' and weather == 'sunny' and (location == 'pasture' or location == 'cowshed'):
        print('mow grass')
    else:
        print('wait')
    if location == 'pasture' and (milking_status == True or (slurry == True and (weather == 'rainy' or weather == 'neutral')) or (grass_status == True and season == 'spring' and weather == 'sunny')):
        print('take cows back to pasture')

farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
farm_action('bowling', 'night', False, 'cowshed', 'winter', False, True)
farm_action('sunny', 'night', True, 'cowshed', 'summer', False, True)