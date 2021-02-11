# agente_dirigido_por_tabela
Agente Dirigido por Tabela.

Esse programa demosntra um programa de agente bastante trivial que acompanha a sequência de percepções e depois a utiliza para realizar a indexação em uma tabela de
ações, a fim de decidir o que fazer. A tabela representa explicitamente a função do agente que o programa do agente incorpora. Para construir um agente racional desse modo, devemos construir uma tabela que contenha a ação apropriada para todas as sequências de percepções possíveis.

função AGENTE-DIRIGIDO-POR-TABELA(percepção) retorna uma ação
  variáveis estáticas: percepções, uma sequência, inicialmente vazia
  tabela, uma tabela de ações, indexada por sequências de percepções,
  inicialmente completamente especificada
  anexar percepção ao fim de percepções
  ação ← ACESSAR(percepções, tabela)
  retornar ação
