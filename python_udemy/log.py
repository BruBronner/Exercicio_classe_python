#abstração
#herança
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self,msg):
        raise NotImplementedError('implemente o metodo log')

    def Log_error(self,msg):
        return self._log(f'Error: {msg}')

    def Log_sucess(self,msg):
        return self._log(f'Sucess: {msg}')



class LogFileMixin(Log):
    def _log(self,msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('salvando no log...', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self,msg):
        print(f'{msg} (0veio do print)')


if __name__ == "__main__":
    l = LogPrintMixin()
    #print(l.Log_error('qualquer coisa'))
    #print(l.Log_sucess('que legal'))
lf = LogFileMixin()
lf.Log_error('qualquer coisa')
lf.Log_sucess('Que legal')