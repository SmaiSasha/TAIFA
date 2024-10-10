class mealey_machine:
    def __init__(self, states, inputs, transitions):
        """
        Инициализация автомата Мили.

        :param states: Набор состояний автомата Мили.
        :param inputs: Набор входных символов.
        :param transitions: Функция переходов автомата Мили (словарь), которая определяет следующее состояние и выходной символ для
                            каждого состояния и входного символа.
        """
        self.states = states
        self.inputs = inputs
        self.transitions = transitions

    @classmethod
    def from_file(cls, file_path: str):
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
        return cls(states, inputs, transitions)
    
    def mealey_to_moore(mealy_machine):
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
        return moore_states, moore_inputs, moore_transitions, moore_outputs_mapping

class moore_machine:
    def __init__(self, states, inputs, transitions, output_mapping):
        """
        Инициализация автомата Мура.

        :param states: Набор состояний автомата Мура.
        :param inputs: Набор входных символов.
        :param transitions: Функция переходов автомата Мура (словарь), которая определяет следующее состояние для
                            каждого состояния и входного символа.
        :param output_mapping: Функция, которая сопоставляет состояниям автомата Мура соответствующие выходные символы.
        """
        self.states = states
        self.inputs = inputs
        self.transitions = transitions
        self.output_mapping = output_mapping
    
    @classmethod
    def from_file(cls, file_path: str):
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
        return cls(states, inputs, transitions, output_mapping)
    
    def moore_to_mealey(moore_machine):
        # Извлекаем состояния, входы, переходы и отображение выходов из moore_machine
        moore_states = moore_machine.states
        moore_inputs = moore_machine.inputs
        moore_transitions = moore_machine.transitions
        moore_output_mapping = moore_machine.output_mapping

        # Готовим структуру для хранения переходов Mealy-машины
        mealey_transitions = {}

        # Проходим по всем состояниям и входам
        for state in moore_states:
            for input_signal in moore_inputs:
                # Определяем новое состояние, в которое переходит машина при данном входе
                new_state = moore_transitions[(state, input_signal)]

                # Для Mealy-машины нужно также получить выход на переходе, который соответствует выходу нового состояния в Moore-машине
                output_signal = moore_output_mapping[new_state]

                # Добавляем в таблицу переходов для Mealy-машины: текущий state, вход и переход в новую state с соответствующим выходом
                mealey_transitions[(state, input_signal)] = (new_state, output_signal)
        return moore_states, moore_inputs, mealey_transitions