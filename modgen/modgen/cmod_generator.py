from .mod_generator import ModGenerator


class CModGenerator(ModGenerator):

    def generate(self):
        print('Creating C module')
        self.generate_h_file()
        self.generate_c_file()

    def generate_h_file(self):
        h_file_name = '{}.h'.format(self.module_name)
        print('Generating "{}"'.format(h_file_name))
        with open(h_file_name, 'w') as f:
            for line in self.parse_template_iterator():
                f.write(line)

    def generate_c_file(self):
        print('Generating "{}.c"'.format(self.module_name))

