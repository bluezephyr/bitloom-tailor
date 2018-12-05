import abc
import re


class Variable(object):
    def __init__(self, name, config):
        self.name = name
        self.config = config

    def __str__(self):
        variables = self.config.values['variables']
        result = ''

        try:
            result = variables[self.name]
        except KeyError:
            print('{} not defined'.format(self.name))

        return result


class ModGenerator(metaclass=abc.ABCMeta):

    def __init__(self, module_name, template, config):
        self.module_name = module_name
        self.template = template
        self.config = config

    @abc.abstractmethod
    def generate(self):
        pass

    def parse_template_iterator(self):
        """
        Parse the template file and return the lines in the file one by one
        with all the variables replaced with appropriate strings.
        """
        with open(self.template, 'r') as f:
            for line in f:
                token_list = self._parse_line(line)
                modified_line = ''.join([str(x) for x in token_list])
                yield modified_line

    def _parse_line(self, line):
        """
        This function parses one line in the template file and finds all
        variables.  A list is created that contains strings and variables.
        """
        token_list = []
        current_pos = 0

        for item in re.finditer(r'\${(.*?)}', line):
            token_list.append(line[current_pos:item.start()])
            current_pos = item.end()
            variable = Variable(item.group(1), self.config)
            token_list.append(variable)

        token_list.append(line[current_pos:])

        return token_list


