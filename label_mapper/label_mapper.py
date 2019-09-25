# encoding=utf-8
"""Main module of the label mapper"""

# Import external modules
import sys

# Import internals
from .log_importer import get_set_from_log
from .model_importer import get_activities_from_model, ProcessModelType, apply_label_mappings
from .cmd_parser import parse_args
from .gui_labeler import build_main_window
from .gui_pathdialog import get_file_names


def main():
    """
    Main program for the label mapper
    :return:
    """
    # 1. Set up argument parser
    args = parse_args()

    # 2. Get event log path and model path from the cmd arguments
    if args.log is not None or args.model is not None:
        log_path = args.log
        model_path = args.model
        out_path = args.out
    else:
        model_path, log_path, out_path = get_file_names()
    
    # 3. Get all available activity and event log names
    # Get all activity names from the model
    activities = get_activities_from_model(model_path, ProcessModelType.dcr_graph)

    # Get all event names from the event log
    events = get_set_from_log(log_path)

    # 4. Set up GUI and get mapping
    mapping = build_main_window(activities, events)

    print(mapping)

    # 5. Apply Mapping
    apply_label_mappings(mapping, model_path, out_path)


if __name__ == '__main__':
    main()
    sys.exit(0)
