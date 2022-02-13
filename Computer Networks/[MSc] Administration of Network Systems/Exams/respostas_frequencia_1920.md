# Respostas Frequência Administração de Sistemas em Rede 2019/2020

## João Pedro da Cruz Brito, m9984

## Pergunta 1

**a)** A política da empresa deve reinar acima de tudo, tendo um caráter quase sagrado. As regras são para cumprir e o que está escrito no regulamento interno deve ser respeitado.
Um outro princípio prende-se com a previsibilidade de um sistema. Qualquer que seja a instalação ou arquitetura em vigor, deve caminhar com vista a um sistema global previsível. Algo previsível é algo passível de ser confiado e seguro.
O último conceito fundamental tem que ver com a escalabilidade do sistema implementado. O sistema tanto deve funcionar bem com 10 clientes como com 150. Ou seja, a propriedade que um sistema tem de funcionar bem é independente de pormenores de tamanho ou complexidade.

**b)** De forma geral, nesse email deveriam constar os seguintes aspetos:
* a equipa de SysAdmin, não pretendendo contestar a ordem dada, teria que avaliar se o software que precisa de ser instalado vai afetar, ou não, a atual configuração na empresa;
* após a avaliação, há-que avaliar se existe total e real necessidade de instalação do novo software (às vezes basta reconfigurar soluções já existentes);
* após este processo, e confirmando-se que de facto é necessária a aquisição do software e que este não vai interferir com a normal atividade da empresa, a instalação seria feita. Após a mesma, seria feito um acompanhamento, de modo a avaliar se tudo corria normalmente;
* por fim, relatórios seriam enviados aos executivos de topo da empresa, para relatar todo o processo de instalação do software.

**c)** O sysAdmin, sendo uma pessoa criativa por requisito, poderia tentar realocar os serviços atualmente executados para um menor número de máquinas. Deste modo, deixaria livre uma ou mais máquinas para a instalação do novo software.

**d)** Conversas de corredor, ainda para mais com um caráter importante e em que existe um prazo a cumprir, devem ser reduzidas ao mínimo possível. Se há um problema ou algo que tem de ser feito, todas as partes interessadas devem ser informadas atempadamente. Possivelmente poderia repensar a minha decisão e informar o CEO da situação, já que o interesse da empresa deve prevalecer.

## Pergunta 2

**a)** O primeiro aspeto quando se trata de lidar com possíveis vulnerabilidades ou falhas, é manter a cabeça fria e não entrar em pânico. Posto isto, após uma boa pesquisa para encontrar as tais vulnerabilidades, seria adequado consultar a política da empresa e ver se existe um procedimento definido nestes casos. Se houver, executa-se. Se não, as ações comuns incluem a análise do servidor em si (logs, mensagens de erro, etc...) para tentar encontrar as ditas vulnerabilidades. Se a vulnerabilidade está enquadrado numa sequência de ações específica, executar essas ações (tentar reproduzir o problema). Por fim, consultar fóruns especializados ou outros profissionais da área, a fim de cruzar conhecimento e possíveis soluções.

**b)** A forma mais direta seria instalar no servidor uma versão que não apresente os tais problemas. Se as novas funcionalidades do software problemático não forem cruciais, instala-se uma versão mais antiga e confiável. Não sendo possível retroceder nas versões, procurar por patches ou atualizações entretanto lançadas que possam resolver o problema. Por fim, poder-se-ia consultar as opiniões de outros SysAdmin, tendo estes passado por situações semlhantes.

**c)** Em primeiro lugar e mantendo a calma, analisar por onde, de que forma, como e durante quanto tempo o ataque foi feito (potencialmente contactar a empresa afetada e manter uma estreita colaboração, com vista à resolução do problema). A partir daqui, podem ser aplicadas as soluções referidas e proteger da melhor forma o servidor em causa. Em casos extremos poder-se-ia considerar a hipótese de não usar o equipamento em produção, e aguardar por futuras correções. 

**d)** Em muitos casos, soluções externas acabam por ser mais baratas, a médio ou longo prazo. Por outro lado, a manutenção estaria a cargo dos fornecedores externos, aliviando os SysAdmin da empresa para outras tarefas. Por fim, a computação externa oferecida pode ser mais poderosa e capaz do que a que atualmente existe na empresa.


