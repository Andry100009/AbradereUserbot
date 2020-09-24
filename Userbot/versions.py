# Copyright © 2020 di @Abradere Github, <https://github.com/Andry100009>.
#
# Questi file sono per il progetto <https://github.com/Andry100009/AbradereUserbot>,
# Vengono pubblicati con la licenza "Licenza GNU Affero General Public v3.0".
# Si prega di leggere la licenza su <https://github.com/Andry100009/AbradereUserbot/blob/master/LICENSE>
#
# Tutti i diritti riservati sono riservati all'autore @Abradere.

import sys


__version_mjaor__ = 2
__version_minor__ = 1
__version_micro__ = 0
__version_beta__ = 1

__version__ = "{}.{}.{}".format(__version_mjaor__,
                                __version_minor__,
                                f"{__version_micro__}-beta.{__version_beta__}" \
                                    if __version_beta__ else __version_micro__)

__license__ = "[Licenza AGPL-3.0]" + \
                "(https://github.com/Andry100009/AbradereUserbot/blob/master/LICENSE)"

__copyright__ = "© 2020 dev [Andry100009](https://github.com/Andry100009)"

__python_version__ = "{}.{}.{}".format(sys.version_info[0],
                                       sys.version_info[1], 
                                       sys.version_info[2])
