from modules.auth import login, register
from modules.utils import load_json
from modules.setup_utils import setup_environment  # 💡 NEW!

def main():
    setup_environment()  # 🛠️ Tự động kiểm tra & tạo data nếu cần

    users = load_json("data/users.json")
    while True:
        print("\n🔐 Secure Login System")
        print("1. Login\n2. Register\n3. Exit")
        choice = input("Select: ")

        if choice == '1':
            login(users)
        elif choice == '2':
            register(users)
        elif choice == '3':
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
