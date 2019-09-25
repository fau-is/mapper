# encoding=utf-8
"""
Importer for process models
"""
from enum import Enum, auto
from xml.etree import ElementTree as Etree


class ProcessModelType(Enum):
    """
    Enum that is used to determine which Process Model Type is used
    """
    dcr_graph = auto()
    petri_net = auto()


def get_activities_from_model(model_path, model_type: ProcessModelType):
    """
    Takes the DCR Graph that is stored at the given path and returns all activities as a set
    :return: All activities as a set
    """
    if model_type is ProcessModelType.dcr_graph:
        return get_activities_dcr(model_path)
    else:
        raise NotImplementedError("This feature is not implemented")


def get_activities_dcr(model_path):
    """
    Only purpose is to get the activities from the DCR Graph XML into the data structure
    :return: a set of all activity names in a dcr graph
    """
    # Get dcr graph from the tree
    dcr_graph = Etree.parse(model_path)
    dcr_root = dcr_graph.getroot()

    # Get mappings from dcr graph and return
    return create_labels(dcr_root)


def create_labels(dcr_root):
    """
    Returns activity name event label mapping function
    :param dcr_root: The Etree root element of a dcr graph
    :return: Dictionary of all labels and names
    """
    mappings = []
    for mapping in dcr_root.iter('labelMapping'):
        mappings.append(mapping.get('labelId'))
    return mappings


def apply_label_mappings(mappings, in_path, out_path):
    """
    Function to apply the label mapping
    Reads from in_path to get a dcr graph as xml ElementTree replace the mappings in the xml
    and write the modified version to an output_file
    :param mappings: the created mappings that should be applied
    :param in_path: input (process model) path
    :param out_path: output (process model) path
    :return: None
    """

    # Get the dcr graph from a file
    dcr_graph = Etree.parse(in_path)
    dcr_root = dcr_graph.getroot()

    # Get the mapping elements and tags
    for label in dcr_root.iter('labelMapping'):
        if mappings[label.get('labelId')] != label:
            label.set('labelId', mappings[label.get('labelId')])

    # If the outpath does not end with .xml add it, to indicate fileformat for OS
    if not out_path.endswith(".xml"):
        out_path = out_path + ".xml"

    # Write the dcr graph xml
    with open(out_path, "wb") as f:
        dcr_graph.write(f)
