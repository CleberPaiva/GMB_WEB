from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from arma.models import Arma
from django.db.models import Q


@login_required
def relatorio(request):
    return render(request, 'gerencia/relatorio.html')


@login_required
def menu(request):
    armas_apx = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX').count()
    armas_th9 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9').count()
    armas_pt940 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940').count()
    armas_pt840 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840').count()
    armas_pt100 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT100PLUS').count()
    armas_apx_rg01 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX')\
        .filter(regional='SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS').count()
    armas_th9_rg01 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9')\
        .filter(regional='SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS').count()
    armas_pt100_rg01 = Arma.objects.filter(
        regional='SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS')\
        .filter(Q(modelo='PT100') | Q(modelo='PT100PLUS'))\
        .filter(Q(tipo='INDIVIDUAL') | Q(tipo='INSTITUCIONAL')).count()
    armas_pt940_rg01 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940')\
        .filter(regional='SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS').count()
    armas_pt840_rg01 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840')\
        .filter(regional='SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS').count()
    armas_cal12_rg01 = Arma.objects.filter(especie='Espingarda')\
        .filter(regional='SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS').count()
    armas_ctt_rg01 = Arma.objects.filter(especie='Carabina')\
        .filter(regional='SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS').count()
    armas_fuzil_rg01 = Arma.objects.filter(especie='Fuzil / Carabina')\
        .filter(regional='SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS').count()
    armas_apx_rg02 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX')\
        .filter(regional='SR02 - SUPERINTENDÊNCIA REGIONAL SUL').count() 
    armas_th9_rg02 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9')\
        .filter(regional='SR02 - SUPERINTENDÊNCIA REGIONAL SUL').count()
    armas_pt100_rg02 = Arma.objects.filter(
        regional='SR02 - SUPERINTENDÊNCIA REGIONAL SUL')\
        .filter(Q(modelo='PT100') | Q(modelo='PT100PLUS'))\
        .filter(Q(tipo='INDIVIDUAL') | Q(tipo='INSTITUCIONAL')).count()
    armas_pt940_rg02 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940')\
        .filter(regional='SR02 - SUPERINTENDÊNCIA REGIONAL SUL').count()
    armas_pt840_rg02 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840')\
        .filter(regional='SR02 - SUPERINTENDÊNCIA REGIONAL SUL').count()
    armas_cal12_rg02 = Arma.objects.filter(especie='Espingarda')\
        .filter(regional='SR02 - SUPERINTENDÊNCIA REGIONAL SUL').count()
    armas_ctt_rg02 = Arma.objects.filter(especie='Carabina')\
        .filter(regional='SR02 - SUPERINTENDÊNCIA REGIONAL SUL').count()
    armas_fuzil_rg02 = Arma.objects.filter(especie='Fuzil / Carabina')\
        .filter(regional='SR02 - SUPERINTENDÊNCIA REGIONAL SUL').count()   
    armas_apx_rg03 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX')\
        .filter(regional='SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE').count() 
    armas_th9_rg03 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9')\
        .filter(regional='SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE').count()
    armas_pt100_rg03 = Arma.objects.filter(
        regional='SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE')\
            .filter(Q(modelo='PT100') | Q(modelo='PT100PLUS'))\
            .filter(Q(tipo='INDIVIDUAL') | Q(tipo='INSTITUCIONAL')).count()
    armas_pt940_rg03 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940')\
        .filter(regional='SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE').count()
    armas_pt840_rg03 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840')\
        .filter(regional='SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE').count()
    armas_cal12_rg03 = Arma.objects.filter(especie='Espingarda')\
        .filter(regional='SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE').count()
    armas_ctt_rg03 = Arma.objects.filter(especie='Carabina')\
        .filter(regional='SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE').count()
    armas_fuzil_rg03 = Arma.objects.filter(especie='Fuzil / Carabina')\
        .filter(regional='SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE').count()  
    armas_apx_rg04 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX')\
        .filter(regional='SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ').count() 
    armas_th9_rg04 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9')\
        .filter(regional='SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ').count()
    armas_pt100_rg04 = Arma.objects.filter(
        regional='SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ')\
        .filter(Q(modelo='PT100') | Q(modelo='PT100PLUS'))\
        .filter(Q(tipo='INDIVIDUAL') | Q(tipo='INSTITUCIONAL')).count()
    armas_pt940_rg04 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940')\
        .filter(regional='SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ').count()
    armas_pt840_rg04 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840')\
        .filter(regional='SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ').count()
    armas_cal12_rg04 = Arma.objects.filter(especie='Espingarda')\
        .filter(regional='SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ').count()
    armas_ctt_rg04 = Arma.objects.filter(especie='Carabina')\
        .filter(regional='SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ').count()
    armas_fuzil_rg04 = Arma.objects.filter(especie='Fuzil / Carabina')\
        .filter(regional='SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ').count()  
    armas_apx_rg05 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX')\
        .filter(regional='SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA').count() 
    armas_th9_rg05 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9')\
        .filter(regional='SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA').count()
    armas_pt100_rg05 = Arma.objects.filter(
        regional='SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA')\
        .filter(Q(modelo='PT100') | Q(modelo='PT100PLUS'))\
        .filter(Q(tipo='INDIVIDUAL') | Q(tipo='INSTITUCIONAL')).count()
    armas_pt940_rg05 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940')\
        .filter(regional='SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA').count()
    armas_pt840_rg05 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840')\
        .filter(regional='SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA').count()
    armas_cal12_rg05 = Arma.objects.filter(especie='Espingarda')\
        .filter(regional='SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA').count()
    armas_ctt_rg05 = Arma.objects.filter(especie='Carabina')\
        .filter(regional='SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA').count()
    armas_fuzil_rg05 = Arma.objects.filter(especie='Fuzil / Carabina')\
        .filter(regional='SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA').count()  
    armas_apx_rg06 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX')\
        .filter(regional='SR06 - SUPERINTENDÊNCIA REGIONAL OESTE').count() 
    armas_th9_rg06 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9')\
        .filter(regional='SR06 - SUPERINTENDÊNCIA REGIONAL OESTE').count()
    armas_pt100_rg06 = Arma.objects.filter(
        regional='SR06 - SUPERINTENDÊNCIA REGIONAL OESTE')\
        .filter(Q(modelo='PT100') | Q(modelo='PT100PLUS'))\
        .filter(Q(tipo='INDIVIDUAL') | Q(tipo='INSTITUCIONAL')).count()
    armas_pt940_rg06 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940')\
        .filter(regional='SR06 - SUPERINTENDÊNCIA REGIONAL OESTE').count()
    armas_pt840_rg06 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840')\
        .filter(regional='SR06 - SUPERINTENDÊNCIA REGIONAL OESTE').count()
    armas_cal12_rg06 = Arma.objects.filter(especie='Espingarda')\
        .filter(regional='SR06 - SUPERINTENDÊNCIA REGIONAL OESTE').count()
    armas_ctt_rg06 = Arma.objects.filter(especie='Carabina')\
        .filter(regional='SR06 - SUPERINTENDÊNCIA REGIONAL OESTE').count()
    armas_fuzil_rg06 = Arma.objects.filter(especie='Fuzil / Carabina')\
        .filter(regional='SR06 - SUPERINTENDÊNCIA REGIONAL OESTE').count()  
    armas_apx_rg07 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX')\
        .filter(regional='SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ').count() 
    armas_th9_rg07 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9')\
        .filter(regional='SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ').count()
    armas_pt100_rg07 = Arma.objects.filter(
        regional='SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ')\
        .filter(Q(modelo='PT100') | Q(modelo='PT100PLUS'))\
        .filter(Q(tipo='INDIVIDUAL') | Q(tipo='INSTITUCIONAL')).count()
    armas_pt940_rg07 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940')\
        .filter(regional='SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ').count()
    armas_pt840_rg07 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840')\
        .filter(regional='SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ').count()
    armas_cal12_rg07 = Arma.objects.filter(especie='Espingarda')\
        .filter(regional='SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ').count()
    armas_ctt_rg07 = Arma.objects.filter(especie='Carabina')\
        .filter(regional='SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ').count()
    armas_fuzil_rg07 = Arma.objects.filter(especie='Fuzil / Carabina')\
        .filter(regional='SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ').count() 
    armas_apx_rg08 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='APX')\
        .filter(regional='SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE').count() 
    armas_th9_rg08 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='TH9')\
        .filter(regional='SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE').count()
    armas_pt100_rg08 = Arma.objects.filter(
        regional='SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE')\
        .filter(Q(modelo='PT100') | Q(modelo='PT100PLUS'))\
        .filter(Q(tipo='INDIVIDUAL') | Q(tipo='INSTITUCIONAL')).count()
    armas_pt940_rg08 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT940')\
        .filter(regional='SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE').count()
    armas_pt840_rg08 = Arma.objects.filter(
        tipo='INDIVIDUAL')\
        .filter(modelo='PT840')\
        .filter(regional='SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE').count()
    armas_cal12_rg08 = Arma.objects.filter(especie='Espingarda')\
        .filter(regional='SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE').count()
    armas_ctt_rg08 = Arma.objects.filter(especie='Carabina')\
        .filter(regional='SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE').count()
    armas_fuzil_rg08 = Arma.objects.filter(especie='Fuzil / Carabina')\
        .filter(regional='SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE').count()               
    armas_sem_arma = 384
    return render(request, 'gerencia/menu.html', {'armas_apx': armas_apx,
                                                  'armas_th9': armas_th9,
                                                  'armas_pt940': armas_pt940,
                                                  'armas_pt840': armas_pt840,
                                                  'armas_pt100': armas_pt100,
                                                  'armas_apx_rg01': armas_apx_rg01,
                                                  'armas_th9_rg01': armas_th9_rg01,
                                                  'armas_pt940_rg01': armas_pt940_rg01,
                                                  'armas_pt840_rg01': armas_pt840_rg01,
                                                  'armas_pt100_rg01': armas_pt100_rg01,
                                                  'armas_cal12_rg01': armas_cal12_rg01,
                                                  'armas_ctt_rg01': armas_ctt_rg01,
                                                  'armas_fuzil_rg01': armas_fuzil_rg01,
                                                  'armas_apx_rg02': armas_apx_rg02,
                                                  'armas_th9_rg02': armas_th9_rg02,
                                                  'armas_pt940_rg02': armas_pt940_rg02,
                                                  'armas_pt840_rg02': armas_pt840_rg02,
                                                  'armas_pt100_rg02': armas_pt100_rg02,
                                                  'armas_cal12_rg02': armas_cal12_rg02,
                                                  'armas_ctt_rg02': armas_ctt_rg02,
                                                  'armas_fuzil_rg02': armas_fuzil_rg02,
                                                  'armas_apx_rg03': armas_apx_rg03,
                                                  'armas_th9_rg03': armas_th9_rg03,
                                                  'armas_pt940_rg03': armas_pt940_rg03,
                                                  'armas_pt840_rg03': armas_pt840_rg03,
                                                  'armas_pt100_rg03': armas_pt100_rg03,
                                                  'armas_cal12_rg03': armas_cal12_rg03,
                                                  'armas_ctt_rg03': armas_ctt_rg03,
                                                  'armas_fuzil_rg03': armas_fuzil_rg03,
                                                  'armas_apx_rg04': armas_apx_rg04,
                                                  'armas_th9_rg04': armas_th9_rg04,
                                                  'armas_pt940_rg04': armas_pt940_rg04,
                                                  'armas_pt840_rg04': armas_pt840_rg04,
                                                  'armas_pt100_rg04': armas_pt100_rg04,
                                                  'armas_cal12_rg04': armas_cal12_rg04,
                                                  'armas_ctt_rg04': armas_ctt_rg04,
                                                  'armas_fuzil_rg04': armas_fuzil_rg04,
                                                  'armas_apx_rg05': armas_apx_rg05,
                                                  'armas_th9_rg05': armas_th9_rg05,
                                                  'armas_pt940_rg05': armas_pt940_rg05,
                                                  'armas_pt840_rg05': armas_pt840_rg05,
                                                  'armas_pt100_rg05': armas_pt100_rg05,
                                                  'armas_cal12_rg05': armas_cal12_rg05,
                                                  'armas_ctt_rg05': armas_ctt_rg05,
                                                  'armas_fuzil_rg05': armas_fuzil_rg05,
                                                  'armas_apx_rg06': armas_apx_rg06,
                                                  'armas_th9_rg06': armas_th9_rg06,
                                                  'armas_pt940_rg06': armas_pt940_rg06,
                                                  'armas_pt840_rg06': armas_pt840_rg06,
                                                  'armas_pt100_rg06': armas_pt100_rg06,
                                                  'armas_cal12_rg06': armas_cal12_rg06,
                                                  'armas_ctt_rg06': armas_ctt_rg06,
                                                  'armas_fuzil_rg06': armas_fuzil_rg06,
                                                  'armas_apx_rg07': armas_apx_rg07,
                                                  'armas_th9_rg07': armas_th9_rg07,
                                                  'armas_pt940_rg07': armas_pt940_rg07,
                                                  'armas_pt840_rg07': armas_pt840_rg07,
                                                  'armas_pt100_rg07': armas_pt100_rg07,
                                                  'armas_cal12_rg07': armas_cal12_rg07,
                                                  'armas_ctt_rg07': armas_ctt_rg07,
                                                  'armas_fuzil_rg07': armas_fuzil_rg07,
                                                  'armas_apx_rg08': armas_apx_rg08,
                                                  'armas_th9_rg08': armas_th9_rg08,
                                                  'armas_pt940_rg08': armas_pt940_rg08,
                                                  'armas_pt840_rg08': armas_pt840_rg08,
                                                  'armas_pt100_rg08': armas_pt100_rg08,
                                                  'armas_cal12_rg08': armas_cal12_rg08,
                                                  'armas_ctt_rg08': armas_ctt_rg08,
                                                  'armas_fuzil_rg08': armas_fuzil_rg08,
                                                  'armas_sem_arma': armas_sem_arma,})


