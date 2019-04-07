'''
Main entry point for predicting the results of a March Madness tournament.

todo: argparse
'''

def main:
    #todo: I think this is how I want it to work...
    '''
    input_file = parsed_from_command_line_options
    model_style = also_parsed_from_command_line

    model = model_style match: # I know python doesn't do match, but what does it do?
        case Massey:
            Massey.from_file(input_file)
        case Colley:
            Colley.from_file(input_file)
        case SomeMachineLearningThingIllDo:
            Thing.from_file(input_file)

    rankings = model.rank()
    predicted_bracket = model.predict_bracket()

    actual_results = parsed_from_command_line
    model.evaluate(actual_results)
    '''
    pass

if __name__ == '__main__':
    main()