# from datetime import datetime
# import locale


# def mes_ano_atual(request):
#     locale.setlocale(locale.LC_TIME, 'pt_BR')
#     data_atual = datetime.now()

    
#     mes_atual = data_atual.strftime('%B')
#     ano_atual = data_atual.strftime('%Y')  

#     mes_ano_formatado = f'{mes_atual.capitalize()} {ano_atual}'

#     return {'mes_ano_atual': mes_ano_formatado}