@login_required
def sr01(request):
    regional = "SR01 - SUPERINTENDÊNCIA REGIONAL DA GRANDE FLORIANÓPOLIS"
    armas = Arma.objects.filter(regional=regional).count()
    armas_institucional = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL').count()
    armas_individual = Arma.objects.filter(regional=regional)\
        .filter(tipo='INDIVIDUAL').count()
    armas_pistola = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='COPE - COMPLEXO PENITENCIÁRIO DO ESTADO')\
        .filter(especie='pistola').count()
    armas_espingarda = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='COPE - COMPLEXO PENITENCIÁRIO DO ESTADO')\
        .filter(especie='espingarda').count()
    armas_pistola_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='pistola').count()
    armas_espingarda_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='espingarda').count()
    armas_carabina_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='carabina').count()
    armas_fuzil_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_t2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_carabina = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='COPE - COMPLEXO PENITENCIÁRIO DO ESTADO')\
        .filter(especie='carabina').count()
    armas_fuzil = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='COPE - COMPLEXO PENITENCIÁRIO DO ESTADO')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='COPE - COMPLEXO PENITENCIÁRIO DO ESTADO')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_pistola2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRA DE FLORIANÓPOLIS')\
        .filter(especie='pistola').count()
    armas_espingarda2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRA DE FLORIANÓPOLIS')\
        .filter(especie='espingarda').count()
    armas_carabina2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRA DE FLORIANÓPOLIS')\
        .filter(especie='carabina').count()
    armas_fuzil2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRA DE FLORIANÓPOLIS')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil2_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRA DE FLORIANÓPOLIS')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    return render(request, 'gerencia/sr01.html', {'armas': armas,
                                                  'armas_institucional': armas_institucional,
                                                  'armas_individual': armas_individual,
                                                  'armas_pistola_t': armas_pistola_t,
                                                  'armas_espingarda_t': armas_espingarda_t,
                                                  'armas_carabina_t': armas_carabina_t,
                                                  'armas_fuzil_t': armas_fuzil_t,
                                                  'armas_fuzil_t2': armas_fuzil_t2,
                                                  'armas_pistola': armas_pistola,
                                                  'armas_espingarda': armas_espingarda,
                                                  'armas_carabina': armas_carabina,
                                                  'armas_fuzil': armas_fuzil,
                                                  'armas_fuzil_7': armas_fuzil_7,
                                                  'armas_pistola2': armas_pistola2,
                                                  'armas_espingarda2': armas_espingarda2,
                                                  'armas_carabina2': armas_carabina2,
                                                  'armas_fuzil2': armas_fuzil2,
                                                  'armas_fuzil2_7': armas_fuzil2_7})

