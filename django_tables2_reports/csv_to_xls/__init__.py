# -*- coding: utf-8 -*-
# Copyright (c) 2012-2013 by Pablo Martín <goinnn@gmail.com>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.


def convert_to_excel(response, excel_support, encoding='utf-8', title_sheet='Sheet 1'):
    if excel_support == 'xlwt':
        from .xlwt_converter import convert_to_excel as convert_to_excel_xlwt
        convert_to_excel_xlwt(response,
                              encoding=encoding,
                              title_sheet=title_sheet)
    elif excel_support == 'pyexcelerator':
        from .pyexcelerator_converter import convert_to_excel as convert_to_excel_pyexcelerator
        convert_to_excel_pyexcelerator(response,
                                       encoding=encoding,
                                       title_sheet=title_sheet)
    elif excel_support == 'openpyxl':
        from .openpyxl_converter import convert_to_excel as convert_to_excel_openpyxl
        convert_to_excel_openpyxl(response,
                                  encoding=encoding,
                                  title_sheet=title_sheet)
    else:
        raise RuntimeError("No support for xls generation available")
