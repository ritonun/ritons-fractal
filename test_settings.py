import src.parameters


def test_config_read(config):
    if config['display']['width'] == "600":
        print('WIDTH: OK!')
    else:
        print('ERROR: width')
        return

    if config['fractal']['max_iter'] == "80":
        print('Max_iter: OK!')
    else:
        print('ERROR: max_iter')
        return


def test_modify_config(conf):
    conf.modify_settings('display', 'width', 0)
    config = conf.read_settings()
    if config['display']['width'] != "0":
        print('EROOR: width not modifiy')
    else:
        print('TEST OK!')


'''
conf = src.parameters.Config(filepath="data/settings.ini")
conf.write_default_settings()
config = conf.read_settings()
test_config_read(config)
test_modify_config(conf)
'''