@login_required
def sr02(request):
    regional = "SR02 - SUPERINTENDÊNCIA REGIONAL SUL"
    armas = Arma.objects.filter(regional=regional).count()
    armas_institucional = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL').count()
    armas_individual = Arma.objects.filter(regional=regional)\
        .filter(tipo='INDIVIDUAL').count()
    armas_pistola = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA SUL')\
        .filter(especie='pistola').count()
    armas_espingarda = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA SUL')\
        .filter(especie='espingarda').count()
    armas_pistola_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='pistola').count()
    armas_espingarda_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='espingarda').count()
    armas_carabina_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='carabina').count()
    armas_fuzil_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_t2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_carabina = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA SUL')\
        .filter(especie='carabina').count()
    armas_fuzil = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA SUL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA SUL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_pistola2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE CRICIÚMA')\
        .filter(especie='pistola').count()
    armas_espingarda2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE CRICIÚMA')\
        .filter(especie='espingarda').count()
    armas_carabina2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE CRICIÚMA')\
        .filter(especie='carabina').count()
    armas_fuzil2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE CRICIÚMA')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil2_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE CRICIÚMA')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    return render(request, 'gerencia/sr02.html', {'armas': armas,
                                                  'armas_institucional': armas_institucional,
                                                  'armas_individual': armas_individual,
                                                  'armas_pistola_t': armas_pistola_t,
                                                  'armas_espingarda_t': armas_espingarda_t,
                                                  'armas_carabina_t': armas_carabina_t,
                                                  'armas_fuzil_t': armas_fuzil_t,
                                                  'armas_fuzil_t2': armas_fuzil_t2,
                                                  'armas_pistola': armas_pistola,
                                                  'armas_espingarda': armas_espingarda,
                                                  'armas_carabina': armas_carabina,
                                                  'armas_fuzil': armas_fuzil,
                                                  'armas_fuzil_7': armas_fuzil_7,
                                                  'armas_pistola2': armas_pistola2,
                                                  'armas_espingarda2': armas_espingarda2,
                                                  'armas_carabina2': armas_carabina2,
                                                  'armas_fuzil2': armas_fuzil2,
                                                  'armas_fuzil2_7': armas_fuzil2_7})


