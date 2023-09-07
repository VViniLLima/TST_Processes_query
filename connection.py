from requests_html import HTMLSession
import time

class Connection:
  def create_session_object(self):
      session_object = HTMLSession()
      return  session_object
      
  def create_request_object(self, process_number_to_request):
      numeroTst,digitoTst,anoTst,orgaoTst,tribunalTst,varaTst = process_number_to_request
      request = self.create_session_object().get(f'https://consultaprocessual.tst.jus.br/consultaProcessual/consultaTstNumUnica.do?consulta=Consultar&conscsjt=&numeroTst={numeroTst}&digitoTst={digitoTst}&anoTst={anoTst}&orgaoTst={orgaoTst}&tribunalTst={tribunalTst}&varaTst={varaTst}&submit=Consultar')
      
      while not self.check_page_availability(request):
         print('Recapcha... Waiting 10s.')
         time.sleep(10)
         print('Trying again.')
         request = self.create_session_object().get(f'https://consultaprocessual.tst.jus.br/consultaProcessual/consultaTstNumUnica.do?consulta=Consultar&conscsjt=&numeroTst={numeroTst}&digitoTst={digitoTst}&anoTst={anoTst}&orgaoTst={orgaoTst}&tribunalTst={tribunalTst}&varaTst={varaTst}&submit=Consultar')
      
      print('Request OK.:')
      return request
      
  def check_page_availability(self, request):
    if not request.html.find('#googleRecaptcha'):
      return True
