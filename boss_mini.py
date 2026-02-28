# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.



# SECURITY AUDIT: Hardcoded credential (backdoor). This secret should not exist in source control.
# BONUS FIX: Remove SECRET_CODE entirely and delete the cheat path that compares input to it.
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50
MAX_HP = 50

def attack():
    global b_hp
   # ATTACK LOGIC BUG: This function prints damage but does NOT subtract from b_hp,
    # so boss HP never changes and the game cannot progress to victory.
    # BONUS FIX: Add `b_hp -= 10` and clamp to 0 (e.g., `b_hp = max(0, b_hp)`).
    print("You deal 10 damage!")

def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += HEAL_AMOUNT
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
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