@login_required
def sr03(request):
    regional = "SR03 - SUPERINTENDÊNCIA REGIONAL DO NORTE CATARINENSE"
    armas = Arma.objects.filter(regional=regional).count()
    armas_institucional = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL').count()
    armas_individual = Arma.objects.filter(regional=regional)\
        .filter(tipo='INDIVIDUAL').count()
    armas_pistola = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE JOINVILLE')\
        .filter(especie='pistola').count()
    armas_espingarda = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE JOINVILLE')\
        .filter(especie='espingarda').count()
    armas_pistola_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='pistola').count()
    armas_espingarda_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='espingarda').count()
    armas_carabina_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='carabina').count()
    armas_fuzil_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_t2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_carabina = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE JOINVILLE')\
        .filter(especie='carabina').count()
    armas_fuzil = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE JOINVILLE')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE JOINVILLE')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_pistola2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JOINVILLE')\
        .filter(especie='pistola').count()
    armas_espingarda2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JOINVILLE')\
        .filter(especie='espingarda').count()
    armas_carabina2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JOINVILLE')\
        .filter(especie='carabina').count()
    armas_fuzil2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JOINVILLE')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil2_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JOINVILLE')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    return render(request, 'gerencia/sr03.html', {'armas': armas,
                                                  'armas_institucional': armas_institucional,
                                                  'armas_individual': armas_individual,
                                                  'armas_pistola_t': armas_pistola_t,
                                                  'armas_espingarda_t': armas_espingarda_t,
                                                  'armas_carabina_t': armas_carabina_t,
                                                  'armas_fuzil_t': armas_fuzil_t,
                                                  'armas_fuzil_t2': armas_fuzil_t2,
                                                  'armas_pistola': armas_pistola,
                                                  'armas_espingarda': armas_espingarda,
                                                  'armas_carabina': armas_carabina,
                                                  'armas_fuzil': armas_fuzil,
                                                  'armas_fuzil_7': armas_fuzil_7,
                                                  'armas_pistola2': armas_pistola2,
                                                  'armas_espingarda2': armas_espingarda2,
                                                  'armas_carabina2': armas_carabina2,
                                                  'armas_fuzil2': armas_fuzil2,
                                                  'armas_fuzil2_7': armas_fuzil2_7})


