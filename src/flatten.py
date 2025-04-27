class SoloListasError(Exception):
    """Custom exception for non-flattenable elements encountered"""
    pass

def list_flattener(input_list):
    """
    Flatten a nested structure including lists, tuples, and dictionaries.
    For dictionaries, both keys and values are added to the flattened list.
    
    Args:
        input_list: The structure to flatten
        
    Returns:
        A flattened list containing all atomic elements
        
    Raises:
        SoloListasError: If any element is not flattenable (customizable based on needs)
    """
    flattened = []
    for item in input_list:
        if isinstance(item, (list, tuple)):
            flattened.extend(list_flattener(item))
        elif isinstance(item, dict):
            # For dictionaries, we flatten both keys and values
            flattened.extend(list_flattener(list(item.items())))
        elif isinstance(item, (int, float, str, bool)) or item is None:
            flattened.append(item)
        else:
            raise SoloListasError(f"Unsupported type for flattening: {type(item)}")
    return flattened