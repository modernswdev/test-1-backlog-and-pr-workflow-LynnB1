# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# this variable and the cheat logic must be removed to close the backdoor vulnerability in the game, as it allows players to bypass the intended gameplay mechanics and win without engaging in combat or strategy. Commenting to remove it from the game while keeping it visible for educational purposes.
# SECURITY ISSUE: Hardcoded secret code creates a backdoor vulnerability.
# This allows users to bypass intended gameplay.
# FIX: Remove this variable and all cheat logic before production release.
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

# the math to subtract 10 health from the Boss (b_hp) is missing and must be added to the attack() function for it to work properly.
    # BUG: The boss HP (b_hp) is not reduced when the player attacks.
    # Because no damage is applied, the boss never loses health.
    # FIX: Subtract 10 from b_hp to apply damage.
def attack():
  global b_hp
    b_hp -= 10
    print("You deal 10 damage!")

# the heal() function should include a check to ensure that the player's HP does not exceed 50 and that they cannot heal if their HP is 0 or less.
def heal():
  global p_hp
  if p_hp <= 0:
    print("You can't heal when you're down!")
    return
    # BUG: No boundary checks exist for player HP.
  # Players can overheal past 50 HP or potentially heal while at 0 HP.
  # FIX: Add max HP cap (50) and block healing when HP is 0.
p_hp += 20
  if p_hp > 50:
    p_hp = 50
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
# remove the cheat code option from the game loop to prevent players from bypassing the intended gameplay mechanics and ensure that they engage in combat or strategy to win the game.
# add a victory message and break the loop when the Boss's health reaches 0 or less to indicate that the player has won the game.
# add a defeat message and break the loop when the player's health reaches 0 or less to indicate that the player has been defeated.
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  else:
    print("Invalid choice! Please choose 'a' to attack or 'h' to heal.")
  
  if b_hp > 0:
    p_hp -= 10

  if b_hp <= 0:
    print("Victory! You defeated the boss!")
      break
  if p_hp <= 0:
    print("You have been defeated!")
    break
# BUG: No victory condition message exists when boss HP reaches 0.
# FIX: Add a victory message when b_hp <= 0 before ending the game.
print("Game Over!")
Documented security and combat logic fixes for boss_mini.py