@login_required
def sr04(request):
    regional = "SR04 - SUPERINTENDÊNCIA REGIONAL DO VALE DO ITAJAÍ"
    armas = Arma.objects.filter(regional=regional).count()
    armas_institucional = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL').count()
    armas_individual = Arma.objects.filter(regional=regional)\
        .filter(tipo='INDIVIDUAL').count()
    armas_pistola = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA DE ITAJAÍ')\
        .filter(especie='pistola').count()
    armas_espingarda = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA DE ITAJAÍ')\
        .filter(especie='espingarda').count()
    armas_pistola_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='pistola').count()
    armas_espingarda_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='espingarda').count()
    armas_carabina_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='carabina').count()
    armas_fuzil_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_t2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_carabina = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA DE ITAJAÍ')\
        .filter(especie='carabina').count()
    armas_fuzil = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA DE ITAJAÍ')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA DE ITAJAÍ')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_pistola2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE ITAJAÍ')\
        .filter(especie='pistola').count()
    armas_espingarda2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE ITAJAÍ')\
        .filter(especie='espingarda').count()
    armas_carabina2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE ITAJAÍ')\
        .filter(especie='carabina').count()
    armas_fuzil2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE ITAJAÍ')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil2_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO REGIONAL DE ITAJAÍ')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    return render(request, 'gerencia/sr04.html', {'armas': armas,
                                                  'armas_institucional': armas_institucional,
                                                  'armas_individual': armas_individual,
                                                  'armas_pistola_t': armas_pistola_t,
                                                  'armas_espingarda_t': armas_espingarda_t,
                                                  'armas_carabina_t': armas_carabina_t,
                                                  'armas_fuzil_t': armas_fuzil_t,
                                                  'armas_fuzil_t2': armas_fuzil_t2,
                                                  'armas_pistola': armas_pistola,
                                                  'armas_espingarda': armas_espingarda,
                                                  'armas_carabina': armas_carabina,
                                                  'armas_fuzil': armas_fuzil,
                                                  'armas_fuzil_7': armas_fuzil_7,
                                                  'armas_pistola2': armas_pistola2,
                                                  'armas_espingarda2': armas_espingarda2,
                                                  'armas_carabina2': armas_carabina2,
                                                  'armas_fuzil2': armas_fuzil2,
                                                  'armas_fuzil2_7': armas_fuzil2_7})


