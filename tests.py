from functions.get_files_info import get_files_info

def main():
    print("getting (calculator, .)")
    print(get_files_info("calculator" , "."))
    print("getting (calculator, pkg)")
    print(get_files_info("calculator", "pkg"))
    print("getting (calculator, /bin)")
    print(get_files_info("calculator", "/bin"))
    print("getting (calculator, ../)")
    print(get_files_info("calculator", "../"))

if __name__ == "__main__":
    main()