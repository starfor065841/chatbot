from fsm import TocMachine

machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': [
                'user',
                'state2'
            ],
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': [
                'user',
                'state1'
            ],
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


if __name__ == "__main__":
    while True:
        text = input('input: ')
        print('---')
        print('LAST STATE: ' + machine.state)

        machine.advance(text)
        #machine.advance('go to state1')
        #machine.state1
        print('FINAL STATE: ' + machine.state)
        print('---')