@login_required
def sr05(request):
    regional = "SR05 - SUPERINTENDÊNCIA REGIONAL SERRANA"
    armas = Arma.objects.filter(regional=regional).count()
    armas_institucional = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL').count()
    armas_individual = Arma.objects.filter(regional=regional)\
        .filter(tipo='INDIVIDUAL').count()
    armas_pistola = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA REGIONAL DE CURITIBANOS')\
        .filter(especie='pistola').count()
    armas_espingarda = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA REGIONAL DE CURITIBANOS')\
        .filter(especie='espingarda').count()
    armas_pistola_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='pistola').count()
    armas_espingarda_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='espingarda').count()
    armas_carabina_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='carabina').count()
    armas_fuzil_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_t2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_carabina = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA REGIONAL DE CURITIBANOS')\
        .filter(especie='carabina').count()
    armas_fuzil = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA REGIONAL DE CURITIBANOS')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA REGIONAL DE CURITIBANOS')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_pistola2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='pistola').count()
    armas_espingarda2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='espingarda').count()
    armas_carabina2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='carabina').count()
    armas_fuzil2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil2_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    return render(request, 'gerencia/sr05.html', {'armas': armas,
                                                  'armas_institucional': armas_institucional,
                                                  'armas_individual': armas_individual,
                                                  'armas_pistola_t': armas_pistola_t,
                                                  'armas_espingarda_t': armas_espingarda_t,
                                                  'armas_carabina_t': armas_carabina_t,
                                                  'armas_fuzil_t': armas_fuzil_t,
                                                  'armas_fuzil_t2': armas_fuzil_t2,
                                                  'armas_pistola': armas_pistola,
                                                  'armas_espingarda': armas_espingarda,
                                                  'armas_carabina': armas_carabina,
                                                  'armas_fuzil': armas_fuzil,
                                                  'armas_fuzil_7': armas_fuzil_7,
                                                  'armas_pistola2': armas_pistola2,
                                                  'armas_espingarda2': armas_espingarda2,
                                                  'armas_carabina2': armas_carabina2,
                                                  'armas_fuzil2': armas_fuzil2,
                                                  'armas_fuzil2_7': armas_fuzil2_7})


