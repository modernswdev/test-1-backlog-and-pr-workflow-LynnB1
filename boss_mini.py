# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# SECURITY RISK: Hardcoded secret creates a backdoor vulnerability.
# FIX: Remove SECRET_CODE and the cheat logic.
# SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50
MAX_HP = 50

def attack():
    global b_hp
    # BUG FIX: Boss HP was not decreasing.
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    # BUG FIX: Add guardrails to prevent overheal and healing when dead.
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()

    # WIN CONDITION FIX
    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
