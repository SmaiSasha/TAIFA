import milmur

mealy_states, mealy_inputs, mealy_transitions = milmur.parse_mealy_machine('input.txt')
mealy_machine = milmur.mealy_machine(mealy_states, mealy_inputs, mealy_transitions)

moore_states_unnum = []
for i in mealy_transitions:
    moore_states_unnum.append(mealy_transitions[i])
moore_states_unnum = list(set(moore_states_unnum))
moore_states_unnum.sort()
moore_states = []
for i in range(len(moore_states_unnum)):
    moore_states.append("q" + str(i))
moore_inputs = mealy_inputs
moore_outputs_mapping = {moore_states[i]: moore_states_unnum[i] for i in range(len(moore_states))}
moore_transitions = {}
for state in moore_states:
    for inpt in moore_inputs:
        transition = list(moore_outputs_mapping.keys())[list(moore_outputs_mapping.values()).index(mealy_transitions[(moore_outputs_mapping[state][0], inpt)])]
        moore_transitions[(state, inpt)] = transition

moore_machine = milmur.moore_machine(moore_states, moore_inputs, moore_transitions, moore_outputs_mapping)

print('moore_transitions:', moore_transitions)

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