@login_required
def sr06(request):
    regional = "SR06 - SUPERINTENDÊNCIA REGIONAL OESTE"
    armas = Arma.objects.filter(regional=regional).count()
    armas_institucional = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL').count()
    armas_individual = Arma.objects.filter(regional=regional)\
        .filter(tipo='INDIVIDUAL').count()
    armas_pistola = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA AGRÍCOLA DE CHAPECÓ')\
        .filter(especie='pistola').count()
    armas_espingarda = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA AGRÍCOLA DE CHAPECÓ')\
        .filter(especie='espingarda').count()
    armas_pistola_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='pistola').count()
    armas_espingarda_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='espingarda').count()
    armas_carabina_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='carabina').count()
    armas_fuzil_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_t2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_carabina = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA AGRÍCOLA DE CHAPECÓ')\
        .filter(especie='carabina').count()
    armas_fuzil = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA AGRÍCOLA DE CHAPECÓ')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA AGRÍCOLA DE CHAPECÓ')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_pistola2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='pistola').count()
    armas_espingarda2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='espingarda').count()
    armas_carabina2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='carabina').count()
    armas_fuzil2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil2_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO MASCULINO DE LAGES')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    return render(request, 'gerencia/sr06.html', {'armas': armas,
                                                  'armas_institucional': armas_institucional,
                                                  'armas_individual': armas_individual,
                                                  'armas_pistola_t': armas_pistola_t,
                                                  'armas_espingarda_t': armas_espingarda_t,
                                                  'armas_carabina_t': armas_carabina_t,
                                                  'armas_fuzil_t': armas_fuzil_t,
                                                  'armas_fuzil_t2': armas_fuzil_t2,
                                                  'armas_pistola': armas_pistola,
                                                  'armas_espingarda': armas_espingarda,
                                                  'armas_carabina': armas_carabina,
                                                  'armas_fuzil': armas_fuzil,
                                                  'armas_fuzil_7': armas_fuzil_7,
                                                  'armas_pistola2': armas_pistola2,
                                                  'armas_espingarda2': armas_espingarda2,
                                                  'armas_carabina2': armas_carabina2,
                                                  'armas_fuzil2': armas_fuzil2,
                                                  'armas_fuzil2_7': armas_fuzil2_7})


