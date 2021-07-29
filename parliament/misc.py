import jsoncfg


def make_list(v):
    """
    If the object is not a list already, it converts it to one
    Examples:
    [1, 2, 3] -> [1, 2, 3]
    [1] -> [1]
    1 -> [1]
    """
    if not jsoncfg.node_is_array(v):
        if jsoncfg.node_is_scalar(v):
            location = jsoncfg.node_location(v)
            line = location.line
            column = location.column
        elif jsoncfg.node_exists(v):
            line = v.line
            column = v.column
        else:
            return []

        a = jsoncfg.config_classes.ConfigJSONArray(line, column)
        a._append(v)
        return a
    return v


def make_simple_list(v):
    """wrap a element in a list if it's not already a list, convert jsoncfg scalar and array values to list
    [1] -> [1]
    1 -> [1]
    jsoncfg_scalar(1,2) -> [1,2]
    jsoncfg_arr(1,2) -> [1,2]
    """

    if isinstance(v, list):
        return v
    else:
        return [v]


def value_from_jsoncfg_object(jsoncfg_object):
    # returns a list or a string
    if jsoncfg.node_is_scalar(jsoncfg_object) or jsoncfg.node_is_object(jsoncfg_object):
        return jsoncfg_object.value
    elif jsoncfg.node_is_array(jsoncfg_object):
        # recursively convert the jsoncfg_object to str or list
        result = []
        for ele in list(jsoncfg_object):
            result.append(value_from_jsoncfg_object(ele))
        return result
    else:
        # do nothing if jsoncfg_object is not a jsoncfg object
        return jsoncfg_object


def jsoncfg_to_dict(jsoncfg_object):
    if jsoncfg.node_is_scalar(jsoncfg_object):
        return jsoncfg_object.value
    elif jsoncfg.node_is_object(jsoncfg_object):
        return jsoncfg_to_dict(jsoncfg_object.value)
    elif jsoncfg.node_is_array(jsoncfg_object):
        # recursively convert the jsoncfg_object to str or list
        result = []
        for ele in list(jsoncfg_object):
            result.append(value_from_jsoncfg_object(ele))
        return result
    elif isinstance(jsoncfg_object, dict):
        d = {}
        for k in jsoncfg_object.keys():
            d[k] = jsoncfg_to_dict(jsoncfg_object[k])
        return d
    else:
        # do nothing and return argument
        return jsoncfg_object


class ACCESS_DECISION:
    IMPLICIT_DENY = 0
    EXPLICIT_DENY = 1
    EXPLICIT_ALLOW = 2
