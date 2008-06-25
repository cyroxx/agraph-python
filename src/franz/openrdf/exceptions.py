#!/usr/bin/env python
# -*- coding: utf-8 -*-

##***** BEGIN LICENSE BLOCK *****
##Version: MPL 1.1
##
##The contents of this file are subject to the Mozilla Public License Version
##1.1 (the "License"); you may not use this file except in compliance with
##the License. You may obtain a copy of the License at
##http:##www.mozilla.org/MPL/
##
##Software distributed under the License is distributed on an "AS IS" basis,
##WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
##for the specific language governing rights and limitations under the
##License.
##
##The Original Code is the AllegroGraph Java Client interface.
##
##The Original Code was written by Franz Inc.
##Copyright (C) 2006 Franz Inc.  All Rights Reserved.
##
##***** END LICENSE BLOCK *****

class IllegalOptionException(Exception):
    pass

class IllegalArgumentException (Exception):
    pass

class InitializationException(Exception):
    pass

class UnimplementedMethodException(Exception):
    pass


class IllegalStateException (Exception):
    pass

class AllegroGraphException (Exception):
    pass

class IOException (Exception):
    pass

class InterruptedException (Exception):
    pass

class ConnectException(Exception):
    pass

class BadnessException(Exception):
    """
    General badness with no explanation.
    """
    pass

class JDBCException(Exception):
    """
    Exception during iterator over a JDBC ResultSet
    """
    pass

#class NiceException(Exception):
#    pass
#
#class RuntimeException(Exception):
#    pass
#
#class FakeException(Exception):
#    pass