# Pergunta 3

**a)** Como qualquer entrada de um novo sistema em produção, teriam que ser feitas análises de riscos e se a nova solução realmente é necessária. Seria preciso considerar também se a atual infraestrutura vai colaborar bem com o SAN instalado.
O sistema de ficheiros que usaria seria um que permita a colaboração com a atual infraestrutura da empresa e, também, permita o armazenamento de ficheiros de grandes dimensões. Se a empresa trabalha com Windows, NTFS. Se trabalha com Linux, ext4

**b)** A vantagem do SAN é que permite a realocação de recursos em caso de falha. Contudo, como qualquer nova tecnologia, o SAN requer um conhecimento especializado, o que pode não existir em abundância no contexto da empresa.

**c)** Pelas capacidades de um SAN resistir a falhas e por apresentar velocidades superiores. 

**d)** Todas as pessoas da empresa teriam de passar por um período de treino, no qual ficam familiarizadas com a nova solução. Em geral, aplicar medidas que combatam os erros humanos, pensando que o humano é falível e o sistema tem de continuar a dar resposta.

# Pergunta 4

**a)** Comparar o relatório e as alegações que faz com outras fontes (online, outros profissionais, etc...) e se a fonte de onde veio é confiável. Sendo verdadeiro, faria uma pesquisa a fim de saber se existem atualizações ou medidas para fazer face ao bug anunciado. Havendo, indicaria tais medidas aos membros do Conselho de Administração. Não havendo, sugeriria aos membros do CA a troca do equipamento ou a não utilização do equipamento dentro de portas da empresa.

**b)** O SysAdmin deve saber tudo de tudo. Estar a par dos problemas, atualizações, desenvolvimentos ou notícias no mundo dos sistemas com os quais trabalha, mas também da tecnologia em geral. Estar informado é estar um passo à frente na hora de tomar medidas e solucionar problemas.

**c)** Todos os equipamentos usados dentro da empresa devem seguir a política definida. Se não houver política, define-se uma. Nela deve constar que: 
* todo e qualquer equipamento deve desativar as atualizações automáticas de software;
* os equipamentos devem fazer parte de um lote já validado e que se sabe que, em princípio, não acarretará problemas;
* sendo um equipamento potencialmente perigoso, impedir o seu uso na empresa ou desativar as funcionalidades de rede;
* os utilizadores de equipamentos perigosos têm uma janela de alguns dias ou semanas para trocar de equipamento por um validado.

**d)** Sim, sem dúvida. Com o advento da Internet Of Things, todos os equipamentos tecnológicos vêm pairar sobre eles uma nuvem de suspeição. Muitos equipamentos aparentemente inofensivos podem ser o veículo de transmissão de problemas e desastres.

# Pergunta 5

**a)** Perder o emprego, seria uma das preocupações que surgiriam na minha mente. Posto isto, na minha mente deveria também estar a preocupação com a resolução do problema em si (ver se o equipamento ainda pode ser reparado com vista a recuperação de alguns dados). Adicionalmente, haveria ainda a preocupação de ter de ser necessário adquirir novos equipamentos para substituir o danificado.

**b)** O facto de ser antigo e, por consequência, mas suscetível a falhas. A falta de informação e talvez conhecimento sobre um sistema antigo pode ter contribuido para este desfecho. Possivelment também ajudou o facto de se ter usado um sistema destes para uma tarefa tão importante, teria sido melhor alocá-lo para tarefas mais simples. 

**c)** Em suma, a empresa deveria ter investido na renovação da sua infraestrutura e na correta alocação de determinadas máquinas para tarefas mais simples. Neste momento, é avaliar a recuperabilidade do sistema em causa e das informações que contém. De seguida, inevitavelmente terá de ser feita a aquisição de novos equipamentos (não havendo na empresa equipamentos disponíveis) e colocação do sistema de faturação em funcionamento o mais rápido possível.

**d)** A estratégia de comunicação da empresa teria de ser adequada, dado que os utilizadores merecem saber se os seus dados estão comprometidos e se o processo de transição para o sistema novo foi bem sucedido. A nível tecnológico, as dificuldades depreendem-se com a instalação do novo equipamento, transfeência de software e dados existentes no antigo sistema e na futura manutenção.
