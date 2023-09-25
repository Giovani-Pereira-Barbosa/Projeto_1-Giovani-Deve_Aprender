
#PROGRAMA QUE CAUCULA FATORIAL
# O que iremos aprender neste curso?
# 00:00:39 - Pré-Requisitos | Dúvidas Frequentes
# 00:04:23 - Porque um software é criado?
# 00:08:38 - Como software é criado do zero e onde a lógica encaixa nisso?
#00:14:12 -  O problema que todo iniciante enfrenta
#00:17:30 - Aprenda resolver problemas através da análise crítica
#00:24:30 - O que são algorítimos e como montar um do zero
#00:35:57 - 4 Conceitos OBRIGATÓRIOS ser capaz de resolver problemas!
#00:48:21 - Criando soluções em Pseudocódigo  do básico ao avançado
#00:52:19 - Pseudocódigo #1 - Método 5Q's
#00:57:22 - Pseudocódigo #2 - Método 5Q's
#00:59:20 - Pseudocódigo #3 - Método 5Q's
#01:01:30 - Pseudocódigo #4 - Método 5Q's
#01:11:26 - Pseudocódigo #5 - Método 5Q's
#01:16:07 - Pseudocódigo #6 - Método 5Q's
#01:21:15 - Alertas sobre pseudocódigo
#01:24:09 - Criando soluções com Fluxogramas
#01:34:28 - Seu primeiro programa em Python
#01:38:10 - Variáveis
#01:48:36 - Condicionais
#02:02:27 - Laços de Repetição
#02:14:01 - Coleções(Listas)
#02:21:52 - Projeto 1 - Fatorial de um número
#02:31:30 - Projeto 2 -Chute o número
#02:46:00 - Projeto 3 - Medidor de Velocidade
#02:58:32 - Como lidar com problemas e projetos mais complexos?
#02:59:27 - Mensagem final!?
#03:00:14 - Para aonde ir a partir daqui?
numero = int (input("digite um numero"))
if numero > 0:
  fatorial = 1
  for item in range (1,numero +1):
     fatorial = fatorial * item;
  print(fatorial)