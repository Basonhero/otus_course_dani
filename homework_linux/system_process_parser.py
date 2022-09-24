import datetime
import subprocess


def main():
    users_to_processes = {}
    total_cpu = 0
    total_mem = 0
    max_cpu = 0
    max_mem = 0
    max_mem_process_name = ""
    max_cpu_process_name = ""

    ps_result = subprocess.run(['ps', 'aux'], capture_output=True).stdout
    result_list = str(ps_result).split("\\n")

    for string in result_list[1:-1]:
        splitted_str = list(filter(''.__ne__, string.split(' ')))

        """ User and process """
        user = splitted_str[0]
        process_name = splitted_str[-1]
        if user not in users_to_processes.keys():
            users_to_processes[user] = 1
        else:
            users_to_processes[user] += 1

        """ CPU and MEM """
        cpu = float(splitted_str[2])
        mem = float(splitted_str[3])

        if max_mem < mem:
            max_mem = mem
            max_mem_process_name = process_name

        if max_cpu < cpu:
            max_cpu = cpu
            max_cpu_process_name = process_name

        total_cpu += cpu
        total_mem += mem

    users_to_processes_for_report = '\n'.join([f'{user}: {process}' for user, process in users_to_processes.items()])

    report = \
        f"Отчёт о состоянии системы:\n" \
        f"Пользователи системы: {list(users_to_processes.keys()).__str__()[1:-1]}\n" \
        f"Процессов запущено: {sum(users_to_processes.values())}\n" \
        f"Пользовательских процессов:\n" \
        f"{users_to_processes_for_report}\n" \
        f"Всего памяти используется: {total_mem}%\n" \
        f"Всего CPU используется: {total_cpu}%\n" \
        f"Больше всего памяти использует: {max_mem}% - {max_mem_process_name[:20]}\n" \
        f"Больше всего CPU использует: {max_cpu}% - {max_cpu_process_name[:20]}\n"

    print(report)
    with open(f"{datetime.datetime.now()}_scan.txt", 'w') as f:
        f.write(report)


if __name__ == '__main__':
    main()
