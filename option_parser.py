from optparse import OptionParser
import traceback
from errors import OptionParserError

class OptParser:
    @classmethod
    def parseopts(self):
        try:
            parser = OptionParser(usage = "Arguments for Free Work")

            parser.add_option("-u", "--user", action = "store",
                                                 type = "string",
                                                 help = "Username",
                                                 dest = "username",
                             )

            parser.add_option("-p", "--password", action = "store",
                                                 type = "string",
                                                 help = "Passowrd for user",
                                                 dest = "password",
                             )
            try:
                (options, args) = parser.parse_args()
            except:
                raise OptionParserError

            if not options.username or not options.password :
                raise ValueError('Username and password are mandatory.')

            if options.username and options.password:
                kwargs = {
                    "username": options.username,
                    "password": options.password,
                }
                return kwargs
            raise OptionParserError('There is some unknown erros \n') # code should never reach this line.

        except OptionParserError:
            raise OptionParserError('Type -h for help \n\t %s' % USAGE)
        except:
            raise OptionParserError(traceback.format_exc())
