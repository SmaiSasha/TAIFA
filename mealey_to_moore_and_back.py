import mealy_moore_machines_classes as mm

def parse_mealy_machine(file_path):
    """
    Парсинг файла автомата Мили и преобразование его в структуры данных для MealyMachine.

    :param file_path: Путь к файлу с таблицей автомата Мили.
    :return: Кортеж, содержащий (states, inputs, transitions, outputs), которые можно использовать для инициализации MealyMachine.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Разделение строк на ячейки по разделителю ";"
    parsed_lines = [line.strip().split(';') for line in lines]

    # Первая строка - это состояния (s0, s1, s2, ...)
    states = parsed_lines[0][1:]  # Пропускаем первый пустой элемент (так как перед ';' ничего нет)

    # Входные значения - это первый столбец (x1, x2, x3, ...)
    inputs = [line[0] for line in parsed_lines[1:]]

    # Инициализируем словари для переходов и выходов
    transitions = {}

    # Проходим по всем строкам (кроме заголовка) и обрабатываем каждую ячейку
    for i, input_symbol in enumerate(inputs):
        for j, state in enumerate(states):
            transition_output = parsed_lines[i + 1][j + 1]
            next_state, output = transition_output.split('/')  # Разделение состояния и выхода по символу "/"
            
            # Заполняем переходы и выходы для автомата Мили
            transitions[(state, input_symbol)] = (next_state, output)
    return mm.mealy_machine(states, inputs, transitions)


def parse_moore_machine(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    # Разделяем строки и удаляем лишние пробелы
    parsed_lines = [line.strip().split(";") for line in lines]

    # Первая строка - выходные значения
    output_mapping_values = parsed_lines[0][1:]

    # Вторая строка - состояния
    states = parsed_lines[1][1:]

    # Остальные строки - входы и переходы
    inputs = [line[0] for line in parsed_lines[2:]]
    transitions_data = [line[1:] for line in parsed_lines[2:]]

    # Составляем таблицу переходов
    transitions = {}
    for i, input_signal in enumerate(inputs):
        for j, state in enumerate(states):
            transitions[(state, input_signal)] = transitions_data[i][j]

    # Составляем выходные значения для каждого состояния
    output_mapping = {state: output_mapping_values[i] for i, state in enumerate(states)}

    # Создаем объект moore_machine
    moore_machine = mm.moore_machine(states, inputs, transitions, output_mapping)
    
    return moore_machine


def mealy_to_moore(mealy_machine):
    moore_states_unnum = []
    for i in mealy_machine.transitions:
        moore_states_unnum.append(mealy_machine.transitions[i]) 
    moore_states_unnum = list(set(moore_states_unnum))
    moore_states_unnum.sort()
    moore_states = []
    for i in range(len(moore_states_unnum)):
        moore_states.append("q" + str(i))
    moore_inputs = mealy_machine.inputs
    temp_moore_outputs_mapping = {moore_states[i]: moore_states_unnum[i] for i in range(len(moore_states))}
    moore_outputs_mapping = {moore_states[i]: moore_states_unnum[i][1] for i in range(len(moore_states))}
    moore_transitions = {}
    for state in moore_states:
        for inpt in moore_inputs:
            transition = list(temp_moore_outputs_mapping.keys())[list(temp_moore_outputs_mapping.values()).index(mealy_machine.transitions[(temp_moore_outputs_mapping[state][0], inpt)])]
            moore_transitions[(state, inpt)] = transition
    moore_machine = mm.moore_machine(moore_states, moore_inputs, moore_transitions, moore_outputs_mapping)
    return moore_machine

def moore_to_mealy(moore_machine):
    # Извлекаем состояния, входы, переходы и отображение выходов из moore_machine
    moore_states = moore_machine.states
    moore_inputs = moore_machine.inputs
    moore_transitions = moore_machine.transitions
    moore_output_mapping = moore_machine.output_mapping

    # Готовим структуру для хранения переходов Mealy-машины
    mealy_transitions = {}

    # Проходим по всем состояниям и входам
    for state in moore_states:
        for input_signal in moore_inputs:
            # Определяем новое состояние, в которое переходит машина при данном входе
            new_state = moore_transitions[(state, input_signal)]

            # Для Mealy-машины нужно также получить выход на переходе, который соответствует выходу нового состояния в Moore-машине
            output_signal = moore_output_mapping[new_state]

            # Добавляем в таблицу переходов для Mealy-машины: текущий state, вход и переход в новую state с соответствующим выходом
            mealy_transitions[(state, input_signal)] = (new_state, output_signal)

    # Создаем объект Mealy-машины с соответствующими состояниями, входами и переходами
    mealy_machine = mm.mealy_machine(moore_states, moore_inputs, mealy_transitions)
    
    return mealy_machine
