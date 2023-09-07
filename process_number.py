
class Process:
    def process_input_to_list(self, process_input):
        return [p for p in process_input.replace(' ', '').split(',') ]


    def process_number_to_parts(self, numero_do_processo):
        numeroTst = numero_do_processo.split('-')[0]
        digitoTst,anoTst,orgaoTst,tribunalTst,varaTst = numero_do_processo.split('-')[1].split('.')
        return numeroTst,digitoTst,anoTst,orgaoTst,tribunalTst,varaTst