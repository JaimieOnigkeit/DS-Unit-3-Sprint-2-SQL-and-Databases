import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "data\\rpg_db.sqlite3"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()


queries = [
    '''SELECT 
    COUNT(character_id) 
    FROM charactercreator_character;''',
    '''SELECT C
    OUNT (distinct character_id) AS Total 
    ,COUNT (distinct cleric.character_ptr_id) AS Clerics
    , COUNT (distinct fighter.character_ptr_id) AS Fighters
    , COUNT (distinct mage.character_ptr_id) AS Mages
    , COUNT (distinct thief.character_ptr_id) AS Thieves
    , COUNT (distinct n.mage_ptr_id) AS Necromancers 
    FROM charactercreator_character AS main 
    LEFT JOIN charactercreator_cleric AS cleric ON main.character_id = cleric.character_ptr_id 
    LEFT JOIN charactercreator_fighter AS fighter ON main.character_id = fighter.character_ptr_id 
    LEFT JOIN charactercreator_mage AS mage ON main.character_id = mage.character_ptr_id 
    LEFT JOIN charactercreator_thief AS thief ON main.character_id = thief.character_ptr_id 
    LEFT JOIN charactercreator_necromancer AS n ON main.character_id = n.mage_ptr_id;''',
    '''SELECT 
    COUNT(item_id) 
    FROM armory_item;''',
    '''SELECT 
    COUNT(item_ptr_id) 
    FROM armory_weapon;''',
    '''SELECT main.character_id
    , main.name AS Name
    ,COUNT (distinct inv.item_id) AS Items 
    FROM charactercreator_character AS main  
    INNER JOIN charactercreator_character_inventory AS inv ON main.character_id=inv.character_id 
    GROUP BY main.character_id LIMIT 20;''',
    '''SELECT main.character_id
    , main.name AS Name
    , COUNT (distinct inv.item_id) AS Items
    , COUNT (DISTINCT armory_weapon.item_ptr_id) AS Weapons 
    FROM charactercreator_character AS main 
    INNER JOIN charactercreator_character_inventory AS inv ON main.character_id=inv.character_id
    LEFT JOIN armory_weapon ON inv.item_id = armory_weapon.item_ptr_id 
    GROUP BY main.character_id LIMIT 20;''',
    '''SELECT AVG(Weapons) 
    FROM( 
        SELECT main.character_id
        , main.name AS Name,COUNT (distinct inv.item_id) AS Items
        ,COUNT (DISTINCT armory_weapon.item_ptr_id) AS Weapons 
        FROM charactercreator_character AS main 
        INNER JOIN charactercreator_character_inventory AS inv ON main.character_id=inv.character_id 
        LEFT JOIN armory_weapon ON inv.item_id = armory_weapon.item_ptr_id GROUP BY main.character_id 
    );''',
    '''SELECT AVG(Items) 
    FROM(
        SELECT main.character_id
        , main.name AS Name
        ,COUNT (distinct inv.item_id) AS Items
        ,COUNT (DISTINCT armory_weapon.item_ptr_id) AS Weapons 
        FROM charactercreator_character AS main 
        INNER JOIN charactercreator_character_inventory AS inv ON main.character_id=inv.character_id 
        LEFT JOIN armory_weapon ON inv.item_id = armory_weapon.item_ptr_id 
        GROUP BY main.character_id
    );'''
]

for query in queries:
    print("--------------")
    print(f"QUERY: '{query}'")
    results = cursor.execute(query).fetchall()
    print("RESULTS:")
    print(results)

