################################################################################
#
# Package   : AlphaPy
# Module    : utilities
# Created   : July 11, 2013
#
# Copyright 2017 ScottFree Analytics LLC
# Mark Conway & Robert D. Scott II
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################


#
# Imports
#

from alphapy.globals import PSEP, USEP

import argparse
from datetime import datetime
import inspect
from itertools import groupby
from os import listdir
from os.path import isfile, join
import re


#
# Function remove_list_items
#

def remove_list_items(elements, alist):
    r"""Remove one or more items from the given list.

    Parameters
    ----------
    elements : list
        The items to remove from the list ``alist``.
    alist : list
        Any object of any type can be a list item.

    Returns
    -------
    sublist : list
        The subset of items after removal.

    Examples
    --------

    >>> test_list = ['a', 'b', 'c', test_func]
    >>> remove_list_items([test_func], test_list)  # ['a', 'b', 'c']

    """
    sublist = [x for x in alist if x not in elements]
    return sublist


#
# Function subtract_days
#

def subtract_days(date_string, ndays):
    r"""Subtract a number of days from a given date.

    Parameters
    ----------
    date_string : str
        An alphanumeric string in the format %Y-%m-%d.
    ndays : int
        Number of days to subtract.

    Returns
    -------
    new_date_string : str
        The adjusted date string in the format %Y-%m-%d.

    Examples
    --------

    >>> subtract_days('2017-11-10', 31)   # '2017-10-10'

    """
    new_date_string = None
    valid = valid_date(date_string)
    if valid:
        date_dt = datetime.strptime(date_string, "%Y-%m-%d")
        new_date = date_dt - timedelta(days=ndays)
        new_date_string = new_date.strftime("%Y-%m-%d")
    return new_date_string


#
# Function valid_date
#

def valid_date(date_string):
    r"""Determine whether or not the given string is a valid date.

    Parameters
    ----------
    date_string : str
        An alphanumeric string in the format %Y-%m-%d.

    Returns
    -------
    valid : bool
        ``True`` if the given date is valid.

    Raises
    ------
    ValueError
        Not a valid date.

    Examples
    --------

    >>> valid_date('2016-7-1')   # datetime.datetime(2016, 7, 1, 0, 0)
    >>> valid_date('345')        # ValueError: Not a valid date

    """
    valid = False
    try:
        date_time = datetime.strptime(date_string, "%Y-%m-%d")
        valid = True
    except:
        message = "Not a valid date: '{0}'.".format(date_string)
        raise argparse.ArgumentTypeError(message)
    return valid


#
# Function valid_name
#

def valid_name(name):
    r"""Determine whether or not the given string is a valid
    alphanumeric string.

    Parameters
    ----------
    name : str
        An alphanumeric identifier.

    Returns
    -------
    result : bool
        ``True`` if the name is valid, else ``False``.

    Examples
    --------

    >>> valid_name('alpha')   # True
    >>> valid_name('!alpha')  # False

    """
    identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
    result = re.match(identifier, name)
    return result is not None
