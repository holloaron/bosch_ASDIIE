**SegmentFault coding protocol**
______________________________

Git commit message format

	TAG: filemane.extension - message

      TAG: ADD; CHD; RMV
	
______________________________

Names

	- classes:
		every first letter is capital, no spaces
        (FirstClass)
    
	- variables, functions:
		everithing is lowcase, space = _
        (my_variable, some_function)

______________________________

Files

	One file holds only one class. (there can be some exceptions: Enums, ...)
  
	The header of every file:

```
"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : (...)
AUTHOR       : (...)
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
(...)

********************************************************************
********************************************************************
"""
```
	
	IMPORTS:
		1. third party libraries
		2. our files and libraries
    

	FUNCTIONS:
      - use typehints
      - use docstring
      - 1 linebreak before incode comment 
      - 1 linebreak before return
      - 2 linebreaks between every function
  
```
def xyz_func(number: int, name: str) -> [return type]
    """ docstring

    @args:
        var_name [type] - description
    @return:
        var_name [type] - description
    """

    # incode comment
    code ...
    
    return ...
```
