from process_number import Process
from routine import routine


def main (list_of_process):
    generated_process_list = Process()
    process_list = generated_process_list.process_input_to_list(list_of_process)
    
    return routine(process_list)

if __name__ == '__main__':
    main('Single string with processes numbers separated by comma')
