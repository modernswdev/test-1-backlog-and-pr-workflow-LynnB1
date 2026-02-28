# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.



SECRET_CODE = "ADMIN_ACCESS_2025"


p_hp = 50
b_hp = 50
MAX_HP = 50

def attack():
    global b_hp
     # BUG (in non-production version): attack() often prints damage but fails to subtract from b_hp,
    # so the boss never takes damage and the game cannot reach Victory.
    # FIX: subtract a constant damage amount (e.g., 10) from b_hp and clamp at 0.
    b_hp -= 10 # BUG (in non-production version): attack() often prints damage but fails to subtract from b_hp,
    # so the boss never takes damage and the game cannot reach Victory.
    # FIX: subtract a constant damage amount (e.g., 10) from b_hp and clamp at 0.
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    # BUG/RISK (in non-production version): heal() may allow healing while defeated (p_hp <= 0),
    # which breaks game logic and player state. Add a guard clause to block healing if p_hp <= 0.
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    # BUG/RISK (in non-production version): heal() may over-heal above MAX_HP.
    # FIX: after applying healing, clamp p_hp to MAX_HP (boundary check).
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# SECURITY AUDIT NOTE:
# BUG (in vulnerable version): a SECRET_CODE / cheat variable and logic block may exist that bypasses gameplay.
# FIX: remove SECRET_CODE and delete the associated cheat logic entirely to close the backdoor vulnerability.

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

    # WIN CONDITION:
    # BUG (in non-production version): loop may continue even when b_hp reaches 0.
    # FIX: when b_hp <= 0, print Victory and break (terminate loop).
    
    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
