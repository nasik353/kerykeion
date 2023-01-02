"""
    This is part of Kerykeion (C) 2022 Giacomo Battaglia
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class KerykeionException(Exception):
    """
    Custom Kerykeion Exception
    """

    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
