import sys
import random
import AsciiImgs


capybara = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}
capybaraBonus = {'HPb' : 0, 'ATKb' : 0, 'DEFb' : 0}
capybaraTitle = ''

player = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}
playerBonus = {'HPb' : 0, 'ATKb' : 0, 'DEFb' : 0}

def SelTitle():
    adjectiveList = ('Fat', 'Unyielding', 'Smiling', 'Classy', 'Discreet', 'Amused', 'Stern', 'Exalted', 'Air Head', 
                      'Billowy', 'Fluffy', 'Willful', 'Jealous', 'Cautious', 'Nasty', 'Mean', 'Hairless', 'Baby', 
                      'Poor', 'Bright', 'Shaman', 'Electric', 'Worthless', 'Clueless', 
                      'Rat', 'Saint', 'Thin', 'Old', 'Strong', 'Envious', 'Animated', 'Decomposing', 
                      'Quirky', 'Nutritious', 'Shallow', 'Obscene', 'Ablaze', 'Valuable', 'Elated')
    lottery = random.randint(0, 39)
    
    subject = adjectiveList[lottery] + ' Capybara'
    
    return subject
    
    

def StartBattle(GameOn : bool):
    
    GameOn = True
    
    while GameOn:
        Enemy = SelTitle()
        
        
        BattleScreen = f"""
        -------------------------------------------------------------------
                                {Enemy}
            {capybara['HP']}/Health             {capybara['ATK']}/Attack                {capybara['DEF']}/Defense
        -------------------------------------------------------------------
        {AsciiImgs.capybaraImg}
        -------------------------------------------------------------------
                                    Player
            {player['HP']}/Health               {player['ATK']}/Attack                  {player['DEF']}/Defense
        -------------------------------------------------------------------
        
        """
        while True:
            Selection = input("""A foe has appeared, what do you do
                > 1: Attack (a simple attack)
                > 2: Defend (diminish damage equal to your Defense attribute)
                > 3: Flee (1/10 change o skipping this fight, but you dont level up)
            """)
            
            if Selection.upper() != 1 or "ATTACK" or "DEFEND" or "FLEE":
                print(f"''{Selection}'' is not a valid option choose a valid option\n")
            else:
                break
            
    
StartBattle(True)