# data.py

food_items_breakfast = {
    "protein": {
        "eggs": {"calories": 78, "type": "non-vegetarian"},
        "greek_yogurt": {"calories": 130, "type": "vegetarian"},
        "cottage_cheese": {"calories": 206, "type": "vegetarian"},
        "turkey_slices": {"calories": 104, "type": "non-vegetarian"},
        "smoked_salmon": {"calories": 117, "type": "non-vegetarian"}
    },
    "whole_grains": {
        "whole_wheat_bread": {"calories": 79, "type": "vegan"},
        "oatmeal": {"calories": 150, "type": "vegan"},
        "quinoa": {"calories": 222, "type": "vegan"},
        "whole_grain_cereal": {"calories": 120, "type": "vegan"},
        "granola": {"calories": 494, "type": "vegan"}
    },
    "fruits": {
        "berries": {"calories": 50, "type": "vegan"},
        "bananas": {"calories": 96, "type": "vegan"},
        "apples": {"calories": 52, "type": "vegan"},
        "oranges": {"calories": 62, "type": "vegan"},
        "grapefruit": {"calories": 52, "type": "vegan"},
        "melon_slices": {"calories": 30, "type": "vegan"}
    },
    "vegetables": {
        "spinach": {"calories": 7, "type": "vegan"},
        "tomatoes": {"calories": 18, "type": "vegan"},
        "avocado": {"calories": 160, "type": "vegan"},
        "bell_peppers": {"calories": 25, "type": "vegan"},
        "mushrooms": {"calories": 15, "type": "vegan"}
    },
    "healthy_fats": {
        "nut_butter": {"calories": 94, "type": "vegan"},
        "nuts": {"calories": 163, "type": "vegan"},
        "chia_seeds": {"calories": 58, "type": "vegan"},
        "flaxseeds": {"calories": 55, "type": "vegan"},
        "avocado_slices": {"calories": 50, "type": "vegan"}
    },
    "dairy": {
        "milk": {"calories": 103, "type": "vegetarian"},
        "cheese": {"calories": 113, "type": "vegetarian"},
        "yogurt": {"calories": 150, "type": "vegetarian"},
        "dairy-free_alternatives": {"calories": 80, "type": "vegan"}
    },
    "other": {
        "honey": {"calories": 64, "type": "vegetarian"},
        "maple_syrup": {"calories": 52, "type": "vegan"},
        "coffee": {"calories": 2, "type": "vegan"},
        "jam": {"calories": 49, "type": "vegan"},
        "peanut_butter": {"calories": 188, "type": "vegan"},
        "cocoa_powder": {"calories": 12, "type": "vegan"}
    }
}

food_items_lunch = {
    "protein": {
        "grilled_chicken_breast": {"calories": 165, "type": "non-vegetarian"},
        "salmon_fillet": {"calories": 206, "type": "non-vegetarian"},
        "tofu": {"calories": 144, "type": "vegan"},
        "lean_beef": {"calories": 176, "type": "non-vegetarian"},
        "shrimp": {"calories": 99, "type": "non-vegetarian"}
    },
    "whole_grains": {
        "brown_rice": {"calories": 216, "type": "vegan"},
        "quinoa": {"calories": 222, "type": "vegan"},
        "whole_wheat_pasta": {"calories": 180, "type": "vegan"},
        "barley": {"calories": 270, "type": "vegan"},
        "couscous": {"calories": 176, "type": "vegan"}
    },
    "vegetables": {
        "leafy_greens": {"calories": 10, "type": "vegan"},
        "broccoli": {"calories": 55, "type": "vegan"},
        "cauliflower": {"calories": 25, "type": "vegan"},
        "carrots": {"calories": 41, "type": "vegan"},
        "bell_peppers": {"calories": 31, "type": "vegan"},
        "cucumbers": {"calories": 16, "type": "vegan"},
        "tomatoes": {"calories": 18, "type": "vegan"},
        "zucchini": {"calories": 17, "type": "vegan"}
    },
    "legumes": {
        "chickpeas": {"calories": 269, "type": "vegan"},
        "lentils": {"calories": 230, "type": "vegan"},
        "black_beans": {"calories": 227, "type": "vegan"},
        "kidney_beans": {"calories": 225, "type": "vegan"},
        "edamame": {"calories": 121, "type": "vegan"}
    },
    "healthy_fats": {
        "avocado": {"calories": 234, "type": "vegan"},
        "nuts": {"calories": 160, "type": "vegan"},
        "seeds": {"calories": 160, "type": "vegan"},
        "olive_oil": {"calories": 119, "type": "vegan"},
        "coconut_oil": {"calories": 121, "type": "vegan"}
    },
    "dairy_or_dairy_alternatives": {
        "greek_yogurt": {"calories": 130, "type": "vegetarian"},
        "cottage_cheese": {"calories": 206, "type": "vegetarian"},
        "cheese": {"calories": 113, "type": "vegetarian"},
        "dairy-free_alternatives": {"calories": 80, "type": "vegan"}
    },
    "additional_toppings_condiments": {
        "sliced_avocado": {"calories": 50, "type": "vegan"},
        "hummus": {"calories": 27, "type": "vegan"},
        "salsa": {"calories": 20, "type": "vegan"},
        "salad_dressings": {"calories": 73, "type": "vegetarian"},
        "herbs_and_spices": {"calories": 0, "type": "vegan"}
    }
}

