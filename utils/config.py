import json
from bunch import Bunch
import os
import sys

def get_config_from_json(json_file):
    """
    Get the config from a json file
    :param json_file:
    :return: config(namespace) or config(dictionary)
    """

    try:
        with open(json_file, 'r') as config_file:
            config_dict = json.load(config_file)


        config = Bunch(config_dict)
    except OSError as e:
        print("OS error: {0}".format(e))
    except Exception as e:
        print("Unexpected error: ", sys.exec_info()[0])

    
    return config, config_dic

###############################################################################
def process_config(json_file):
    """

    :param json_file:
    "return: config
    """
    try: 
        config, _ = get_config_from_json(json_file)
        config.summary_dic = os.path.join("../experiments", config.exp_name, "summary/")
        config.checkpoint_dir = os.path.join("../experiments", config.exp_name, "checkpint/")
    except OSError as e:
        print("OS error: {0}".format(e))
    except Exception as e:
        print("Unexpected error: ", sys.exec_info()[0])

    return config
