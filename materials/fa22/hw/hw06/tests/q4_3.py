test = {   'name': 'q4_3',
    'points': [0, 5],
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure to return the number of face cards, not a proportion\n'
                                               '>>> num_face = deck_simulation_and_statistic(13, deck_model_probabilities)\n'
                                               '>>> num_face % 1 == 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The statistic should be between 0 and 13 face cards for\n'
                                               '>>> # a sample size of 13\n'
                                               '>>> num_face = deck_simulation_and_statistic(13, deck_model_probabilities)\n'
                                               '>>> 0 <= num_face <= 13\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