food_items_dinner = {
    "proteins": {
        "chicken_breast": {"calories": 165, "type": "non-vegetarian"},
        "salmon": {"calories": 206, "type": "non-vegetarian"},
        "beef_steak": {"calories": 250, "type": "non-vegetarian"},
        "tofu": {"calories": 144, "type": "vegan"},
        "shrimp": {"calories": 84, "type": "non-vegetarian"},
        "lentils": {"calories": 116, "type": "vegan"}
    },
    "grains_and_starches": {
        "brown_rice": {"calories": 216, "type": "vegan"},
        "quinoa": {"calories": 222, "type": "vegan"},
        "sweet_potatoes": {"calories": 180, "type": "vegan"},
        "whole_wheat_pasta": {"calories": 174, "type": "vegan"},
        "couscous": {"calories": 176, "type": "vegan"},
        "barley": {"calories": 193, "type": "vegan"}
    },
    "vegetables": {
        "broccoli": {"calories": 55, "type": "vegan"},
        "cauliflower": {"calories": 25, "type": "vegan"},
        "green_beans": {"calories": 31, "type": "vegan"},
        "asparagus": {"calories": 27, "type": "vegan"},
        "brussels_sprouts": {"calories": 38, "type": "vegan"},
        "carrots": {"calories": 41, "type": "vegan"},
        "zucchini": {"calories": 17, "type": "vegan"}
    },
    "legumes": {
        "black_beans": {"calories": 227, "type": "vegan"},
        "chickpeas": {"calories": 269, "type": "vegan"},
        "kidney_beans": {"calories": 333, "type": "vegan"},
        "lentils": {"calories": 353, "type": "vegan"}
    },
    "healthy_fats": {
        "avocado": {"calories": 160, "type": "vegan"},
        "olive_oil": {"calories": 119, "type": "vegan"},
        "nuts": {"calories": 160, "type": "vegan"},
        "seeds": {"calories": 150, "type": "vegan"}
    },
    "dairy_or_dairy_alternatives": {
        "greek_yogurt": {"calories": 59, "type": "vegetarian"},
        "cheese": {"calories": 113, "type": "vegetarian"},
        "almond_milk": {"calories": 40, "type": "vegan"}
    },
    "sauces_and_condiments": {
        "tomato_sauce": {"calories": 32, "type": "vegan"},
        "soy_sauce": {"calories": 8, "type": "vegan"},
        "balsamic_vinegar": {"calories": 14, "type": "vegan"},
        "mustard": {"calories": 10, "type": "vegan"},
        "salsa": {"calories": 15, "type": "vegan"},
        "guacamole": {"calories": 50, "type": "vegan"},
        "hummus": {"calories": 27, "type": "vegan"}
    },
    "herbs_and_spices": {
        "basil": {"calories": 22, "type": "vegan"},
        "oregano": {"calories": 5, "type": "vegan"},
        "rosemary": {"calories": 2, "type": "vegan"},
        "thyme": {"calories": 3, "type": "vegan"},
        "cumin": {"calories": 22, "type": "vegan"},
        "paprika": {"calories": 20, "type": "vegan"},
        "garlic_powder": {"calories": 9, "type": "vegan"},
        "onion_powder": {"calories": 7, "type": "vegan"}
    }
}
