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
    moore_outputs_mapping = {moore_states[i]: moore_states_unnum[i] for i in range(len(moore_states))}
    moore_transitions = {}
    for state in moore_states:
        for inpt in moore_inputs:
            transition = list(moore_outputs_mapping.keys())[list(moore_outputs_mapping.values()).index(mealy_machine.transitions[(moore_outputs_mapping[state][0], inpt)])]
            moore_transitions[(state, inpt)] = transition

    moore_machine = mm.moore_machine(moore_states, moore_inputs, moore_transitions, moore_outputs_mapping)
    return moore_machine

def moore_to_mealy(moore_machine):
    """
    Преобразует автомат Мура в автомат Мили.

    :param moore_machine: Объект класса moore_machine.
    :return: Объект класса mealy_machine, представляющий эквивалентный автомат Мили.
    """
    # Инициализируем состояния и входы автомата Мили
    mealy_states = list(set([moore_machine.output_mapping[state][0] for state in moore_machine.states]))  # Уникальные состояния
    mealy_inputs = moore_machine.inputs

    # Инициализируем словарь переходов для автомата Мили
    mealy_transitions = {}

    # Проходим по всем состояниям автомата Мура
    for moore_state in moore_machine.states:
        current_mealy_state = moore_machine.output_mapping[moore_state][0]  # Текущее состояние автомата Мили

        for input_symbol in mealy_inputs:
            # Найти следующее состояние автомата Мура
            next_moore_state = moore_machine.transitions[(moore_state, input_symbol)]
            
            # Извлекаем следующее состояние автомата Мили и соответствующий выход
            next_mealy_state = moore_machine.output_mapping[next_moore_state][0]
            output = moore_machine.output_mapping[next_moore_state][1]
            
            # Формируем переход для автомата Мили
            mealy_transitions[(current_mealy_state, input_symbol)] = (next_mealy_state, output)

    # Возвращаем эквивалентный автомат Мили
    return mm.mealy_machine(mealy_states, mealy_inputs, mealy_transitions)



