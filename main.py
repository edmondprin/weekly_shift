from shifts import gather_user_shift
from storage import save_shift

def main():
    new_shift = gather_user_shift()
    save_shift(new_shift)

if __name__ == "__main__":
    main()