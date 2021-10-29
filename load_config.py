import yaml
import json


def yaml_to_dicto(yaml_file):
    with open(yaml_file, 'r') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    return cfg

# Turns a dictionary into a class in case you prefer it this way
class Dict2Class:
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])

# just another way to convert dicto into class (only the first keys)
class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def yaml_to_class(yaml_file):
    cfg = yaml_to_dicto(yaml_file)
    cfg = Struct(**cfg)
    return cfg


if __name__=='__main__':
    yaml_file = './yaml_example.yaml'
    cfg = yaml_to_dicto(yaml_file)
    print('\ncfg: ', json.dumps(cfg, indent=2))
    cfg_2 = Dict2Class(cfg)
    print('\nclass cfg: ', cfg_2)
    print('\nclass cfg dicto parsed json: ', json.dumps(cfg_2.__dict__, indent=2))
    print('\ncfg_2.BACKBONE', cfg_2.HYPERPARAMETERS)
    print('\ncfg hypers:', cfg['HYPERPARAMETERS'])

    # https://stackoverflow.com/questions/6866600/how-to-parse-read-a-yaml-file-into-a-python-object
    s = Struct(**cfg)
    print("s: ", s.__dict__)
    print('..', type(cfg_2.HYPERPARAMETERS), type(s.HYPERPARAMETERS))

    cfg_class = yaml_to_class(yaml_file)

    print("\ncfg_class: " , type(cfg_class.__dict__))
    print("cfg_class: ", cfg_class.__dict__)


