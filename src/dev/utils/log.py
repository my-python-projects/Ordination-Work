from datetime import datetime

class Log:

    def escrever(self, texto):
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

        print('\n------------', data_e_hora_em_texto, ' ', texto)
