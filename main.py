import mealey_to_moore_and_back as mtmb

mealey_machine = mtmb.parse_mealy_machine('input_mealey.txt')
moore_machine = mtmb.mealy_to_moore(mealey_machine)

moore_machine2 = mtmb.parse_moore_machine('input_moore.txt')
mealey_machine2 = mtmb.moore_to_mealy(moore_machine2)

# print('mealy_machine.states:', mealey_machine.states)
# print('mealy_machine.inputs:', mealey_machine.inputs)
# print('mealey_machine.transitions:', mealey_machine.transitions)

# print('mealy_machine.states:', mealey_machine2.states)
# print('mealy_machine.inputs:', mealey_machine2.inputs)
# print('mealey_machine.transitions:', mealey_machine2.transitions)

# print('mealy_machine.states:', mealey_machine2.states == mealey_machine.states)
# print('mealy_machine.inputs:', mealey_machine2.inputs == mealey_machine.inputs)
# print('mealey_machine.transitions:', mealey_machine2.transitions == mealey_machine.transitions)

# print('moore_machine.states:',moore_machine.states)
# print('moore_machine.inputs:',moore_machine.inputs)
# print('moore_machine.transitions:',moore_machine.transitions)
# print('moore_machine.output_mapping;',moore_machine.output_mapping)

# print('moore_machine.states:',moore_machine2.states)
# print('moore_machine.inputs:',moore_machine2.inputs)
# print('moore_machine.transitions:',moore_machine2.transitions)
# print('moore_machine.output_mapping;',moore_machine2.output_mapping)

#   ;  s0   ; s1   ; s2   ; s3
# x1; s3/y1; s0/y2; s2/y3; s0/y5
# x2; s1/y1; s2/y1; s0/y4; s3/y2
# x3; s0/y2; s1/y4; s3/y1; s1/y5


# q0 s0/y2
# q1 s0/y4
# q2 s0/y5
# q3 s1/y1
# q4 s1/y4
# q5 s1/y5
# q6 s2/y1
# q7 s2/y3
# q8 s3/y1
# q9 s3/y2


#   ;y2;y4;y5;y1;y4;y5;y1;y3;y1;y2
#   ;q0;q1;q2;q3;q4;q5;q6;q7;q8;q9
# x1;q8;q8;q8;q0;q0;q0;q7;q7;q2;q2
# x2;q3;q3;q3;q6;q6;q6;q1;q1;q9;q9
# x3;q2;q2;q2;q4;q4;q4;q8;q8;q5;q5


# 	Мур:
#   ;y2;y4;y5;y1;y4;y5;y1;y3;y1;y2
#   ;q0;q1;q2;q3;q4;q5;q6;q7;q8;q9
# x1;q8;q8;q8;q0;q0;q0;q7;q7;q2;q2
# x2;q3;q3;q3;q6;q6;q6;q1;q1;q9;q9
# x3;q2;q2;q2;q4;q4;q4;q8;q8;q5;q5

# Мили:
#   ;  q0;    q1;    q2;    q3;    q4;    q5;    q6;    q7;    q8;    q9
# x1; q8/y1; q8/y1; q8/y1; q0/y2; q0/y2; q0/y2; q7/y3; q7/y3; q2/y5; q2/y5
# x2; q3/y1; q3/y1; q3/y1; q6/y1; q6/y1; q6/y1; q1/y4; q1/y4; q9/y2; q9/y2
# x3; q2/y5; q2/y5; q2/y5; q4/y4; q4/y4; q4/y4; q8/y1; q8/y1; q5/y5; q5/y5
