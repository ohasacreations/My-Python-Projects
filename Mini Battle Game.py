# --- SETUP (Same as before) ---
hero_hp = 100
hero_attack = 15
monster_hp_list = [40, 30, 55]
monster_attack_list = [10, 12, 8]

# --- THE MAIN BATTLE LOOP ---
for i in range(len(monster_hp_list)):
    current_monster_hp = monster_hp_list[i]
    current_monster_attack = monster_attack_list[i]
    
    print("\n-------------------------------------------") # Added for spacing
    print(f"--- A monster with {current_monster_hp} HP appears! ---")
    print(f"Your HP: {hero_hp}")
    print("-------------------------------------------")

    # --- THE INTERACTIVE COMBAT LOOP ---
    while current_monster_hp > 0:
        
        # NEW: We ask the user for their action!
        # The program will PAUSE here and wait for the user to press Enter.
        action = input("Press Enter to ATTACK!")
        
        # The code only continues after the user presses Enter.
        # The 'action' variable will be an empty string "" if they just press Enter.
        # For this simple version, we only have one action.
        
        # a. Hero's Turn
        print("\n> You attack the monster!")
        current_monster_hp -= hero_attack
        # We use max(0, ...) to ensure the HP doesn't display as a negative number
        print(f"  Monster's HP is now {max(0, current_monster_hp)}.")
        
        # b. Check if monster is defeated
        if current_monster_hp <= 0:
            print("\n*** Monster defeated! ***")
            break # Exit the inner 'while' loop to find the next monster

        # c. Monster's Turn (if it's still alive)
        print("> The monster attacks you!")
        hero_hp -= current_monster_attack
        print(f"  Your HP is now {max(0, hero_hp)}.")

        # d. Check if hero is defeated
        if hero_hp <= 0:
            print("\n*** You have been defeated... GAME OVER. ***")
            break # Exit the inner 'while' loop

    # After each battle, check if the hero has been defeated
    if hero_hp <= 0:
        break # Exit the outer 'for' loop and end the game

# --- END OF GAME ---
# This part is only reached if the outer loop finished without the hero being defeated.
if hero_hp > 0:
    print("\n=============================================")
    print("   Congratulations! You defeated all monsters!   ")
    print("=============================================")