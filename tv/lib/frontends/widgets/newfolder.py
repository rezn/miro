# Miro - an RSS based video player application
# Copyright (C) 2005, 2006, 2007, 2008, 2009, 2010, 2011
# Participatory Culture Foundation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
#
# In addition, as a special exception, the copyright holders give
# permission to link the code of portions of this program with the OpenSSL
# library.
#
# You must obey the GNU General Public License in all respects for all of
# the code used other than OpenSSL. If you modify file(s) with this
# exception, you may extend this exception to your version of the file(s),
# but you are not obligated to do so. If you do not wish to do so, delete
# this exception statement from your version. If you delete this exception
# statement from all source files in the program, then also delete it here.

"""miro.frontends.widgets.newfolder -- Holds dialog and processing
code for adding a new folder.
"""

from miro.gtcache import gettext as _

from miro.plat.frontends.widgets import widgetset
from miro.frontends.widgets.dialogs import MainDialog
from miro.dialogs import BUTTON_CANCEL, BUTTON_CREATE_FOLDER

import logging

def _run_dialog(title, description, default_type):
    """Creates and launches the New Folder dialog.  This dialog waits for
    the user to press "Create Folder" or "Cancel".

    Returns a the name, or None.
    """
    window = MainDialog(title, description)
    try:
        try:
            window.add_button(BUTTON_CREATE_FOLDER.text)
            window.add_button(BUTTON_CANCEL.text)

            extra = widgetset.VBox()

            lab = widgetset.Label(_('Folder name:'))
            name_entry = widgetset.TextEntry()
            name_entry.set_activates_default(True)

            h = widgetset.HBox()
            h.pack_start(lab, padding=5)
            h.pack_start(name_entry, expand=True)
            extra.pack_start(h, padding=5)

            window.set_extra_widget(extra)

            response = window.run()

            if response == 0:
                name = name_entry.get_text()
                if name:
                    return name

            return None

        except StandardError:
            logging.exception("newfeed threw exception.")
    finally:
        window.destroy()

def run_dialog(default_type):
    """Creates and launches the New Folder dialog.  This dialog waits for
    the user to press "Create Folder" or "Cancel".

    Returns the name, or None.
    """
    return _run_dialog(_('Create Podcast Folder'),
            _('Enter the name of the folder to add'), default_type)
