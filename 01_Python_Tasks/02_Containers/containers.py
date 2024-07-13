def run_task_1():
    import Firelink
    print("[0] Google\n[1] LinkedIn\n[2] Facebook\n[3] Copilot")
    link_id = int(input("Enter which website ID want to open [0 : 3]: "))
    if link_id in range(0, len(Firelink.fav_links)):
        print(f"Openning {Firelink.fav_links[link_id]}")
        Firelink.firefox(Firelink.fav_links[link_id])
    else:
        print("Error input")


def run_task_2():
    import requests
    import pprint
    url = "https://api.ipify.org/?format=json"
    ip = requests.get(url).json()["ip"]
    url_ip = f"https://ipinfo.io/{ip}/geo"
    dict_data = requests.get(url_ip).json()
    pprint.pprint(dict_data)

def run_task_null():
    print("Error task ID")

def select_task(task_id):
    tasks = {
        1: run_task_1,
        2: run_task_2,
    }
    if task_id in range(1, (len(tasks.keys()) + 1)):
        tasks[task_id]()
    else:
        run_task_null()

if __name__ == "__main__":
    print("Task 1: openning website using firelink module")
    print("Task 2: request module to get the location")
    select_task(int(input("Enter task ID: ")))