@login_required
def sr07(request):
    regional = "SR07 - SUPERINTENDÊNCIA REGIONAL DO MÉDIO VALE DO ITAJAÍ"
    armas = Arma.objects.filter(regional=regional).count()
    armas_institucional = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL').count()
    armas_individual = Arma.objects.filter(regional=regional)\
        .filter(tipo='INDIVIDUAL').count()
    armas_pistola = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE BLUMENAU')\
        .filter(especie='pistola').count()
    armas_espingarda = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE BLUMENAU')\
        .filter(especie='espingarda').count()
    armas_pistola_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='pistola').count()
    armas_espingarda_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='espingarda').count()
    armas_carabina_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='carabina').count()
    armas_fuzil_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_t2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_carabina = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE BLUMENAU')\
        .filter(especie='carabina').count()
    armas_fuzil = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE BLUMENAU')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PENITENCIÁRIA INDUSTRIAL DE BLUMENAU')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_pistola2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE BLUMENAU')\
        .filter(especie='pistola').count()
    armas_espingarda2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE BLUMENAU')\
        .filter(especie='espingarda').count()
    armas_carabina2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE BLUMENAU')\
        .filter(especie='carabina').count()
    armas_fuzil2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE BLUMENAU')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil2_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE BLUMENAU')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    return render(request, 'gerencia/sr07.html', {'armas': armas,
                                                  'armas_institucional': armas_institucional,
                                                  'armas_individual': armas_individual,
                                                  'armas_pistola_t': armas_pistola_t,
                                                  'armas_espingarda_t': armas_espingarda_t,
                                                  'armas_carabina_t': armas_carabina_t,
                                                  'armas_fuzil_t': armas_fuzil_t,
                                                  'armas_fuzil_t2': armas_fuzil_t2,
                                                  'armas_pistola': armas_pistola,
                                                  'armas_espingarda': armas_espingarda,
                                                  'armas_carabina': armas_carabina,
                                                  'armas_fuzil': armas_fuzil,
                                                  'armas_fuzil_7': armas_fuzil_7,
                                                  'armas_pistola2': armas_pistola2,
                                                  'armas_espingarda2': armas_espingarda2,
                                                  'armas_carabina2': armas_carabina2,
                                                  'armas_fuzil2': armas_fuzil2,
                                                  'armas_fuzil2_7': armas_fuzil2_7})


@login_required
def sr08(request):
    regional = "SR08 - SUPERINTENDÊNCIA REGIONAL DO PLANALTO NORTE"
    armas = Arma.objects.filter(regional=regional).count()
    armas_institucional = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL').count()
    armas_individual = Arma.objects.filter(regional=regional)\
        .filter(tipo='INDIVIDUAL').count()
    armas_pistola = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JARAGUÁ DO SUL')\
        .filter(especie='pistola').count()
    armas_espingarda = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JARAGUÁ DO SUL')\
        .filter(especie='espingarda').count()
    armas_pistola_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='pistola').count()
    armas_espingarda_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='espingarda').count()
    armas_carabina_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='carabina').count()
    armas_fuzil_t = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_t2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_carabina = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JARAGUÁ DO SUL')\
        .filter(especie='carabina').count()
    armas_fuzil = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JARAGUÁ DO SUL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE JARAGUÁ DO SUL')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    armas_pistola2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE MAFRA')\
        .filter(especie='pistola').count()
    armas_espingarda2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE MAFRA')\
        .filter(especie='espingarda').count()
    armas_carabina2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE MAFRA')\
        .filter(especie='carabina').count()
    armas_fuzil2 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE MAFRA')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='556 MM').count()
    armas_fuzil2_7 = Arma.objects.filter(regional=regional)\
        .filter(tipo='INSTITUCIONAL')\
        .filter(unidade='PRESÍDIO DE MAFRA')\
        .filter(especie='Fuzil / Carabina')\
        .filter(calibre='762 MM').count()
    return render(request, 'gerencia/sr08.html', {'armas': armas,
                                                  'armas_institucional': armas_institucional,
                                                  'armas_individual': armas_individual,
                                                  'armas_pistola_t': armas_pistola_t,
                                                  'armas_espingarda_t': armas_espingarda_t,
                                                  'armas_carabina_t': armas_carabina_t,
                                                  'armas_fuzil_t': armas_fuzil_t,
                                                  'armas_fuzil_t2': armas_fuzil_t2,
                                                  'armas_pistola': armas_pistola,
                                                  'armas_espingarda': armas_espingarda,
                                                  'armas_carabina': armas_carabina,
                                                  'armas_fuzil': armas_fuzil,
                                                  'armas_fuzil_7': armas_fuzil_7,
                                                  'armas_pistola2': armas_pistola2,
                                                  'armas_espingarda2': armas_espingarda2,
                                                  'armas_carabina2': armas_carabina2,
                                                  'armas_fuzil2': armas_fuzil2,
                                                  'armas_fuzil2_7': armas_fuzil2_7})












































