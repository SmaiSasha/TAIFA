class mealy_machine:
    def __init__(self, states, inputs, transitions):
        """
        Инициализация автомата Мили.

        :param states: Набор состояний автомата Мили.
        :param inputs: Набор входных символов.
        :param transitions: Функция переходов автомата Мили (словарь), которая определяет следующее состояние для
                            каждого состояния и входного символа.
        """
        self.states = states
        self.inputs = inputs
        self.transitions = transitions

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

    return states, inputs, transitions
