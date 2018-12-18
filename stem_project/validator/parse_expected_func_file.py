import os

from stem_project.function_models import FunctionWrapper
from stem_project.function_models import FunctionBlock


def _read_function_name(words):
    """
    Read the function name from a list of words - assume this is the first item
    :param words: list of words to read function name from
    :return: tuple of (function_name, [updated list of words])
    """
    # read function name
    function_name = words[0]
    # remove function name from the list
    words.remove(words[0])
    # return the function name and the updated list of words
    return function_name, words


def _read_function_args(words):
    """
    Read the function arguments from a list of words - assume this is the first item
    :param words: list of words to read arguments from
    :return: tuple of ([function_args], [updated list of words])
    """
    # read and split the function arguments
    arguments = words[0].split(",")
    # remove function arguments from words list
    words.remove(words[0])
    # return arguments and updated list of words
    return arguments, words


def _construct_function_wrappers(words):
    """
    Take a list of words and constructs a list of function wrappers
    :param words: the list of words to construct function block from
    :return: list of function blocks
    """
    function_wrappers = []
    # While there are still words left to read
    while words:
        function_name, words = _read_function_name(words)
        arguments, words = _read_function_args(words)
        try:
            arguments = [int(i) for i in arguments]
        except ValueError:
            pass
        function_wrappers.append(FunctionWrapper(function_name, arguments))
    return function_wrappers


def _does_file_exist_in_dir(file_path):
    return os.path.isfile(file_path)


def read_expected_from_file(file_path):
    """
    Read a file and construct a function block for each line.
    :param file_path: the path to the file to read
    :return: a list of function blocks
    """
    if not _does_file_exist_in_dir(file_path):
        raise RuntimeError("File path to expected functions does not exist")
    expected_functions = []
    with open(file_path, "r") as expected_file:
        for line in expected_file.readlines():
            function_wrappers = _construct_function_wrappers(line.split())
            expected_functions.append(FunctionBlock(function_wrappers))
    return expected_functions
