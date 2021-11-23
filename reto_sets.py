def remove_duplicates_whith_sets(some_list):
    return list(set(some_list))

def run():
    ramdon_list = [1, 1, 2, 2, 4,"platzi", "platzi"]
    print(remove_duplicates_whith_sets(ramdon_list))

if __name__ == '__main__':
    run()