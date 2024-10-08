class mealy_machine:
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